"""Set up of django admin site for events app"""
from django.contrib import admin
from .models import County, Event, Comment


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    """
    County model - admin site set up:
    Show all fields in list display
    """
    list_display = ('friendly_name', 'name')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Event model - admin set up: fields to show in list view,
    Allow filtering by county, and search by name + website.
    """
    list_display = (
        'name', 'location', 'county', 'date', 'date_passed',
        )
    list_filter = ('county',)
    search_fields = ['name', ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin set up for Comments model - show fields in list display and
    allow filtering of comments by event or comment author, add link
    fields and allow search on comment.
    """
    readonly_fields = ['id', ]
    list_display = ('id', 'author_comment', 'event', 'created_on', 'comment', )
    list_filter = ('event', 'author_comment', )
    list_display_links = ('id', 'created_on', 'comment',)
    search_fields = ['comment', ]