"""Models for 'events' app"""
import datetime
from django.db import models
from django.contrib.auth.models import User


class County(models.Model):
    """
    County model - to hold counties in Ireland plus Dublin codes.
    Foreign key in Event model so events list can be filtered by
    standardised list of counties in Ireland + by Dublin areas.
    """

    class Meta:
        """Specify correct plural so it doesn't appear as Countys"""
        verbose_name_plural = 'Counties'
        ordering = ['name']

    name = models.CharField(max_length=20, unique=True)
    friendly_name = models.CharField(max_length=20)

    def __str__(self):
        """string method - return the county name"""
        return self.name

    def get_friendly_name(self):
        """return the user friendly name for views/frontend"""
        return self.friendly_name


class Event(models.Model):
    """Details about the events - date time etc."""
    class Meta:
        """order by date, newest date first"""
        ordering = ['-date']

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    county = models.ForeignKey(
        County, on_delete=models.CASCADE, related_name='events'
        )
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.ImageField(null=True, blank=True)
    event_description = models.TextField()
    month_book = models.CharField(max_length=200, default="The Club")
    book_author = models.CharField(max_length=200, default="Jane Austen")
    other_image = models.ImageField(null=True, blank=True)

    @property
    def date_passed(self):
        """For superuser views so can flag event has passed"""
        return self.date < datetime.date.today()

    def __str__(self):
        """string method - return the event name and formatted date"""
        event_date = self.date.strftime('%d/%m/%Y')
        return f'{self.name} on {event_date}'


class Comment(models.Model):
    """Model for users to add comments on events"""
    class Meta:
        """order by when created, oldest comments first"""
        ordering = ['created_on']

    author_comment = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='event_comments'
        )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name='comments'
        )
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author_comment}, {self.created_on}, on {self.event}'
