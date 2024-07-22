from repos import DadosRepositorios
from manipula_repos import ManipulaRepositorios


amz_repo = DadosRepositorios('amzn')
ling_mais_usadas_amz = amz_repo.cria_df_linguagens()

print(f'{ling_mais_usadas_amz}')

flix_repo = DadosRepositorios('netflix')
ling_mais_usadas_flix = flix_repo.cria_df_linguagens()

print(f'{ling_mais_usadas_flix}')

spot_repo = DadosRepositorios('spotify')
ling_mais_usadas_spot = spot_repo.cria_df_linguagens()

print(f'{ling_mais_usadas_spot}')

# Salvando os dados processados

ling_mais_usadas_amz.to_csv('processados/linguagens_amz.csv')
ling_mais_usadas_flix.to_csv('processados/linguagens_flix.csv')
ling_mais_usadas_spot.to_csv('processados/linguagens_spot.csv')

# Iniciando Repositorio
my_repo = ManipulaRepositorios('mrtokun')
nome_repo = 'linguages-utilizadas_empresas'
my_repo.cria_repo(nome_repo)

# Salvando no repositorio
my_repo.salva_arquivo(nome_repo=nome_repo, nome_arquivo='linguagens_amz.csv', caminho_arquivo='processados/')
my_repo.salva_arquivo(nome_repo=nome_repo, nome_arquivo='linguagens_flix.csv', caminho_arquivo='processados/')
my_repo.salva_arquivo(nome_repo=nome_repo, nome_arquivo='linguagens_spot.csv', caminho_arquivo='processados/')