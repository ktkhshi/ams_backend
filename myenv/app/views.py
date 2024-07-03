import datetime
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Post
from accounts.models import UserAccount
from .models import Client
from .models import Project
from .models import Contract
from .models import UserOnProject
from .models import UserOnProjectIndex
from .models import UserOnProjectMonth
from .models import UserOnProjectDay
from .models import UserOnProjectTime
from .models import AttendanceType
from .models import UserSpecialAttendance
from .serializers import PostSerializer
from .serializers import UserSerializer
from .serializers import ClientSerializer
from .serializers import ProjectSerializer
from .serializers import ContractSerializer
from .serializers import UserOnProjectSerializer
from .serializers import UserOnProjectMonthSerializer
from .serializers import UserOnProjectDaySerializer
from .serializers import AttendanceTypeSerializer
from .serializers import UserSpecialAttendanceSerializer

# 投稿一覧を提供するAPIビュー
class PostListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = Post.objects.all().order_by("-updated_at")
  serializer_class = PostSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)

# 特定の投稿の詳細を提供するAPIビュー
class PostDetailView(RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  # 投稿を識別するためにuidフィールドを使用
  lookup_field = "uid"

# 新規投稿、投稿編集、投稿削除を行うAPIビューセット
class PostViewSet(ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  # 投稿を識別するためにuidフィールドを使用
  lookup_field = "uid"

  # 新規投稿時のユーザ情報の保存処理
  def perform_create(self, serializer, **kwargs):
    # 投稿を作成するユーザを設定
    serializer.save(user=self.request.user)

# ユーザ一覧を提供するAPIビュー
class UserListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = UserAccount.objects.all().order_by("-updated_at")
  serializer_class = UserSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

# クライアント一覧を提供するAPIビュー
class ClientListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = Client.objects.all().order_by("-updated_at")
  serializer_class = ClientSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

# 新規ユーザ作成、編集、削除を行うAPIビューセット
class UserViewSet(ModelViewSet):
  queryset = UserAccount.objects.all()
  serializer_class = UserSerializer
  # クライアントを識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 新規ユーザ作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # クライアントを作成する
    serializer.save()

# 新規クライアント作成、編集、削除を行うAPIビューセット
class ClientViewSet(ModelViewSet):
  queryset = Client.objects.all()
  serializer_class = ClientSerializer
  # クライアントを識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 新規クライアント作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # クライアントを作成する
    serializer.save()

 # プロジェクト一覧を提供するAPIビュー
class ProjectListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = Project.objects.all().order_by("-updated_at")
  serializer_class = ProjectSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

# 新規プロジェクト作成、編集、削除を行うAPIビューセット
class ProjectViewSet(ModelViewSet):
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  # プロジェクトを識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 新規プロジェクト作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # プロジェクトを作成する
    serializer.save()

 # 契約一覧を提供するAPIビュー
class ContractListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = Contract.objects.all().order_by("-updated_at")
  serializer_class = ContractSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

# 新規プロジェクト契約作成、編集、削除を行うAPIビューセット
class ContractViewSet(ModelViewSet):
  queryset = Contract.objects.all()
  serializer_class = ContractSerializer
  # 契約を識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 新規契約作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # プロジェクト契約を作成する
    serializer.save()

# ユーザプロジェクト一覧を提供するAPIビュー
class UserOnProjectListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = UserOnProject.objects.all().order_by("-updated_at")
  serializer_class = UserOnProjectSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

# 新規ユーザプロジェクト作成、編集、削除を行うAPIビューセット
class UserOnProjectViewSet(ModelViewSet):
  queryset = UserOnProject.objects.all()
  serializer_class = UserOnProjectSerializer
  # ユーザプロジェクトを識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 新規ユーザプロジェクト作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # ユーザプロジェクトを作成する
    serializer.save()

class MyUserOnProjectListView(ListAPIView):
  serializer_class = UserOnProjectSerializer
  permission_classes = (AllowAny,)

  def get_queryset(self):
    strdate = self.kwargs['yearmonth']
    bufdate = datetime.datetime.strptime(strdate, '%Y%m')
    target_date = datetime.datetime(bufdate.year, bufdate.month, 1)

    uop_items = UserOnProject.objects.select_related('user') \
                                      .select_related('project') \
                                      .filter(user__uid=self.kwargs['uid']) \
                                      .prefetch_related('indexes') \
                                      .filter(indexes__date_year_month=target_date)
    return uop_items
  
# ユーザプロジェクト勤務月詳細（日にち）一覧を提供するAPIビュー
class UserOnProjectMonthDetailView(RetrieveAPIView):
  serializer_class = UserOnProjectMonthSerializer
  permission_classes = (AllowAny,)

  def get_object(self):
    strdate = self.kwargs['yearmonth']
    bufdate = datetime.datetime.strptime(strdate, '%Y%m')
    target_date = datetime.datetime(bufdate.year, bufdate.month, 1)

    uop = UserOnProject.objects.select_related('user').get(user__uid=self.kwargs['uid'], project__uid=self.kwargs['puid'])
    uopm = UserOnProjectIndex.objects.all() \
            .select_related('user_on_project_month') \
            .values_list('user_on_project_month', flat=True) \
            .get(date_year_month=target_date, user_on_project_id=uop.uid)
    month = UserOnProjectMonth.objects.get(uid=uopm)
    return month

# ユーザプロジェクト勤務日詳細（時間）一覧を提供するAPIビュー
class UserOnProjectDayDetailView(RetrieveAPIView):
  queryset = UserOnProjectDay.objects.all()
  serializer_class = UserOnProjectDaySerializer
  lookup_field = 'uid'
  permission_classes = (AllowAny,)

# ユーザプロジェクト勤務日詳細更新を行うAPIビュー
class UserOnProjectDayDetailUpdateView(UpdateAPIView):
  queryset = UserOnProjectDay.objects.all()
  serializer_class = UserOnProjectDaySerializer
  update_fields = ['work_started_at', 'work_ended_at', 'rest_hours', 'private_note', 'public_note']
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)

  # 更新時の処理
  def post(self, request, **kwargs):
    day_instance = UserOnProjectDay.objects.get(uid=self.kwargs['uid'])
   
    times_data = request.data.get('times', [])
    if times_data:
        index = 0
        for time_data in times_data:
          index += 1
          time_instance, _ = UserOnProjectTime.objects.update_or_create(
            day_id=day_instance.uid,time_index=index, 
            defaults={"work_started_at": time_data.get('work_started_at'),
                      "work_ended_at": time_data.get('work_ended_at'),
                      "rest_started_at": time_data.get('rest_started_at'),
                      "rest_ended_at": time_data.get('rest_ended_at'),
                      "private_note": time_data.get('private_note'),
                      "public_note": time_data.get('public_note')},
            create_defaults={"work_started_at": time_data.get('work_started_at'),
                             "work_ended_at": time_data.get('work_ended_at'),
                             "rest_started_at": time_data.get('rest_started_at'),
                             "rest_ended_at": time_data.get('rest_ended_at'),
                             "private_note": time_data.get('private_note'),
                             "public_note": time_data.get('public_note')})
          time_instance.save()

        # 日を更新する
        day_instance.work_started_at = request.data.get('work_started_at', day_instance.work_started_at)
        day_instance.work_ended_at = request.data.get('work_ended_at', day_instance.work_ended_at)
        day_instance.rest_hours = request.data.get('rest_hours', day_instance.rest_hours)
        day_instance.private_note = request.data.get('private_note', day_instance.private_note)
        day_instance.public_note = request.data.get('public_note', day_instance.public_note)
        day_instance.save(force_insert=False)
        # 更新後のデータをシリアライザでシリアライズする
        serializer = self.get_serializer(day_instance)
        # 成功レスポンスを返す
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # エラー処理: 時間モデルのデータがリクエストに含まれていない場合
        return Response({'error': 'Times data is required'}, status=status.HTTP_400_BAD_REQUEST)

# 勤務タイプ一覧を提供するAPIビュー
class AttendanceListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = AttendanceType.objects.all().order_by("sort_order")
  serializer_class = AttendanceTypeSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)

# ユーザ特別勤務一覧を提供するAPIビュー
class UserSpecialAttendanceListView(ListAPIView):
  # 日付で降順に並び替え
  serializer_class = UserSpecialAttendanceSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)

  def get_queryset(self):
    usa_items = UserSpecialAttendance.objects.select_related('user') \
          .filter(user__uid=self.kwargs['uid']).order_by("-date_day")
    return usa_items

# 新規ユーザ特別勤務作成、編集、削除を行うAPIビューセット
class UserSpecialAttendanceViewSet(ModelViewSet):
  queryset = UserSpecialAttendance.objects.all()
  serializer_class = UserSpecialAttendanceSerializer
  # ユーザ特別勤務を識別するためにuidフィールドを使用
  lookup_field = "uid"
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)

  # 新規ユーザ特別勤務作成時の保存処理
  def perform_create(self, serializer, **kwargs):
    # 作成をリクエストしたユーザでユーザ特別勤務を作成する
    serializer.save(user=self.request.user)