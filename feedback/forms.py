from django import forms
from .models import Feedback


class FeedbackForms(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # fields = ['name', 'surname', 'rating']
        # exclude = ['rating']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'rating': 'Рейтинг',
            'feedback': 'Отзыв',

        }
        error_messages = {
            'name': {'max_length': 'ой как много символов',
                     'min_length': 'ой как мало символов',
                     'required': 'Не должно быть пустым'
                     },
            'surname': {'max_length': 'ой как много символов',
                        'min_length': 'ой как мало символов',
                        'required': 'Не должно быть пустым'
                        },
            'feedback': {'max_length': 'ой как много символов',
                         'min_length': 'ой как мало символов',
                         'required': 'Не должно быть пустым'
                         },
        }
