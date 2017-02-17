class User(models.Model):
    first_name = models.Charfield(max_length=255)
    last_name = models.Charfield(max_length=255)
    email = models.Emailfield(max_length=255)
    password = models.Charfield(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(autp_now=True)

class Message(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(autp_now=True)
    user = models.ForeignKey(User)

class Comment(models.Model):
    comment = message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(autp_now=True)
    message = models.ForeignKey(Message)
    user = models.ForeignKey(User)
