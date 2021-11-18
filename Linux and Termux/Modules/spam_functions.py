import requests

def alfapharm(number):
    value = 0;
    try:
        data = '{"fromForgot":false,"number":"' + number + '"}'
        headers = {
            'authority': 'api.alfapharm.am',
            'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
            'language': 'hy',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhYjEzYmMwMC1lYWJlLTRjOWEtYTIwMC04OWRiMGYxOTUyMDgiLCJ1bmlxdWVfbmFtZSI6ImFiMTNiYzAwLWVhYmUtNGM5YS1hMjAwLTg5ZGIwZjE5NTIwOCIsImp0aSI6IjkyZmU2NTIyLTdiMzYtNGEyMS1iYTFiLTJmZjY5YjYzNzcyNSIsImlhdCI6MTYzMzI1NjAyMSwibmJmIjoxNjMzMjU2MDIwLCJleHAiOjE2NjQ3OTIwMjAsImlzcyI6IndlYkFwaSIsImF1ZCI6Imh0dHA6Ly9sb2NhbGhvc3Q6NTAwMC8ifQ.H35uXMT978C_eWAb3EFc0vgGbI2e85omZ_pepSAZj3w',
            'content-type': 'application/json',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
            'ostype': '3',
            'sec-ch-ua-platform': '"Windows"',
            'accept': '*/*',
            'origin': 'https://alfapharm.am',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://alfapharm.am/',
            'accept-language': 'en-US,en;q=0.9',
        }
        response = requests.post('https://api.alfapharm.am/api/auth/code', headers=headers, data=data)
        value = 1
    except:
        value = 0
    return value