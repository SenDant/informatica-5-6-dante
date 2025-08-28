#I wanna do it with pesos :P ‼️‼️‼️
def main():
    print("-------Máquina expendora de Coca Cola-------")
    name = input("Por favor inserte su nombre: ")
    print("--------------------------------------------")
    print("               |PAGUE AQUÍ|                 ")
    total = 0
    PRICE = 25
    while True:
        coin = int(input("Porfavor inserte una moneda a la vez: "))
        if coin == 1 or coin == 2 or coin == 5 or coin == 10:
            print(f"*Introdujo una moneda de {coin}*")
            total += coin
            print(f"Faltan: {PRICE - total} pesos.")
            if total == PRICE:
                print("----------------------------------------")
                print("Pago Completado.")
                print(f"Aquí está una Coca Cola para {name}.🥤")
                print("    		        _                                   ")
                print("          .!.!.                             ")
                print("           ! !                                   ")
                print("           ; :                                ")
                print("          ;   :                                ")
                print("         ;_____:                                 ")
                print(f"        !{name}!                                 ")
                print("         !_____!                                 ")
                print("         :     :")
                print("         :     ;                                       ")
                print("         .'   '.                             ")
                print("         :     :                          ")
                print("          '''''")
                break
            elif total > PRICE:
                total -= PRICE
                print("----------------------------------------")
                print(f"Su cambio: ${total}")
                print(f"Aquí está una Coca Cola para {name}.🥤")
                print("    		        _                                   ")
                print("          .!.!.                             ")
                print("           ! !                                   ")
                print("           ; :                                ")
                print("          ;   :                                ")
                print("         ;_____:                                 ")
                print(f"        !{name}!                                 ")
                print("         !_____!                                 ")
                print("         :     :")
                print("         :     ;                                       ")
                print("         .'   '.                             ")
                print("         :     :                          ")
                print("          '''''")
                break
        else:
            print("--------------------------------------------")
            print("Moneda Inválida. Iniciando autodestrucción. (⊙_⊙;)")
            print("💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥💥")
            break
main()