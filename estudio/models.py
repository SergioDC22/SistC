from xmlrpc.client import boolean
from django.db import models

# Create your models here.
class Impuesto(models.Model):
    idImpuesto = models.AutoField(primary_key=True)
    nombreImpuesto= models.CharField(max_length=30, verbose_name='Nombre')

    def __str__(self):
        fila= "ID: "+ str(self.idImpuesto)+" - "+"Nombre del Impuesto: "+ self.nombreImpuesto
        return fila

class  Cliente(models.Model):
    idCli=models.AutoField(primary_key=True)
    CUIT=models.IntegerField()
    claveFiscal=models.CharField(max_length=64, verbose_name="claveFiscal")
    RazonSocial=models.CharField(max_length=50, verbose_name="RazonSocial")
    isEstado=models.BooleanField()

    def __str__(self):
        fila= "Id Cliente: "+str(self.idCli)+" - "+"CUIT: "+str(self.CUIT)+" - "+"Clave Fiscal: "+str(self.claveFiscal)+" - "+"Razon Social: "+self.RazonSocial+ " - "+"Estado: "+ str(self.isEstado)
        return fila