from __future__ import unicode_literals

from django.db import models
from ..login.models import User
from ..course.models import Course

class abc(models.Model):
    user = models.ForeignKey(User)
    course = models.ForeignKey(Course)
