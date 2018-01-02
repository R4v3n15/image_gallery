import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

#Write the models for DB tables
class Album(models.Model):
    title       = models.CharField(max_length=70)
    description = models.TextField(max_length=1024)
    thumb       = ProcessedImageField(
								    	upload_to='albums', 
									    processors=[ResizeToFit(300)], 
									    format='JPEG', 
									    options={'quality': 85}
								    )
    tags        = models.CharField(max_length=250)
    is_visible  = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    modified    = models.DateTimeField(auto_now_add=True)
    slug        = models.SlugField(max_length=50, unique=True)

    #Python 2
    def __unicode__(self):
        return self.title
    
    #Python 3
    def __str__(self):
        return self.title

class AlbumImage(models.Model):
    image   = ProcessedImageField(upload_to='albums', 
							      processors=[ResizeToFit(1280)], 
							      format='JPEG', 
							      options={'quality': 85}
							      )
    thumb   = ProcessedImageField(upload_to='albums', 
						    	  processors=[ResizeToFit(300)], 
						    	  format='JPEG', 
						    	  options={'quality': 85}
						    	  )
    album   = models.ForeignKey('album', on_delete=models.CASCADE,)
    alt     = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width   = models.IntegerField(default=900)
    height  = models.IntegerField(default=506)
    slug    = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)