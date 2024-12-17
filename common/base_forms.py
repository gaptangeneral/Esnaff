# common/base_forms.py

from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class BaseForm(forms.ModelForm):
    """Tüm formlar için Tailwind uyumlu ortak yapılandırma"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Ortak stil ayarları
            field.widget.attrs.update({
                'class': 'w-full rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500',
            })

            # TextInput ve NumberInput için özel stil ayarları
            if isinstance(field.widget, (forms.TextInput, forms.NumberInput)):
                field.widget.attrs.update({
                    'class': field.widget.attrs['class'] + ' px-4 py-2', 
                    'placeholder': field.label,
                })

            # Textarea için özel stil ayarları
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({
                    'class': field.widget.attrs['class'] + ' px-4 py-2',
                    'placeholder': field.label,
                    'rows': 4,
                })

            # Select için özel stil ayarları
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs.update({
                    'class': field.widget.attrs['class'] + ' px-4 py-2',
                })

            # CheckboxInput için özel stil ayarları
            elif isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({
                    'class': 'form-checkbox text-blue-500 h-4 w-4',
                })

            # DateInput için özel stil ayarları
            elif isinstance(field.widget, forms.DateInput):
                field.widget.attrs.update({
                    'type': 'date',
                    'class': 'form-input rounded-lg border-gray-300 focus:ring-blue-500 focus:border-blue-500 w-full',
                    'placeholder': 'Tarih seçiniz',
                })
                 # Hata durumunda ek sınıf ekleyin
           
