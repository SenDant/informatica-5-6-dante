#i wanna do it with pesos :P
def main():
    print("----Máquina expendora de Coca Cola----")
    name = input("Por favor inserte su nombre: ")
    total = 0
    while True:
        coin = int(input("Porfavor inserte una moneda a la vez: "))
        if coin == 1 or 2 or 5 or 10:
            print(f"*Introdujo una moneda de {coin}*")
            total += coin
            if total == 25:
                print("Pago Completado.")
                print(f"Aquí está una Coca Cola para {name}.")
                break
            elif total > 25:
                total -= 25
                print(f"Su cambio: ${total}")
                print(f"Aquí está una Coca Cola para {name}.")
                break
        if coin != 1 or 2 or 5 or 10 or coin > 1 or coin < 1:
            print("Moneda Inválida. Iniciando autodestrucción.")
            break
main()