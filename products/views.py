from django.shortcuts import render
from rest_framework import generics, mixins, authentication, permissions
from .mixins import UserQuerySetMixin
from .models import Product
from .serializer import ProductSerializer


class ProductsDetailsView(UserQuerySetMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

products_details_view = ProductsDetailsView.as_view()



class ProductsListCreateAPIView(UserQuerySetMixin, generics.ListCreateAPIView ):      # 1.43
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *arg, **kwarg):   # ????????????????
    #     qs = super().get_queryset(*arg, **kwarg)
    #     request = self.request  # ?????????????????????
    #     if not request.user.is_authenticated:
    #         return qs.none()
    #     return qs.filter(user=request.user)



products_list_create_view = ProductsListCreateAPIView.as_view()



class ProductUpdateAPIView(UserQuerySetMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    def perform_update(self, serializer):
        obj = serializer.save()
        if not obj.content:
            obj.content = obj.title

product_update_view = ProductUpdateAPIView.as_view()



class ProductDestroyAPIView(UserQuerySetMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser]
    # lookup_field = 'pk'
    # def perform_destroy(self, instance):
    #     # instance
    #     super().perform_destroy(instance)     #????????????????????????????????????????????????????????

product_destroy_view = ProductDestroyAPIView.as_view()

########################################################################################################################

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):  # HTTP -> get
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

product_mixin_view = ProductMixinView.as_view()

########################################################################################################################























# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method  # کد دستی
#
#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)
#
#     if method == "POST":
#         # create an item
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)
