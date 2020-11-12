import re
import jieba
from wordcloud import WordCloud
if __name__ == '__main__':
    with open("ddm.csv","r")as tt:
        mytext = tt.read()
    # 删除特殊符号
        mytext = re.sub(r"[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+", "", mytext)
    # 进行分词，这里选用的jieba.cut_for_search（互联网分词方法）
        wordlist_jieba = jieba.cut(mytext, HMM=True)
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
        wc.to_file("pngs/弹幕" + ".png")
        print("弹幕" + "ok")
    tt.close()