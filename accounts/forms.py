from django.db import transaction
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


from accounts.models.user import User
from accounts.models.user import Gestor


class SignInForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        
    )

    codigo = forms.CharField(
        label="Codigo",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        
    )    
    class Meta:
        model = User
        fields = ["nome","codigo","email","contato"]
        widgets = {"nome": forms.TextInput(attrs={"class": "form-control"}),
                   "codigo": forms.TextInput(attrs={"class": "form-control"}),
                   "email": forms.EmailInput(attrs={"class": "form-control"}),
                   "contato": forms.TextInput(attrs={"class": "form-control"})
                   }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print("Aqui ta certo")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Senhas não combinam!")
        return password2
    
    def verificar_codigo(self):
        codigo = self.cleaned_data.get("codigo")
        print("Aqui ta certo codigo")
        if User.objects.filter(codigo=codigo).exists():
            raise ValidationError("Código já existe")
        return codigo
    
   
    def save(self, commit=True):
        user = super().save(commit=False)
        print("Ok")
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class GSignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["nome","codigo","email","contato"]
        widgets = {"nome": forms.TextInput(attrs={"class": "form-control"}),
                   "codigo": forms.TextInput(attrs={"class": "form-control"}),
                   "email": forms.EmailInput(attrs={"class": "form-control"}),
                   "contato": forms.TextInput(attrs={"class": "form-control"})
                   }
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Password didn't match!")
        return password2
    

    def save(self):
        user = super().save(commit=False)
        print("Okkkkk")
        user.is_gestor = True
        user.nome = self.cleaned_data.get('nome')
        user.codigo = self.cleaned_data.get('codigo')
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data["password1"])
        user.save()
        gestor = Gestor.objects.create(user=user)
        gestor.save()
        return user
