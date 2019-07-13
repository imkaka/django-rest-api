from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from snippets.views import SnippetViewSet, UserViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)

# The API URLs are now determined automatically by the router.

# Schema view
schema_view = get_schema_view(title="Pastebin API")

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', schema_view),
]
