# -*- coding: utf-8 -*-
from naivebayes1 import NaiveBays
nb=NaiveBays()
nb.trainModel('D:\spamham.csv')
num=nb.getAcuuracy()
print(num)
predict=nb.getPrediction('I i am gonna be home soon and i dont wanna talk about this stuff anymore  tonight , k? i have cried enough'  )
#predict=nb.getPrediction("england v barcelona - dont miss the goals/team.news.up national team to 87077 eg ENGLAND to 8545 try:wales ,SCOTLAND 4fwefej/tx1.20")                             
print(predict)