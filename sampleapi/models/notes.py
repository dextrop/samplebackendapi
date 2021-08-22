from django.db import models

class Notes(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    Title = models.CharField(default="", max_length=200)
    Description = models.CharField(default="", max_length=1000)
    Link = models.CharField(default="", max_length=1000)
    Image = models.CharField(default="", max_length=1000)
    Category = models.CharField(default="", max_length=1000)

    _created = models.DateTimeField(auto_now_add=True)
    _updated = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Notes, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self._id)

    class Meta:
        db_table = 'notes'
        app_label = 'sampleapi'
