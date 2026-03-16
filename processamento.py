def media(lista):
    medias = []
    for aluno in lista:
        notas = aluno[1]
        media_aluno = sum(notas) / len(notas)
        medias.append(media_aluno)
    return medias
    

def validar_lista(lista):
    try:
        if not lista:               
            return "Vazia/None"
        if not isinstance(lista, list):
            return "Corrompida"
        return "Válida"
    except TypeError:
        return "Corrompida"
    
def add_lista(lista):
    while True:
        nome = input("Digite o nome do aluno: ")
        notas = []
        for i in range(4):
            notas.append(float(input(f"Digite a {i+1}ª nota do aluno: ")))
        t_add = (nome, notas)
        lista.append(t_add)
        continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break


def tratar_lista(nome, notas):
    lista = []
    notasf = []
    notasf.append(float(notas))
    tupla = (nome, notas)
    lista.append(tupla)
    return lista

def media_personal(media):

    a = ""
    maior = 0

    if media >= 7:
        a = "Recuperacao"
    for i in range(len(media)):
        if media[i] > maior:
            maior = media[i]
            a = "Top Student"

    print(f"Média: {media}, Situação: {a}")



def imprimir(lista, media):
    for a in lista:
        print(f"Aluno: {a[0]}, Notas: {a[1]}, Média: {media}")


