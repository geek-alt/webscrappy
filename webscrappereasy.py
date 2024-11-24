from bs4 import BeautifulSoup
import requests
import sqlite3

url= 'https://store.steampowered.com/search/?filter=popularnew&sort_by=Released_DESC&os=win'

response = requests.get(url)
html_content=response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all <a> tags
games = soup.find_all('a', class_='search_result_row')


conn = sqlite3.connect('steam_games.db')
cursor = conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS games(
               title TEXT,
               url TEXT,
               image_url TEXT,
               release_date TEXT,
               price TEXT
    )
''')




for game in games:
    title = game.find('span', class_='title').text
    url = game['href']
    image_url = game.find('img')['src']
    release_date_element = game.find('div', class_='col search_released responsive_secondrow')
    release_date = release_date_element.text.strip() if release_date_element else 'No Release Date'
    price_element = game.find('div', class_='discount_final_price')
    price = price_element.text.strip() if price_element else 'N/A'

    cursor.execute('''
        INSERT INTO GAMES(title, url, image_url, release_date, price)
        VALUES(?,?,?,?,?)
    ''',(title, url, image_url, release_date, price))

    
conn.commit()
conn.close()


