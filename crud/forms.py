from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label='Имя')
    age = forms.IntegerField(label='Возраст', error_messages={
        'required': 'Поле обязательно для заполнения',
        'max_value': 'Возраст не может быть больше 100',
        'min_value': 'Возраст не может быть меньше 0',
    })

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)
    price = forms.IntegerField()