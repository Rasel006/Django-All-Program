from django.urls import path
from . import views
urlpatterns = [

    path('',views.link_page),
    path('about/',views.about),
    path('contact/',views.contact),
    path('extra/',views.extra),
    path('services/',views.services),
]