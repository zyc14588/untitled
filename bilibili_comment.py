import requests
import json
import xmnlp
from xmnlp.sentiment import load, predict
import sys
#sys.path.append("C:/Users/zyc14588/AppData/Local/Programs/Python/Python38/Lib/site-packages/xmnlp/sentiment")
load('E:/untiled/stentiment_gj.pickle')
xmnlp.set_stopword('E:/untiled/百度停用词表.txt')
def getHTML(html,av):
    count=1
    fi=open('bilibili.txt','w',encoding='utf-8')
    fii=open('bilibili_hot.txt','w',encoding='utf-8')

    while(True):
        url=html+str(count)+"&oid="+str(av)
        url=requests.get(url)
        if url.status_code==200:
            cont=json.loads(url.text)
        else:
            break
        if cont['data']['replies']== None:
            break
        lengthRpy = len(cont['data']['replies'])
        if count==1:
            try:
                lengthHot=len(cont['data']['hots'])
                for i in range(lengthHot):
                    # 热门评论内容
                    hotMsg=cont['data']['hots'][i]['content']['message']
                    fii.write(hotMsg + '\n')
                    if xmnlp.sentiment(hotMsg)<0.1:
                        print('热评:', hotMsg)
                        print('情感倾向',xmnlp.sentiment(hotMsg))
                    if cont['data']['hots'][i]['replies']==None:
                        continue
                    leng=len(cont['data']['hots'][i]['replies'])
                    for j in range(leng):
                        # 热门评论回复内容
                        hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                        fii.write(hotMsgRp+'\n')
            except:
                pass
        if lengthRpy!=0:
            for i in range(lengthRpy):
                comMsg=cont['data']['replies'][i]['content']['message']
                fi.write(comMsg + '\n')
                if xmnlp.sentiment(comMsg)<0.1:
                    print('评论:',comMsg)
                    print('情感倾向', xmnlp.sentiment(comMsg))
                '''
                if cont['data']['replies'][i]['replies']== None:
                    continue
                leng=len(cont['data']['replies'][i]['replies']['message'])
                for j in range(leng):
                    comMsgRp=cont['data']['replies'][i]['replies'][j]['content']['message']
                    fi.write(comMsgRp + '\n')
                '''
        else:
            break
        #print("第%d页写入成功！"%count)
        count += 1
    fi.close()
    print(count-1,'页评论写入成功！')

html="https://api.bilibili.com/x/v2/reply?type=1&pn="
av=input("input your url:")
getHTML(html,av)