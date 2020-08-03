from django.db import models


class Treat(models.Model):
    source_id = models.CharField()
    name = models.TextField() 
    description = models.TextField()    
    sources_of_threat = models.CharField()
    objects_of_influence = models.CharField()
    confidentiality_violation = models.BooleanField()
    integrity_violance = models.BooleanField()
    accessibility violation = models.BooleanField()
    pub_date = models.DateField('date of publication')
    mod_date = models.DateField('date of modification')

class Justification(models.Model):
    threat = models.ForeignKey(
        'Treat', on_delete=models.CASCADE, related_name='related_threat'
    )
    mod_date = models.DateField('date of modification')



     






    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author'
    )
    group = models.ForeignKey(
        'posts.Group', on_delete=models.CASCADE, blank=True, null=True, 
        related_name='post_group'
    )   
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    
    def __str__(self):
        return self.text
