from django import forms
from .models import GelirGider, AlacakVerecek, CekSenet, Fis, Fatura, Veresiye, Kategori
from common.base_forms import BaseForm, DateInput

class KategoriForm(BaseForm):
    class Meta:
        model = Kategori
        fields = ['ad', 'tür']

class GelirGiderForm(BaseForm):
    class Meta:
        model = GelirGider
        fields = ['tür', 'tutar', 'açıklama', 'kategori']
        widgets = {
            'açıklama': forms.Textarea(attrs={
                'class': 'form-textarea rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Açıklama Giriniz',
                'rows': 4,
            }),
            'kategori': forms.Select(attrs={
                'class': 'form-select rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
            }),
        }

class AlacakVerecekForm(BaseForm):
    class Meta:
        model = AlacakVerecek
        fields = ['kişi', 'tür', 'tutar', 'son_odeme_tarihi', 'durum']
        widgets = {
            'son_odeme_tarihi': DateInput(),
        }

class CekSenetForm(BaseForm):
    class Meta:
        model = CekSenet
        fields = ['tür', 'numara', 'tutar', 'tarih', 'durum']
        widgets = {
            'tarih': DateInput(),
        }

class FisForm(BaseForm):
    class Meta:
        model = Fis
        fields = ['tür', 'tutar', 'tarih', 'açıklama']
        widgets = {
            'açıklama': forms.Textarea(attrs={
                'class': 'form-textarea rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Açıklama Giriniz',
                'rows': 4,
            }),
            'tarih': DateInput(),
        }

class FaturaForm(BaseForm):
    class Meta:
        model = Fatura
        fields = ['numara', 'müşteri', 'tutar', 'tarih', 'kdv_oranı']
        widgets = {
            'numara': forms.TextInput(attrs={
                'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Fatura Numarasını Giriniz',
            }),
            'müşteri': forms.TextInput(attrs={
                'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Müşteri İsmini Giriniz',
            }),
            'kdv_oranı': forms.NumberInput(attrs={
                'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'KDV Oranını Giriniz',
            }),
            'tarih': DateInput(),
        }

class VeresiyeForm(BaseForm):
    class Meta:
        model = Veresiye
        fields = ['kişi', 'tutar', 'son_odeme_tarihi', 'durum', 'alacak_verecek']
        widgets = {
            'kişi': forms.TextInput(attrs={
                'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Kişi İsmini Giriniz',
            }),
            'tutar': forms.NumberInput(attrs={
                'type': 'number',
                'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                'placeholder': 'Tutar Giriniz',
            }),
            'son_odeme_tarihi': DateInput(),
            'alacak_verecek': forms.Select(attrs={
                'class': 'form-select rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
            }),
        }