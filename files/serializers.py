from rest_framework import serializers

from files.models import File
from files.validators import check_file_size


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_empty_file=False, required=True, validators=[
        check_file_size
    ])

    class Meta:
        model = File
        fields = '__all__'
        read_only_fields = ('id', 'processed', 'uploaded_at')
