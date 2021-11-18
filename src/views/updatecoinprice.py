from rest_framework import generics
from rest_framework import mixins
from rest_framework.status import HTTP_200_OK
from src.lib.customresponse import CustomResponse
from src.lib.logging_mixin import LoggingMixin
from src.controllers.coinpricecontroller import CoinPriceController

class UpdateCoinPriceView(LoggingMixin, generics.GenericAPIView, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                     mixins.ListModelMixin):

    def get(self, requests):
        Response = CoinPriceController().update_coin_price()
        return CustomResponse(message="Login Api view", payload=Response, code=HTTP_200_OK)



