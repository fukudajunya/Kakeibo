from django import forms
from .models import Kakeibo
import bootstrap_datepicker_plus as datetimepicker


class KakeiboForm(forms.ModelForm):
    """
    新規データ登録用画面のフォーム定義
    """
    class Meta:
        model = Kakeibo
        fields = ["date", "category", "money", "memo"]
        widgets = {
            "date": datetimepicker.DatePickerInput(
                format= '%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            "category" : forms.Select(attrs={'size':1}),
        }
