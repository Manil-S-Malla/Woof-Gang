from django.urls import path
from .views import main, GangList, GangCreate


urlpatterns = [
    path('', main),
    path('gang/', GangList.as_view()),
    path('gang/create/', GangCreate.as_view()),
]
