from django import forms
from accounts.models.user import User

from relatorio.models import Equipe 
     
class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, funcionario):
        return "%s" % funcionario.email 
  
  
class EquipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(EquipeForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = User.objects.all()
        
    class Meta:
       
        model = Equipe
        fields = ['nome','codigoV','contato','funcionario']
        
    funcionario = CustomMMCF(queryset=None,
                            widget=forms.CheckboxSelectMultiple)
