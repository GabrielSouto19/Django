from typing import Any
from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    #auto incrementa na tabela com essa função de AutoField campo automatico
    model = models.CharField(max_length=200)
    #max length o maximo de caracteres  , blank quanod eu criar um campo em branco ele deixa e ele deixa oc
    # boa pratica é colocar o nome das varivaeis em ingles 
    brand = models.ForeignKey(Brand,on_delete=models.PROTECT,related_name="car_brand")
    factory_year = models.IntegerField(blank=True,null=True)
    model_year = models.IntegerField(blank=True,null=True)
    value = models.FloatField(blank=True,null=True)

    def __str__(self):
        return self.model

#Como aplicamos isso tudo ao banco de dados 
