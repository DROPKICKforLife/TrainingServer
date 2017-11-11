from django.shortcuts import render
from django.http import HttpResponse
import configparser
import os
import glob
import re
import random
from django.http import HttpResponseRedirect
from .models import Trees
def index(request):

    return HttpResponse("HI")
    pass
def treeTrain(request):
    if request.method == "GET":
        config = configparser.ConfigParser()
        config.read('Questions.ini',encoding="utf-8")
        treeQuests = config['TreeQuests']
        trees= []
        questions = []
        for opt in treeQuests:
            trees.append(config.get('TreeQuests',opt))
            questions.append(opt)
            pass
        print(trees)
        filenames = os.listdir(os.path.join(os.getcwd(),'static/images'))
        for i in Trees.objects.all():
            while True:
                ran = random.randrange(0,len(filenames))
                if ran == int(i.treeID)-1:
                    continue
                else:
                    print(ran)
                    print("==")
                    print(int(i.treeID)-1)
                    break
        filename = filenames[ran]

        quest = []
        for i in questions:
            quest.append(re.sub("\d","",i))
        print(quest)
        return render(request, 'index.html', {'trees':trees,'filename':filename,'quest':quest, 'tq' : zip(trees,quest),'treenum' :filename.split('.')[0].split('tree')[1]})
    else:
        return HttpResponse("Please GET request..")
    pass
def getTrain(request):
    if request.method == 'GET':
        return HttpResponse("Please POST request..")
    postdata = request.POST.dict()
    answer = []
    print(postdata)
    treenum = postdata['treenum']
    postdata.popitem()
    for i in postdata.values():
        print(i)
        if i == 'yes':
            answer.append(1)
            continue
            pass
        elif i == 'no':
            answer.append(0)
            continue
            pass
        else:
            answer.append(int(i))
            pass

        pass
    query = Trees.objects.create(
        treeID = treenum,
        Answer1 = answer[0],
        Answer2 = answer[1],
        Answer3 = answer[2],
        Answer4 = answer[3],
        Answer5 = answer[4],
        confirm = True
    )
    query.save()
    return HttpResponseRedirect('tree')

    pass
# Create your views here.
