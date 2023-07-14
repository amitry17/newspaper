from django.urls import path
from .views import PostList, PostDetail, PostSearch, NewsPostCreate, NewsPostUpdate, NewsPostDelete, ArticlePostCreate, ArticlePostDelete, ArticlePostUpdate


urlpatterns = [
    path('', PostList.as_view(), name = 'posts'),
    path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
    path('search/', PostSearch.as_view(), name = 'search'),
    path('news/create/', NewsPostCreate.as_view(), name = 'news_post_create'),
    path('news/<int:pk>/update/', NewsPostUpdate.as_view(), name='news_post_update'),
    path('news/<int:pk>/delete/', NewsPostDelete.as_view(), name='news_post_delete'),
    path('article/create/', ArticlePostCreate.as_view(), name = 'article_post_create'),
    path('article/<int:pk>/update/', ArticlePostUpdate.as_view(), name='article_post_update'),
    path('article/<int:pk>/delete/', ArticlePostDelete.as_view(), name='article_post_delete'),
    path('article/<int:pk>/delete/', ArticlePostDelete.as_view(), name='article_post_delete')
]