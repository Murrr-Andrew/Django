# === Django ORM queries ============================================
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/

# === Lesson 1 ======================================================
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

# === Lesson 2 ======================================================
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

# <field_name>__<filter_name>
# News.objects.filter(pk__gt=1) => pk Greater then 1

# News.objects.filter(pk__gte=1) => pk Greater than or equal to

# News.objects.filter(title__contains='Happy')

# News.objects.filter(pk__in=[1, 2, 3])

# === Lesson 3 ======================================================
# News.objects.first()

# News.objects.last()

# News.objects.order_by('pk').first()

# News.objects.latest('updated_at')

# News.objects.earliest('updated_at')

# Passing a queryset to second query call
# cats = Category.objects.filter(pk__in=[1, 3])
# News.objects.filter(category__in=cats)

# cat1 = Category.objects.get(pk=1)
# cat1.news_set.exists()
# cat1.news_set.count()

# news = News.objects.get(pk=1)
# news.get_next_by_created_at()
# news.get_previous_by_created_at()

# === Lesson 4 ======================================================
# <field_name_foreign_key>__<field_name_origin_model>

# News.objects.filter(category__title='Myself')

# Category.objects.filter(news__title__contains='Happy')

# .distinct() => unique
# Category.objects.filter(news__title__contains='Happy').distinct()

# ====== Q ==========================================================

# from django.db.models import Q

# Q - If needs to use 'OR' operator!
# | - Logical 'OR'
# ~ - logical 'Not'

# News.objects.filter(Q(pk__in=[1, 2]) | Q(title__contains='Awesome'))
# News.objects.filter(Q(pk__in=[1, 2]) | Q(title__contains='Awesome') & ~Q(pk__gt=1))



