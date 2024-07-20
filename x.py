import requests
import time
import random
import datetime

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

def tap_tap_task(account_token):
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
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; vivo 2019 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36',
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

def claim_tap_guru(account_token):
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
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; vivo 2019 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36',
        'X-Requested-With': 'org.telegram.plus'
    }
    payload = {}
    if send_request(url, headers, payload):
        print(f'Tap Guru claimed for token {account_token}.')

def claim_full_tank_energy(account_token):
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
        'User-Agent': 'Mozilla/5.0 (Linux; Android 12; vivo 2019 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.134 Mobile Safari/537.36',
        'X-Requested-With': 'org.telegram.plus'
    }
    payload = {}
    if send_request(url, headers, payload):
        print(f'Full Tank Energy claimed for token {account_token}.')

def main():
    account_tokens = read_data('data.txt')
    total_accounts = len(account_tokens)
    
    while True:
        for i, token in enumerate(account_tokens):
            print(f'Processing account {i+1}/{total_accounts} with token {token}')
            tap_tap_task(token)
            time.sleep(5)  # Delay between account switches
        
        countdown_timer(600, 'Tap Tap')  # 10-minute countdown after all accounts are processed
        
        for token in account_tokens:
            claim_full_tank_energy(token)
            time.sleep(5)  # Delay between account switches
        countdown_timer(43200, 'Full Tank Energy')  # 12-hour countdown for Full Tank Energy
        
        for token in account_tokens:
            claim_tap_guru(token)
            time.sleep(5)  # Delay between account switches
        next_claim_date = datetime.datetime.now() + datetime.timedelta(days=1)
        while datetime.datetime.now() < next_claim_date:
            remaining_time = (next_claim_date - datetime.datetime.now()).total_seconds()
            countdown_timer(int(remaining_time), 'Tap Guru')  # 1-day countdown for Tap Guru

if __name__ == "__main__":
    main()
