#/ Follow twitter @Ag0rism

def welcome():
    print('''

                                              _       _  ___          _    
                                  __ _  ___ _| |_ __ | |/ _ \ _ __   / \        discord.gg/qzsu787Be3
                                 |__` |/ _ \__ | '_ \| | | | | '_ \ / _ \       twitter.com/Ag0rism
                                    | | (_) || | |_) | | |_| | |_) / ___ \      youtube.com/Agorism
                                    |_|\___/__/|_.__/|_|\___/| .__/_/   \_\     github.com/Agorism
                                                              \___|        
''') 

def calculate():
    operation = input('''
Digite a operação matemática que deseja realizar:
+ Adição
- Subtração
* Multiplicação
/ Divisão

Ctrl + C se deseja fechar a calculadora.
''')

    number_1 = int(input('Digite o primeiro número: '))
    number_2 = int(input('Digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')

    again()

def again():
    calc_again = input('''
Você quer calcular novamente?
Digite Y para SIM ou N para NÃO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('Até logo.')
    else:
        again()

welcome()
calculate()
