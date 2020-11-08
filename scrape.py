import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

hot_topic_links = links + links2
hot_topic_subtext = subtext + subtext2

def sort_stories_by_popularity(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_by_aya(links, subtext):
  hn = []
  for idx, item in enumerate(links):
    title = item.getText()
    href = item.get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace(' points', ''))
      if points > 100:
        hn.append({'title': title, 'link': href, 'votes': points})
  return sort_stories_by_popularity(hn)

print("Here are today's hot topics!! Enjoy!!")
pprint.pprint(create_custom_by_aya(hot_topic_links, hot_topic_subtext))
print('Keep learning and enjoy your day!!')
