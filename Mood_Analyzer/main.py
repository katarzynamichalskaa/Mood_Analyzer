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
