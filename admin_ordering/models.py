from django.db import models
from django.db.models import Max
from django.utils.translation import gettext_lazy as _


class OrderableModel(models.Model):
    number = models.PositiveIntegerField(_("number"), default=0)

    class Meta:
        abstract = True
        ordering = ["number"]

    def save(self, *args, **kwargs):
        if not self.number:
            max = self.__class__._default_manager.aggregate(m=Max("number"))["m"]
            self.number = 1 + (max or 0)
        super(OrderableModel, self).save(*args, **kwargs)

    save.alters_data = True
