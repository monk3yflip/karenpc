from cgitb import text
from tabnanny import verbose
from django.db import models
from django.contrib import admin
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Заголовкок")
    description = models.TextField(verbose_name = 'Краткое содержание')
    content = models.TextField(verbose_name = 'Полное содержание')
    posted = models.DateTimeField(default=datetime.now(), db_index = True, verbose_name='Опубликована')
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    image = models.FileField(default='temp.jpg', verbose_name="Путь к изображению")
    
    
    def get_absolute_url(self):
        return reverse('blogpost', args=[str(self.id)])
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Posts'
        ordering = ['-posted'] #по убыванию
        verbose_name = 'Статья блога'
        verbose_name_plural = 'Стати блога'
        
admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name="Текст комментария")
    date = models.DateTimeField(default=datetime.now(), db_index = True, verbose_name='Дата комментария')
    author = models.ForeignKey(User,  on_delete=models.CASCADE, verbose_name='Автор комментария')
    post = models.ForeignKey(Blog,  on_delete=models.CASCADE, verbose_name='Статья комментария')
    
    def __str__(self):
        return 'Комментарий %d %s к %s'% (self.id, self.author, self.post)

    class Meta:
        db_table = "Comment"
        ordering = ["-date"]
        verbose_name = 'Комментарий к статье блога'
        verbose_name_plural = 'Комментарии к статьям блога'
        
admin.site.register(Comment)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    # Добавьте дополнительные поля для обработки заказа

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
       return self.quantity, self.product.name
           
admin.site.register(Product)
