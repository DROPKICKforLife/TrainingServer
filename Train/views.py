from django.shortcuts import render
from django.http import HttpResponse
import configparser
import os
import glob
import re
import random
from django.http import HttpResponseRedirect
from .models import Trees
from PIL import Image
import io
import base64
from matplotlib import pyplot as plt
import numpy as np
def index(request):
    trees = np.load('tree.npy')
    print(trees.size)
    for i in range(1):
        print(trees[i])
        # trees[i] = np.reshape(trees[i],(28,28))
        img = np.reshape(trees[i],(28,28))
        print(np.shape(img))
        im = Image.fromarray(img)
        image = im.crop()
        bytearr = io.BytesIO()
        image.save(bytearr,format="PNG")
        bytearr = bytearr.getvalue()
        encodebyte = base64.b64encode(bytearr)
        str = encodebyte.decode('ascii')
        print(str)
        im.show()
        print(np.size(trees))
        print(len(trees))
        return HttpResponse("""
        <html>
            <img src='data:image/png;base64,%s' style='width:280px'/>
        
        </html>
        
        """%str)

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
        for i in Trees.objects.all():
            while True:
                ran = random.randrange(0,filecounts)
                if ran == int(i.treeID)-1:
                    continue
                else:
                    print("random int : %s"%ran)
                    break
                    pass
                pass

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
