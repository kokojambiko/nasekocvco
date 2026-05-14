from django.db import models


class Order(models.Model):

    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('progress', 'В работе'),
        ('ready', 'Готов'),
        ('done', 'Выдан'),
        ('cancel', 'Отменено'),
    ]

    PAYMENT_STATUS = [
        ('unpaid', 'Не оплачено'),
        ('partial', 'Частично'),
        ('paid', 'Оплачено'),
    ]

    client_name = models.CharField(
        max_length=255,
        verbose_name='Имя клиента'
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        verbose_name='Телефон'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )

    order_type = models.CharField(
        max_length=255,
        verbose_name='Вид заказа'
    )

    order_details = models.TextField(
        verbose_name='Данные заказа'
    )

    extra_info = models.TextField(
        blank=True,
        verbose_name='Дополнительные данные'
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Оплата'
    )

    prepayment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Предоплата'
    )

    remaining = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Остаток'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Готовность заказа'
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='unpaid'
    )

    def save(self, *args, **kwargs):

        self.remaining = self.total_price - self.prepayment

        if self.prepayment <= 0:
            self.payment_status = 'unpaid'

        elif self.remaining > 0:
            self.payment_status = 'partial'

        else:
            self.payment_status = 'paid'

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.client_name} - {self.order_type}"