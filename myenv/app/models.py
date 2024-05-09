from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from hashids import Hashids
import uuid

# 投稿モデル
class Post(models.Model):
    uid = models.CharField("uid", max_length=30, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to="post", verbose_name="サムネイル", null=True, blank=True
    )
    title = models.CharField("タイトル", max_length=255)
    content = models.TextField("内容")
    updated_at = models.DateTimeField("更新日", auto_now=True)
    created_at = models.DateTimeField("作成日", auto_now_add=True)

    class Meta:
        verbose_name = "投稿"
        verbose_name_plural = "投稿"

    def __str__(self):
        return self.title


# 投稿が保存された後に実行されるシグナルレシーバー
@receiver(post_save, sender=Post)
def generate_random_post_uid(sender, instance, created, **kwargs):
    # 新規作成時にランダムUIDを生成
    if created:
        hashids = Hashids(salt="udkKour52sRr3tc7rEd5jsJsYBD8as54", min_length=8)
        instance.uid = hashids.encode(instance.id)
        instance.save()

# プロジェクトモデル
class Project(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    main_name = models.CharField("メイン名", max_length=255)
    sub_name = models.CharField("サブ名", max_length=255)

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "プロジェクト"
        verbose_name_plural = "プロジェクト"

    def __str__(self):
        return self.main_name + "-" + self.sub_name
    
# プロジェクト契約モデル
class ProjectContract(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    unit_price = models.DecimalField(verbose_name="単価", max_digits=10, decimal_places=2)
    contract_type = models.PositiveSmallIntegerField("契約タイプ")
    lower_hours_a_month = models.DecimalField(verbose_name="下限時間", max_digits=5, decimal_places=2)
    upper_hours_a_month = models.DecimalField(verbose_name="上限時間", max_digits=5, decimal_places=2)
    latest_work_started_at = models.TimeField(verbose_name="規定の開始時刻")
    earliest_work_ended_at = models.TimeField(verbose_name="規定の終了時刻")
    work_hours_a_day = models.DecimalField(verbose_name="所定勤務時間", max_digits=4, decimal_places=2)
    contract_started_on = models.DateField(verbose_name="契約開始日")
    contract_ended_on = models.DateField(verbose_name="契約終了日", blank=True, null=True)
    contract_name = models.CharField("契約名", max_length=255, default="")

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "プロジェクト契約"
        verbose_name_plural = "プロジェクト契約"

    def __str__(self):
        return self.contract_name + "-" + self.contract_started_on.strftime('%Y%m%d')
    
# クライアントモデル
class Client(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    person_in_charge = models.CharField(verbose_name="担当者名", max_length=45)
    address = models.CharField(verbose_name="住所", max_length=255)
    note = models.CharField(verbose_name="備考", max_length=255, blank=True, default="")
    
    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "クライアント"
        verbose_name_plural = "クライアント"

    def __str__(self):
        return self.person_in_charge + "-" + self.address

# ユーザプロジェクトモデル
class UserOnProject(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE
    )

    project = models.ForeignKey(
        Project, verbose_name="プロジェクト", on_delete=models.CASCADE
    )

    project_contract = models.ForeignKey(
        ProjectContract, verbose_name="プロジェクト契約", on_delete=models.PROTECT
    )

    client = models.ForeignKey(
        Client, verbose_name="クライアント", on_delete=models.PROTECT
    )

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "ユーザプロジェクト"
        verbose_name_plural = "ユーザプロジェクト"
    
    def __str__(self):
        return str(self.uid)

# ユーザプロジェクト月モデル
class UserOnProjectMonth(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    adjusted_hours = models.DecimalField(verbose_name="調整時間", max_digits=5, decimal_places=2)
    private_note = models.CharField(verbose_name="個人メモ", max_length=255, blank=True, default="")
    public_note = models.CharField(verbose_name="公開メモ", max_length=255, blank=True, default="")

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "ユーザプロジェクト月"
        verbose_name_plural = "ユーザプロジェクト月"

    def __str__(self):
        return str(self.uid)

# ユーザプロジェクト日モデル
class UserOnProjectDay(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    month = models.ForeignKey(
        UserOnProjectMonth, verbose_name="ユーザプロジェクト月", on_delete=models.PROTECT
    )
    day_index = models.PositiveSmallIntegerField("日にちインデックス")

    should_work_day = models.BooleanField(verbose_name="稼働日", default=True)
    date_day = models.DateField(verbose_name="日付")
    private_note = models.CharField(verbose_name="個人メモ", max_length=255, blank=True, default="")
    public_note = models.CharField(verbose_name="公開メモ", max_length=255, blank=True, default="")

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        verbose_name = "ユーザプロジェクト日"
        verbose_name_plural = "ユーザプロジェクト日"
        constraints = [
            models.UniqueConstraint(fields=['month', 'day_index'], name='unique_user_project_day')
        ]

    def __str__(self):
        return str(self.month.uid) + "-" + f'{self.day_index:02}'

# ユーザプロジェクト時間モデル
class UserOnProjectTime(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    month = models.ForeignKey(
        UserOnProjectMonth, verbose_name="ユーザプロジェクト月", on_delete=models.PROTECT
    )
    day_index = models.PositiveSmallIntegerField("日にちインデックス")
    time_index = models.PositiveSmallIntegerField("時間インデックス")

    work_started_at = models.TimeField(verbose_name="開始時刻")
    work_ended_at = models.TimeField(verbose_name="終了時刻")
    rest_started_at = models.TimeField(verbose_name="休憩開始時刻")
    rest_ended_at = models.TimeField(verbose_name="休憩終了時刻")
    private_note = models.CharField(verbose_name="個人メモ", max_length=255, blank=True, default="")
    public_note = models.CharField(verbose_name="公開メモ", max_length=255, blank=True, default="")

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "ユーザプロジェクト時間"
        verbose_name_plural = "ユーザプロジェクト時間"
        constraints = [
            models.UniqueConstraint(fields=['month', 'day_index', 'time_index'], name='unique_user_project_time')
        ]

    def __str__(self):
        return str(self.month.uid) + "-" + f'{self.day_index:02}' + "-" + f'{self.time_index:02}'

# ユーザプロジェクトインデックスモデル
class UserOnProjectIndex(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user_on_project = models.ForeignKey(
        UserOnProject, verbose_name="ユーザプロジェクト", on_delete=models.PROTECT
    )
    date_year_month = models.DateField("年月")

    user_on_project_month = models.ForeignKey(
        UserOnProjectMonth, verbose_name="ユーザプロジェクト月", on_delete=models.PROTECT
    )

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "ユーザプロジェクトインデックス"
        verbose_name_plural = "ユーザプロジェクトインデックス"
        constraints = [
            models.UniqueConstraint(fields=['user_on_project', 'date_year_month'], name='unique_user_project_index')
        ]
    
    def __str__(self):
        return str(self.uid)

# 勤務タイプ
class AttendanceType(models.Model):
    id = models.PositiveSmallIntegerField("id", unique=True, primary_key=True)

    attendance_name = models.CharField(verbose_name="勤務タイプ名", max_length=255, blank=True, default="")
    
    sort_order = models.PositiveSmallIntegerField(verbose_name="表示順")

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.attendance_name

# ユーザ特別勤務モデル
class UserSpecialAttendance(models.Model):
    uid = models.CharField("uid", max_length=40, unique=True, primary_key=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="ユーザー", on_delete=models.CASCADE
    )
    date_day = models.DateField(verbose_name="日付")

    attendance_type = models.ForeignKey(
        AttendanceType, verbose_name="勤務タイプ", on_delete=models.PROTECT, default=""
    )

    created_at = models.DateTimeField("作成日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)
    class Meta:
        verbose_name = "ユーザ特別勤務"
        verbose_name_plural = "ユーザ特別勤務"
        constraints = [
            models.UniqueConstraint(fields=['user', 'date_day'], name='unique_user_special_attendance')
        ]

    def __str__(self):
        return self.user.uid, self.date_day

@receiver(post_save, sender=UserSpecialAttendance)
def generate_user_special_attendance_uid(sender, instance, created, **kwargs):
    # 新規作成時にUIDを生成
    if created:
        instance.uid = sender.user.uid + "-" + sender.date_day.strftime('%Y%m%d')
        instance.save()

# 共通祝日モデル
class CommonHoliday(models.Model):
    date_day = models.DateField("日付", unique=True, primary_key=True)

    name = models.CharField(verbose_name="祝日名", max_length=32)

    class Meta:
        verbose_name = "共通祝日"
        verbose_name_plural = "共通祝日"

    def __str__(self):
        return self.date_day
