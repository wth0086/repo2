import datetime
from django.db import models
from django.utils import timezone
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

    user = models.ForeignKey(
        "users.User", related_name="reservation", blank=True, on_delete=models.CASCADE
    )
    checkin = models.DateField()
    checkout = models.DateField()
    roomtype = models.ForeignKey(
        "rooms.RoomType",
        related_name="reservation",
        blank=True,
        on_delete=models.CASCADE,
    )
    bedtype = models.ForeignKey(
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

    def save(self, *args, **kwargs):  # 날짜를 확인하고 없으면 새로운 BookedDay를 생성하는 부분을 만들어야 한다.
        start = self.checkin
        end = self.checkout
        difference = end - start

        for date in range(difference.days + 1):
            day = start + datetime.timedelta(days=date)
            obj = BookedDay.objects.all().filter(roomtype=self.roomtype, day=day)
            if not obj.exists():
                BookedDay.objects.create(
                    created=timezone.now(),
                    updated=timezone.now(),
                    roomtype=self.roomtype,
                    day=day,
                    count=1,
                )

            else:
                Getobj = obj.get()
                Getobj.count = Getobj.count + 1
                Getobj.save()


class BookedDay(core_models.TimeStampedModel):
    roomtype = models.ForeignKey(
        "rooms.RoomType",
        on_delete=models.CASCADE,
    )
    day = models.DateField(null=True)
    count = models.IntegerField(default=0)
