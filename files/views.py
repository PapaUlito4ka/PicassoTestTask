from rest_framework import generics, status
from rest_framework.response import Response

from files.models import File
from files.serializers import FileSerializer
from files.tasks import process_file


class ListFilesView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class UploadFileView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        process_file.apply_async(args=[serializer.data.get('id')])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
