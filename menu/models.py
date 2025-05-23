from django.db import models
from django.db.models import Max

class Category(models.Model):
    name  = models.CharField("Категория", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=0)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category        = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name="Категория", related_name='dishes'
    )
    title           = models.CharField("Название", max_length=200)
    description     = models.TextField("Описание", blank=True)
    price           = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    image           = models.ImageField(
        "Фото блюда", upload_to="dishes/", blank=True, null=True
    )
    is_available    = models.BooleanField("В продаже", default=True)
    sequence_number = models.PositiveIntegerField(
        "Номер товара",
        unique=True,
        editable=False,
        null=True,
        help_text="Устанавливается автоматически при создании"
    )

    def save(self, *args, **kwargs):
        # при первом сохранении ставим последний +1
        if self._state.adding and self.sequence_number is None:
            agg = self.__class__.objects.aggregate(max_seq=Max("sequence_number"))
            last = agg.get("max_seq") or 0
            self.sequence_number = last + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"#{self.sequence_number} – {self.title}"
