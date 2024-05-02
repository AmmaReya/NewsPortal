from django.urls import path
from . import views


urlpatterns = [
   path('', views.PostList.as_view(), name='post_list'),
   path('<int:pk>', views.PostDetail.as_view(), name='post_detail'),
   path('search/', views.PostSearch.as_view(), name='post_search'),

   path('news/create/', views.PostCreate.as_view(), name='new_create'),
   path('news/<int:pk>/update/', views.PostUpdate.as_view(), name='new_update'),
   path('news/<int:pk>/delete/', views.PostDelete.as_view(), name='new_delete'),

   path('articles/create/', views.PostCreate.as_view(), name='article_create'),
   path('articles/<int:pk>/update/', views.PostUpdate.as_view(), name='article_update'),
   path('articles/<int:pk>/delete/', views.PostDelete.as_view(), name='article_delete'),
]
