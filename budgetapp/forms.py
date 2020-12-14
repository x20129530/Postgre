from django import forms 

class ExpenseForm(forms.Form):
    title = forms.CharField()
    amount = forms.DecimalField(max_digits=8 , decimal_places=2)
    category = forms.CharField()