from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
#from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
SUBSCRIPTON = (
    ('F', 'FREE'),
    ('M', 'MONTHLY'),
    ('Y', 'YEARLY')
    )

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_pro = models.BooleanField(default=False)
    pro_expiry_date = models.DateTimeField(null=True, blank=True)
    subscription_type = models.CharField(max_length=100, choices=SUBSCRIPTON, default='FREE' )

class Document(models.Model):
    document_name = models.CharField(max_length=200)
    document_description = RichTextField()
    document_source = models.CharField(max_length=200)
    type_document = models.CharField(max_length=200)
    is_premium = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.document_name)
        super(Document, self).save(*args, **kwargs)

    def __str__(self):
        return self.document_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_description = RichTextField()
    is_premium = models.BooleanField(default=False)
    course_image = models.ImageField(upload_to = 'media/course')
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return self.course_name

class DocumentModule(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    document_module_name = models.CharField(max_length=100)
    can_view = models.BooleanField(default=True)


