from django.contrib import admin
from cars.models import Car,Brand

# Register your models here.

#Temos que registrar nosso modelo de carro aqui 

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CarAdmin(admin.ModelAdmin):#classe pronta do django a de ModelAdmin
    list_display = ('model','brand','factory_year','model_year','value',)#estamos subescrevendo os campos que vem por padrão no ModelAdmin
    search_fields = ('model','brand')
    #seach field me permite fazer busca no campo de busca


admin.site.register(Brand,BrandAdmin)
admin.site.register(Car,CarAdmin)