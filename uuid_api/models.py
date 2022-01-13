from django.db import models
import uuid

class the_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,  unique=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.time_stamp)

