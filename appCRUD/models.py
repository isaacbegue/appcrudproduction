from django.db import models		
		
# Create your models here.		
		
class Tarea(models.Model):		
	tarea = models.CharField(max_length=50)	
	descripcion = models.CharField(max_length=150)
	def __str__(self):	
		return self.tarea, self.descripcion
		