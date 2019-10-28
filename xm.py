#import sys
#sys.path.append("C:/Users/zyc14588/AppData/Local/Programs/Python/Python38/Lib/site-packages/xmnlp/sentiment")

#sys.path.append('E:/untitled')
from xmnlp.trainer import SentimentTrainer

SentimentTrainer.sentiment('E:/untitled/pos_2.txt', 'E:/untitled/neg_2.txt', 'E:/untitled/sentiment_gj_600k_2.pickle')
