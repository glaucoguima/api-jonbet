import requests
import time

def resultados():

    cookies = {
        '_gid': 'GA1.2.781127896.1714749072',
        'AMP_MKTG': 'JTdCJTdE',
        '_did': 'web_712234434B09A034',
        'kwai_uuid': '4f8f5347e9db8f1a30e3a0751d616c40',
        '_gcl_au': '1.1.1274132088.1714749077',
        '_fbp': 'fb.1.1714749077202.1498210684',
        'AMP': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5NTBlMTNlMy05MDBiLTQwMTQtYWE2Yy0xZDY4MWEzOGVmNzYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzQ5MDc0MzA0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDc0OTA3NDM5MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMCU3RA==',
        '_ga_LR2H8FWXB7': 'GS1.1.1714757367.3.1.1714757372.0.0.0',
        '_ga': 'GA1.1.1834781342.1714749072',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,zh;q=0.5,it;q=0.4,es;q=0.3,ru;q=0.2',
        # 'cookie': '_gid=GA1.2.781127896.1714749072; AMP_MKTG=JTdCJTdE; _did=web_712234434B09A034; kwai_uuid=4f8f5347e9db8f1a30e3a0751d616c40; _gcl_au=1.1.1274132088.1714749077; _fbp=fb.1.1714749077202.1498210684; AMP=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI5NTBlMTNlMy05MDBiLTQwMTQtYWE2Yy0xZDY4MWEzOGVmNzYlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE0NzQ5MDc0MzA0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNDc0OTA3NDM5MCUyQyUyMmxhc3RFdmVudElkJTIyJTNBMCU3RA==; _ga_LR2H8FWXB7=GS1.1.1714757367.3.1.1714757372.0.0.0; _ga=GA1.1.1834781342.1714749072',
        'device_id': '950e13e3-900b-4014-aa6c-1d681a38ef76',
        'ipcountry': 'BR',
        'priority': 'u=1, i',
        'referer': 'https://jonbet.com/pt/games/double',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'session_id': '1714749074304',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-client-language': 'pt',
        'x-client-version': 'v2.280.0',
        'x-kl-kis-ajax-request': 'Ajax_Request',
    }

    response = requests.get('https://jonbet.com/api/roulette_games/recent', cookies=cookies, headers=headers)

    if response.status_code == 200:
       data = response.json()
       results =  [result ['roll'] for result in data]
       return results
    
resultado_anterior = []    
    
while True: 

    results = resultados()

    if resultado_anterior != results:
        resultado_anterior = results
        print('Resultado:', results)
    time.sleep(3)


