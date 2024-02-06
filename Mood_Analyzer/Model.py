from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Model():

    def __init__(self):
        self.sid = SentimentIntensityAnalyzer()

    def analyze(self, post):
        ss = self.sid.polarity_scores(post)
        for k in sorted(ss):
            print('{0}: {1}, '.format(k, ss[k]), end='')
        print('\n')







