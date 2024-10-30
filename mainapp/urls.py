from rest_framework import routers
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register(
    "projectcategory", views.ProjectCategoryView, basename="projectcategory"
)
urlpatterns = [
    path("allprojects/<pk>/", views.AllProjects, name="allprojects"),
    path("resume/<str:category>/", views.GetResume, name="getresume"),
    path("resumecategory/", views.GetResumeCategory, name="resumecategory"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("myself/", views.MyselfView.as_view(), name="myself"),
    path("skills/", views.SkillsView.as_view(), name="skills"),
    path("tools/", views.ToolsView.as_view(), name="tools"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
] + router.urls
