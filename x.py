import requests
import time
import random
import datetime
import json

def read_data(filename):
    with open(filename, 'r') as file:
        return file.read().splitlines()

def send_request(url, headers, payload):
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code == 200

def countdown_timer(seconds, task_name):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        print(f'{task_name} countdown: {time_format}', end='\r')
        time.sleep(1)
        seconds -= 1
    print()

def generate_random_user_agent():
    android_versions = ['10', '11', '12', '13']
    device_models = [
        'vivo 2019', 'Samsung Galaxy S21', 'OnePlus 9', 'Google Pixel 6',
        'Xiaomi Mi 11', 'Huawei P40', 'Sony Xperia 5', 'Oppo Find X3'
    ]
    chrome_versions = ['91.0.4472.120', '92.0.4515.131', '93.0.4577.62', '94.0.4606.71']
    
    android_version = random.choice(android_versions)
    device_model = random.choice(device_models)
    chrome_version = random.choice(chrome_versions)
    
    user_agent = f'Mozilla/5.0 (Linux; Android {android_version}; {device_model} Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_version} Mobile Safari/537.36'
    return user_agent

def tap_tap_task(account_token, user_agent):
    url = 'https://xaptapbot.exaprotocol.com/api/tap/'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7',
        'App-Token': account_token,
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Content-Type': 'application/json',
        'Cookie': 'PHPSESSID=70thdk8pdatu56r1boc1nkf3rg; _ga=GA1.1.53767043.1721434341; _ga_E0WZ3KR44F=GS1.1.1721439234.2.1.1721439602.0.0.0',
        'Host': 'xaptapbot.exaprotocol.com',
        'Origin': 'https://xaptapbot.exaprotocol.com',
        'Referer': 'https://xaptapbot.exaprotocol.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user_agent,
        'X-Requested-With': 'org.telegram.plus'
    }
    points = 0
    while points < 250:
        taps_inc = random.randint(1, 5)
        payload = {
            "tapsInc": taps_inc,
            "initTimestamp": int(time.time() * 1000)
        }
        if send_request(url, headers, payload):
            points += taps_inc
        time.sleep(random.uniform(0.5, 1.5))
    print(f'Tap Tap task completed for token {account_token} with {points} points.')

def claim_tap_guru(account_token, user_agent):
    url = 'https://xaptapbot.exaprotocol.com/api/tappingGuru/'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7',
        'App-Token': account_token,
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Content-Type': 'application/json',
        'Cookie': 'PHPSESSID=70thdk8pdatu56r1boc1nkf3rg; _ga=GA1.1.53767043.1721434341; _ga_E0WZ3KR44F=GS1.1.1721439234.2.1.1721439602.0.0.0',
        'Host': 'xaptapbot.exaprotocol.com',
        'Origin': 'https://xaptapbot.exaprotocol.com',
        'Referer': 'https://xaptapbot.exaprotocol.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user_agent,
        'X-Requested-With': 'org.telegram.plus'
    }
    payload = {}
    if send_request(url, headers, payload):
        print(f'Tap Guru claimed for token {account_token}.')

def claim_full_tank_energy(account_token, user_agent):
    url = 'https://xaptapbot.exaprotocol.com/api/fullTank/'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7',
        'App-Token': account_token,
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Content-Type': 'application/json',
        'Cookie': 'PHPSESSID=70thdk8pdatu56r1boc1nkf3rg; _ga=GA1.1.53767043.1721434341; _ga_E0WZ3KR44F=GS1.1.1721439234.2.1.1721439602.0.0.0',
        'Host': 'xaptapbot.exaprotocol.com',
        'Origin': 'https://xaptapbot.exaprotocol.com',
        'Referer': 'https://xaptapbot.exaprotocol.com/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Android WebView";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': user_agent,
        'X-Requested-With': 'org.telegram.plus'
    }
    payload = {}
    if send_request(url, headers, payload):
        print(f'Full Tank Energy claimed for token {account_token}.')

def main():
    account_tokens = read_data('data.txt')
    total_accounts = len(account_tokens)
    
    user_agents = [generate_random_user_agent() for _ in account_tokens]
    
    while True:
        print(f'Starting Tap Tap task for {total_accounts} accounts.')
        for i, (token, user_agent) in enumerate(zip(account_tokens, user_agents)):
            print(f'Processing Tap Tap for account {i+1}/{total_accounts} with token {token} and user agent {user_agent}')
            tap_tap_task(token, user_agent)
            time.sleep(5)  # Delay between account switches
        print('All Tap Tap tasks completed.')
        
        countdown_timer(600, 'Tap Tap')  # 10-minute countdown after all accounts are processed
        
        print(f'Starting Full Tank Energy task for {total_accounts} accounts.')
        for i, (token, user_agent) in enumerate(zip(account_tokens, user_agents)):
            print(f'Processing Full Tank Energy for account {i+1}/{total_accounts} with token {token} and user agent {user_agent}')
            claim_full_tank_energy(token, user_agent)
            time.sleep(5)  # Delay between account switches
        print('All Full Tank Energy tasks completed.')
        
        countdown_timer(43200, 'Full Tank Energy')  # 12-hour countdown for Full Tank Energy
        
        print(f'Starting Tap Guru task for {total_accounts} accounts.')
        for i, (token, user_agent) in enumerate(zip(account_tokens, user_agents)):
            print(f'Processing Tap Guru for account {i+1}/{total_accounts} with token {token} and user agent {user_agent}')
            claim_tap_guru(token, user_agent)
            time.sleep(5)  # Delay between account switches
        print('All Tap Guru tasks completed.')
        
        countdown_timer(86400, 'Tap Guru')  # 1-day countdown for Tap Guru

if __name__ == "__main__":
    main()
