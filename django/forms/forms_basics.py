# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):

    'Definimos uma classe que modela um formulário de contato com os campos name, email e message'

    name = forms.CharField(label = 'nome', max_length = 30, required = False)
    email = forms.EmailField(label = 'e-mail')
    is_help = forms.BooleanField(label = 'Ajuda ?', default = False)
    subject = forms.CharField(label = 'assunto', max_length = 30)
    message = forms.CharField(label = 'mensagem', max_length = 255, widget = forms.Textarea)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name) < 2:
            raise forms.ValidationError('Nome muito curto')
        return name

    def clean(self):
        cleaned_data = super().clean()
        is_help = cleaned_data.get('is_help')
        if is_help:
            subject = cleaned_data.get('subject')
            if 'Dúvida' not in subject:
                raise forms.ValidationError(
                    'Assunto %(subject)s -> não especifica a palavra dúvida '
                    'por favor espefique melhor o campo assunto.',
                    code = 'invalid',
                    params = {'subject': subject}
                )


# -> Vinculando dados

>>> form = ContactForm(label_suffix = '', auto_id = 'id_for_%s') # label_suffix por padrão é ':' e auto_id por padrão é 'id_%s'
>>> form.is_bound
False
>>> form = ContactForm({'subject': 'hello'})
>>> form.is_bound
True
>>> form = ContactForm({})
>>> form.is_bound
True

# -> Validando o formulário
# A instância de um Form possui um método is_valid() chame-o com um formulário vinculado e o mesmo validará os dados e retornará um
# booleano. True caso o mesmo possua todos os campos válidos e False caso ao menos um campo esteja inválido.

>>> data = {'name': 'john',
...         'email': 'john@email.com',
...         'is_help': True,
...         'subject': 'Dúvida',
...         'message': 'Escrevo aqui minha dúvida'}
>>> form = ContactForm(data)
>>> form.is_valid()
True

# -> Erro ao validar o formulário
# Ao chamar o método is_valid() numa instância de Form com dados vinculados se o mesmo retornar False o atributo errors conterá
# informações referentes aos campos inválidos.

>>> form = ContactForm({})
>>> form.is_valid()
False
>>> form.errors
{
    'email': ['Este campo é obrigatório.'],
    'subject': ['Este campo é obrigatório.'],
    'message': ['Este campo é obrigatório.']
}

# Você pode acessar errors sem ter que ligar is_valid() primeiro. Os dadosdo formulário serão validados na primeira vez que você
# ligar is_valid() ou acessar errors. 

# -> Form.initial: Usado para declarar os valores iniciais dos campos no formulário em tempo de execução

def create_article(request):

    form = ArticleForm(request.POST or None, initial = {'user': request.user}) 
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_article.html', {'form': form})

# Obs: Se initial for definido no field e também na instanciação do form, o último será usado. Use
# get_initial_for_field(field, field_name) para recuperar os valores iniciais de um campo de formulário
# Ele recupera dados de Form.initial e Field.initial, nessa ordem e avalia todos os valores iniciais que 
# podem podem ser chamados.

# -> Form.has_changed() Retorna True se os dados foram alterados apartir dos dados iniciais(initial) ou False
# caso não.

>>> data = {'name': 'john',
...         'email': 'john@email.com',
...         'is_help': True,
...         'subject': 'Dúvida',
...         'message': 'Escrevo aqui minha dúvida'}
>>> form = ContactForm(request.POST, initial = data)
>>> form.has_changed()
False

# -> Form.changed_data()
# Retorna uma lista com o nome dos campos cujos valores no dados vinculados (geralmente request.POST) diferem
# do qual foi fornecido em initial, retorna uma lista vazia caso nenhum campo tenha sido alterado.

>>> form = ContactForm(request.POST, initial = data)
>>> if form.has_changed():
...     print('Campos alterados: {}'.format(', '.join(form.changed_data)))

# -> Acessando os campos do formulário

>>> form = ContactForm()
>>> for name, type_field in form.fields.items():
...
<django.forms.fields.CharField object at 0x7ffaac632510>
<django.forms.fields.URLField object at 0x7ffaac632f90>
<django.forms.fields.CharField object at 0x7ffaac3aa050> 
>>> form.fields['name']
<django.forms.fields.CharField object at 0x7ffaac6324d0>
>>> form.fields['name'].label = 'Username'

