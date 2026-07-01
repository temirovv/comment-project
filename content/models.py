from django.db import models


class People(models.Model):
    full_name = models.CharField(max_length=255, help_text="Komentator ismi")
    phone_number = models.CharField(max_length=12, help_text="Telefon raqami")
    written_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Comment(models.Model):
    title = models.CharField(max_length=255, help_text="Sarlavhasi")
    full_comment = models.CharField(max_length=1000, help_text="to'liq komment")

    people = models.ForeignKey(People, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment of {self.people}"
