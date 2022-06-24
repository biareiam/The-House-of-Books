"""Views for 'events' app - craft events seller will be attending"""
import datetime
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from django.http import Http404
from django.contrib import messages
from django.db.models.functions import Lower
from django.utils.safestring import mark_safe
from profiles.models import SavedEventList, UserProfile
from .models import Event, County, Comment
from .forms import EventForm, CommentForm


def show_events(request):
    """
    Show events with date of today or later, earliest first
    If superuser, show all events (default ordering, latest first)
    If sort is present in the get request, then sort the events by that
    option + pass current sorting back to context.
    If user logged in, get their saved events list if they have one (so
    that template can show if event on their saved list or not)
    If 'county' in get request then filter results by that county.
    If 'view' in get request then show past events only.
    """
    today = datetime.date.today()
    saved_events_list = None
    sort = None
    sort_direction = None
    county = None
    view = None

    if request.user.is_superuser:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(date__gte=today).order_by('date')
    # used in context to generate dropdown of available counties to filter by
    all_events = events.order_by('county')

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        try:
            saved_events_list = get_object_or_404(
                SavedEventList, user=user_profile
                )
        except Http404:
            saved_events_list = None

    # GET requests for sorting and filtering
    if request.GET:
        # to filter to past events
        if 'view' in request.GET:
            view = request.GET['view']
            if view == 'past':
                events = Event.objects.filter(date__lt=today).order_by(
                    'date')
                # to generate dropdown counties to filter by in template
                all_events = events.order_by('county')

        # handles sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # if sorting by event name, add lowercase name to model to sort
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))
            # if direction is descending then reverse the sorting
            if 'direction' in request.GET:
                sort_direction = request.GET['direction']
                if sort_direction == 'desc':
                    sortkey = f'-{sortkey}'
            events = events.order_by(sortkey)

        # handles filtering by county
        if 'county' in request.GET:
            county = request.GET['county']
            county = get_object_or_404(County, name=county)
            events = events.filter(county=county)

    # used in context for select box to show the selected option
    current_sorting = f'{sort}_{sort_direction}'

    # used in template to determine options to show for button and sorting
    current_view = view

    # dict for context so count of saves for each event can be got in template
    events_saves = {
        event.id: SavedEventList.objects.filter(event__in=[event]).count()
        for event in events
        }

    context = {
        'events': events,
        'saved_events_list': saved_events_list,
        'current_view': current_view,
        'current_sorting': current_sorting,
        'current_county': county,
        'all_events': all_events,
        'events_saves': events_saves,
    }
    template = 'events/events.html'
    return render(request, template, context)


def event_details(request, event_id):
    """
    View to show an individual event and the comments on that event.
    Need to also retrieve the user's saved event list if they have one,
    so that the page shows whether the event is saved or not.
    Show comment form and handle posting of the form. If user not logged
    in then raise 403 as must be logged in to post comment.
    """
    saved_events_list = None
    event = get_object_or_404(Event, pk=event_id)
    comments = event.comments.all()
    event_saves = SavedEventList.objects.filter(event__in=[event]).count()

    if request.user.is_authenticated:
        user_profile = get_object_or_404(UserProfile, user=request.user)
        try:
            saved_events_list = get_object_or_404(
                SavedEventList, user=user_profile
                )
        except Http404:
            saved_events_list = None

    if request.method == 'POST':
        if not request.user.is_authenticated:
            raise PermissionDenied()
        else:
            form = CommentForm(request.POST)
            redirect_url = request.POST.get('redirect_url')
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author_comment = request.user
                comment.event = event
                comment.save()
                messages.success(
                    request,
                    f'Comment on: "{event}" successfully posted!'
                    )
                return redirect(redirect_url)
            else:
                messages.error(
                    request,
                    'Comment NOT posted. Please check the form for errors and '
                    're-submit.'
                    )
    else:
        form = CommentForm()

    context = {
        'event': event,
        'comments': comments,
        'form': form,
        'saved_events_list': saved_events_list,
        'event_saves': event_saves,
    }
    return render(request, 'events/event_details.html', context)


@require_POST
@login_required
def delete_comment(request, comment_id):
    """
    View for user to delete a comment they posted on a event.
    Raise 403 if the user is not the user who posted the comment.
    Post request only: delete comment, show success message.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if not request.user == comment.author_comment:
        raise PermissionDenied()
    event = comment.event
    comment.delete()
    messages.success(
        request,
        f'Comment from {comment.created_on.strftime("%d/%m/%Y, %-I.%M %p")}'
        f' posted on "{event}" deleted!'
        )
    return redirect(reverse('event_details', args=[event.id]))


@login_required()
def edit_comment(request, comment_id):
    """
    Show form for user to edit their comment. Raise 403 if not
    comment author_comment.Handle posting of form, show success/error messages.
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if not request.user == comment.author_comment:
        raise PermissionDenied()
    event = comment.event
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            messages.success(
                request,
                f'Updates to comment originally posted on '
                f'{comment.created_on.strftime("%d/%m/%Y, %-I.%M %p")} saved!'
                f' Comment is posted on "{event}"'
                )
            return redirect(reverse('event_details', args=[event.id]))
        else:
            messages.error(
                request,
                'Comment NOT updated. Please check the form for errors and '
                're-submit.'
                )
    else:
        form = CommentForm(instance=comment)

    context = {
        'event': event,
        'form': form,
        'comment': comment,
    }
    template = 'events/edit_comment.html'
    return render(request, template, context)


@login_required()
def add_event(request):
    """
    Show event form for admin user to add event. Raise 403 if not admin.
    Handle posting of form, show success/error messages.
    """
    if not request.user.is_superuser:
        raise PermissionDenied()
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(
                request, f'New event: "{event}" added!'
                )
            return redirect('events')
        else:
            messages.error(
                request,
                'Event not added. Please check the form for errors and '
                're-submit.'
                )
    else:
        form = EventForm()
    context = {
        'form': form,
    }
    template = 'events/add_event.html'
    return render(request, template, context)


@login_required()
def edit_event(request, event_id):
    """
    Show form for admin user to edit existing event. Raise 403 if not admin.
    Handle posting of form, show success/error messages.
    Show alert if editing a event with a past date.
    """
    if not request.user.is_superuser:
        raise PermissionDenied()
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            messages.success(
                request,
                f'Updates to event: "{event}" saved!'
                )
            return redirect('events')
        else:
            messages.error(
                request,
                'Event NOT updated. Please check the form for errors and '
                're-submit.'
                )
    else:
        form = EventForm(instance=event)
        today = datetime.date.today()
        if event.date < today:
            messages.info(
                request,
                mark_safe(
                    'You\'re editing a past event. You can update the '
                    'details but if you change the date, the new date must be '
                    'a future date.<br>If you want to post details of this '
                    'event on a new date, then create a new event record '
                    'using the Add Event form.'
                )
            )

    context = {
        'event': event,
        'form': form,
    }
    template = 'events/edit_event.html'
    return render(request, template, context)


@require_POST
@login_required
def delete_event(request, event_id):
    """
    View for admin user to delete event from front end.
    Raise 403 if not admin.
    Post request only: delete event, show success message.
    """
    if not request.user.is_superuser:
        raise PermissionDenied()
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(
        request, f'Event: "{event}" deleted!'
        )
    return redirect('events')
