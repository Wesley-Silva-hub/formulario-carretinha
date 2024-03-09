from django.urls import path
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_pessoa/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]
