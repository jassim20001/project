from django.urls import include, path

from . import views
from .views import *
urlpatterns = [

    path('myhome',views.home,name='vizeta'),
    path('login',views.Login_user,name='login'),
    path('logout_view',views.logout_view,name='logout'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('<slug:slug>/',views.detal_doctor,name='detail'),
    path('form',views.form,name='form'),
    path('signup',views.signup,name='signup'),
    path('api-auth', include('rest_framework.urls')),
    path('blogs',views.blog,name='blog'),
    path('add_blog',views.AddBlog,name='AddBlog'),

    # =============================={API}
    path('api/midecal/',Mixin.as_view(),name='Mixin'),
    path('api/Mixin_user/',Mixin_user.as_view(),name='Mixin_user'),
    
    path('Mixin_pk/<int:pk>',Mixin_pk.as_view(),name='Mixin_pk'),
  # =============================={API}
    # ===================={medical}
    path('',views.home2,name='home'),
    path('book',views.index,name='book'),
    path('servese',views.serves,name='serv'),
    path('blog',views.blog,name='blog'),
    path('about',views.about,name='about'),
    path('doctor',views.Expertdoctors,name='doctor'),
    
    path('Comment',views.Comment,name='Comment'),
    path('callUs',views.callUs,name='callUs'),
    # =================={Dashbord}
    path('dashbord',views.Dash,name='dash'),
    path('dashbord_doctor',views.Dash_doctor,name='dash_d'),
    path('delete_p/<str:pk>',views.delete_p,name='delete'),
    path('delete_doc/<str:pk>',views.delete_d,name='delete_d'),
    path('update/<str:pk>',views.update,name='update'),
    path('update2/<str:pk>',views.update2,name='update2'),
    # =========================={comment}
    path('updateComment/<str:pk>',views.updateComment,name='updateComment'),
    path('delete_comment/<str:pk>',views.deleteComment,name='deleteComment'),
    # ========================{Blog Api}
    
 
    path('generic_list/api/',Mixin_blog.as_view()),
    path('mixin_doctor/api/',Mixin_doctor.as_view()),

]

