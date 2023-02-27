from django.contrib import admin
from django.urls import path
from rest_framework import routers

from core import views as core_views

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    path("api/resources/", core_views.ResourceAPIView.as_view()),
    path("api/resources/<uuid:id>/", core_views.ResourceAPIView.as_view()),
    path("api/nodes/", core_views.NodeAPIView.as_view()),
    path("api/nodes/<int:id>/", core_views.NodeAPIView.as_view()),
]
