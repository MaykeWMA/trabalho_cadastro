##variáveis
nome = "str"
sexo = "str"
optionSX = "str"
idade = "float"
EstadoCivil = "str"
optionEC = "str"
salario = "float"
alt="alt"
##váriavel Nome e Sexo
nome = str(input ("Qual o seu nome?: "))
if nome.endswith("a") or nome.endswith("i")  or nome.endswith("y") or nome.endswith("s") or nome.endswith("l") or nome.endswith("n") or nome.endswith("m") or nome.endswith("u"):
    print(("Bem vinda(o) ")+(nome)+("!"))
    print ("Seu sexo é Feminio?")
    optionSX = str(input("Digite 'Sim' para confirmar, caso contrário digite 'Não': "))
    if optionSX == "Sim" or optionSX== "SIM" or optionSX=="sim" or optionSX=="S" or optionSX=="s":
        sexo = "Feminino"
    elif optionSX == "Não" or optionSX=="NÃO" or optionSX=="não" or optionSX=="Nao" or optionSX=="NAO" or optionSX=="nao" or optionSX=="N" or optionSX=="Ñ" or optionSX=="ñ":
        optionSX = str(input("Digite 'M' para Masculino ou então 'I' para Indefinido: "))
        if optionSX == "M" or optionSX=="m":
            sexo = "Masculino"
        elif optionSX == "I" or optionSX=="i":
            sexo = "Indefinido"
    else:
        print("Por favor ativar a função 'sexo' no menu apos o preenchimento do cadastro para digitar corretamente!")
elif nome.endswith("o") or nome.endswith("e")  or nome.endswith("w") or nome.endswith("s") or nome.endswith("l") or nome.endswith("n") or nome.endswith("m") or nome.endswith("u"):
    print(("Bem vindo(a) ")+(nome)+("!"))
    print ("Seu sexo é Masculino?")
    optionSX = str(input("Digite 'Sim' para confirmar, caso contrário digite 'Não': "))
    if optionSX == "Sim" or optionSX== "SIM" or optionSX=="sim" or optionSX=="S" or optionSX=="s":
        sexo = "Masculino"
    elif optionSX == "Não" or optionSX=="NÃO" or optionSX=="não" or optionSX=="Nao" or optionSX=="NAO" or optionSX=="nao" or optionSX=="N" or optionSX=="Ñ" or optionSX=="ñ":
        optionSX = str(input("Digite 'F' para Feminino ou então 'I' para Indefinido: "))
        if optionSX == "F" or optionSX=="f":
            sexo = "Feminino"
        elif optionSX == "I" or optionSX=="i":
            sexo = "Indefinido"
    else:
        print("Por favor ativar a função 'sexo' no menu após o preenchimento do cadastro para digitar corretamente!")
print(("Sexo: ")+str(sexo))

##variável Idade
idade =  float(input ("Qual Sua Idade?: "))
if len (str(idade)) >=6:
    print("Idade inválida por favor digite Corretamente")
elif idade >=130:
    print("Idade inválida por favor digite novamente")
elif len (str(idade)) <=5:
    print(("Sua idade é: ")+str(idade)+(" Anos"))
elif  idade >=0:
    print("Sua idade é: " + str(idade)+(" Anos"))
else:
        print("Por favor ativar a função 'idade' no menu após o preenchimento do cadastro para digitar corretamente!")
    
##variável salário
salario = float(input("Qual seu salário em reais?: "))
print(("Seu salário é de R$:") + str(salario))
if salario<= 0:
    print ("Seu salário (R$:" + str(salario) + ") é inválido")
    print("Por favor ativar a função 'Salário' no menu após o preenchimento do cadastro para digitar corretamente!")
    
##Variável Estado Civil
print("Qual o seu estado civil?")
print("Se for Solteiro(a) digite apenas 'S'")
print("Se for Casado(a) digite apenas 'C'")
optionEC = str(input("E se for Viúvo(a) digite apenas 'F': "))
if optionEC =="F" or optionEC=="f":
    EstadoCivil = "Viúvo(a)"
    print(("EC: ")+str(EstadoCivil))
elif optionEC == "C" or optionEC=="c":
    EstadoCivil = "Casado(a)"
    print(("EC: ")+str(EstadoCivil))
elif optionEC=="S" or optionEC=="s":
    EstadoCivil = "Solteiro(a)"
    print(("EC: ")+str(EstadoCivil))
