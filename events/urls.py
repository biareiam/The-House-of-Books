"""URL paths for the 'events' app"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_events, name='events'),
    path('<int:event_id>/', views.event_details, name='event_details'),
    path('add/', views.add_event, name='add_event'),
    path('edit/<int:event_id>/', views.edit_event, name='edit_event'),
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),
    path(
        'edit_comment/<int:comment_id>/',
        views.edit_comment,
        name='edit_comment'
        ),
    path(
        'delete_comment/<int:comment_id>/',
        views.delete_comment,
        name='delete_comment'
        ),
]