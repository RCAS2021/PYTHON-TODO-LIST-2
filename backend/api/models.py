from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    # Adding title
    title = models.CharField(max_length=100)
    # Adding content text field
    content = models.TextField()
    # Adding created time auto generated
    created_at = models.DateTimeField(auto_now_add=True)
    # Adding author, links to User, on user deletion, also delete notes,
    # related_name tells what field name on user references all notes
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return str(self.title)
