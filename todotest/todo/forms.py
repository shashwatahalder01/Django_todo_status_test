from django import forms




class todoform(forms.Form):
    taskname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'task name'}))
    status = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'status'}))
    

    