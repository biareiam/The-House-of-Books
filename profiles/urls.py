""" Libraries """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path(
        'update_my_events/<event_id>',
        views.update_saved_events_list,
        name='update_my_events'
        ),
    path(
        'my_events/', views.show_saved_events, name='my_events'
        ),
]

