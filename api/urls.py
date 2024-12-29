
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, UpcomingEventsView, AddAttendeeView, RemoveAttendeeView
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('upcoming-events/', UpcomingEventsView.as_view(), name='upcoming-events'),
    path('events/<int:event_id>/add-attendee/', AddAttendeeView.as_view(), name='add-attendee'),
    path('events/<int:event_id>/remove-attendee/', RemoveAttendeeView.as_view(), name='remove-attendee'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
"""



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet, UpcomingEventsView, AddAttendeeView, RemoveAttendeeView
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('upcoming/', UpcomingEventsView.as_view(), name='upcoming_events'),
    path('events/<int:event_id>/add-attendee/', AddAttendeeView.as_view(), name='add_attendee'),
    path('events/<int:event_id>/remove-attendee/', RemoveAttendeeView.as_view(), name='remove_attendee'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
