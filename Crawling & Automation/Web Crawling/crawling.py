import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
cookie = {
    'session-id': '138-0631276-4451358', 'i18n-prefs':'USD', 'sp-cdn':'"L5Z9:KR"', 'ubid-main': '135-2401861-0852649', 'session-id-time': '2082787201l', 'session-token': 'vEqLdNe1J49fcNf2alz9p+/t0hSkM2HOsc7ZT7jigVpR0GU+jWCvm5v8U9ESSAxQzpvWrRWzv1vwYS27qnFj9Z3iuM4nQ5QJl9N1BB5UPF5hv5/d8YsYs8fz9h/7MEvAjBVbrFQzhBQ9dm93vxO8ZHzPT3ZwqvjCEwyHIpUqCxjPQjyTXTPhHx5VBS5rti14NrucT7E0xQppjgYzacWHXYpNLYat7FCWOSMCKCcZuLT962Om1jY2gWh0JJXrfkJXCITcF5tMIxWWV7SYCehd0bNuUi3qcyyTsjOKNoSQIplArxyI7ae5L8t5uVzMxbw8mjpG5kPRhMBhwMo7sgb6hZG6/ApzICTb', 'csm-hit': 'tb:1F387E9S26GM0XQGW8WC+s-1F387E9S26GM0XQGW8WC|1718203525789&t:1718203525790&adb:adblk_no'
}

r = requests.get('https://www.amazon.com/s?k=monitor&ref=nb_sb_noss_2', headers=header, cookies=cookie)
print(r.status_code)
print(r.content)
soup = BeautifulSoup(r.content, 'lxml')
print(soup.select('.a-size-medium'))