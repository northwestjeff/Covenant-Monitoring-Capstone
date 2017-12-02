from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^connectToQuickbooks/?$', views.connectToQuickbooks, name='connectToQuickbooks'),
    url(r'^signInWithIntuit/?$', views.signInWithIntuit, name='signInWithIntuit'),
    url(r'^getAppNow/?$', views.getAppNow, name='getAppNow'),
    url(r'^authCodeHandler/?$', views.authCodeHandler, name='authCodeHandler'),
    url(r'^disconnect/?$', views.disconnect, name='disconnect'),
    url(r'^apiCall/?$', views.apiCall, name='apiCall'),
    url(r'^connected/?$', views.connected, name='connected'),
    url(r'^refreshTokenCall/?$', views.refreshTokenCall, name='refreshTokenCall'),
]