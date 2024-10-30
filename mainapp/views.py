from . import models, serializers
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Safwan
# Saf@12345


class ProjectCategoryView(viewsets.ModelViewSet):
    queryset = models.ProjectCategory.objects.all()
    serializer_class = serializers.ProjectCategorySerializer

    def retrieve(self, request, pk=None):
        if pk=='0':
            projects = models.Projects.objects.all()
        else:
            category = models.ProjectCategory.objects.get(id=pk)
            projects = models.Projects.objects.filter(category=category).all()
        projectserializer = serializers.ProjectSerializer(
            projects, many=True, context={"request": request}
        )
        return Response(projectserializer.data)


@api_view(["GET"])
def AllProjects(request,pk):
    if pk=='0':
        projects = models.Projects.objects.all()
    else:
        projects = models.Projects.objects.filter(pk=pk).all()
    projectserializer = serializers.ProjectSerializer(
        projects, many=True, context={"request": request}
    )
    return Response(projectserializer.data)


class ContactView(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

class MyselfView(generics.ListAPIView):
    queryset = models.Myself.objects.all()
    serializer_class = serializers.MyselfSerializer

class SkillsView(generics.ListAPIView):
    queryset = models.Skills.objects.all()
    serializer_class = serializers.SkillsSerializer
    
class ToolsView(generics.ListAPIView):
    queryset = models.Tools.objects.all()
    serializer_class = serializers.ToolsSerializer

class ResumeView(generics.ListAPIView):
    queryset = models.Resume.objects.all()
    serializer_class = serializers.ResumeSerializer


@api_view(["GET"])
def GetResume(request, category):
    if category=='All':
        resume = models.Resume.objects.all()
    else:
        category = models.ResumeCategory.objects.filter(category_name=category).all()
        category=category[0]
        resume = models.Resume.objects.filter(category=category).all()
    
    projectserializer = serializers.ResumeSerializer(
        resume, many=True, context={"request": request}
    )
    return Response(projectserializer.data)

@api_view(["GET"])
def GetResumeCategory(request):
    category = models.ResumeCategory.objects.all()
    projectserializer = serializers.ResumeCategorySerializer(
        category, many=True, context={"request": request}
    )
    return Response(projectserializer.data)


# /resume/?category__icontains=education
