from django.db import models

class Trees(models.Model):
    treeID = models.TextField('TREEID',max_length=100)
    confirm = models.BooleanField('CONFIRM')
    confirmDATE = models.DateTimeField('CONFIRMDATE',auto_now=True)
    Answer1 = models.IntegerField('Answer1', null=True)
    Answer2 = models.IntegerField('Answer2', null=True)
    Answer3 = models.IntegerField('Answer3', null=True)
    Answer4 = models.IntegerField('Answer4', null=True)
    Answer5 = models.IntegerField('Answer5', null=True)
    Answer6 = models.IntegerField('Answer6', null=True)
class Houses(models.Model):
    houseID = models.TextField('HOUSEID',max_length=100)
    confirmDATE = models.DateTimeField('CONFIRMDATE', auto_now=True)
    Answer1 = models.IntegerField('Answer1', null=True)
    Answer2 = models.IntegerField('Answer2', null=True)
    Answer3 = models.IntegerField('Answer3', null=True)
    Answer4 = models.IntegerField('Answer4', null=True)
    Answer5 = models.IntegerField('Answer5', null=True)
    Answer6 = models.IntegerField('Answer6', null=True)





