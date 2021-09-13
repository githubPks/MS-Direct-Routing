from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

region =(
    ("sel","Open this menu to select your Region"),
    # ("region1","AMRS"),
    # ("region2","APAC"),
    # ("region3","EMEA"),
    # ("region4","LATAM"),
    ("AMRS","AMRS"),
    ("APAC","APAC"),
    ("EMEA","EMEA"),
    ("LATAM","LATAM"),
)
deal = (
    ("option","open this select menu"),
    ("Lead","Lead"),
    ("Opportunity","Opportunity"),
    ("In Contract","In Contract"),
    ("Won","Won"),
    ("Lost","Lost"),
    ("On Hold","On Hold"),
    ("Cancelled","Cancelled")
)

class UserRequestForm(forms.Form):
    select_region = forms.ChoiceField(choices=region,label='Select Your Region')
    company_name = forms.CharField(max_length=64,label='Comapny Name',widget=forms.TextInput(attrs={'placeholder': 'Comapny Name'}),required=True)
    project_name = forms.CharField(max_length=64,label='Project Name',widget=forms.TextInput(attrs={'placeholder': 'Project Name'}),required=True)
    project_comments = forms.CharField(max_length=64,label= 'Project Comments/Notes',widget=forms.TextInput(attrs={'placeholder': 'Project Comments/Notes'}),required=True)
    first_name = forms.CharField(max_length=64,label='First Name',widget=forms.TextInput(attrs={'placeholder': 'First Name'}),required=True)
    last_name = forms.CharField(max_length=64,label='Last Name',widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),required=True)
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'placeholder': 'Email'}),required=True)
    street_address1 = forms.CharField(max_length=256,label='Street Address One',widget=forms.TextInput(attrs={'placeholder': 'Street Address One'}),required=True)
    street_address2 = forms.CharField(max_length=256, label='Street Address Two',widget=forms.TextInput(attrs={'placeholder': 'Street Address Two'}),required=True)
    city = forms.CharField(max_length=64,label='City',widget=forms.TextInput(attrs={'placeholder': 'City'}),required=True)
    state = forms.CharField(max_length=64,label='State Province',widget=forms.TextInput(attrs={'placeholder': 'State Province'}),required=True)
    postal_code = forms.IntegerField(label='Postal Code',widget=forms.TextInput(attrs={'placeholder': 'Postal Code','type':'number'}),required=True)
    country = forms.CharField(max_length=64,label='Country',widget=forms.TextInput(attrs={'placeholder': 'Country'}),required=True)
    deal_status = forms.ChoiceField(choices=deal,label='Deal Status')
    primary_contact = forms.IntegerField(label='Primary Contact Number',widget=forms.TextInput(attrs={'placeholder': 'Primary Contact Number','type':'number'}),required=True)
    Do_you_require_new_did = forms.BooleanField(required=False)
no_type = (
    ('option','select no type'),
    ('DID','DID'),
    ('TOLL','TOLL')
)

country = (
    ('option','select country'),
    ('USA','USA'),
    ('UK','UK')
)
state = (
    ('option','select state'),
    ('NJ','NJ'),
    ('NY','NY')
)
city = (
    ('option','select city'),
    ('NJ','NJ'),
    ('NY','NY')
)

class DIDProvisonForm(forms.Form):
    number_type = forms.ChoiceField(choices=no_type,label='Number Type')
    country = forms.ChoiceField(choices=country,label='Country')
    state = forms.ChoiceField(choices=state,label='State Province')
    city = forms.ChoiceField(choices=city,label='City')
    max_count = forms.IntegerField(label='Max Count', widget=forms.TextInput(attrs={'placeholder': '50','type':'number'}))
    number_format = forms.IntegerField(label='Number Format', widget=forms.TextInput(attrs={'placeholder': '616-555-1000','type':'number'}))
