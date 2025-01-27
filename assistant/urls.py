from django.urls import path
from .views import assistant

urlpatterns = [
    path('', view=assistant, name='assistant' )
]