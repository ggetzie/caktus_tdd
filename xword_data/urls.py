from django.urls import include, path

import xword_data.views as views

app_name = "xword_data"

urlpatterns = [
    path("answer/<int:pk>",
         views.AnswerView.as_view(),
         name="answer"),
    path("", views.drill, name="drill")
]
