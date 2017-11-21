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
from .models import Imgs
from matplotlib import pyplot as plt
import numpy as np
from .preopen import XYData
xy = XYData()
for i in range(np.size(xy.count)):
    # trees[i] = np.reshape(trees[i],(28,28))
    maxLen = Imgs.objects.count()
    if i < maxLen:
        continue

    for j in range(xy.count[i]):
        plt.plot(xy.x[i][j], xy.y[i][j], color='black')
    plt.axis('off')
    btio = io.BytesIO()
    file = plt.savefig(btio, format='png', facecolor='w')
    btio = btio.getvalue()
    encodebyte = base64.b64encode(btio)
    strPNG = encodebyte.decode('ascii')
    sql = Imgs.objects.create(
    ImgNum=i,
    ImgData=strPNG
    )
    sql.save()
    print(str(i) + " fin.")



def index(request):
    for i in range(1):
        # trees[i] = np.reshape(trees[i],(28,28))
        maxLen = Imgs.objects.count()
        if i < maxLen:
            continue

        for j in range(xy.count[i]):
            plt.plot(xy.x[i][j],xy.y[i][j],color='black')
        plt.axis('off')
        btio = io.BytesIO()
        file = plt.savefig(btio, format='png', facecolor='w')
        btio = btio.getvalue()
        encodebyte = base64.b64encode(btio)
        strPNG = encodebyte.decode('ascii')
        sql = Imgs.objects.create(
            ImgNum = i,
            ImgData = strPNG
        )
        sql.save()
        print(str(i)+" fin.")
        #im = Image.fromarray([xy.x[i],xy.y[i]])
        # image = im.crop()
        # bytearr = io.BytesIO()
        # image.save(bytearr,format="PNG")
        # bytearr = bytearr.getvalue()
        # encodebyte = base64.b64encode(bytearr)
        # str = encodebyte.decode('ascii')
        # print(str)
        # im.show()
        # print(np.size(trees))
        # print(len(trees))
        # return HttpResponse("""
        # <html>
        #     <img src='data:image/png;base64,%s' style='width:280px'/>
        #
        # </html>
        #
        # """%str)

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

        treearr = np.load('tree.npy')
        filecounts = len(treearr)
        print(filecounts)
        tf = True
        while True:
            ran = random.randrange(0, filecounts)
            for i in Trees.objects.all():
                if ran != int(i.treeID)-1:
                    tf = True
                else:
                    tf = False
                    break
            if tf == True:
                break
        pass

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

        img = np.reshape(treearr[ran],(28,28))
        imarr = Image.fromarray(img)
        imcrop = imarr.crop()
        btio = io.BytesIO()
        imcrop.save(btio,format='PNG')
        btio = btio.getvalue()
        encodebyte = base64.b64encode(btio)
        strPNG = encodebyte.decode('ascii')


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
        return render(request,'index.html',{'trees':trees,'quest':quest,'tq':zip(trees,quest),'treenum':ran,'treedata':strPNG,'maxnum':len(treearr)})
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
