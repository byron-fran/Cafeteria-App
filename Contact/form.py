from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100, required=True, 
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField(label='email', required=True, 
                            widget=forms.EmailInput(attrs={'class': 'form-control'}),
                            max_length=100, min_length=2)
    	
    message = forms.CharField(label='Describe your problem', 
                            widget=forms.Textarea(
                                attrs={'class': 'form-control', 
                                       'rows': 5, 
                                       'placeholder': 'Describe your problem',
                                       }), 
                            required=True, max_length=1000, min_length=2)
    
    