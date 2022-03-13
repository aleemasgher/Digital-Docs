from rest_framework import serializers
from digitalization.models import Topic, Folder, Document


class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ['id', 'name']


class DocumentSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()

    class Meta:
        model = Document
        fields = ['id', 'file']

    def get_file(self, instance):
        request = self.context.get('request')
        file_url = instance.file.url
        return request.build_absolute_uri(file_url)


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ['id', 'name']


class CreateDocumentSerializer(serializers.Serializer):
    folder_name = serializers.CharField(max_length=100, required=True)
    file = serializers.FileField(required=True)
    topic_name = serializers.CharField(max_length=100, required=True)


class GetDocumentSerializer(serializers.Serializer):
    folder_name = serializers.CharField(max_length=100, required=True)
    topic_name = serializers.CharField(max_length=100, required=True)
