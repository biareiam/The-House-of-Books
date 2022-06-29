"""Views for profile app - user profile"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import Http404
from django.db.models.functions import Lower
from checkout.models import Order
from events.models import Event, County
from .models import UserProfile, SavedEventList
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@require_POST
@login_required
def update_saved_events_list(request, event_id):
    """
    Add or remove a event to the user's SavedEventList:
    Get SavedEventList for user if it exists, otherwise create it.
    If event is in the list, then remove it, then check if list is now
    empty, if it is then delete the list. If event not in list, then add it.
    Redirect to the page the user sent the request from (events or my_events)
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    event = get_object_or_404(Event, pk=event_id)
    redirect_url = request.POST.get('redirect_url')

    try:
        saved_events_list = get_object_or_404(
            SavedEventList, user=user_profile
            )
    except Http404:
        saved_events_list = SavedEventList(user=user_profile)
        saved_events_list.save()

    if event in saved_events_list.event.all():
        saved_events_list.event.remove(event)
        action = 'removed from'
        saved_events_list.save()
        if not saved_events_list.event.all().exists():
            saved_events_list.delete()
    else:
        saved_events_list.event.add(event)
        action = 'added to'
        saved_events_list.save()

    messages.success(
        request, f'Event: "{event}" { action } your saved events!'
        )
    return redirect(redirect_url)


@login_required
def show_saved_events(request):
    """
    """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    sort = None
    sort_direction = None
    saved_events = None
    county = None
    try:
        saved_events_list = get_object_or_404(
            SavedEventList, user=user_profile
            )
        saved_events = saved_events_list.event.all()
        all_events = saved_events.order_by('county')
    except Http404:
        saved_events_list = None
        all_events = None

    # GET requests for sorting
    if request.GET:
        # handles sorting
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            # if sorting by event name, add lowercase name to sort
            if sortkey == 'name':
                sortkey = 'lower_name'
                saved_events = saved_events.annotate(
                    lower_name=Lower('name')
                    )
            # if direction is descending then reverse the sorting
            if 'direction' in request.GET:
                sort_direction = request.GET['direction']
                if sort_direction == 'desc':
                    sortkey = f'-{sortkey}'
            saved_events = saved_events.order_by(sortkey)
        # handles filtering by county
        if 'county' in request.GET:
            county = request.GET['county']
            county = get_object_or_404(County, name=county)
            saved_events = saved_events.filter(county=county)

    # used in context for select box to show the selected option
    current_sorting = f'{sort}_{sort_direction}'

    context = {
        'saved_events_list': saved_events_list,
        'current_sorting': current_sorting,
        'events': saved_events,
        'current_county': county,
        'all_events': all_events,
        'on_my_events_page': True,
    }
    template = 'profiles/my_events.html'
    return render(request, template, context)
