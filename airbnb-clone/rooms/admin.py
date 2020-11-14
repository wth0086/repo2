from django.contrib import admin
from django.utils.html import mark_safe  # 장고에서 url을 사용할 수 있게 보안해제를 허가하는 클래스
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)  # 외래키로 연결된 애를 여기서도 생성할 수 있게 해준다.

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),  # 많은내용이 있을 때 숨겼다가 나타났다가 할 수 있게 해주는 기능
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        "count_photos",
        "total_rating",
    )

    list_filter = (
        "instant_book",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    raw_id_fields = ("host",)  # 호스트리스트가 많아지면 검색할수있게해주는것 (우편번호 찾기 같이)

    search_fields = ("city", "^host__username")

    filter_horizontal = ("amenities", "facilities", "house_rules")

    # def save_model(self, request, obj, form, change): # admin에서 관리하고 싶을 때
    #     super().save_model(request, obj, form, change)

    # 여기서 self는 현재 내가 작성하고 있는 메소드의 클래스이고, obj는 현재 행을 의미한다.
    # 이해 안되면 6.2강 3:30 참고
    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = (
        "Count Amenities"  # 이름을 정해주고, 정렬의 대상이 되지 못하도록 해준다.
    )

    def count_photos(self, obj):
        return obj.photos.count()

    count_photos.short_description = "Photo Count"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition"""

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"