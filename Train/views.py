from django.shortcuts import render
from django.http import HttpResponse
import configparser
import os
import glob
import re
import random
from django.http import HttpResponseRedirect
from PIL import Image
import io
import base64
from .models import Trees
from .models import Houses
from matplotlib import pyplot as plt
import numpy as np


def index(request):

    return HttpResponse("HI")
    pass
def houseTrain(request):
    if request.method =="GET":
        maxlen = 144721
        config = configparser.ConfigParser()
        config.read('Questions.ini',encoding='utf-8')
        houseQuests = config['HouseQuests']
        houses = []
        questions = []
        for opt in houseQuests:
            houses.append(config.get('HouseQuests',opt))
            questions.append(opt)
            pass
        print(houses)
        tf = True
        while True:
            ran = random.randrange(0,maxlen)
            for i in Houses.objects.all():
                if ran != int(i.houseID)-1:
                    tf = True
                else:
                    tf = False
                    break
            if tf == True:
                break
        num = ran
        filename = 'house'+str(num)+'.png'
        quest = []
        for i in questions:
            quest.append(re.sub("\d","",i))
        count = Houses.objects.count()
        return render(request, 'house.html',
                      {'house': houses, 'quest': quest, 'hq': zip(houses, quest), 'housenum': num, 'houseurl': filename,
                       'maxnum': 144721, 'count': count})


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

        # treearr = np.load('tree.npy')
        # filecounts = len(treearr)
        # print(filecounts)
        tf = True
        while True:
            ran = random.randrange(0, 144721)
            for i in Trees.objects.all():
                if ran != int(i.treeID)-1:
                    tf = True
                else:
                    tf = False
                    break
            if tf == True:
                break
        pass
        print('Create Random Number!')
        # for i in Trees.objects.all():
        #     while True:
        #         ran = random.randrange(0,filecounts)
        #         if ran == int(i.treeID)-1:
        #             continue
        #         else:
        #             print("random int : %s"%ran)
        #             break
        #             pass
        #         pass

        # img = np.reshape(treearr[ran],(28,28))
        # imarr = Image.fromarray(img)
        # imcrop = imarr.crop()
        # btio = io.BytesIO()
        # imcrop.save(btio,format='PNG')
        # btio = btio.getvalue()
        # encodebyte = base64.b64encode(btio)

        # num = dbset[ran].ImgNum
        num = ran
        print("tree data load..")
        print(())
        filename = 'tree'+str(num)+'.png'


        # tree = ranobj[ran]
        # print(type(tree))
        # print("tree data loaded!")
        count = Trees.objects.count()
        # strPNG = encodebyte.decode('ascii')


        # filenames = os.listdir(os.path.join(os.getcwd(),'static/images'))
        # for i in Trees.objects.all():
        #     while True:
        #         ran = random.randrange(0,len(filenames))
        #         if ran == int(i.treeID)-1:
        #             continue
        #         else:
        #             print(ran)
        #             print("==")
        #             print(int(i.treeID)-1)
        #             break
        # filename = filenames[ran]

        quest = []
        for i in questions:
            quest.append(re.sub("\d","",i))
        print(quest)
        # return render(request, 'index.html', {'trees':trees,'filename':filename,'quest':quest, 'tq' : zip(trees,quest),'treenum' :filename.split('.')[0].split('tree')[1]})
        # return render(request,'index.html',{'trees':trees,'quest':quest,'tq':zip(trees,quest),'treenum':ran,'treedata':strPNG,'maxnum':len(treearr)})
        return render(request, 'index.html',
                  {'trees': trees, 'quest': quest, 'tq': zip(trees, quest), 'treenum': num, 'treeurl': filename,
                   'maxnum': 144721,'count' : count})

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
    postdata.pop('treenum',None)
    import operator
    postdata = sorted(postdata.items(),key=operator.itemgetter(0))
    print(type(postdata))
    for i in postdata:
        if i[1] == 'yes':
            answer.append(1)
            continue
            pass
        elif i[1] == 'no':
            answer.append(0)
            continue
            pass
        else:
            answer.append(int(i[1]))
            pass

        pass
    print(answer)
    query = Trees.objects.create(
        treeID = treenum,
        Answer1 = answer[0],
        Answer2 = answer[1],
        Answer3 = answer[2],
        Answer4 = answer[3],
        Answer5 = answer[4],
        Answer6 = answer[5],
        confirm = True
    )
    query.save()

    return HttpResponseRedirect('tree')
    pass
# Create your views here.
