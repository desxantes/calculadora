import tkinter as tk

def text_user(number="", lista=""):
    if number == '':
        texto = "".join(lista)
        return texto.replace(".", ",")
    elif lista == "":
        texto = "".join(number)
        return texto.replace(".", ",")
    texto = "".join(lista) + "".join(number)
    return texto.replace(".", ",")

def converte_float_visual(numero):
    return str(numero).replace(".", ",")


def converte_decimal(numero):
    numero_convert = str(numero).replace(",", ".")
    numero_float = round(float(numero_convert), 7)
    if numero_float.is_integer():
        return int(numero_float)
    else:
        return converte_float_visual(numero_float)


def limite_caracter(label, lista):
        if len(lista) > 15:
            label.config(text="Limite de caracteres atingido")
            return True

def clear(label, number, resul, lista):
    number.clear()
    resul.clear()
    lista.clear()
    label.config(text='')




def add_last_number(lista, number):
    
    
    ultimo_numero = ""
    for numero in number:
        ultimo_numero += numero
    lista.append(ultimo_numero)

def result(label, lista, number):
    add_last_number(lista, number)
    if limite_caracter(label, lista):
        return

    value = resolve_operations(lista)
    
    lista.clear()
    number.clear()

    mensagem_erro = "Não é possivel dividir por 0"
    if mensagem_erro == value:
        label.config(text=mensagem_erro)
        return
    
    value = str(converte_decimal(value))

    number.append(value)
    numero_convertido = str(converte_decimal(value))
    label.config(text=numero_convertido)



def resolve_operations_basics(sub_list):
    result = float(sub_list[0])
    for i in range(1, len(sub_list), 2):
        operador = sub_list[i]
        next_number = float(sub_list[i+1])
        match operador:
            case "+":
                result += next_number
            case "-":
                result -= next_number

    return result


def resolve_operations(sub_list):
    while ("÷" in sub_list) or ("x" in sub_list):
        for operador in sub_list:
            if operador == "x" and "x" in sub_list:
                i = sub_list.index("x")
                indice_anterior = i-1
                indice_sucessor = i+1
                operacao = float(sub_list[indice_anterior]) * float(sub_list[indice_sucessor])
                sub_list[indice_anterior] = operacao
                del sub_list[indice_sucessor]
                del sub_list[i]

            if (operador == "÷") and ("÷" in sub_list):
                i = sub_list.index("÷")
                indice_anterior = i-1
                indice_sucessor = i+1

                if sub_list[indice_sucessor] == "0":
                    return f"Não é possivel dividir por 0"
                
                operacao = float(sub_list[indice_anterior]) / float(sub_list[indice_sucessor])

                if len(sub_list) == 3:
                    return operacao

                sub_list[indice_anterior] = operacao
                del sub_list[indice_sucessor]
                del sub_list[i]

    return str(resolve_operations_basics(sub_list))



def comma(label, number, resul, lista):
    if limite_caracter(label, number):
        return
    
    
    if len(number) == 0:
        number.append("0")
    else:
        if "." in number:
            label.config(text=text_user(number, lista)) 
            return
    number.append(".")
    label.config(text=text_user(number, lista))



def verificar_operacao(lista, op):
    if len(lista) > 0:
        if lista[-1] == "+" or "-" or "x" or "÷":
            del lista[-1]
            lista.append(op)
    
def addSub(label, number, lista):
    if limite_caracter(label, lista):
        return
    
    if len(number) > 0 and number[-1] != "-":
        number_checked = "".join(number)
        lista.append(number_checked)
        lista.append("-")
        number.clear()
        label.config(text=("".join(lista)).replace(".", ","))
        
    else:
        if len(number) == 0 and len(lista) == 0:
            number.append("-")
            label.config(text=text_user(number, lista))
        else:
            verificar_operacao(lista, "-")
            label.config(text=text_user(lista))
            
            

def addSum(label, number, lista):
    if limite_caracter(label, lista):
        return

    if len(number) > 0:
        number_checked = "".join(number)
        lista.append(number_checked)
        lista.append("+")
        number.clear()
        label.config(text=("".join(lista)).replace(".", ","))
        return
    else:
        verificar_operacao(lista, "+")
        label.config(text=text_user(lista))

def addMul(label, number, lista):
    if limite_caracter(label, lista):
        return


    if len(number) > 0:
        number_checked = "".join(number)
        lista.append(number_checked)
        lista.append("x")
        number.clear()
        label.config(text=("".join(lista)).replace(".", ","))
        return
    else:
        verificar_operacao(lista, "x")
        label.config(text=text_user(lista))

def addDiv(label, number, lista):
    if limite_caracter(label, lista):
        return

    if len(number) > 0:
        number_checked = "".join(number)
        lista.append(number_checked)
        lista.append("÷")
        number.clear()
        label.config(text=("".join(lista)).replace(".", ","))
        return
    else:
        verificar_operacao(lista, "÷")
        label.config(text=text_user(lista))


