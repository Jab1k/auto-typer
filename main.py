
import requests
import time as t

discord_token = 'NzUzODAxODM4OTUxOTIzODMy.GAug5S.jbbmk_v72WQR7ZyQeh95y6tUp0mi-m-MlIL04c'
channel_id = '952308179621015584'
cnt = """
# СДАМ
```
скользкую - 10k
```
"""""
with open('x.jpg', 'rb') as file:
    image_data = file.read()
while True:
            
    response = requests.post(
    f'https://discord.com/api/v9/channels/{channel_id}/messages', 
    headers={
        'Authorization': discord_token,
    },
    files={
         'file': ('photo.png', image_data),
    },
    data={
    'content':cnt,
    
    'content-type': 'application/json',
    })
    if response.status_code == 200:
        print('Photo sent successfully!')
    else:
        print('Failed to send the photo:', response.text)
    t.sleep(2000)