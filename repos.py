import pandas as pd
import requests
import base64
from math import ceil

class DadosRepositorios:

    def __init__(self, owner):
        self.owner = owner
        self.api_base_url = 'https://api.github.com'
        # self.access_token = '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'
        self.access_token = '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'
        self.headers = {
            # 'Authorization': 'Bearer ' + self.access_token,
                         'X-GitHub-Api-Version': '2022-11-28'}

    def lista_repositorios(self):
        repos_list = []

        url = f'{self.api_base_url}/users/{self.owner}'
        response = requests.get(url)
        num_page = ceil(response.json()['public_repos']/30)

        for page_num in range(1, num_page+1):
            try:
                url = f'{self.api_base_url}/users/{self.owner}/repos?page={page_num}'
                response = requests.get(url, headers=self.headers)
                repos_list.append(response.json())
            except:
                repos_list.append(None)

        # print(f'{repos_list}')
        return repos_list
    
    def nomes_repos(self, repos_list):
        repos_name = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_name.append(repo['name'])
                except:
                    pass
        return repos_name 

    def nomes_linguagens(self, repos_list):
        repos_langs = []
        for page in repos_list:
            for repo in page:
                try:
                    repos_langs.append(repo['language'])
                except:
                    pass
        return repos_langs
    
    def cria_df_linguagens(self):
        
        repositorios = self.lista_repositorios()
        nomes = self.nomes_repos(repositorios)
        linguagens = self.nomes_linguagens(repositorios)

        amz_repos = pd.DataFrame()
        amz_repos['repos_name'] = nomes
        amz_repos['repos_langs'] = linguagens
        print(f'{amz_repos}')

        amz_repos.to_csv('amazon.csv')
        
        return amz_repos




    # r = requests.get('https://api.github.com/versions')
    # r.json()


