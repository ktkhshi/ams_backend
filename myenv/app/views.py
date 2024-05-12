from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .models import Client
from .serializers import PostSerializer
from .serializers import ClientSerializer

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



# クライアント一覧を提供するAPIビュー
class ClientListView(ListAPIView):
  # 更新日時で降順に並び替え
  queryset = Client.objects.all().order_by("-updated_at")
  serializer_class = ClientSerializer
  # どのユーザでもアクセス可能
  permission_classes = (AllowAny,)
  #permission_classes = (IsAdminUser,)


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