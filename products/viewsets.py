from rest_framework import viewsets, mixins
from .models import Product
from .serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial Update
    delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default


class ProductGenericViewSet(  # 3.24
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # default


product_list_view = ProductGenericViewSet.as_view({'get': 'list'})  # 3.24
product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})  # 3.24
