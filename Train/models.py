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
    Answer7 = models.IntegerField('Answer7', null=True)
    Answer8 = models.IntegerField('Answer8', null=True)
    Answer9 = models.IntegerField('Answer9', null=True)
    Answer10 = models.IntegerField('Answer10', null=True)
    Answer11 = models.IntegerField('Answer11', null=True)
    Answer12 = models.IntegerField('Answer12', null=True)
    Answer13 = models.IntegerField('Answer13', null=True)




