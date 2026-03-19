while True:
    salario = float(input("Qual seu salário? "))
    cargo = input("Qual seu cargo? ")

    if cargo == "junior":
     novo_salario = salario * 1.1  
    elif cargo == "pleno":
     novo_salario = salario * 1.2
    elif cargo == "senior":
      novo_salario = salario * 1.3
    else:
        print("erro na digitação do cargo")

    print(f"O meu salário é R$ {salario:.2f}, mas com meu cargo de: {cargo} Meu salário se torna: R$ {novo_salario:.2f}. ")

    sair = input("Você deseja continuar no programa?")
    if sair == "sim":
      continue
    elif sair == "não":
      break 
i = 1
while i <= 3:
    print("Beleza")
    i += 1
    
    