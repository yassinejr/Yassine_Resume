from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender", null=True)
    email = models.EmailField(max_length=200,null=True)
    subject = models.CharField(max_length=200,null=True)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" + self.email
