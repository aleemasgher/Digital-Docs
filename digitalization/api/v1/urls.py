from digitalization.api.v1.viewsets import FolderViewSet, DocumentViewSet, TopicViewSet, CreateDocumentView, \
    GetDocumentView
from rest_framework.routers import DefaultRouter
from django.urls import path, include


router = DefaultRouter()
router.register("folder", FolderViewSet, basename="folder")
router.register("document", DocumentViewSet, basename="document")
router.register("topic", TopicViewSet, basename="topic")
router.register("create_doc", CreateDocumentView, basename="create")
router.register("get_doc", GetDocumentView, basename="get")

urlpatterns = [
    path("", include(router.urls)),
]

