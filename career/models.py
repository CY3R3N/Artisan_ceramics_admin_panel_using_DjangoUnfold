from django.db import models

class Job(models.Model):
    JOB_TYPES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('CT', 'Contract'),
        ('IN', 'Internship'),
    ]
    JOB_LOCATION = [
        ('Head Office', 'Head Office'),
        ('Factory', 'Factory'),
    ]

    position = models.CharField(max_length=100, verbose_name="Job Title")
    job_type = models.CharField(max_length=2, choices=JOB_TYPES, verbose_name="Job Type")
    location = models.CharField(max_length=50, choices=JOB_LOCATION, verbose_name="Location")
    salary = models.CharField(max_length=32, verbose_name="Salary")
    vacancy = models.PositiveIntegerField(verbose_name="Vacancy")
    deadline = models.DateField(verbose_name="Deadline")
    description = models.TextField(verbose_name="Job Description")

    def __str__(self):
        return self.position
