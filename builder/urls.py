from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('ChooseTemplates',views.choose_templates),
    path('Base',views.Collector),
    path('view_resume',views.view_resume,name='view_resume'),
    path('download',views.generate_view),
]