import requests
s=requests.session()
payload = {
    'username' : 'razifrizqullah@gmail.com',
    'password' : 'aichika21'
}
response = s.post('https://www.investopedia.com/auth/realms/investopedia/login-actions/authenticate', data=payload)
print(response.status_code)