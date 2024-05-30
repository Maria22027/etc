from django import forms
from app.models import Usuario



#define o formulário
class FormuUsuario(forms.ModelForm):

#dados do formulário
    class Meta:

#modelo utilizado (tabela)
        model = Usuario

#campos que devem aparecer no form
        fields = ('nome','email')