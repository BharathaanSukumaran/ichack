from django import forms

# Create your forms here.

class ItemForm(forms.Form):
	ingredient = forms.CharField(max_length = 50)
	amount = forms.CharField(max_length = 50)
	units = forms.CharField(max_length = 150)
	expiry_date = forms.CharField(widget = forms.SelectDateWidget, max_length = 2000)