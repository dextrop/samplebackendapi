from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from sampleapi.libraries.customresponse import CustomResponse
from sampleapi.controllers.notecontroller import NotesController

class NotesView(generics.GenericAPIView):
    def get(self, requests):
        Response = NotesController(requests=requests.GET).get()
        return CustomResponse(message="Notes GET API", payload=Response, code=HTTP_200_OK)

    def post(self, requests):
        Response = NotesController(requests=requests.data).add()
        return CustomResponse(message="Notes API", payload=Response, code=HTTP_200_OK)


    def put(self, requests):
        Response = NotesController(requests=requests.data).modify()
        return CustomResponse(message="Notes API", payload=Response, code=HTTP_200_OK)

    def delete(self, requests):
        Response = NotesController(requests=requests.data).delete()
        return CustomResponse(message="Notes API", payload=Response, code=HTTP_200_OK)
