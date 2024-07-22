import pandas as pd
import requests
import base64

r = requests.get('https://api.github.com/versions')
r.json()


headers = {'Authorization': 'Bearer' + access_token, 'X-GitHub-Api-Version': '2022-11-28'}

# api_base_url = 'https://api.github.com'
# owner = 'amzn'
# url = f'{api_base_url}/users/{owner}/repos'

# repos_list = []
# for page_num in range(1,8):
#     try:
#         url_page = f'{url}?page={page_num}'
#         response = requests.get(url_page, headers=headers)
#         repos_list.append(response.json())
#     except:
#         repos_list.append(None)

# repos_name = []
# for page in repos_list:
#     for repo in page:
#         repos_name.append(repo['name'])
# repos_name  


# repos_langs = []
# for page in repos_list:
#     for repo in page:
#         repos_langs.append(repo['name'])



# amz_repos = pd.DataFrame()
# amz_repos['repos_name'] = repos_name
# amz_repos['repos_langs'] = repos_langs
# print(f'{amz_repos}')

# amz_repos.to_csv('amazon.csv')


headers = {'Accept':'application/vnd.github+json',
    'Authorization': 'Bearer ' + access_token, 
           'X-GitHub-Api-Version': '2022-11-28',
           }

api_base_url = 'https://api.github.com'
url = f'{api_base_url}/user/repos'

data = {
    'name': 'linguagens-utilizadas',
    'description':'Repositorio com as linguagens de prog da Amazon',
    'private':False
}

response = requests.post(url, json=data, headers=headers)
#  response.status_code

print(f'{response.status_code}')
print(f'{response.text}')
# print(f'{response.json}')
# print(f'{response.iter_content}')

with open('amazon.csv', 'rb') as arquivo:
    file_content = arquivo.read()

encoded_content = base64.b64enconde(file_content)

api_base_url = 'https://api.github.com'
username = 'mrtokun'
repo =  'linguagens-utilizadas'
path = 'arquivos/amazon.csv'

url = f'{api_base_url}/repos/{username}/{repo}/contents/{path}'
url