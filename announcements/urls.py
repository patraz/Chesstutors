from django.urls import URLPattern, path
from .views import (
    announcement_list_view,
    announcement_detail_view,
    announcement_create_view,
    announcement_update_view,
    announcement_delete_view,
    av_form,
    av_delete


)

app_name = 'announcements'

urlpatterns = [
    path('', announcement_list_view, name='list'),
    path('<int:id>', announcement_detail_view, name= 'detail'),
    path('create/', announcement_create_view, name = 'create'),
    path("<int:id>/delete/", announcement_delete_view, name='delete'),
    path('<int:id>/edit/', announcement_update_view, name = 'update'),
    path("<int:id>/create/add/", av_form, name='hx_av'),
    path("<int:id>/<int:av_id>/av/delete/", av_delete, name='av_delete'),
    ]