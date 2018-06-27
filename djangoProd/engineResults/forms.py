from django import forms

class QuestionForm(forms.Form):
    your_question = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['your_question'].widget = forms.TextInput(attrs={
        'class': 'form-control input-lg',
        'name': 'questionInput',
        'type': 'text',
        'placeholder': 'What is human right?'})