elif optionEC!="C" or optionEC!="c" and optionEC!="F" or optionEC!="f" and EstadoCivil !="S" or optionEC!="s":
    print("Caractere inválido!")
    print("Por favor ativar a função 'EC'(Estado Civil) no menu após o preenchimento do cadastro para digitar corretamente!")
    
##Função Nome
def Nome():
    global nome
    nome = str(input ("Qual o seu nome?: "))
    if len(nome) <=3:
        print ("Por favor digite corretamente!")
    elif len (nome) >3:
        print(("Seu nome ficou como: ")+str(nome))
        
##função Idade
def Idade1():
    global idade
    idade = float(input ("Qual sua idade?: "))
    if len (str(idade))>=6:
        print("Idade incorreta, Por favor corrigir idade ")
    elif idade>=130:
        print("Idade Incorreta, por favor digite corretamente!")
    elif len (str(idade)) <=5:
        print(("Sua idade é: ")+str(idade)+(" Anos"))
    elif  idade >=0:
        print("Sua idade é: " + str(idade)+(" Anos"))
    
    else:
        print ("por favor digite corretamente!")
        
##função Salário
def Salário():
    global salario
    salario = float(input ("Qual o seu salário?: "))
    if salario > 0:
        print ("Parabéns seu salário foi aprovado!")
    else:
        salario<= 0
        print ("Seu salário (R$:" + str(salario) + ") é inválido")
        
##Função Sexo
def Sexo():
    global optionSX
    global sexo
    print("Qual o seu SEXO?")
    print("Para FEMININO digite 'F'")
    print("Para MASCULINO digite 'M'")
    print("para INDEFINIDO digite 'I'")
    optionSX = str(input("E para Indefinido digite I: "))
    if optionSX =="F" or optionSX=="f":
        sexo = "Feminimo"
        print(("Sexo:")+str(sexo))
    elif optionSX == "M" or optionSX=="m":
        sexo = "Masculino"
        print(("Sexo:")+str(sexo))
    elif optionSX == "I" or optionSX =="i":
        sexo = "Indefinido"
        print(("Sexo:")+str(sexo))
    else:
        print("Caractere inválido!")
        
##Função Estado Civil
def EC():
    global optionEC
    global EstadoCivil
    print("Qual o seu estado civil?")
    print("Para Solteiro(a) digite apenas 'S'")
    print("Para Casado(a) digite apenas 'C'")
    optionEC = str(input ("E para Viúvo(a) digite apenas 'F': "))
    if optionEC =="F" or optionEC=="f":
        EstadoCivil = "Viúvo(a)"
        print(("EC: ")+str(EstadoCivil))
    elif optionEC == "C"or optionEC=="c":
        EstadoCivil = "Casado(a)"
        print(("EC: ")+str(EstadoCivil))
    elif optionEC == "S" or optionEC=="s":
        EstadoCivil = "Solteiro(a)"
        print(("EC: ")+str(EstadoCivil))
    elif optionEC!= "C" or optionEC!="c" and optionEC !="F" or optionEC!="f" and optionEC!="S" or optionEC!="s":
        print("Caractere inválido!")

#função alterar
def alterar():
    global sexo
    global nome
    global idade
    global salario
    print("Olá oque deseja alterar?")
    print("Para ALTERAR seu nome digite nome")
    print("Para ALTERAR seu sexo digite 'sexo'")
    print("para ALTERAR sua idade digite 'idade'")
    print("para ALTERAR seu estado civil digite 'ec'")
    print("Para ALTERAR seu salário digite 'salario'")
    print("para CONSULTAR alguma informação digite 'consulta'")
    alt = input("Para DELETAR alguma informação digite 'del'")
    if alt == "nome"or alt=="Nome"or alt=="NOME":
        Nome()
    elif alt == "idade"or alt=="Idade"or alt=="IDADE":
        Idade1()
    elif alt == "salario"or alt=="Salario"or alt=="SALARIO"or alt=="salário"or alt=="Salário"or alt=="SALÁRIO":
        Salário()
    elif alt == "sexo"or alt=="Sexo"or alt=="SEXO":
        Sexo()
    elif alt=="EC"or alt=="ec"or alt=="Ec":
        EC()
    elif alt=="consultar"or alt=="consulta"or alt=="Consultar"or alt=="Consulta"or alt=="CONSULTAR"or alt=="CONSULTA":
        consulta()
    elif alt=="del" or alt=="DEL" or alt=="Del":
        deletar()
    else:
        print("Opção inválida!, por favor digite corretamente")
    

