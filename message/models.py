from django.db import models



class Message(models.Model):
    # user= models.ForeignKey('User', on_delete=models.CASCADE)
    # sender = models.ForeignKey('User, on_delete=models.CASCADE)
    # receiver = models.ForeignKey('User, on_delete=models.CASCADE)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.body}" 