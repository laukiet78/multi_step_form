from django import forms

class Step1Form(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)


class Step2Form(forms.Form):
    local_address = forms.CharField(label='Local Address', max_length=200)
    permanent_address = forms.CharField(label='Permanent Address',
             max_length=200)

class Step3Form(forms.Form):
    images = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'multiple': True}))
    
   