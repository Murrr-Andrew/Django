# === Django ORM queries ============================================
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/


# ===================================================================
# === Lesson 1 ======================================================
# ===================================================================
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


# ===================================================================
# === Lesson 2 ======================================================
# ===================================================================
# https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

# <field_name>__<filter_name>
# News.objects.filter(pk__gt=1) => pk Greater then 1

# News.objects.filter(pk__gte=1) => pk Greater than or equal to

# News.objects.filter(title__contains='Happy')

# News.objects.filter(pk__in=[1, 2, 3])


# ===================================================================
# === Lesson 3 ======================================================
# ===================================================================
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


# ===================================================================
# === Lesson 4 ======================================================
# ===================================================================
# <field_name_foreign_key>__<field_name_origin_model>

# News.objects.filter(category__title='Myself')

# Category.objects.filter(news__title__contains='Happy')

# .distinct() => unique
# Category.objects.filter(news__title__contains='Happy').distinct()


# ===================================================================
# ====== Q ==========================================================
# ===================================================================
# from django.db.models import Q

# Q - If needs to use 'OR' operator!
# | - Logical 'OR'
# ~ - logical 'Not'

# News.objects.filter(Q(pk__in=[1, 2]) | Q(title__contains='Awesome'))
# News.objects.filter(Q(pk__in=[1, 2]) | Q(title__contains='Awesome') & ~Q(pk__gt=1))


# ===================================================================
# === Lesson 5 ======================================================
# ===================================================================
# News.objects.all()[:2]
# News.objects.all()[1:]
# News.objects.all()[3:5]

# from django.db.models import *
# News.objects.aggregate(Min('views'), Max('views')) => {'views__min': 111, 'views__max': 287}
# News.objects.aggregate(min_views=Min('views'), max_views=Max('views')) => {'min_views': 111, 'max_views': 287}
# News.objects.aggregate(diff=Min('views') - Max('views')) => {'diff': -176}
# News.objects.aggregate(Sum('views')) => {'views__sum': 654}
# News.objects.aggregate(Avg('views')) => {'views__avg': 218.0}


# ===================================================================
# === Lesson 6 ======================================================
# ===================================================================
# .annotate(RULE_FOR_GROUP(resultFieldName='modelName__modelField')) => Like 'Group By'
# cats = Category.objects.annotate(qty=Count('news'))
# for item in cats:
#    print(item.title, item.qty)

# For all categories find the most viewed news in each category
# cats = Category.objects.annotate(max_views=Max('news__views'))
# for item in cats:
#    print(item.title, item.max_views)

# For each category calculate the sum of views in each news
# cats = Category.objects.annotate(sum_views=Sum('news__views'))
# for item in cats:
#    print(item.title, item.sum_views)

# Get only categories which contains news in it (without empty categories)
# cats = Category.objects.annotate(qty=Count('news')).filter(qty__gt=0)
# for item in cats:
#    print(item.title)


# ===================================================================
# === Lesson 7 ======================================================
# ===================================================================
# .values() => needs if we want only to get certain fields from the db
# Its like in SQL SELECT title, views from ....

# news1 = News.objects.values('title', 'views').get(pk=1)

# from django.db import connection
# news = News.objects.values('title', 'views', 'category__title')
# connection.queries


# ===================================================================
# ====== F ==========================================================
# ===================================================================
# Better to user F class when we need to change/retrieve data of fields, instead of directed changes
# from django.db.models import F

# news1 = News.objects.get(pk=1)
# news1.views = F('views') + 1
# news1.save()

# Get all news which in content(field) contains value of the title(field)
# News.objects.filter(content__icontains=F('title'))


# ===================================================================
# ====== SQL ========================================================
# ===================================================================
# from django.db.models.functions import *

# news = News.objects.annotate(length=Length('title')).all()
# for item in news:
#     print(item.title, item.length)


# ===================================================================
# === Lesson 8 === RAW SQL ==========================================
# ===================================================================
# news = News.objects.raw('SELECT * FROM news_news')
# for item in news:
#     print(item.title, item.views)


# Better to pass params and store them with second param as list in .raw(). Use %s for param
# It will prevent from SQL injection

# news = News.objects.raw('SELECT * FROM news_news WHERE title = %s', ['Happy New 2023 Year!'])
# for item in news:
#     print(item.title, item.views)
