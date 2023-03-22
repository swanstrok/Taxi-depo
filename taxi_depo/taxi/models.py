from django.db import models


# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, db_index=True, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    document_number = models.CharField(max_length=30, unique=True, db_index=True,
                                       verbose_name='Номер удостоверения')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')
    cars = models.ManyToManyField(to='Car', related_name='car', verbose_name='Автомобили')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Car(models.Model):
    mark = models.ForeignKey(to='CarManufacturer', on_delete=models.CASCADE,
                             verbose_name='Марка')
    name = models.CharField(max_length=60, db_index=True, verbose_name='Линейка')
    body = models.ForeignKey(to='CarBodyType', on_delete=models.CASCADE,
                             verbose_name='Тип кузова')
    color = models.ForeignKey(to='CarColor', on_delete=models.CASCADE,
                              verbose_name='Цвет')
    characteristics = models.ForeignKey(to='CarCharacteristic', on_delete=models.CASCADE,
                                        verbose_name='Характеристики')

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f'{self.mark} {self.name}'


class CarColor(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Цвет машины')

    class Meta:
        verbose_name = 'Цвет автомобиля'
        verbose_name_plural = 'Цвета автомобиля'

    def __str__(self):
        return self.name


class CarBodyType(models.Model):
    body_type = models.CharField(max_length=20, unique=True, verbose_name='Тип кузова')

    class Meta:
        verbose_name = 'Тип кузова'
        verbose_name_plural = 'Типы кузова'

    def __str__(self):
        return self.body_type


class CarManufacturer(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Произодитель')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.name


class CarCharacteristic(models.Model):
    TYPES = (
        ('Дизель', 'Дизель'),
        ('Бензин', 'Бензин'),
        ('Газ', 'Газ'),
        ('Электро', 'Электро'),
        ('Гибрид', 'Гибрид')
    )

    engine_type = models.CharField(max_length=15, db_index=True, verbose_name='Тип двигателя',
                                   choices=TYPES)
    engine_volume = models.FloatField(verbose_name='Объем двигателя')
    weight = models.PositiveIntegerField(verbose_name='Вес')
    length = models.PositiveIntegerField(verbose_name='Длина')
    width = models.PositiveIntegerField(verbose_name='Ширина')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'

    def __str__(self):
        return f'{self.engine_type} {self.engine_volume}'


class Passenger(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, db_index=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'

    def __str__(self):
        return f'{self.name} {self.surname}'


class Flight(models.Model):
    driver = models.ForeignKey(to='Driver', on_delete=models.CASCADE, verbose_name='Водитель')
    passenger = models.ManyToManyField(to='Passenger', related_name='passenger',
                                       verbose_name='Пассажир')
    date_flight = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')
    address_from = models.CharField(max_length=255, verbose_name='Откуда')
    address_to = models.CharField(max_length=255, verbose_name='Куда')
    is_completed = models.BooleanField(default=False, verbose_name='Завершен')

    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'

    def __str__(self):
        return f'Flight №{self.id}'