# -> Dados limpos

# -> Form.cleaned_data

>>> data = {'name': 'john',
...         'email': 'john@email.com',
...         'is_help': True,
...         'subject': 'Dúvida',
...         'message': 'Escrevo aqui minha dúvida'}
>>> form = ContactForm(data)
>>> form.is_valid()
True
>>> form.cleaned_data
{'name': 'john',
'email': 'john@email.com',
'is_help': True,
'subject': 'Dúvida',
'message': 'Escrevo aqui minha dúvida'}

# -> Campos opcionais

from django import forms

class OptionPersonForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    nick_name = forms.CharField(required = False)


>>> data = {'first_name': 'John', 'last_name': 'Lennon'}
>>> form = OptionPersonForm(data)
>>> form.is_valid()
True
>>> form.cleaned_data
{'nick_name': '', 'first_name': 'John', 'last_name': 'Lennon'}

# -> Estilos de saída

# -> Form.as_p()
# Renderiza o formulário como uma série de <p> tags com cada tag contendo um campo

# -> Form.as_ul()
# Renderiza o formulário como uma série de <li> tags com cada tag contendo um campo ele não inclui a tag <ul>
# ou </ul> 

# -> Form.as_table()
# Renderiza o formulário de forma padrão, não insere as tags <table> nem </table>

# -> error_class_css
# Lembrando que adicionar as css classes somente no label

class ArticleForm(forms.Form):

    error_css_class = 'error'
    required_css_class = 'required'


# -> Form.auto_id
# -> auto_id pode ser True, False, ou um string
# Se for False o campo não terá o atributo id
# Se for True o atributo id será o nome do campo
# Se for uma string contendo %s o mesmo será substítuido pelo nome do campo exemplo: 
# Para um campo de nome subject, id_for_%s será id_for_subject.
>>> form = ContactForm(auto_id = 'id_for_%s')
>>> print(form)
<tr><th><label for="id_for_subject">Subject:</label></th><td><input id="id_for_subject" type="text" name="subject" maxlength="100" required /></td></tr>


# -> Form.label_suffix
# Uma string será usada após os labels de cada campo por padrão é ':'

>>> form = ContactForm(label_suffix = ' ->')
>>> print(form)
<tr><th><label for="id_for_subject">Subject -></label></th><td><input id="id_for_subject" type="text" name="subject" maxlength="100" required /></td></tr>

# -> Form.use_required_attribute
# Quando definido como True(o padrão), os campos obrigatórios terão o required atributo.

# -> Form.default_renderer

from django import forms

class MyForm(forms.Form):

    default_renderer = MyRenderer() # Especificado em FORM_RENDERER por padrão é 'django.forms.renderers.DjangoTemplates'


# -> Form.field_order
# Por padrão é None que retém a ordem na qual você define os campos no formulário

class MyForm(forms.Form):

    field_order = ['name', 'text']

    text = forms.CharField(label = 'texto', min_length = 10, max_length = 255)
    name = forms.CharField(label = 'nome', min_length = 3, max_length = 30)
    
# Obs: Mesmo definindo os campos como text, name por especificr field_order diferente de None ele usára 
# a ordem passada na lista se nem todos os campos forem especificados, seguirão a sua ordem de definição





# -> ModelForms

from .models import Article

class ArticleModelForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('name', 'description', 'text') # usar '__all__' se quiser utilizar todos os campos do modelo no formulário


# -> Extendendo forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):

    email = forms.EmailField(label = 'E-mail', required = True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email):
            raise forms.ValidationError('Email já em uso')
        return email


# -> Subclasseando formulários

class ContactForm(forms.Form):

	prefix = 'contact' # Prefixo do formulário caso possua vários formulários numa única tag <form>
					   # Campos prefixados (name, for, id)

	name = forms.CharField(label = 'nome', max_length = 30, error_messages = {'required': 'Digite um nome'})
	age = forms.IntegerField(label = 'idade')


class ContactFormWithPriority(ContactForm):
	'Sequência dos campos: name, age, priority se quiser desabilitar um campo da classe base basta fazer '
	'field_name = None'
	CHOICES = ((1, 'Alta'), (2, 'Mediana'), (3, 'Baixa'))
	priority = forms.ChoiceField(choices = CHOICES)
