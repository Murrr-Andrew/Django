# === Django ORM queries ======
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

# === Lesson 1 ======
# from news.models import News, Category

# News.objects.all()

# News.objects.order_by('pk')

# News.objects.get(pk=1)

# <name connected model>_set => To get data by the category (From Category to News [reversed way])(default attr)
# cat3 = Category.objects.get(pk=3)
# cat3.news_set.all()

# If specified 'related_name' in model on field attr like: related_name='get_news'
# Example: category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='get_news')
# cat3.get_news.all()

# === Lesson 2 ======
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

# <field_name>__<filter_name>
# News.objects.filter(pk__gt=1) => pk Greater then 1

# News.objects.filter(pk__gte=1) => pk Greater than or equal to

# News.objects.filter(title__contains='Happy')

# News.objects.filter(pk__in=[1, 2, 3])

# === Lesson 3 ======

