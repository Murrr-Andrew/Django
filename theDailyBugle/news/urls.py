from django.urls import path
from .views import *


urlpatterns = [
    # In case of use ListView class => call .as_view() for it. Example HomeNews.as_view()
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', add_news, name='add_news')
]
