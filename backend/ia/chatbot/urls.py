from django.urls import path
from .views import chatbot_response, index

urlpatterns = [
    path('', index, name='index'),
    path('ask/', chatbot_response, name='chatbot_response'),
]
