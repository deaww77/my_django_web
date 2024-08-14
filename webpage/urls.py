from django.urls import path
from . import views
urlpatterns = [
    path("",  views.indexPage, name="index"),
    path("about/", views.aboutUs, name="aboutUs"),
    path("contact/", views.contactUs, name="contactUs"),
    path("for/", views.forPage, name="for_page"),
    path("card/", views.card, name="card"),
    path("card_color/", views.card_color, name="card_color"),
    path("form/", views.form, name="form")
]
