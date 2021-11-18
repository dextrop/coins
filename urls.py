"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from src.views.loginview import LoginView
from src.views.signupview import SignupView
from src.views.statusview import StatusView
from src.views.coinprice import CoinPriceView
from src.views.updatecoinprice import UpdateCoinPriceView


from django.shortcuts import render
from django.conf.urls.static import static
from coins import settings


def docs(request):
    return render(request, "docs.html", {"message": "on localhost"})

urlpatterns = [
    path("doc/", docs, name="documentation"),
    path('', StatusView.as_view()),
    path('v1/login/', LoginView.as_view()),
    path('v1/signup/', SignupView.as_view()),
    path('v1/coins/price/', CoinPriceView.as_view()),
    path('v1/update/price/', UpdateCoinPriceView.as_view()),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
