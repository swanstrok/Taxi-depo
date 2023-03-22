from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(CarColor)
admin.site.register(CarManufacturer)
admin.site.register(CarBodyType)


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver', 'address_from', 'address_to', 'date_flight', 'is_completed')
    list_filter = ('is_completed', 'date_flight', 'driver')
    list_editable = ('is_completed',)
    filter_horizontal = ('passenger',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'age', 'document_number', 'phone')
    filter_horizontal = ('cars',)
    list_display_links = ('id', 'surname', 'document_number')


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'email', 'phone')
    list_display_links = ('surname', 'email')


# class CarCharacteristicsInline(admin.TabularInline):
#     model = CarCharacteristic
#     # raw_id_fields = ['engine_type']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('mark', 'name', 'body', 'color', 'characteristics')
    list_filter = ('mark', 'body')
    list_display_links = ('mark', 'name')


class CarTabular(admin.TabularInline):
    model = Car
    raw_id_fields = ['characteristics']


@admin.register(CarCharacteristic)
class CarCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('engine_type', 'engine_volume', 'weight', 'length', 'width')
    list_filter = ('engine_type',)
    inlines = [CarTabular]
