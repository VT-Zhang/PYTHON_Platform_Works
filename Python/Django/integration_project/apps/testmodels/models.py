from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from ..course.models import Course

class abc(models.Model):
    user = models.ForeignKey(User, related_name='user')
    course = models.ForeignKey(Course, related_name='course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistrationManager()

class RegistrationManager(models.Manager):
    def isregister(self, user_id, course_id):
        check = abc.objects.filter(user_id=user_id).filter(course_id=course_id)
        if not check:
            return True
        else:
            return False
