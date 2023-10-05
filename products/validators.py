from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


def validate_title(value):  # 3.47  validating_method_2
    qs = Product.objects.filter(title__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f'{value} is already a product name.')
    return value


uniq_product_title = UniqueValidator(queryset=Product.objects.all()) #یک فانشکن اماده است که به ولیدیتور های فیلدی که میخواهیم یونیک باشد اعطا میشود
                                                                        #  و صد البته در سریالایزر استفاده میشود