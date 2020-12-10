from django import forms
from admin.models import *

class RecoveryIdForm(forms.Form):

    c_name = forms.CharField(widget=forms.TextInput,)
    c_phone = forms.IntegerField(widget=forms.NumberInput,)

    class Meta:
        models = customer_tbl

        fields = ['c_name', 'c_phone']

    def __init__(self, *args, **kwargs):
        super(RecoveryIdForm, self).__init__(*args, **kwargs)
        self.fields['c_name'].label = '이름'
        self.fields['c_name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_c_name',
        })
        self.fields['c_phone'].label = '전화번호'
        self.fields['c_phone'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_c_phone'
        })


class RecoveryPwForm(forms.Form):
    user_id = forms.CharField(
        widget=forms.TextInput,)
    name = forms.CharField(
        widget=forms.TextInput,)
    email = forms.EmailField(
        widget=forms.EmailInput,)

    class Meta:
        fields = ['user_id', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_name',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })

