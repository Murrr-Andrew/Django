from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
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


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category
    }

    return render(request, 'news/category.html', context=context)


def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item
    }

    return render(request, 'news/view_news.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect(to=news)
    else:
        form = NewsForm()

    return render(request, 'news/add_news.html', {'form': form})
