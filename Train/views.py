from django.shortcuts import render
from django.http import HttpResponse
import configparser
import os
import glob
import re
import random
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
        ran = random.randrange(0,len(filenames))
        filename = filenames[ran]
        quest = []
        for i in questions:
            quest.append(re.sub("\d","",i))
        print(quest)
        return render(request, 'index.html', {'trees':trees,'filename':filename,'quest':quest, 'tq' : zip(trees,quest)})
    else:
        return HttpResponse("HI")
    pass

# Create your views here.
