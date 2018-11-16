# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views


app_name = 'pyfb_customerportal'
urlpatterns = [
    url(
        regex="^PortalSettings/~create/$",
        view=views.PortalSettingsCreateView.as_view(),
        name='PortalSettings_create',
    ),
    url(
        regex="^PortalSettings/(?P<pk>\d+)/~delete/$",
        view=views.PortalSettingsDeleteView.as_view(),
        name='PortalSettings_delete',
    ),
    url(
        regex="^PortalSettings/(?P<pk>\d+)/$",
        view=views.PortalSettingsDetailView.as_view(),
        name='PortalSettings_detail',
    ),
    url(
        regex="^PortalSettings/(?P<pk>\d+)/~update/$",
        view=views.PortalSettingsUpdateView.as_view(),
        name='PortalSettings_update',
    ),
    url(
        regex="^PortalSettings/$",
        view=views.PortalSettingsListView.as_view(),
        name='PortalSettings_list',
    ),
	]
