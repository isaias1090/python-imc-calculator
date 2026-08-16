print("Calculadora de Índice de massa corporal (IMC)\n")
altura=float(input("Dígite sua altura: "))
peso=float(input("Dígite seu peso: "))
if altura>3:
    altura=altura/100
imc= peso/(altura*altura)
if imc<18.5:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como abaixo peso")
elif imc>=18.5 and imc<=24.9:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como peso normal")
elif imc>=25 and imc<=29.9:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como sobrepeso")
elif imc>=30 and imc<=34.9:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como obesidade grau I")
elif imc>=35 and imc<=39.9:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como peso obesidade grau II")
elif imc>=40:
    print(f"Seu imc é {imc:.2f}kg/m² e está classificado como obesidade grau III")
