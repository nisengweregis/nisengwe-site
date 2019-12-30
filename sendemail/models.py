from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=50)
    from_email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.subject} {self.from_email}'

