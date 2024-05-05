from django.db import models
from django.utils.translation import gettext_lazy
from django.contrib.auth import get_user_model


User = get_user_model()


class Article(models.Model):
    """Article Model"""
    STATUS_CHOICES = (
        ('p', gettext_lazy('Published')),
        ('d', gettext_lazy('Draft')),
    )

    title = models.CharField(max_length=90,
                             verbose_name=gettext_lazy('Title (*)'),
                             db_index=True)
    body = models.TextField(verbose_name=gettext_lazy('Body'),
                            blank=True)
    author = models.ForeignKey(User,
                               verbose_name='Author',
                               on_delete=models.CASCADE,
                               related_name='articles')
    status = models.CharField(gettext_lazy('Status (*)'),
                              max_length=1,
                              choices=STATUS_CHOICES,
                              default='s',
                              null=True,
                              blank=True)
    create_date = models.DateTimeField(verbose_name=gettext_lazy('Create Date'),
                                       auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_date']
        verbose_name = "Article"
        verbose_name_plural = "Articles"