#função deletar informação
def deletar():
    global sexo
    global nome
    global idade
    global salario
    print("Olá, o que deseja delete?")
    print("Para deletar sua IDADE digite 'idade'")
    print("para deletar seu NOME digite 'nome'")
    print("para alterar alguma informação digite 'alt'")
    delete = input("E para ver sua sexualidade digite 'sexo': ")
    if delete == "sexo"or delete=="Sexo"or delete=="SEXO":
        optionSX = "i"
        print(("Sexo:")+str(sexo))
    elif delete =="salario" or delete=="Salario" or delete=="Salário" or delete == "salário":
        salario ="Salário zerado!"
        print(salario)
    elif delete =="nome" or delete=="Nome"or delete=="NOME":
        nome = "registrar novamente"
        print(nome)
    elif delete =="idade" or delete=="Idade" or delete=="IDADE":
        idade = "registrar idade"
        print(idade)
    elif delete == "ALT" or delete=="Alt" or delete=="alt":
        alterar()
    else:
        print("Opção inválida!, por favor digite corretamente")

##Função Consultar
def consulta():
    global sexo
    global EstadoCivil
    global salario
    global nome
    global idade
    print("Olá, o que deseja consultar?")
    print("Para CONSULTAR sua IDADE digite 'idade'")
    print("Para consultar seu SALÁRIO digite 'salario'")
    print("Para saber seu ESTADO CIVIL digite 'ec'")
    print("para consultar seu NOME digite 'nome'")
    print("para alterar alguma informação digite 'alt'")
    consultar = input("E para ver sua sexualidade digite 'sexo': ")
    if consultar == "salario" or consultar=="Salario" or consultar=="SALARIO" or consultar=="salário" or consultar=="Salário" or consultar=="SALÁRIO":
        print(("Seu salário é de R$:")+str(salario))
    elif consultar =="EC"or consultar=="ec"or consultar=="Ec":
        print(("Seu EC é de: ")+str(EstadoCivil))
    elif consultar == "sexo"or consultar=="Sexo"or consultar=="SEXO":
        print(("Sexo: ")+str(sexo))
    elif consultar =="nome" or consultar=="Nome"or consultar=="NOME":
        print(("Segundo informado seu nome é: ")+str(nome))
    elif consultar =="idade" or consultar=="Idade" or consultar=="IDADE":
        print(("idade: ")+str(idade)+(" Anos"))
    elif delete == "ALT" or delete=="Alt" or delete=="alt":
        alterar()
    else:
        print("Opção inválida!,por favor digite corretamente")
        
##Menú de opções        
opcao="menu"
while opcao!="sair" or  opcao!="Sair" or opcao!="SAIR":
    print("Digite 'nome' para ALTERAR seu Nome")
    print("Para ALTERAR sua IDADE digite 'idade'")
    print("Para ALTERAR seu SALÁRIO digite salario")
    print("Para ALTERAR seu SEXO digite 'sexo'")
    print("Para ALTERAR seu ESTADO CIVIL digite 'EC'")
    print("Para DELETAR alguma informação digite 'del'")
    opcao = input("Ou para CONSULTAR digite 'consultar' ou então digite 'sair' para sair: ")
    if opcao == "nome"or opcao=="Nome"or opcao=="NOME":
        Nome()
    elif opcao == "idade"or opcao=="Idade"or opcao=="IDADE":
        Idade1()
    elif opcao == "salario"or opcao=="Salario"or opcao=="SALARIO"or opcao=="salário"or opcao=="Salário"or opcao=="SALÁRIO":
        Salário()
    elif opcao == "sexo"or opcao=="Sexo"or opcao=="SEXO":
        Sexo()
    elif opcao == "EC"or opcao=="ec"or opcao=="Ec":
        EC()
    elif opcao =="consultar"or opcao=="consulta"or opcao=="Consultar"or opcao=="Consulta"or opcao=="CONSULTAR"or opcao=="CONSULTA":
        consulta()
    else:
        opcao == "sair"or opcao=="Sair"or opcao=="SAIR"
        print("Obrigado, volte sempre")
        break
