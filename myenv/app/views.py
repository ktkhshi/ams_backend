import datetime
from rest_framework.generics import ListAPIView, RetrieveAPIView
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
from .models import UserOnProjectDay
from .serializers import PostSerializer
from .serializers import UserSerializer
from .serializers import ClientSerializer
from .serializers import ProjectSerializer
from .serializers import ContractSerializer
from .serializers import UserOnProjectSerializer
from .serializers import UserOnProjectDaySerializer

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


# ユーザプロジェクト勤務（日にち）一覧を提供するAPIビュー
class UserOnProjectDayListView(ListAPIView):
  serializer_class = UserOnProjectDaySerializer
  permission_classes = (AllowAny,)

  def get_queryset(self):
    strdate = self.kwargs['yearmonth']
    bufdate = datetime.datetime.strptime(strdate, '%Y%m')
    target_date = datetime.datetime(bufdate.year, bufdate.month, 1)

    # Todo クエリを1回だけ発行するように変更する
    # Dayに足してすべての行にMonthがくっついてきているので、先頭行のみPrefetchしたい・・
    uop = UserOnProject.objects.get(user__id=self.kwargs['uid'], project__uid=self.kwargs['puid'])
    uopm = UserOnProjectIndex.objects.all() \
            .select_related('user_on_project_month') \
            .values_list('user_on_project_month', flat=True) \
            .get(date_year_month=target_date, user_on_project_id=uop.uid)
    uopd_items = UserOnProjectDay.objects.filter(month=uopm).prefetch_related('month').order_by('day_index')
    return uopd_items