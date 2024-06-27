from django.contrib import admin
from django.contrib.admin import ModelAdmin
from app.models import Post

from app.models import Client
from app.models import Project
from app.models import Contract
from app.models import UserOnProject
from app.models import UserSpecialAttendance
from app.models import UserOnProjectTime
from app.models import UserOnProjectMonth
from app.models import UserOnProjectIndex
from app.models import UserOnProjectDay

class PostCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "user", "title", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid", "user", "title")
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(Post, PostCustom)

class ClientCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "person_in_charge", "address", "note", "created_at", "updated_at")
    # リンク
    list_display_links = ("uid", "person_in_charge", "address")
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(Client, ClientCustom)

class ProjectCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "main_name", "sub_name", "note", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid", "main_name", "sub_name")
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(Project, ProjectCustom)

class ContractCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "unit_price", "contract_type", "lower_hours_a_month", "upper_hours_a_month", "latest_work_started_at", "earliest_work_ended_at", "work_hours_a_day", "started_on", "ended_on", "contract_name", "note",  "updated_at", "created_at")
    # リンク
    list_display_links = ("uid", "contract_name")
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(Contract, ContractCustom)

class UserOnProjectCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "client_id", "project_id", "contract_id", "user_id", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserOnProject, UserOnProjectCustom)

class UserOnProjectIndexCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "user_on_project", "date_year_month", "user_on_project_month", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserOnProjectIndex, UserOnProjectIndexCustom)

class UserOnProjectMonthCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "adjusted_hours", "private_note", "public_note", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserOnProjectMonth, UserOnProjectMonthCustom)

class UserOnProjectDayCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "month", "day_index", "should_work_day", "date_day", "private_note", "public_note", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserOnProjectDay, UserOnProjectDayCustom)

class UserOnProjectTimeCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "day", "time_index", "work_started_at", "work_ended_at", "rest_started_at", "rest_ended_at", "private_note", "public_note", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserOnProjectTime, UserOnProjectTimeCustom)

class UserSpecialAttendanceCustom(ModelAdmin):
    # 一覧
    list_display = ("uid", "user", "date_day", "updated_at", "created_at")
    # リンク
    list_display_links = ("uid",)
    # 順番
    ordering = ("-updated_at",)
    # 編集不可
    readonly_fields = ("uid", "updated_at", "created_at")

admin.site.register(UserSpecialAttendance, UserSpecialAttendanceCustom)