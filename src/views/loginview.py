from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse
from src.lib.logging_mixin import LoggingMixin
from src.controllers.userscontroller import UsersController

class LoginView(LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin):

    def post(self, requests):
        Response = UsersController().login(email=requests.data["email"], password=requests.data["password"])
        return CustomResponse(message="Login Api view", payload=Response, code=HTTP_200_OK)
