from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from digitalization.models import Folder, Topic, Document
from digitalization.api.v1.serializers import FolderSerializer, TopicSerializer, DocumentSerializer, \
    CreateDocumentSerializer, GetDocumentSerializer
from rest_framework.response import Response
from rest_framework import status


class FolderViewSet(ReadOnlyModelViewSet):
    serializer_class = FolderSerializer
    queryset = Folder.objects.all()


class TopicViewSet(ReadOnlyModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class DocumentViewSet(ReadOnlyModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class CreateDocumentView(ModelViewSet):
    serializer_class = CreateDocumentSerializer
    queryset = Document.objects.all()
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            topic_instance = Topic(name=serializer.validated_data['topic_name'])
            topic_instance.save()
            folder_instance = Folder(name=serializer.validated_data['folder_name'])
            folder_instance.save()
            document_instance = Document(file=serializer.validated_data['file'],
                                         folder=folder_instance,
                                         topic=topic_instance)
            document_instance.save()
            return Response({"response": "File uploaded"}, status=status.HTTP_201_CREATED)
        return Response({"response": "File not uploaded"}, status=status.HTTP_400_BAD_REQUEST)


class GetDocumentView(ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = GetDocumentSerializer
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        documents = Document.objects.filter(folder__name=serializer.validated_data["folder_name"],
                                            topic__name=serializer.validated_data["topic_name"])
        response = DocumentSerializer(documents, context={"request": self.request}, many=True).data
        return Response(response, status=status.HTTP_200_OK, headers=headers)
