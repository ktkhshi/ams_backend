from rest_framework import serializers
from accounts.serializers import UserSerializer
from mysite.utils import Base64ImageField
from app.models import Post
from accounts.models import UserAccount
from app.models import Client
from app.models import Project
from app.models import Contract
from app.models import UserOnProject

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

# ユーザのシリアライザー
class UserSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.CharField(read_only=True)

  class Meta:
    model = UserAccount
    fields = "__all__"

# クライアントのシリアライザー
class ClientSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.UUIDField(read_only=True)

  class Meta:
    model = Client
    fields = "__all__"

# プロジェクトのシリアライザー
class ProjectSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.UUIDField(read_only=True)

  class Meta:
    model = Project
    fields = "__all__"

# 契約のシリアライザー
class ContractSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.UUIDField(read_only=True)

  class Meta:
    model = Contract
    fields = "__all__"

# ユーザプロジェクトのシリアライザー
class UserOnProjectSerializer(serializers.ModelSerializer):
  # uidフィールドは読み取り専用
  uid = serializers.UUIDField(read_only=True)

  user = UserSerializer(read_only=True)
  user_id = serializers.PrimaryKeyRelatedField(queryset=UserAccount.objects.all(), write_only=True)
  project = ProjectSerializer(read_only=True)
  project_uid = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), write_only=True)
  client = ClientSerializer(read_only=True)
  client_uid = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), write_only=True)
  contract = ContractSerializer(read_only=True)
  contract_uid = serializers.PrimaryKeyRelatedField(queryset=Contract.objects.all(), write_only=True)

  def create(self, validated_data):
    validated_data['user'] = validated_data.get('user_id', None)
    if validated_data['user'] is None:
        raise serializers.ValidationError("user not found.") 
    del validated_data['user_id']

    validated_data['project'] = validated_data.get('project_uid', None)
    if validated_data['project'] is None:
        raise serializers.ValidationError("project not found.") 
    del validated_data['project_uid']

    validated_data['client'] = validated_data.get('client_uid', None)
    if validated_data['client'] is None:
        raise serializers.ValidationError("client not found.") 
    del validated_data['client_uid']

    validated_data['contract'] = validated_data.get('contract_uid', None)
    if validated_data['contract'] is None:
        raise serializers.ValidationError("contract not found.") 
    del validated_data['contract_uid']

    return UserOnProject.objects.create(**validated_data)
  class Meta:
    model = UserOnProject
    fields = "__all__"

