from django.urls import path
from .views import newsletter_signup,newsletter_unsuscribe

app_name="newsletters"

urlpatterns = [
    path('signup/',newsletter_signup,name="optin"),
    path('unsuscribe/',newsletter_unsuscribe,name="unsuscribe"),
]
