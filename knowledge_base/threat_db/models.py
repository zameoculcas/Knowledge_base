from django.contrib.auth import get_user_model
from django.db import models 


User = get_user_model()


class Threat(models.Model):
    source_id = models.CharField(max_length=35) #id used in source db
    pub_date = models.DateField('date of publication')


class ThreatsDescription(models.Model):
    threat = models.ForeignKey(
        'threat_db.Threat', on_delete=models.CASCADE, 
        related_name='related_descriptions'
    )
    name = models.TextField() 
    description = models.TextField()    
    sources_of_threat = models.TextField()
    objects_of_influence = models.TextField()
    confidentiality_violation = models.BooleanField()
    integrity_violation = models.BooleanField()
    accessibility_violation = models.BooleanField()
    pub_date = models.DateField('date of publication')


class TypicalJustificationItems(models.Model):
    threats = models.ManyToManyField('threat_db.Justification')
    text = models.TextField()
    pub_date = models.DateField('date of publication')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='justification_items'
    )


class Justification(models.Model):
    pub_date = models.DateField('date of publication')
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='justifications'
    )
    threat = models.ForeignKey(
        'threat_db.Threat', on_delete=models.CASCADE, 
        related_name='justifications'
    )


class approval(models.Model):
    approval_date = models.DateField()
    justification = models.ForeignKey(
        'threat_db.Justification', on_delete=models.CASCADE, 
        related_name='approval'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='approvals'
    )

