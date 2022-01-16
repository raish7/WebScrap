
import bs4
import requests
import pandas as pd

req = requests.get('https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating')

soup = bs4.BeautifulSoup(req.text,'html.parser')

name_container = soup.find_all("h3",class_="lister-item-header")
names = [i.a.text for i in name_container]

rankings = [i.span.text for i in name_container]

year_container = soup.find_all('span',{'class':'lister-item-year text-muted unbold'})
year = [i.text.strip() for i in year_container]

rating_container = soup.find_all('div',class_="inline-block ratings-imdb-rating")
rating = [i.strong.text for i in rating_container]

print(len(names),len(rankings),len(year),len(rating))

df = pd.DataFrame({'Ranking' : rankings,
                  'Names' : names,
                  'Year' : year,
                  'Rating' : rating,
                  })

df.to_csv('IMDb1008.csv',index=False)
