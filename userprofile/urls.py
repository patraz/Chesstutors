
from django.urls import  path


from .views import (
    signup,
    login_view,
    logout_view,
    edit_description_hx,
    upload_photo
)

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('edit_des', edit_description_hx, name='edit_des'),
    path('upl_prof', upload_photo, name='upload_photo')
]