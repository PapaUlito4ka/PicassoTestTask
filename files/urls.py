from django.urls import path

from files.views import ListFilesView, UploadFileView


urlpatterns = [
    path('upload/', UploadFileView.as_view()),
    path('files', ListFilesView.as_view())
]
