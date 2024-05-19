from django.urls import path, include
from rest_framework import routers
from app import views

router = routers.DefaultRouter()
router.register("posts", views.PostViewSet)
router.register("clients", views.ClientViewSet)
router.register("projects", views.ProjectViewSet)
router.register("contracts", views.ContractViewSet)

urlpatterns = [
    # 投稿一覧
    path("post-list/", views.PostListView.as_view()),
    # 投稿詳細
    path("post-detail/<uid>/", views.PostDetailView.as_view()),
    # 新規、編集、削除
    path("", include(router.urls)),

    # クライアント一覧
    path("client-list/", views.ClientListView.as_view()),

    # プロジェクト一覧
    path("project-list/", views.ProjectListView.as_view()),

    # 契約一覧
    path("contract-list/", views.ContractListView.as_view()),
]
