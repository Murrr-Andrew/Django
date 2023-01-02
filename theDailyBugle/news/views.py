from django.views.generic import ListView, DetailView, CreateView
from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    """
    Creating a ListView class for using class(es) instead of method to render pages
    Needs to specify data for fields:
    model => Model from data to show
    [template_name] => specify template to use (default modelName_list => news_list)
    [context_object_name] => specify the name of the context to be used in template (default object_list)
    [extra_context] => use only for static data, better to use get_context_data method
    """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        # Get all the context that was in it before
        context = super(HomeNews, self).get_context_data(**kwargs)
        context['title'] = 'News'

        return context

    def get_queryset(self):
        # By default returns the whole list of data, we can modify the queryset
        return News.objects.filter(is_published=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    # If category does not exists - show 404 error (Default True) - to show empty data (500 error)
    allow_empty = False

    def get_context_data(self, **kwargs):
        # Get all the context that was in it before
        context = super(NewsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])

        return context

    def get_queryset(self):
        # By default returns the whole list of data, we can modify the queryset
        # Param from url is stored in 'self'. Example self.kwargs['category_id'] (check urls.py for the param)
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    # Default 'modelName_detail' => 'news_detail'
    # Or we can specify which template to use
    # template_name = 'news/news_detail.html'

    # Default 'pk' param should be in urls.py on path string
    # Or we can specify which param to use a 'pk'
    # pk_url_kwarg = 'news_id'


class CreateNews(CreateView):
    """
    Needs to connect form_class to FormClass
    """
    form_class = NewsForm
    template_name = 'news/add_news.html'

    # success_url = 'url to redirect after success form submit' or will use get_absolute_url()
