km_inicial = int( input("Digite o km inicial: "))
km_final = int(input("Digite o km final: "))
litros_gasto = int(input("Quantos litors foram gastos: "))
valor_recebido = float(input("Digite o valor total recebido: "))

km_rodados = km_final - km_inicial
media_consumo = km_rodados / litros_gasto

gasto_combustivel = media_consumo * 1.9

resultado = valor_recebido - gasto_combustivel

print(f"Média do consumo em Km/L: {media_consumo}")
print(f"Resultado financeiro é: R${resultado}")