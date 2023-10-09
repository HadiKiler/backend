from rest_framework import serializers


# method 1 ---- other_products

class ProductInlineSerializer(serializers.Serializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk', read_only=True)    # read only ?????
    title = serializers.CharField(read_only=True)    # read only ?????


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)    # read only ?????
    id = serializers.CharField(read_only=True)  # read only ?????
    other_products = serializers.SerializerMethodField(read_only=True)

    def get_other_products(self, obj):
        user = obj
        other_qs = user.product_set.all()[:5]
        return ProductInlineSerializer(other_qs, many=True, context=self.context).data  # what is context ??????????
