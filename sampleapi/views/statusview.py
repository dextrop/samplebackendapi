from rest_framework import generics
from rest_framework.status import HTTP_200_OK
from sampleapi.libraries.customresponse import CustomResponse

class StatusView(generics.GenericAPIView):

    def get(self, requests):
        Response = True
        return CustomResponse(message="Backend Project Is Up and Running", payload=Response, code=HTTP_200_OK)
