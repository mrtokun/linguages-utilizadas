import requests
import base64
class ManipulaRepositorios:
    def __init__(self, username):
        self.username = username
        self.api_base_url = 'https://api.github.com'
        # self.access_token = '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'
        self.access_token = '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'
        self.headers = {
                        'Authorization': 'Bearer ' + self.access_token,
                         'X-GitHub-Api-Version': '2022-11-28'}
        
    def cria_repo(self, nome_repo):

        url = f'{self.api_base_url}/user/repos'

        data = {
            'name': nome_repo,
            'description':'Repositorio com as linguagens de prog de algumas empresas',
            'private':False
        }

        response = requests.post(url, json=data, headers=self.headers)
        #  response.status_code

        # print(f'{response.status_code}')
        print(f'Status do POST: {response.text}')
        # # print(f'{response.json}')
        # # print(f'{response.iter_content}')

    def salva_arquivo(self, nome_repo, nome_arquivo, caminho_arquivo):


        with open(f'{caminho_arquivo}/{nome_arquivo}', 'rb') as arquivo:
            file_content = arquivo.read()

        encoded_content = base64.b64encode(file_content)

        # Realizando o upload
 
        url = f'{self.api_base_url}/repos/{self.username}/{nome_repo}/contents/{caminho_arquivo}/{nome_arquivo}'

        data = {
            'message':'Adicionando um novo arquivo.',
            'content':encoded_content.decode('utf-8')
        }

        response = requests.put(url, json=data, headers=self.headers)
        print(f'Status do PUT: {response.text}')

