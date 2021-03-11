
"""
Created on Tue Jul  2 15:05:56 2019

@author: ian
"""
#%%
import urllib.request
import bs4 as bs
import matplotlib.pyplot as plt

fourth_news = 0
politics_news = 0
world_news = 0
other_news = 0

def headlineCatagory(h):
    
    global fourth_news
    global politics_news
    global world_news
    global other_news
    
    if headline_catagory_fourth(h):
        fourth_news += 1
    elif headline_catagory_politics(h):
        politics_news += 1
    elif headline_catagory_world(h):
        world_news += 1
    else:
        other_news += 1

def headline_catagory_fourth(h):
    if "Fourth" in h or "4th" in h or "Fireworks" in h:
        return True
    else:
        return False
    
def headline_catagory_politics(h):
    if "Republican" in h or "Democrat" in h or "Congress" in h or "Trump" in h:
        return True
    else:
        return False
    
def headline_catagory_world(h):
    if "US" in h or "Hong Kong" in h or "Switzerland" in h:
        return True
    else:
        return False
    


search_endpoint = "https://www.clickondetroit.com/news"
request = urllib.request.Request(search_endpoint, headers={
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0",
})

html_code = urllib.request.urlopen(search_endpoint).read()

parsed_html = bs.BeautifulSoup(html_code, "html.parser")


headline = parsed_html.select('#article_10154_28243_843690586_1\.0 > div > div > div.primary > article > a > div.content > h3')
headline_string = headline[0].getText().replace('<h3 class="title">','')
print("\n\n********NEWEST HEADLINE: \"" + headline_string + "\"\n")
headlineCatagory(headline_string)

print("****Recent headlines: ")

headline = parsed_html.select('#article_10154_28243_843690586_1\.0 > div > div > div.secondary > article:nth-child(1) > a > div.content > h3')
headline_string = headline[0].getText().replace('<h3 class="title">','')
print("\"" + headline_string + "\"")
headlineCatagory(headline_string)

headline = parsed_html.select('#article_10154_28243_843690586_1\.0 > div > div > div.secondary > article:nth-child(2) > a > div.content > h3')
headline_string = headline[0].getText().replace('<h3 class="title">','')
print("\"" + headline_string + "\"")
headlineCatagory(headline_string)

print("\nTypes of news:")
print("Fourth of July News: " + str(fourth_news))
print("Political News " + str(politics_news))
print("World News: " + str(world_news))
print("Other News: " + str(other_news))


# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ["4th", "Politics", "World", "Other"]
sizes = [fourth_news, politics_news, world_news, other_news]
explode = (0, 0.1, 0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
