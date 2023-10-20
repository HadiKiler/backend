from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from products.models import Product


@register(Product)
class ProductIndex(AlgoliaIndex):
    should_index = "has_offer"
    fields = [
        'user',
        'title',
        'content',
        'price',
        'is_offer'
    ]
    tags = 'get_tags_list'

