from MediaAluno import mediaAluno
def mediaSala(quantidade):
    print("")
    media = 0

    mediasAlunos = [0.0] * quantidade
    nomesAlunos = [""] * quantidade
    statusAlunos = [""] * quantidade
    i = 0
    nomeAlunoMaior = ""
    notaAlunoMaior = 0

    while i < quantidade:
        print("")
        nomeAluno = input("Digite o nome do aluno: ")
        nomesAlunos[i] = nomeAluno
        mediasAlunos[i] = mediaAluno()
        
        print ("O aluno", nomeAluno, f" tirou {mediasAlunos[i]:,.3}")

        if mediasAlunos[i] >= 6:
            print("Aprovado")
            statusAlunos[i] = "aprovado"
        elif mediasAlunos[i] > 4:
            print("Recuperação")
            statusAlunos[i] = "em recuperação"
        else:
            print("Reprovado")
            statusAlunos[i] = "reprovado"
        
        if mediasAlunos[i] > notaAlunoMaior:
            notaAlunoMaior = mediasAlunos[i]
            nomeAlunoMaior = nomeAluno
        
        media += mediasAlunos[i]
        
        i += 1
        print("")

    media /= quantidade


    i = 0

    while i < quantidade:
        print("O aluno ", nomesAlunos[i], f"tirou {mediasAlunos[i]:,.3}", "ele está ", statusAlunos[i])
        i += 1
    print("")
    print("O aluno ", nomeAlunoMaior, " tirou a maior nota que foi de ", f"{notaAlunoMaior:,.3}")


    return media
