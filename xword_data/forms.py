from django import forms
from django.core.exceptions import ValidationError

from xword_data.models import Entry, Clue, Puzzle

class AnswerForm(forms.Form):
    answer = forms.CharField( max_length=50)
    clue_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean_answer(self):
        answer = self.cleaned_data["answer"]
        return answer.upper()

    def clean(self):
        cleaned_data = super().clean()
        clue = Clue.objects.get(id=cleaned_data["clue_id"])
        if not clue.entry.entry_text == cleaned_data["answer"]:
            raise ValidationError(f"{cleaned_data['answer']} is not correct")
        else:
            return cleaned_data



            
