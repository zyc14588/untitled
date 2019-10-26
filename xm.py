#import sys
#sys.path.append("C:/Users/zyc14588/AppData/Local/Programs/Python/Python38/Lib/site-packages/xmnlp/sentiment")

#sys.path.append('E:/untitled')
from xmnlp.trainer import SentimentTrainer

SentimentTrainer.sentiment('E:/untitled/pos.txt', 'E:/untitled/neg.txt', 'E:/untitled/sentiment_gj2.pickle')
