from django.db import models
from django.urls import reverse


class Post(models.Model):
    post_title = models.CharField('Заголовок поста', max_length=100)
    post_text = models.TextField('Текст поста', max_length=1000)
    post_photo = models.ImageField(upload_to="photos/%Y/%m/d%/", blank=True)
    post_author = models.CharField('Автор поста', max_length=100)
    post_date = models.DateTimeField('Дата поста', auto_now_add=True)
    post_date_update = models.DateTimeField('Дата поста', auto_now=True)

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Comment(models.Model):
    comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_text = models.TextField('Текст комментария', max_length=500)
    comment_author = models.CharField('Автор комментария', max_length=100)
    comment_date = models.DateTimeField('Дата комментария', auto_now=True)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
