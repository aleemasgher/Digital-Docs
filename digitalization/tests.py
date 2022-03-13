from rest_framework.test import APITestCase
import io


class TestTopicGet(APITestCase):

    def test_topic(self):
        response = self.client.get("/api/v1/topic/")
        self.assertEqual(response.status_code, 200)


class TestFolderGet(APITestCase):

    def test_folder(self):
        response = self.client.get("/api/v1/folder/")
        self.assertEqual(response.status_code, 200)


class TestCreateDocumentPost(APITestCase):

    def test_create_document(self):
        document_data = {"folder_name": "Test",
                         "file": io.StringIO("Data into the file"),
                         "topic_name": "Testing"}
        response = self.client.post("/api/v1/create_doc/", document_data)
        self.assertEqual(response.status_code, 201)




