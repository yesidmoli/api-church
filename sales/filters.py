import django_filters

from sales.models.sale import Sale

#filter the sale with product name and status
class SaleFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(field_name='product__name')
    status = django_filters.ChoiceFilter(
        field_name='status',
        choices=(('Pagada', 'Pagada'), 
                 ('A Crédito', 'A Crédito'))
    )
    id = django_filters.CharFilter(
        field_name= 'product__id'
    )

    class Meta:
        model = Sale
        fields = ['product', 'status']