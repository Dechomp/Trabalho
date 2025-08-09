from MediaSala import mediaSala
def main():
    nomeEscola = input ("Digite o nome da escola: ")
    print("")
    quantSalas  = int ( input ("Digite a quantidade de salas: "))

    while quantSalas <= 0: 
        print("Número inválido, digite novamente \n")

        quantSalas  = int ( input ("Digite a quantidade de salas: "))

    mediasSalas = [0.0] * quantSalas
    nomesSalas = [""] * quantSalas


    nomeSalaMaior = ""
    notaSalaMaior = 0

    i = 0
    while i < quantSalas:
        print("")
        nomeSala = input ("Digite o nome da sala: ")
        nomesSalas[i] = nomeSala
        
        quantAlunos = int (input ("Digite a quantidade de alunos: "))


        while quantAlunos <= 0:
            print("Valor inválido, digite novamente\n")
            
            quantAlunos = int (input ("Digite a quantidade de alunos: "))

        mediasSalas[i] = mediaSala(quantAlunos)
        
        if mediasSalas[i] > notaSalaMaior:
            notaSalaMaior = mediasSalas[i]
            nomeSalaMaior = nomeSala


        i +=  1
        print("\n")


    i = 0
    print("Chamada da escola: ", nomeEscola)
    while i < quantSalas:
        print("A sala ", nomesSalas[i], " tirou ", f"{mediasSalas[i]:,.3}" )
        i += 1
    
    print("")
    print("A sala ", nomeSalaMaior, " tirou a maior nota que foi de ", f"{notaSalaMaior:,.3}")

    return 0
main()