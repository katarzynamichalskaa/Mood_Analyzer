import requests
from bs4 import BeautifulSoup

class Get_content():
    def __init__(self, url):
        self.url = url

    def get_content(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            return response.text

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

class Posts(Get_content):

    def get_links(self):
        links = []
        content = self.get_content()

        if content:
            soup = BeautifulSoup(content, 'lxml')
            post_links = soup.find_all('a', class_='absolute inset-0', attrs={'slot': 'full-post-link'})

            for link in post_links:
                links.append(link['href'])
        return links

    def get_post(self, links):
        posts_to_analyse = []
        for link in links:
            url = f'https://www.reddit.com{link}'
            new_page_content = Get_content(url).get_content()

            if new_page_content:
                soup = BeautifulSoup(new_page_content, 'lxml')
                post = soup.find('h1', slot='title')
                posts_to_analyse.append(post.text.strip())

        return posts_to_analyse


