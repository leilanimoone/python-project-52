from django.urls import path
from .views import (LabelsListView,
                    LabelCreateView,
                    LabelUpdateView,
                    LabelDeleteView)

urlpatterns = [
    path('', LabelsListView.as_view(), name='home_labels'),
    path('create/', LabelCreateView.as_view(), name='create_label'),
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update_label'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete_label')
]