def add0(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("0")
    label.config(text=text_user(number, lista))

def add1(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("1")
    label.config(text=text_user(number, lista))

def add2(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("2")
    label.config(text=text_user(number, lista))

def add3(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("3")
    label.config(text=text_user(number, lista))

def add4(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("4")
    label.config(text=text_user(number, lista))

def add5(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("5")
    label.config(text=text_user(number, lista))

def add6(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("6")
    label.config(text=text_user(number, lista))

def add7(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("7")
    label.config(text=text_user(number, lista))

def add8(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("8")
    label.config(text=text_user(number, lista))

def add9(label, number, resul, lista):
    if limite_caracter(label, number):
        return 
    number.append("9")
    label.config(text=text_user(number, lista))



def main():
    number = []  
    lista = []
    resul = []

    
    window = tk.Tk()
    window.title("Calculadora Simples")

    label = tk.Label(window, pady=50, font="Arial, 16", justify="right")
    label.grid(row=0, column=0, columnspan=10, pady=5, padx=0)
    
    buttonC = tk.Button(window, text="C", padx=30, pady=20, command=lambda: clear(label, number, resul, lista), foreground="green", borderwidth=4)
    buttonC.grid(row=1, column=0, padx=5, pady=5)

    buttonDiv = tk.Button(window, text="÷", padx=30, pady=20, command=lambda: addDiv(label, number, lista), foreground="green", borderwidth=4)
    buttonDiv.grid(row=1, column=4, padx=5, pady=5)

    button7 = tk.Button(window, text="7", padx=30, pady=20, command=lambda: add7(label, number, resul, lista), borderwidth=4)
    button7.grid(row=2, column=0, pady=5, padx=5)

    button8 = tk.Button(window, text="8", padx=30, pady=20, command=lambda: add8(label, number, resul, lista), borderwidth=4)
    button8.grid(row=2, column=1, pady=5, padx=5)

    button9 = tk.Button(window, text="9", padx=30, pady=20, command=lambda: add9(label, number, resul, lista), borderwidth=4)
    button9.grid(row=2, column=2, pady=5, padx=5)

    buttonMul = tk.Button(window, text="X", padx=30, pady=20, command=lambda: addMul(label, number, lista), foreground="green", borderwidth=4)
    buttonMul.grid(row=2, column=4, padx=5,pady=5)

    button4 = tk.Button(window, text="4", padx=30, pady=20, command=lambda: add4(label, number, resul, lista), borderwidth=4)
    button4.grid(row=3, column=0, pady=5, padx=5)

    button5 = tk.Button(window, text="5", padx=30, pady=20, command=lambda: add5(label, number, resul, lista), borderwidth=4)
    button5.grid(row=3, column=1, pady=5, padx=5)

    button6 = tk.Button(window, text="6", padx=30, pady=20, command=lambda: add6(label, number, resul, lista), borderwidth=4)
    button6.grid(row=3, column=2, pady=5, padx=5)

    buttonSub = tk.Button(window, text="-", padx=30, pady=20, command=lambda: addSub(label, number, lista), foreground="green", borderwidth=4)
    buttonSub.grid(row=3, column=4, padx=5,pady=5)

    button1 = tk.Button(window, text="1", padx=30, pady=20, command=lambda: add1(label, number, resul, lista), borderwidth=4)
    button1.grid(row=4, column=0, pady=5, padx=5)

    button2 = tk.Button(window, text="2", padx=30, pady=20, command=lambda: add2(label, number, resul, lista), borderwidth=4)
    button2.grid(row=4, column=1, pady=5, padx=5)

    button3 = tk.Button(window, text="3", padx=30, pady=20, command=lambda: add3(label, number, resul, lista), borderwidth=4)
    button3.grid(row=4, column=2, pady=5, padx=5)

    buttonSum = tk.Button(window, text="+", padx=30, pady=20, command=lambda: addSum(label, number, lista), foreground="green", borderwidth=4)
    buttonSum.grid(row=4, column=4, padx=5,pady=5)

    button0 = tk.Button(window, text="0", padx=30, pady=20, command=lambda: add0(label, number, resul, lista), borderwidth=4)
    button0.grid(row=5, column=1, pady=5, padx=5)

    buttonComma = tk.Button(window, text=",", padx=30, pady=20, command=lambda: comma(label, number, resul, lista), foreground="green", borderwidth=4)
    buttonComma.grid(row=5, column=2, pady=5, padx=5)

    buttonResul = tk.Button(window, text="=", padx=30, pady=20, command=lambda: result(label, lista, number), foreground="green", borderwidth=4)
    buttonResul.grid(row=5, column=4, padx=5,pady=5)
        
    window.geometry("360x530")
    window.resizable(False, False)

    window.mainloop()

if __name__=="__main__":
    main()