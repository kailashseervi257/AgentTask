from django.db import models

# Create your models here.
class Agent(models.Model):
    agentID = models.CharField(max_length=25)
    agentName = models.CharField(max_length=50)
    agentOccupation = models.CharField(max_length=50)
    agency=models.CharField(max_length=50)
    mobile_no = models.IntegerField()
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return 'Agent ID :{} \nAgent Name{}'.format(self.agentID,self.agentName)