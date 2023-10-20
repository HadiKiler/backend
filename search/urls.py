from django.urls import path, include

from search.views import SearchListView

urlpatterns = [
    path('', SearchListView.as_view())
]
