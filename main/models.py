from django.db import models


class Item(models.Model):
    """
    Stores a single item entry.
    """
    name = models.CharField(
        verbose_name='Название',
        max_length=150
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price_as_int = models.IntegerField(
        verbose_name='Цена',
        help_text='For example, 15.90 should be 1590.'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def price(self):
        """
        Displays the price of the item in a normal way (as a decimal).
        """
        return "{0:.2f}".format(self.price_as_int / 100)


class Order(models.Model):
    items = models.ManyToManyField(Item, through='OrderItem')
    payment_intent_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        return sum(order_item.item.price for order_item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
