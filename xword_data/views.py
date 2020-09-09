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
            success_url = reverse("xword_data:answer",
                                  args=[form.cleaned_data["clue"]])
            return redirect(success_url + "?success")
        clue = Clue.objects.get(id=form.cleaned_data["clue"])
    else:
        clue = random.choice(Clue.objects.all())
        form = AnswerForm(initial={"clue": clue.id})
    return render(request,
                  "xword_data/drill.html",
                  context={"clue": clue,
                           "form": form})

        
class AnswerView(DetailView):
    model = Clue
    template_name = "xword_data/answer.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["success"] = "success" in self.request.GET
        return context
