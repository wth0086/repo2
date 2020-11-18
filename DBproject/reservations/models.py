from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class AdditionalService(AbstractItem):
    class Meta:
        verbose_name = "Additional Service"
        ordering = ["name"]


class Reservation(core_models.TimeStampedModel):

    CARD_1 = "삼성카드"
    CARD_2 = "국민카드"
    CARD_3 = "롯데카드"

    CARD_CHOICES = ((CARD_1, "삼성카드"), (CARD_2, "국민카드"), (CARD_3, "롯데카드"))

    user = models.OneToOneField(
        "users.User", related_name="reservation", blank=True, on_delete=models.CASCADE
    )
    checkin = models.DateField()
    checkout = models.DateField()
    roomtype = models.OneToOneField(
        "rooms.RoomType",
        related_name="reservation",
        blank=True,
        on_delete=models.CASCADE,
    )
    bedtype = models.OneToOneField(
        "rooms.BedType",
        related_name="reservation",
        blank=True,
        on_delete=models.CASCADE,
    )
    card = models.CharField(choices=CARD_CHOICES, max_length=20, blank=True)
    cardNum = models.IntegerField(blank=True, null=True)
    cardExpYear = models.CharField(default="****", max_length=4)
    cardExpMonth = models.CharField(default="**", max_length=2)
    additionalService = models.ManyToManyField(
        AdditionalService,
        blank=True,
    )
