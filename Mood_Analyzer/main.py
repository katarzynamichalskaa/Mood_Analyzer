from model import Model
from reddit import Posts
def main():

    #reddit
    reddit = Posts(url="https://www.reddit.com/r/popular/hot/?geo_filter=us")
    links = reddit.get_links()
    posts_to_analyse = reddit.get_post(links)

    #analyze
    model = Model()
    for post in posts_to_analyse:
        print(post)
        model.analyze(post)

if __name__ == "__main__":
    main()
















'''
sentences = ["That is too expensive.",
    "She is a snob.",
    "Starbucks is one of the best coffee shop for me.",
    "Winter is not my favorite weather.",
    "In my opinion, Facebook is one of the common apps that can be found everywhere.",
    "Italian food tastes best",
    "reading is boring"

 ]

tricky_sentences = [
    "Kasia is GREAT",
    "marriage should be for everyone",
    "the government is in the best position to solve many problems",

 ]

sentences.extend(tricky_sentences)
for sentence in sentences:
     sid = SentimentIntensityAnalyzer()
     print(sentence)
     ss = sid.polarity_scores(sentence)
     for k in sorted(ss):
         print('{0}: {1}, '.format(k, ss[k]), end='')
     print('\n')
'''