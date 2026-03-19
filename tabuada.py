while True:
    n = int(input("Qual número você quer a tabuada? "))
    c = input("Tem certeza amigo?")
    if c == "sim":
        print(f"Tabuada do {n}:")
        from time import sleep
        for i in range(1, 11):
            resultado = n * i
            print(f"{n} {chr(215)} {i} = {resultado}")
            sleep(0.5)
    elif c == "não":
        continue
    elif c == ".":
        i = 1
        while i <= 3:
            print("Tmj mestre")
            i += 1   
    else:
        print("Preparando para desligar computador...")
         
