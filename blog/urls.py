from django.urls import path,include
from  . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('singup/',views.user_singup,name='singup'),
    path('singin/',views.user_singin,name='singin'),
    path('logout/',views.user_logout,name='logout'),
    path('post/',views.user_post,name='post'),
    path('showpost/',views.show_post,name='showpost'),
    path('update/<int:id>/',views.user_update,name='update'),
    path('delete/<int:id>/',views.user_dalete,name='delete'),
    path('test/<int:id>/',views.testing,name='test'),
    path('search/',views.search,name='search'),
]