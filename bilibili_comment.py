import requests
import json
import xmnlp
from xmnlp.sentiment import load, predict
from wordcloud import WordCloud, ImageColorGenerator
import jieba
import re
import sys
sys.path.append("C:/Users/zyc14588/AppData/Local/Programs/Python/Python38/Lib/site-packages/xmnlp/sentiment")
#load("./sentiment_gj_600k_1.pickle")
if __name__ == '__main__':
    with open("av.txt","r",encoding="utf-8") as fx,open("total.txt","w",encoding="utf-8") as tt:
        for av in fx.readlines():
            html="https://api.bilibili.com/x/v2/reply?type=1&pn="
            count=1
            av=str(av).replace('\n','')
            fi=open("comm_csv/"+str(av)+'bilibili.csv','w',encoding='utf-8')
            fii=open("comm_csv/"+str(av)+'bilibili_hot.csv','w',encoding='utf-8')
            fiii=open("datas/"+str(av)+'bilibili.txt','w',encoding='utf-8')

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
                            hotMsg=hotMsg.replace('\n',',')
                            fii.write(hotMsg +','+ '\n')
                            '''
                            if xmnlp.sentiment(hotMsg)<0.1:
                                print('热评:', hotMsg)
                                print('情感倾向',xmnlp.sentiment(hotMsg))
                            '''
                            if cont['data']['hots'][i]['replies']==None:
                                continue
                            leng=len(cont['data']['hots'][i]['replies'])
                            for j in range(leng):
                                # 热门评论回复内容
                                hotMsgRp=cont['data']['hots'][i]['replies'][j]['content']['message']
                                hotMsgRp=hotMsgRp.replace('\n',',')
                                fii.write(hotMsgRp+','+'\n')
                    except:
                        pass
                if lengthRpy!=0:
                    for i in range(lengthRpy):
                        comMsg=cont['data']['replies'][i]['content']['message']
                        comMsg=comMsg.replace('\n',',')
                        comUse=cont['data']['replies'][i]['member']['uname']
                        fi.write(comUse+','+comMsg +','+ '\n')
                        fiii.write(comMsg+'\n')
                        tt.write(comMsg+'\n')
                        '''
                        if xmnlp.sentiment(comMsg)<0.1:
                            print('评论:',comMsg)
                            print('情感倾向', xmnlp.sentiment(comMsg))
                        '''
                        if cont['data']['replies'][i]['replies']== None:
                            continue
                        leng=len(cont['data']['replies'][i]['replies'])
                        for j in range(leng):
                            comMsgRp=cont['data']['replies'][i]['replies'][j]['content']['message']
                            comMsgRp=comMsgRp.replace('\n',',')
                            comUseRp = cont['data']['replies'][i]['replies'][j]['member']['uname']
                            fi.write(comUseRp+','+comMsgRp + '\n')
                            fiii.write(comMsgRp + '\n')
                            tt.write(comMsgRp+'\n')

                else:
                    break
            #print("第%d页写入成功！"%count)
                count += 1
            print(count-1,'页评论写入成功！')
            fi.close()
            fii.close()
            fiii.close()
        fx.close()
        tt.close()
    with open("av.txt", "r", encoding="utf-8") as fx,open("total.txt","r",encoding="utf-8")as tt:
        # 打开文件，将编码设置为UTF-8
        for av in fx.readlines():
            av=str(av).replace('\n','')
            with open("datas/"+str(av)+'bilibili.txt','r',encoding='utf-8') as f:
                mytext = f.read()
    # 删除特殊符号
                mytext = re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", mytext)
    # 进行分词，这里选用的jieba.cut_for_search（互联网分词方法）
                wordlist_jieba = jieba.cut_for_search(mytext,HMM=True)
    # 在每个词之间添加空格
                wl_space_split = " ".join(wordlist_jieba)
    # 设置云词参数
                wc = WordCloud(
                    font_path=r'C:\Windows\Fonts\SIMYOU.TTF',
                    width=800,
                    height=600,
                    margin=10,
                    max_font_size=100,
                    background_color='white',
                    min_font_size=10,
                    max_words=500,
                )
    # 生成分词图
                wc.generate(wl_space_split)
    # 将分词图保存
                wc.to_file("pngs/"+str(av)+".png")
                f.close()
                print(str(av)+"ok")
        mytext = tt.read()
    # 删除特殊符号
        mytext = re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", mytext)
    # 进行分词，这里选用的jieba.cut_for_search（互联网分词方法）
        wordlist_jieba = jieba.cut_for_search(mytext, HMM=True)
    # 在每个词之间添加空格
        wl_space_split = " ".join(wordlist_jieba)
    # 设置云词参数
        wc = WordCloud(
            font_path=r'C:\Windows\Fonts\SIMYOU.TTF',
            width=800,
            height=600,
            margin=10,
            max_font_size=100,
            background_color='white',
            min_font_size=10,
            max_words=500,
        )
    # 生成分词图
        wc.generate(wl_space_split)
    # 将分词图保存
        wc.to_file("pngs/总图" + ".png")
        print("总图" + "ok")
    fx.close()
    tt.close()
    exit(0)
