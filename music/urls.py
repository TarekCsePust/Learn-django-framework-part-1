
from django.urls import path
from . import views
app_name = 'music'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),


    path('register/',views.UserFormView.as_view(),name='register'),


    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    #add
    path('album/add/', views.AlbumCreate.as_view(),name='album-add'),

    #update
    path('album/<int:pk>/', views.AlbumUpdate.as_view(),name='album-update'),

    #delete
    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(),name='album-delete'),
    #path('<int:album_id>/',views.detail,name='detail'),

    #path('<int:album_id>/favorite/',views.favorite,name='favorite'),
    #path('<int:pk>/',views.DetailView.as_view(),name='detail'),
]