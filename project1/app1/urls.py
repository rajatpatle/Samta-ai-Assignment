from django.urls import path
from . views import UploadFileView, SignUpAPI, DataViewSet, NewDataViewSet, PerDataViewSet

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload-file'),
    path('register/', SignUpAPI.as_view()),
    path('data/', DataViewSet.as_view({'get': 'list'}), name='data'),
    path('eastdata/', NewDataViewSet.as_view({'get': 'list'})),
    path('per/', PerDataViewSet.as_view({'get': 'list'})),
]
