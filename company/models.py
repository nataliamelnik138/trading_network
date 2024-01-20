from django.db import models


class Company(models.Model):
    """
    Модель компании в иерархии сети по продаже электроники.
    Компания может быть заводом, розничной сетью или индивидуальным предпринимателем
    """
    name = models.CharField(max_length=200, verbose_name='название компании')
    company_type_choices = [
        ('factory', 'Завод'),
        ('retail_network', 'Розничная сеть'),
        ('individual_entrepreneur', 'Индивидуальный предприниматель'),
    ]
    company_type = models.CharField(
        max_length=23,
        choices=company_type_choices,
        verbose_name='тип компании'
    )
    email = models.EmailField(max_length=150, verbose_name='email')
    country = models.CharField(max_length=150, verbose_name='страна')
    city = models.CharField(max_length=150, verbose_name='город')
    street = models.CharField(max_length=150, verbose_name='улица')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='clients',
                                 verbose_name='поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность перед поставщиком')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return self.name

    @property
    def hierarchy_level(self):
        """
        Определяет и возвращает уровень иерархии компании.
        Заводы всегда находятся на 0 уровне. Для розничных сетей и индивидуальных предпринимателей уровень иерархии
        зависит от типа их поставщика. Если поставщик не указан, уровень считается максимальным.
        :return: уровень иерархии компании
        """
        # Завод всегда находится на 0 уровне
        if self.company_type == 'factory':
            return 0

        # Если поставщик не указан, считаем уровень максимальным
        if not self.supplier:
            return 2

        # В противном случае определяем уровень на основе поставщика
        return self.supplier.hierarchy_level + 1

    class Meta:
        verbose_name = 'компания'
        verbose_name_plural = 'компании'


class Product(models.Model):
    """
    Модель продукта, который продается компанией
    """
    name = models.CharField(max_length=200, verbose_name='название товара')
    model = models.CharField(max_length=200, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    company = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE,
                                verbose_name='компания-владелец')

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
