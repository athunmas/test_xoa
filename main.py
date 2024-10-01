import requests
from bs4 import BeautifulSoup
url = 'https://metruyenvip.com/the-loai/truyen-full#google_vignette'
with open ('filename.txt' , 'w') as file:
    pass
ds = []
response  = requests.get(url)
print(response)
if response.status_code == 200:
    soup = BeautifulSoup(response.text , 'html.parser')
    table = soup.find('div' , class_ = 'w3-row list-content')
    imgs = table.find_all('div', class_ = 'w3-col s2 m2 l2 row-image')
    info = table.find_all('div', class_ = 'w3-col s7 m7 l7 row-info')
    for index,img in enumerate(imgs):
        img_url = img.find('img').get('data-src')
        list_save = []
        list_save.append(img_url)
        pags = info[index].find_all('a')
        texts = [p.get_text(strip = True) for p in pags]
        list_save.extend(texts)
        ds.append(list_save)
for tmp in ds:
    with open('filename.txt', 'a',  encoding='utf=8') as file:
    # Thêm dữ liệu vào tập tin
        file.write(f"{'#'.join(map(str , tmp)) }\n")
