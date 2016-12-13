from django.conf.urls import url

from api.views import CarList, CarListDetail


urlpatterns = [
     url(r'^cars/?$', CarList.as_view()),
     url(r'^cars/(?P<pk>\d+)?$', CarListDetail.as_view()),
]
