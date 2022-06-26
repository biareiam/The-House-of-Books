"""Forms for 'events' app"""
import datetime
from django import forms
from django.core.exceptions import ValidationError
#from products.widgets import CustomClearableFileInput
from .models import Event, County, Comment


class EventForm(forms.ModelForm):
    """
    Event form for admin user to add/edit event from frontend.
    """
    class Meta:
        """
        Helptexts and labels specified for some fields.
        """
        model = Event
        fields = (
            'month_book', 'book_author', 'location', 'county', 'date', 'start_time', 'end_time',
            'event_description', 'image', 'other_image',
        )
        labels = {
            'name': 'Event Name',
        }
        help_texts = {
            'date': 'Cannot be in the past. Only events with today\'s date '
            'or later are shown to users in the Upcoming Events page',
            'start_time': 'Must be before End time!',
            'end_time': 'Must be after Start time!',
            'event_description': 'Please enter a description',
            'month_book': "Please enter the month's book",
            'book_author': " Please enter the name of the author of the book"
            
            }
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'type': 'date'}
                ),
            'start_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'type': 'time'}
                ),
            'end_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'type': 'time'}
                ),
            }

    #image = forms.ImageField(label='Image', required=False, widget=CustomsCleareableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Override init method to make changes to fields
        """
        super().__init__(*args, **kwargs)
        counties = County.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in counties]
        self.fields['county'].choices = friendly_names
        self.fields['county'].choices.insert(
            0, ('', 'Choose county, or Dublin postcode')
            )
        for field in self.fields:
            if field == 'start_time' or field == 'end_time':
                self.fields[field].widget.attrs['class'] = (
                    'brand-form-input time-input')
            else:
                self.fields[field].widget.attrs['class'] = 'brand-form-input'

        today = datetime.date.today()
        if self.instance.date:
            if self.instance.date < today:
                date = self.instance.date.strftime('%d/%m/%Y')
                self.fields['date'].help_text = (
                    f'Editing a past event dated {date}. If you are amending '
                    'the date it can only be changed to a future date.')

    def clean(self):
        """
        Override the clean method on form to include checks on date and times.
        """
        cleaned_data = super().clean()
        event_date = cleaned_data.get('date')
        today = datetime.date.today()
        existing_date = self.instance.date
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time:
            if end_time < start_time:
                self.add_error(
                    'end_time',
                    ValidationError('End time must be after Start time')
                    )
                self.add_error(
                    'start_time',
                    ValidationError('Start time must be before End time')
                    )
                for fieldname in ['end_time', 'start_time']:
                    self.fields[fieldname].help_text = None

        if event_date:
            if event_date < today and event_date != existing_date:
                self.add_error(
                    'date',
                    ValidationError('Event date must not be in the past')
                    )
                self.fields['date'].help_text = None


class CommentForm(forms.ModelForm):
    """
    Comment form to add comments on events
    """
    class Meta:
        """
        Form based on Comment model.
        """
        model = Comment
        fields = ('comment', )
        labels = {'comment': 'Your comment', }

    def __init__(self, *args, **kwargs):
        """
        Override init method to add number of rows + maxlength for textarea
        field and add CSS class.
        """
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs = {'rows': 5, 'maxlength': 1000}
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'brand-form-input'

    def clean(self):
        """
        Override the clean method on form to include check on textarea field.
        """
        cleaned_data = super().clean()
        comment = cleaned_data.get('comment')
        if comment:
            if len(comment) >= 1005:
                self.add_error(
                        'comment',
                        ValidationError(
                            'Comment is too long. Please shorten and re-submit'
                        )
                    )
