from django import forms 

from .models import reg

class PostForm(forms.ModelForm):

	class Meta:
		model = reg
	
		fields = '__all__'
