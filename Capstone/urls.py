"""Capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from pages import views as pages_views

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', pages_views.home, name='home'),
                  url(r'^new_loan/', pages_views.new_loan, name='newloan'),
                  url(r'^new_covenant/', pages_views.new_covenant, name='newcovenant'),
                  url(r'^qboauth/', include('qboauth.urls')),
                  url(r'^display/?$', pages_views.display, name='display'),
                  url(r'^cov/(?P<slug>[\w-]+)', pages_views.covenant, name='cov'),
                  url(r'^cov_set/(?P<id>[\w-]+)', pages_views.checkthing, name='cov_set'),
                  url(r'^covenants/', pages_views.all_covenant, name='covenants'),
                  url(r'^loans/(?P<slug>[\w-]+)', pages_views.view_loan, name='loans'),
                  url(r'^loans/', pages_views.all_loans, name='loans'),
                  url(r'^org/$', pages_views.all_organization, name='organization'),
                  url(r'^organization/(?P<slug>[\w-]+)', pages_views.organization, name='organization'),
                  url(r'^cov_statement/', pages_views.statement_display, name='cov_statement')

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
