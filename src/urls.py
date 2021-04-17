"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toolbox.views import main, mr_redirect, mr_editor, \
    create_act, create_invoice, create_project, create_client, get_model, \
    edit_invoice, edit_client, edit_act, edit_project, delete_model

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('mr_redirect/', mr_redirect, name='mr_redirect'),
    path('mr_editor/<int:model_id>/<str:model_name>/<str:link>', mr_editor, name='mr_editor'),
    path('create_client/', create_client, name='create_client'),
    path('create_project/', create_project, name='create_project'),
    path('create_invoice/', create_invoice, name='create_invoice'),
    path('create_act/', create_act, name='create_act'),
    path('get_model/<str:button>', get_model, name='get_model'),
    path('edit_act/<int:model_id>', edit_act, name='edit_act'),
    path('edit_invoice/<int:model_id>', edit_invoice, name='edit_invoice'),
    path('edit_project/<int:model_id>', edit_project, name='edit_project'),
    path('edit_client/<int:model_id>', edit_client, name='edit_client'),
    path('delete_model/<str:model_name>/<int:model_id>/<str:link>', delete_model, name='delete_model'),
]
