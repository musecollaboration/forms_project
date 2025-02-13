from django import forms


class FeedbackForms(forms.Form):
    name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
        'max_length': 'Нужно меньше символов',
        'min_length': 'Нужно больше символов',
        'required': 'Нужен хотя бы один символ'
    })
    surname = forms.CharField()
    rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)
    feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
