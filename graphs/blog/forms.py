from django import forms
from django.forms import ModelForm

from .models import Graph,Number,Clients


class GraphForm(ModelForm):
	class Meta:
		model=Graph
		fields=['name','type_Of_Graph','x_Attribute','y_Attribute','file_csv']

class NumberForm(ModelForm):
	class Meta:
		model=Number
		fields=['ID_Of_Graph']

class UserForm(ModelForm):
	class Meta:
		model=Clients
		fields=['name_Of_User','email','password']
