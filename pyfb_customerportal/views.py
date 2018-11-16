# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	PortalSettings,
)


class PortalSettingsCreateView(CreateView):

    model = PortalSettings


class PortalSettingsDeleteView(DeleteView):

    model = PortalSettings


class PortalSettingsDetailView(DetailView):

    model = PortalSettings


class PortalSettingsUpdateView(UpdateView):

    model = PortalSettings


class PortalSettingsListView(ListView):

    model = PortalSettings

