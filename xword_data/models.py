from django.db import models

class Puzzle(models.Model):
    title = models.CharField("Title",
                             default="",
                             max_length=255,
                             blank=True)
    date = models.DateField("Publication Date")
    byline = models.CharField("Byline", max_length=255)
    publisher = models.CharField("Publisher", max_length=12)

    class Meta:
        db_table = "puzzles"

    def __str__(self):
        return f"{self.date} - {self.publisher}"

    
class Entry(models.Model):
    entry_text = models.CharField("Entry Text",
                                  max_length=50,
                                  unique=True)

    class Meta:
        db_table = "entries"
        verbose_name_plural = "Entries"

    def __str__(self):
        return f"{self.entry_text}"


class Clue(models.Model):
    entry = models.ForeignKey(Entry,
                              on_delete=models.SET_NULL,
                              null=True)
    puzzle = models.ForeignKey(Puzzle,
                               on_delete=models.SET_NULL,
                               null=True)
    clue_text = models.CharField("Clue Text",
                                 max_length=512)
    theme = models.BooleanField("Theme", default=False)

    class Meta:
        db_table = "clues"

    def __str__(self):
        return f"{self.clue_text} - {self.entry.entry_text}"
                                 
    
