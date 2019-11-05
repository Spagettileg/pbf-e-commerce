from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(urls_reset))
]
