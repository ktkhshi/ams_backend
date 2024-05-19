from rest_framework import serializers
from accounts.serializers import UserSerializer
from mysite.utils import Base64ImageField
from app.models import Post
from app.models import Client
from app.models import Project
from app.models import Contract

# 投稿のシリアライザー
class PostSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.CharField(read_only=True)
  # Userモデルのシリアライザーを組み込み（読み取り専用）
  user = UserSerializer(read_only=True)
  # Base64エンコードされた画像を受け入れるカスタムフィールド
  image = Base64ImageField(
    max_length=None, use_url=True, required=False, allow_null=True
  )

  class Meta:
    model = Post
    fields = "__all__"

# クライアントのシリアライザー
class ClientSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.CharField(read_only=True)

  class Meta:
    model = Client
    fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.CharField(read_only=True)

  class Meta:
    model = Project
    fields = "__all__"

class ContractSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.CharField(read_only=True)

  class Meta:
    model = Contract
    fields = "__all__"