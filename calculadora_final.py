while True:
    numero1 = input('Digite um numero ')
    operador = input('Digite um operador /*-+')
    numero2 = input('Digite outro numero ')


    numeros_validos = None

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True

    except:
        print('erro')
        print('Um ou mais operadores estão invalidos')
        numeros_validos = None

    operadores_permitidos = '/*-+'

    if operador not in operadores_permitidos:
        print('Op. invalido')
        continue

    if len(operador) > 1:
        print('Operadores em excesso')
        continue
    
    if operador == '+':
        print (f'{numero1_float} + {numero2_float} =', numero1_float + numero2_float)

    if operador == '*':
       print (f'{numero1_float} x {numero2_float} =', numero1_float * numero2_float)
 
    if operador == '/':
        print (f'{numero1_float} / {numero2_float} =', numero1_float / numero2_float)

    if operador == '-':
       print (f'{numero1_float} - {numero2_float} =', numero1_float - numero2_float)
 

    sair = input('Deseja sair? [s]/[n]')
    sair = sair.lower().startswith('s')
    if sair is True:
        break




