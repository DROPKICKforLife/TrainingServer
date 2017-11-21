import numpy as np
import jsonlines
from matplotlib import pyplot as plt
import io
import base64
class XYData:
    count = []
    x = []
    y = []
    def __init__(self):

        with jsonlines.open('tree.ndjson') as reader:

            for obj in reader:
                cnt = 0
                xx = []
                yy = []
                for i in obj['drawing']:
                    xx.append(i[0])
                    yy.append(i[1])
                    cnt += 1
                self.x.append(xx)
                self.y.append(yy)
                self.count.append(cnt)

# xy = XYData()
# print(xy.count[0])
# for j in range(xy.count[0]):
#     plt.plot(xy.x[0][j],xy.y[0][j],color='black')
# plt.axis('off')
#
# btio = io.BytesIO()
# file = plt.savefig(btio,format='png',facecolor='w')
# print(file)
#
# btio = btio.getvalue()
# encodebyte = base64.b64encode(btio)
# strPNG = encodebyte.decode('ascii')
# print(strPNG)
# print(len(strPNG))
