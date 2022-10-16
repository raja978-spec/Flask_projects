from google_play_scraper import app,Sort,reviews,reviews_all
from textblob import TextBlob
import matplotlib.pyplot as plt

class StarbasedAnalyzer():
        
    def Star_Lazy_Analysis(self,appid,star):
        try:
            review = reviews_all(
            appid,
            lang='en', # defaults to 'en'
            country='us', # defaults to 'us'
            sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
            filter_score_with=star,
            ) 
            positive = 0
            negative = 0
            neutral = 0
            polarity = 0
            '''
            def percentage(self,part,whole):
                    return 100*float(part)/float(whole)
            '''
            for i in range(len(review)):
                comments=review[i]['content']
                analyzer=TextBlob(comments)
                polarity += analyzer.sentiment.polarity
                if analyzer.sentiment.polarity > 0:
                    positive += 1
                elif analyzer.sentiment.polarity < 0:
                    negative += 1
                elif analyzer.sentiment.polarity == 0:
                    neutral += 1
            positive = 100*float(positive)/float((positive + negative + neutral))
            negative = 100*float(negative)/float((positive + negative + neutral))
            neutral = 100*float(neutral)/float((positive + negative + neutral))
            positive = format(positive,'.2f')
            negative = format(negative,'.2f')
            neutral = format(neutral,'.2f')
            labels = ['Positive Comments ['+str(positive)+'%]', 'Negative Comments ['+str(negative)+'%]', 'Neutral Commments ['+str(neutral)+'%]']
            sizes = [positive, negative, neutral]
            colors = ['blue','red','yellow']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90)
            plt.legend(patches,labels,loc="best")
            #plt.title("Fake Pie Chart")
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig("static/images/piechart.png")
            return 1
        
        except Exception as e:
            return e
    def Star_Quick_Analysis(self,appid,star):
        try:
            result,review = reviews(
                appid,
                lang='en', # defaults to 'en'
                country='us', # defaults to 'us'
                sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
                filter_score_with=star,
            )
            result,_=reviews(
                appid,
                continuation_token=review
                )
            positive = 0
            negative = 0
            neutral = 0
            polarity = 0
            
            '''
            def percentage(self,part,whole):
                    return 100*float(part)/float(whole)
            '''
            for i in range(len(result)):
                comments=result[i]['content']
                analyzer=TextBlob(comments)
                polarity += analyzer.sentiment.polarity
                if analyzer.sentiment.polarity > 0:
                    positive += 1
                elif analyzer.sentiment.polarity < 0:
                    negative += 1
                elif analyzer.sentiment.polarity == 0:
                    neutral += 1
            positive = 100*float(positive)/float((positive + negative + neutral))
            negative = 100*float(negative)/float((positive + negative + neutral))
            neutral = 100*float(neutral)/float((positive + negative + neutral))
            positive = format(positive,'.2f')
            negative = format(negative,'.2f')
            neutral = format(neutral,'.2f')
  
            labels = ['Positive Comments ['+str(positive)+'%]', 'Negative Comments ['+str(negative)+'%]', 'Neutral Comments ['+str(neutral)+'%]']
            sizes = [positive, negative, neutral]
            colors = ['blue','red','yellow']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90,shadow=1)
            plt.legend(patches,labels,loc="best")
            #plt.title("Fake level Pie Chart")
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig("static/images/piechart.png")
            return 1
        
        except Exception as e:
            return e  

class NormalAnalyer():
    def Lazy_Analysis(self,appid):
        try:
            review = reviews_all(
            appid,
            lang='en', # defaults to 'en'
            country='us', # defaults to 'us'
            sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
            ) 
            positive = 0
            negative = 0
            neutral = 0
            polarity = 0
            '''
            def percentage(self,part,whole):
                    return 100*float(part)/float(whole)
            '''
            for i in range(len(review)):
                comments=review[i]['content']
                analyzer=TextBlob(comments)
                polarity += analyzer.sentiment.polarity
                if analyzer.sentiment.polarity > 0:
                    positive += 1
                elif analyzer.sentiment.polarity < 0:
                    negative += 1
                elif analyzer.sentiment.polarity == 0:
                    neutral += 1
            positive = 100*float(positive)/float((positive + negative + neutral))
            negative = 100*float(negative)/float((positive + negative + neutral))
            neutral = 100*float(neutral)/float((positive + negative + neutral))
            positive = format(positive,'.2f')
            negative = format(negative,'.2f')
            neutral = format(neutral,'.2f')
            labels = ['Positive Comments ['+str(positive)+'%]', 'Negative Comments ['+str(negative)+'%]', 'Neutral Commments ['+str(neutral)+'%]']
            sizes = [positive, negative, neutral]
            colors = ['blue','red','yellow']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90)
            plt.legend(patches,labels,loc="best")
            #plt.title("Fake Pie Chart")
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig("static/images/piechart.png")
            return 1
        
        except Exception as e:
            return e
    def Quick_Analysis(self,appid):
        try:
            result,review = reviews(
                appid,
                lang='en', # defaults to 'en'
                country='us', # defaults to 'us'
                sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
            )
            result,_=reviews(
                appid,
                continuation_token=review
                )
            positive = 0
            negative = 0
            neutral = 0
            polarity = 0
            
            '''
            def percentage(self,part,whole):
                    return 100*float(part)/float(whole)
            '''
            for i in range(len(result)):
                comments=result[i]['content']
                analyzer=TextBlob(comments)
                polarity += analyzer.sentiment.polarity
                if analyzer.sentiment.polarity > 0:
                    positive += 1
                elif analyzer.sentiment.polarity < 0:
                    negative += 1
                elif analyzer.sentiment.polarity == 0:
                    neutral += 1
            positive = 100*float(positive)/float((positive + negative + neutral))
            negative = 100*float(negative)/float((positive + negative + neutral))
            neutral = 100*float(neutral)/float((positive + negative + neutral))
            positive = format(positive,'.2f')
            negative = format(negative,'.2f')
            neutral = format(neutral,'.2f')
  
            labels = ['Positive Comments ['+str(positive)+'%]', 'Negative Comments ['+str(negative)+'%]', 'Neutral Comments ['+str(neutral)+'%]']
            sizes = [positive, negative, neutral]
            colors = ['blue','red','yellow']
            patches, texts = plt.pie(sizes, colors=colors, startangle=90,shadow=1,radius=5.00)
            plt.legend(patches,labels,loc="best")
            #plt.title("Fake level Pie Chart")
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig("static/images/piechart.png")
            return 1
        except Exception as e:
            return e 
