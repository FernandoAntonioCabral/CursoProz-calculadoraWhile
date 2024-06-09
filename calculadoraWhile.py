def calculadora(num1, num2, operador) :
  result = 0
  if(operador == 1) :
    result = num1 + num2
  elif(operador == 2) :
    result = num1 - num2  
  elif(operador == 3) :
    result = num1 * num2 
  elif(operador == 4) :
    result = num1 / num2   
  return result

codigo = int(input("Digite um número de acordo com a operação desejada: (1: Soma / 2: Subtração / 3: Multiplicação / 4: Divisão / 0. Sair)"))
while(codigo != 0) :
  if(codigo <= 4) :
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = calculadora(num1, num2, codigo)
    print("resultado: " + str(resultado))
    codigo = int(input("Digite um número de acordo com a operação desejada: (1: Soma / 2: Subtração / 3: Multiplicação / 4: Divisão / 0. Sair)"))
  else :
    print("Essa opção não existe")
    codigo = int(input("Digite um número de acordo com a operação desejada: (1: Soma / 2: Subtração / 3: Multiplicação / 4: Divisão / 0. Sair)"))
print("Operação encerrada")
