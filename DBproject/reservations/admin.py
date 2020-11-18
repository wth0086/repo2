from django.contrib import admin
from . import models


@admin.register(models.AdditionalService)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name",)


@admin.register(models.Reservation)
class RoomAdmin(admin.ModelAdmin):
    filedsets = (
        (
            "fields",
            {
                "fields": (
                    "user",
                    "checkin",
                    "checkout",
                    "roomtype",
                    "bedtype",
                    "card",
                    "cardNum",
                    "cardExpYear",
                    "cardExpMonth",
                )
            },
        ),
    )

    list_display = (
        "user",
        "checkin",
        "checkout",
        "roomtype",
        "bedtype",
        "card",
        "cardNum",
        "cardExpYear",
        "cardExpMonth",
    )

    filter_horizontal = ("additionalService",)
