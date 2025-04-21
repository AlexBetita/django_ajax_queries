from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name       = models.CharField(max_length=100)
    category   = models.ForeignKey(
                    Category,
                    on_delete=models.SET_NULL,
                    null=True,
                    blank=True,
                )
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    ad_id = models.IntegerField(null=True, blank=True)
    ad_type = models.CharField(max_length=50, null=True, blank=True)
