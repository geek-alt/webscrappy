import lxml.html
import requests



html = requests.get('https://store.steampowered.com/search/?filter=popularnew&sort_by=Released_DESC&os=win')
doc = lxml.html.fromstring(html.content)


new_releases = doc.xpath('//div[@id="search_results"]')[0]
prices = new_releases.xpath('//div[@class="discount_final_price"]/text()')
titles = new_releases.xpath('//span[contains(@class, "title")]/text()')
games = doc.xpath('//a[contains(@class, "search_result_row")]')

print("Number of games:", len(games))

print(new_releases)
# print("Extracted new releases element:", new_releases.text_content())
print(titles)
print(prices)

# tags_divs = new_releases.xpath('//div[@class="tab_item_top_tags"]')
# tags=[]
# for div in tags_divs:
#     tags.append(div.text_content())
# tags= [tag.split(', ') for tag in tags]

total_platforms=[]

for game in games:
    platform_spans=game.xpath('.//span[contains(@class, "platform_img")]')

    platforms = []


#loop over platforms span and extract platforms

    for span in platform_spans:
        platform_class = span.get('class', '') #get class attribute
        if 'platform_img' in platform_class:
             # Extracting platforms names like win linux mac
            platform_name = platform_class.split(' ')[1]
            platforms.append(platform_name)

    total_platforms.append(platforms)

print(total_platforms)


#output

output = []
for info in zip(titles,prices,total_platforms):
    resp={}
    resp['title']= info[0]
    resp['price']=info[1]
    resp['platforms']=info[2]
    output.append(resp)


print("Debuged")
for game in games[:5]:  # Print out the first 5 games
    print(lxml.html.tostring(game))

