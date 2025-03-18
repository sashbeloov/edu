from django.db import models

class Course(models.Model):
    objects = None
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False, default=0)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to="images/")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="images/")
    length = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class CourseProperty(models.Model):
    description = models.CharField(max_length=255, null=True)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

class Video(models.Model):
    title = models.CharField(max_length=100, null=False)
    course = models.ForeignKey(Course, null=False, on_delete=models.CASCADE)
    serial_number = models.IntegerField(null=False)
    video_id = models.CharField(max_length=20, null=False)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.title