from django.db import models
from django.utils.text import slugify
from django.shortcuts import reverse
from articles.utils import generate_slug



class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, unique=True,blank=True)
    image = models.ImageField(upload_to='categories/',default='default_category.jpg')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def articles(self):
        return Article.objects.filter(category=self)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('store:catalog_detail',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Article(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=8, unique=True,blank=True)
    description = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    genre = models.CharField(max_length=20,default='woman')
    label = models.CharField(max_length=15,default='without')
    stock = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='articles_portail/',blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def article_images(self):
        return ArticleImage.objects.filter(article=self)



    def __str__(self):
        return f"{self.name}-({self.stock})"

    def get_absolute_url(self):
        return reverse('store:article_detail',kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug()
        return super().save(*args, **kwargs)

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE,null=True,blank=True,related_name='images')
    image = models.ImageField(upload_to='articles_images/')

    def __str__(self):
        return f"{self.article.name}"

