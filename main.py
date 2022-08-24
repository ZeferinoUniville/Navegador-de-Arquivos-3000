import os


response = ''
print("\n\n\n Bem vindo ao Navegador de Arquivos 3000, use --help pra saber a Lista de comandos")

while response != 'exit':

    response = input(os.getcwd()+"> ")

    if response == '--help':
        print("==========================================================================\n")
        print("---------------------- Lista de Comandos Possíveis -----------------------\n")
        print("--help    - Lista todos os comandos \n")
        print("--version - mostra versão do programa \n")
        print("mkdir     - Cria um diretório \n")
        print("rmdir     - Deleta um diretório \n")
        print("cd        - muda o diretorio \n")
        print("ls        - lista os subdiretorios do diretorio atual \n")
        print("touch     - cria um novo arquivo \n")
        print("remove    - remove um arquivo \n")
        print("exit      - sai do terminal \n")
        print("==========================================================================")
        print(" ") 

    elif response == '--version':
        print(" Versão 1.2 \n") 

    elif response.startswith('mkdir'):
        nomeDiretorio = response.replace("mkdir ",'')
        os.makedirs(nomeDiretorio) 
        print(" ") 

    elif response.startswith('rmdir'):
        nomeDiretorio = response.replace("rmdir ",'')
        os.rmdir(nomeDiretorio)
        print(" ")

    elif response.startswith('cd'):
        nomeDiretorio = response.replace("cd ",'')
        os.chdir(nomeDiretorio)
        print(" ") 

    elif response.startswith('ls'):
        nomeDiretorio = response.replace("ls ",'')
        ls = os.listdir()
        print(ls) 

    elif response.startswith('touch'):
        nomeDiretorio = response.replace("touch ",'')
        open(nomeDiretorio,"a")
        print(" ") 

    elif response.startswith('remove'):
        nomeDiretorio = response.replace("remove ",'')
        os.remove(nomeDiretorio)
        print(" ") 

    elif response == 'exit':
        print(" ")

    else:
        print("Comando inválido \n")

print(" Bye ")