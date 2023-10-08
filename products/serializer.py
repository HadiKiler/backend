from rest_framework import serializers
from products.models import Product
from rest_framework.reverse import reverse
from .validators import validate_title, uniq_product_title


class ProductSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    detail_url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field='pk')    # 3.32
    # send_email = serializers.EmailField(write_only=True)   # 3.33
    title = serializers.CharField(validators=[uniq_product_title])  # 3.47  validating_method_2  # 3.50 validate_title or uniq_product_title
    class Meta:     #1111
        model = Product
        fields = [
            # 'url',
            # 'send_email',
            'detail_url',
            'edit_url',
            'id',
            'title',
            'content',
            'price',
            'sale_price',
        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request != None:
            return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
        return None

    # def validate_title(self, value):    # validate_<field name>  3.45  validating_method_1
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f'{value} is already a product name.')
    #     return value

    # def create(self, validated_data):  # 3.33
    #     send_email = validated_data.pop('send_email')
    #     # return Product.objects.create(**validated_data)
    #     return super().create(validated_data)    # ??????????????????
