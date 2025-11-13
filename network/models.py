from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100, blank=True, null=True)
    year = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.name

class Connection(models.Model):
    student1 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='connections_from')
    student2 = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='connections_to')

    def __str__(self):
        return f"{self.student1} ↔ {self.student2}"
