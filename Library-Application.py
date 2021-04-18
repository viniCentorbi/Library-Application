import os
import collections
import json

os.system ("cls")

def imprimir_cadastros (livro):
    print("Nome do livro.: %s" %livro.Titulo)
    print("Subtítulo.: %s" %livro.Subtitulo)
    print("Id.: %s" %livro.Id)
    print("ISBN: %s" %livro.Isbn)
    print("CDD: %s" %livro.Cdd)
    print("Código do autor: %s" %livro.Codigo_Autor)
    print("Edição: %s" %livro.Ediçao)
    print("Autor: %s" %livro.Autor)
    print("Série: %s"%livro.Serie)
    print("Volume: %s"%livro.Volume)
    print("Local da publicação: %s" %livro.Local_Publicaçao)
    print("-------------------------------")


Livro = collections.namedtuple("Livro", "Titulo Subtitulo Id Isbn Cdd Codigo_Autor Ediçao Autor Serie Volume Local_Publicaçao")

livros = []
livros_ordenados = []

indice = 0

while 1:
    print("=============Cadastro de Livros=============")
    print("1. Novo Cadastro")
    print("2. Exibir Cadastros") 
    print("3. Excluir Cadastro ")
    print("4. Ordenar Cadastros")
    print("5. Salvar")
    print("6. Sair")


    menu = int(input("Opção: "))

    #Entrada de dados
    if (menu == 1): 
        os.system ("cls")        

        titulo = input("Nome do livro: ")
        subtitulo = input("Subtítulo: ")
        isbn = int(input("ISNB 13: "))
        cdd = int(input("CDD (Classificação Decimal de Dewey): "))
        codigo_autor = int(input("Código do autor: "))
        ediçao = int(input("Edição: "))
        autor = input("Autor: ")
        serie = input("Série: ")
        volume = int(input("Volume: "))
        local_publicaçao = input("Local da publicação: ")        
        
        livros.append(Livro(titulo, subtitulo, indice, isbn, cdd, codigo_autor, ediçao, autor, serie, volume, local_publicaçao))
        livros_ordenados.append(Livro(titulo, subtitulo, indice, isbn, cdd, codigo_autor, ediçao, autor, serie, volume, local_publicaçao))

        indice += 1
       
    #Saída de dados
    os.system ("cls")

    if (menu == 2):
        
        for livro in livros:
            
            imprimir_cadastros(livro)

    elif (menu == 3):
        for livro in livros:
            print("Nome do livro.: %s" %livro.Titulo)
            print("Id.: %d" %livro.Id)
            print("-------------------------------")

        excluir = int(input("Insira o Id do livro que deseja excluir: ")) 
        
        for livro in livros:
            if livro.Id == excluir:
                livros.remove(livro)
       
        for livro in livros_ordenados:
            if livro.Id == excluir:
                livros_ordenados.remove(livro)

    elif (menu == 4):
        livros_ordenados.sort()

        for livro in livros_ordenados:
           imprimir_cadastros(livro)

    elif (menu == 5):
        salve = []

        #Adiciona o dicionario em uma lista
        for livro in livros:
            salve.append({"Titulo" : livro.Titulo, 
            "Subtitulo" : livro.Subtitulo,
            "ID" : livro.Id,
            "Isbn" : livro.Isbn,
            "Cdd" : livro.Cdd,
            "Codigo do Autor" : livro.Codigo_Autor,
            "Edicao" : livro.Ediçao,
            "Autor" : livro.Autor,
            "Serie" : livro.Serie,
            "Volume" : livro.Volume,
            "Local da Publicacao" : livro.Local_Publicaçao})

        #Escreve arquivo Json
        f = open("Livros.json", "w")
        json.dump(salve,f, sort_keys=False, indent=4)
        f.close()

        print("Cadastro salvo com sucesso!\n")
            
    elif (menu == 6):
        print('Saindo . . .')

        break

    

