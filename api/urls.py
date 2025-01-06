

from django.urls import path, include
from events.views import EventViewSet, UpcomingEventsView, AddAttendeeView, RemoveAttendeeView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet


from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view = swagger_get_schema_view(
    openapi.Info(
        title= "Event Management API",
        default_version= "2.0.0",
        description="API Documentation Of APP"
    ),
    public=True,
)


router = DefaultRouter()
router.register('events', EventViewSet, basename='event')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('upcoming/events/', UpcomingEventsView.as_view(), name='upcoming_events'),
    path('events/<int:event_id>/add-attendee/', AddAttendeeView.as_view(), name='add_attendee'),
    path('events/<int:event_id>/remove-attendee/', RemoveAttendeeView.as_view(), name='remove_attendee'),
    path('swagger/schema/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_schema'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
