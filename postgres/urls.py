from django.urls import path

from . import views


urlpatterns = [

#jquery
    path('',views.showmore, name='showmore'),
    path('megamenu',views.megamenu, name='megamenu'),
    path('appendtext',views.appendtext, name='appendtext'),
    path('remove',views.remove, name='remove'),
    path('traversing',views.traversing, name='traversing'),
    path('get_post',views.get_post, name='get_post'),
    path('filter',views.filter, name='filter'),
    path('get_post',views.get_post, name='get_post'),
    path('serilize',views.serilize, name='serilize'),
    path('toggle',views.toggle),
    path('proxy',views.proxy, name='proxy'),
    path('show_or_hide',views.show_or_hide, name='show_or_hide'),
    path('patient_reg',views.patient_reg, name='patient_reg'),


# javascript
    path('output',views.output, name='output'),
    path('variables',views.variables, name='variables'),


]