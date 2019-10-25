import sys
sys.path.append("C:/Users/zyc14588/AppData/Local/Programs/Python/Python38/Lib/site-packages/xmnlp/sentiment")
from xmnlp.trainer import SentimentTrainer

SentimentTrainer.sentiment('./pos.txt', './neg.txt', './sentiment_gj.pickle')
