import random
from django.conf import settings
from django.db import models
from django.db.models import Q
from django.conf import settings

User = settings.AUTH_USER_MODEL  # ????????????????????


TAGS_MODEL_VALUES = ['electronics', 'cars', 'boats', 'movies', 'cameras']

class ProductQuerySet(models.QuerySet):
    # def is_offer(self):
    #     return self.filter(is_offer=True)

    def search(self, query, user=None):
        lookup = Q(title__icontains=query) | Q(content__icontains=query)    # کیو در اینجا اقدام به تولید شرط میکند که ما ان را در پرانتر فیلتر قرار میدهیم
        # qs = self.is_offer().filter(lookup)     # 4.39.42                 # و با استفاده از ان میتوانیم دو شرط را در یک فیلتر اجرا کنیم
        qs = self.filter(lookup)
        if user is not None:
            qsu = self.filter(user=user).filter(lookup)
            qs = (qs | qsu).distinct()
        return qs


class ProductManger(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)   # ????????????

    def search(self, query, user=None):
        return Product.objects.search(query, user)


class Product(models.Model):
    # pk
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    is_offer = models.BooleanField(default=False)
    objects = ProductManger()

    # objects = ProductQuerySet.as_manager()
    # exp = Expensive()

    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUES)]

    def has_offer(self) -> bool:
        return self.is_offer
    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)

    def get_discount(self):
        return "122"

    def __str__(self):
        return self.title

#    ======= a test for model.Manger and the QuerySet =======
# https://buildatscale.tech/what-is-django-model-manager/#:~:text=Django%20Model%20Manager%20is%20the,to%20use%20custom%20model%20managers.

# class ProductQuerySet(models.QuerySet):
#     def no_content(self):
#         return self.filter(content__iexact="")
#     def with_content(self):
#         return self.exclude(content__iexact="")
#
# class Expensive(models.Manager):
#     def get_queryset(self):
#         return ProductQuerySet(self.model).filter(price__gt=99.99)
#     def no_content(self):
#         return self.get_queryset().no_content()
#     def with_content(self):
#         return self.get_queryset().with_content()
