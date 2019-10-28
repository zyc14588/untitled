import pandas as pd
pd_all = pd.read_csv('F:/BaiduNetdiskDownload/simplifyweibo_4_moods/simplifyweibo_4_moods.csv',encoding='utf-8')
#pd_all = pd.read_csv('F:/BaiduNetdiskDownload/weibo_senti_100k/weibo_senti_100k.csv',encoding='utf-8')
#pd_all = pd.read_csv('E:/untitled/online_shopping_10_cats.csv',encoding='utf-8')

#moods = {0: '喜悦', 1: '愤怒', 2: '厌恶', 3: '低落'}
fi = open('pos.txt', 'a', encoding='utf-8')
fii = open('neg.txt', 'a', encoding='utf-8')
print('微博数目（总体）：%d' % pd_all.shape[0])

#for label, mood in moods.items():
    #print('微博数目（{}）：{}'.format(mood,  pd_all[pd_all.label==label].shape[0]))

for index,row in pd_all.iterrows():
    label=row["label"]
    review=row["review"]
    if label==0:
        fi.write(str(review)+'\n')
    else:
        fii.write(review+'\n')