from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

from .consts import COLORS

User = get_user_model()

# Create your models here.
class Skill(models.Model):
  class Meta:
    verbose_name_plural = 'Skills'
    verbose_name = 'Skill'
  
  name = models.CharField(max_length=20, blank=True, null=True)
  score = models.IntegerField(default=80, blank=True, null=True)
  image = models.FileField(blank=True, null=True, upload_to='skills')
  is_key_skill = models.BooleanField(default=False)
  is_main = models.BooleanField(default=False)

  def __str__(self):
    return self.name
  
class UserProfile(models.Model):
  class Meta:
    verbose_name_plural = 'User Profiles'
    verbose_name = 'User Profile'
  
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(blank=True, null=True, upload_to="avatar")
  title = models.CharField(max_length=200, blank=True, null=True)
  bio = models.TextField(blank=True, null=True)
  skills = models.ManyToManyField(Skill, blank=True)
  cv = models.FileField(blank=True, null=True, upload_to="cv")

  def __str__(self):
    return f"{self.user.first_name} {self.user.last_name}"

class ContactProfile(models.Model):
  class Meta:
    verbose_name_plural = "Contact Profiles"
    verbose_name = "Contact Profile"
    ordering = ["timestamp"]
  
  timestamp = models.DateTimeField(auto_now_add=True)
  name = models.CharField(verbose_name="Name", max_length=100)
  email = models.EmailField(verbose_name="Email")
  message = models.TextField(verbose_name="Message")

  def __str__(self):
    return f'{self.name}'

class Media(models.Model):
  class Meta:
    verbose_name_plural = "Media Files"
    verbose_name = "Media File"
    ordering = ["name"]

  image = models.ImageField(blank=True, null=True, upload_to="media")
  url = models.URLField(blank=True, null=True)
  name = models.CharField(max_length=200, blank=True, null=True)
  is_image = models.BooleanField(default=True)

  def save(self, *args, **kwargs):
    if self.url:
      self.is_image = False
    super(Media, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.name

class Tag(models.Model):
  class Meta:
    verbose_name_plural = 'Tags'
    verbose_name = 'Tag'

  name = models.CharField(max_length=20, blank=False)
  full_name = models.CharField(max_length=50, blank=True, null=True)
  color = models.CharField(max_length=20, choices=COLORS, default=None)

  def __str__(self):
    return self.full_name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ["name"]
        
    date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="portfolio")
    tags = models.ManyToManyField(Tag, blank=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"

class Blog(models.Model):
  class Meta:
    verbose_name_plural = 'Blog Profiles'
    verbose_name = 'Blog'
    ordering = ['updated_at']

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200, blank=False)
  description = models.CharField(max_length=500, blank=True, null=True)
  body = RichTextField(blank=True, null=True)
  slug = models.SlugField(blank=True, null=True)
  image = models.ImageField(blank=True, null=True, upload_to='blog')
  tags = models.ManyToManyField(Tag, blank=True)
  is_active = models.BooleanField(default=True)

  def save(self, *args, **kwargs):
    if not self.id:
      self.slug = slugify(self.title)
    super(Blog, self).save(*args, **kwargs)
  
  def __str__(self):
    return self.title
  
  def get_absolute_url(self):
    return f"/blog/{self.slug}"

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

