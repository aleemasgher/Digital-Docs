from django.db import models


def content_file_name(instance, filename):
    return '/'.join([instance.folder.name, instance.topic.name, filename])


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Topic"
        verbose_name_plural = "Topics"


class Folder(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Folder"
        verbose_name_plural = "Folders"


class Document(models.Model):
    file = models.FileField(upload_to=content_file_name)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="folders")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topics")

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"
