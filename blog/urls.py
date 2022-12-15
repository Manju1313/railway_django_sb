from django.urls import path

from . import views


urlpatterns = [
    path('ajax_state',views.ajax_state, name='ajax_state'),

]