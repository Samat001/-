from django.urls import path
from applications.account.views import *


urlpatterns = [
path('register/' , RegisterAPIVew.as_view()),
path('activate/<uuid:activation_code>/' , ActivationView.as_view())
]