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
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='For example, 15.90 should be 1590.'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_price(self):
        """
        Displays the price of the item in a normal way (as a decimal).
        """
        return "{0:.2f}".format(self.price / 100)
