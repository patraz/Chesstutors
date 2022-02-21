
from django.urls import  path


from .views import (
    signup,
    login_view,
    logout_view,
    edit_description_hx,
    upload_photo,
    edit_number_hx,
    show_number
)

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('edit_des', edit_description_hx, name='edit_des'),
    path('upl_prof', upload_photo, name='upload_photo'),
    path('phone_number', edit_number_hx, name='phone_number'),
    path('show_number/<int:id>', show_number, name='show_number')
]