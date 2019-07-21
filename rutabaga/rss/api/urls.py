from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rss.api import views as qv

router = DefaultRouter()
router.register(r"feeds", qv.FeedViewSet)

urlpatterns = [path("", include(router.urls))]
