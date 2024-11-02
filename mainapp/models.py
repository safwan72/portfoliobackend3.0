from django.db import models
import uuid

class CategoryParent(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        abstract = True

class ProjectCategory(CategoryParent):
    class Meta:
        verbose_name_plural = "Project Category"
        db_table = "Project Category"


class ProjectAdmin(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    url = models.URLField(max_length=200,blank=True)
    github_url = models.URLField(max_length=200, blank=True)
    is_live=models.BooleanField(default=True)
    test_details = models.TextField(blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


def upload_project(instance, filename):
    return f"Projects/{filename}".format(instance=instance)


class UploadImage(models.Model):
    image = models.ImageField(
        upload_to=upload_project,
        blank=True,
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    featured=models.BooleanField(default=False)
    def __str__(self):
        return f"Image {self.image.name.split('/')[-1] }"


class Projects(ProjectAdmin):
    image = models.ManyToManyField(UploadImage,blank=True)
    category = models.ManyToManyField(ProjectCategory, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Projects"
        db_table = "Projects"


class Contact(models.Model):
    email = models.EmailField(max_length=254)
    name = models.CharField(max_length=254)
    text = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.name + " Just Messaged You."

    class Meta:
        verbose_name_plural = "Contact"
        db_table = "Contact"


class Myself(models.Model):
    name = models.TextField(max_length=100, blank=True)
    about = models.TextField(max_length=1000, verbose_name="About")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Myself"
        db_table = "Myself"


def upload_skills(instance, filename):
    return "Skills/{instance.name}/{instance.name}.png".format(instance=instance)

def upload_tools(instance, filename):
    return "Tools/{instance.name}/{instance.name}.png".format(instance=instance)


class Tools(models.Model):
    name = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=100, verbose_name="description")
    image = models.ImageField(
        upload_to=upload_tools,
        blank=True,
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tools"
        db_table = "Tools"

class Skills(models.Model):
    name = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=100, verbose_name="description")
    image = models.ImageField(
        upload_to=upload_skills,
        blank=True,
    )
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Skills"
        db_table = "Skills"


class ResumeCategoryParent(models.Model):
    category_name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        abstract = True


class ResumeCategory(ResumeCategoryParent):
    class Meta:
        verbose_name_plural = "Resume Category"
        db_table = "Resume Category"


class Resume(models.Model):
    position = models.TextField(max_length=500, blank=False)
    company_name = models.TextField(max_length=500, blank=False)
    location = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=1000, verbose_name="description")
    start_date = models.DateField(auto_now_add=False, blank=True, null=True)
    end_date = models.DateField(auto_now=False,blank=True,null=True)
    category = models.ManyToManyField(ResumeCategory, blank=True)
    result = models.CharField(max_length=254,blank=True,null=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = "Resume"
        db_table = "Resume"
