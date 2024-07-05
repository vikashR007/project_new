#Decision models:

from django.db import models

class Decision(models.Model):
    decision = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'Decision: {self.decision}'
  
#File_category:

from django.db import models

class FileCategory(models.Model):
    file_category = models.CharField(max_length=255, null=False)
    mute = models.BooleanField(default=False)

    def __str__(self):
        return self.file_category
    

#Reviewer Specialization:
from django.db import models
from django.contrib.auth.models import User

class Specialization(models.Model):
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.specialization

class Reviewer_Specialization(models.Model):
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reviewer.user.username} - {self.specialization.specialization}'
    

  
    
#Reviewer Invitation
 
from django.db import models
from .models import Submission

class ReviewerInvitation(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    date = models.DateField()
    expiring_date = models.DateField()

    def __str__(self):
        return f'Reviewer: {self.name} ({self.email}), Submission: {self.submission.title}'




