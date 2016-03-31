from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User

TYPE_CHOICES = (
        ('Bar Graph', 'Bar Graph'),
        ('Line Graph', 'Line Graph'),
        ('Pie Graph','Pie Graph'),
    )

class Graph(models.Model):
    	name=models.CharField(max_length=30,blank=False)
    	type_Of_Graph=models.CharField(max_length=10,choices=TYPE_CHOICES,default=1,blank=False)
        x_Attribute=models.CharField(max_length=10,blank=False)
        y_Attribute=models.CharField(max_length=10,blank=False)
        file_csv=models.FileField(upload_to='files/',default='/no-file.csv',blank=False)

    	class Admin:
    				pass

    	def __str__(self):
    		return '%s,%s,%s,%s,%s\n' % (self.x_Attribute,self.y_Attribute,self.file_csv,self.type_Of_Graph,self.name)



class Number(models.Model):
        ID_Of_Graph=models.CharField(max_length=10,default=1)

        class Admin:
                    pass

        def __str__(self):
            return '%s' %(self.ID_Of_Graph)

class Clients(models.Model):
        name_Of_User=models.CharField(max_length=30,blank=False)
        email=models.EmailField(blank=False)
        password=models.CharField(max_length=20,blank=False,default='1234')
        client=models.ForeignKey(User,default=0)

        class Admin:
                    pass

        def __str__(self):
            return '%s,%s' % (self.name_Of_User,self.email)
