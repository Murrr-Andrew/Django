from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page

from theDailyBugle.settings import EMAIL_HOST_USER, EMAIL_WHERE_TO_SEND

from .models import News, Category

from .forms import NewsForm, UserRegisterFrom, UserLoginForm, ContactForm

from .utils import MyMixin


@cache_page(60 * 15)
def register(request):
    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You successfully registered!')
            return redirect('home')
        else:
            messages.error(request, 'Registration field. Try again!')
    else:
        form = UserRegisterFrom()

    context = {
        'form': form
    }

    return render(request, 'news/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(to='home')
    else:
        form = UserLoginForm()

    context = {
        'form': form
    }

    return render(request, 'news/login.html', context=context)


def user_logout(request):
    logout(request)
    return redirect('login')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'],
                             EMAIL_HOST_USER, [EMAIL_WHERE_TO_SEND], fail_silently=True)

            if mail:
                messages.success(request, 'Email sent!')
                return redirect('contact')
            else:
                messages.error(request, 'Email sent error. Try again!')
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'news/contact.html', context=context)


class HomeNews(MyMixin, ListView):
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

    # Pagination
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Get all the context that was in it before
        context = super(HomeNews, self).get_context_data(**kwargs)

        # Calling methods from the MyMixin class which we inherit in the constructor
        context['title'] = self.get_upper('News')
        context['mixin_prop'] = self.get_prop()

        return context

    def get_queryset(self):
        # By default returns the whole list of data, we can modify the queryset
        # .select_related() - to add related data to make less SQL requests
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'

    # Pagination
    paginate_by = 20

    # If category does not exists - show 404 error (Default True) - to show empty data (500 error)
    allow_empty = False

    def get_context_data(self, **kwargs):
        # Get all the context that was in it before
        context = super(NewsByCategory, self).get_context_data(**kwargs)

        # Calling methods from the MyMixin class which we inherit in the constructor
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']).title)
        context['mixin_prop'] = self.get_prop()

        return context

    def get_queryset(self):
        # By default returns the whole list of data, we can modify the queryset
        # Param from url is stored in 'self'. Example self.kwargs['category_id'] (check urls.py for the param)
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    # Default 'modelName_detail' => 'news_detail'
    # Or we can specify which template to use
    # template_name = 'news/news_detail.html'

    # Default 'pk' param should be in urls.py on path string
    # Or we can specify which param to use a 'pk'
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    """
    Needs to connect form_class to FormClass
    """
    form_class = NewsForm
    template_name = 'news/add_news.html'

    # success_url = 'url to redirect after success form submit' or will use get_absolute_url() by default

    # Url to redirect if user is not authenticated
    # login_url = '/admin/'
