
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import WordViewSet, WordList

router = DefaultRouter()
router.register(r"words", WordViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path('words/of/<username>/', WordList.as_view()),
]
