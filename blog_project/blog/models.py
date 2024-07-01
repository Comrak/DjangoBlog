# models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name

#ETIQUETAS 
class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Nombre')
    active = models.BooleanField(default=True, verbose_name='Activo')

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'
        ordering = ['name']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.TextField(verbose_name='Bajada', default='')
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=False, blank=False, default='images/default.jpg')
    tag = models.CharField(max_length=50, null=True, blank=True) 
    etiqueta = models.CharField(max_length=50, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    #RELACION
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='get_posts', verbose_name='Categoría')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='get_posts', verbose_name='Autor')
    tags = models.ManyToManyField(Tag, verbose_name='Etiquetas')
    likes = models.ManyToManyField(User, related_name='blog_posts', verbose_name='Me Gusta')

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.author} en {self.post}'

