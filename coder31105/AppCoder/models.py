from django.db import models

# Create your models here.

#el tema de las clases vendria a ser algo asi como un servidor de discord y sus usuarios, por eso los distintos canales en la clase "Servidor" y los roles o areas de control de los admins

#el modelo de Usuarios se utiliza para guardar los datos de los que se van a loguear
class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    nickname = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+' '+self.apellido+' nickname: '+self.nickname 

#el modelo de Staff se utiliza para mostrar informacion de los admins de cada area
class Staff(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    area_control = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+' '+self.apellido+' '+self.nickname

#el modelo Servidor se utiliza para ver los distintos canales de un servidor de discord
class Servidor(models.Model):
    canal_1= models.CharField(max_length=50,default='DEFAULT VALUE')
    canal_2= models.CharField(max_length=50,default='DEFAULT VALUE')
    canal_3= models.CharField(max_length=50,default='DEFAULT VALUE')
    
    def __str__(self):
        return 'canal 1: '+self.canal_1+'. canal 2: '+self.canal_2+'. canal 3: '+self.canal_3
