def conta(x, y, signal):
    if signal == '+':
        return x + y
    if signal == '-':
        return x - y
    if signal == '*':
        return x * y
    if signal == '/':
        if y == 0:
            return 'Erro: divisão por zero'
        return x / y
    if signal == '^':
        return x ** y

while True:
    try:
          x = float(input('Digite o primeiro valor: '))
          signal = input('Qual o sinal? [+] SOMA [-] SUBTRAÇÃO [*] MULTIPLICAÇÃO [/] DIVISÃO [^] POTENCIAÇÃO')
          y = float(input('Digite o segundo valor: '))
          
    except:
        print('Você deve digitar apenas números')
        continue

    sinais_permitidos = '+-/*^'

    if signal not in sinais_permitidos:
            print ('Sinal inválido')
            continue            

    conta_final = conta(x, y, signal)
    print(f'O resultado de {x} {signal} {y} = {conta_final}')
