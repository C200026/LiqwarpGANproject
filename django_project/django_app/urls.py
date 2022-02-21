from django.urls import path
#from .views import indexfunction
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('list/', views.img_list, name='list'), 
    path('upload/', views.image_upload, name='image_upload'),
    path('login/', views.Login.as_view(), name='login'), 
    path('logout/', views.Logout.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)