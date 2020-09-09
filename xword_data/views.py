from collections import Counter
import random

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, DetailView

from xword_data.models import Puzzle, Entry, Clue
from xword_data.forms import AnswerForm

def drill(request):
    if request.POST:
        data = request.POST.copy()
        form = AnswerForm(data)

        if form.is_valid():
            success_url = reverse("xword-answer",
                                  args=[form.cleaned_data["clue_id"]])
            correct = request.session.get("correct", 0)
            request.session["correct"] = correct + 1
            return redirect(success_url + "?success")
        clue = Clue.objects.get(id=form.cleaned_data["clue_id"])
    else:
        clue = random.choice(Clue.objects.all())
        form = AnswerForm(initial={"clue_id": clue.id})
    attempts = request.session.get("attempts", 0)
    request.session["attempts"] = attempts + 1
    return render(request,
                  "xword_data/drill.html",
                  context={"clue": clue,
                           "clue_id": clue.id,
                           "form": form})

        
class AnswerView(DetailView):
    model = Clue
    template_name = "xword_data/answer.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["success"] = "success" in self.request.GET
        all_clues = Clue.objects.filter(clue_text=self.object.clue_text)
        if all_clues.count() > 1:
            clue_count = Counter([c.entry.entry_text for c in list(all_clues)])
            context["clue_count"] = list(clue_count.items())
        return context
