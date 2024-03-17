import os

def handleStartingApplication():
    try:     
        print('~ Bem Vindo ~ \n')

        quantityOfProductsInKg = input('Digite a quantidade em kilos de frutas compradas/kg: ')
        message = 'O valor que será pago: '

        if quantityOfProductsInKg.startswith('0'):
            refactoredNumber = quantityOfProductsInKg.replace(',', '.', 1)
            removeComma = refactoredNumber.replace(',', '')
            convertingStringToNumber = float(removeComma)
        else:
            refactoredNumber = quantityOfProductsInKg.replace(',', '')
            convertingStringToNumber = float(refactoredNumber)

        if convertingStringToNumber <= 3:
            result = convertingStringToNumber * 3

            print(f'\n{message} {result} \n')
        elif convertingStringToNumber <= 5:
            result = convertingStringToNumber * 2.75

            print(f'\n{message} {result} \n')
        elif convertingStringToNumber <= 10:
            result = convertingStringToNumber * 2.50
            print(f'\n{message} {result} \n')
        else:
            result = convertingStringToNumber * 2.25

            print(f'\n{message} {result} \n')
        
        
        closeProgram = input('Deseja sair? s/n ')

        if closeProgram == 's':
            return
        elif closeProgram == 'n':
            if os.name == 'posix':
                handleCleanTerminal('clear')
            elif os.name == 'nt':
                handleCleanTerminal('cls')
            handleStartingApplication()
        else: 
            print('Não consigo indentificar este comando, até mais \n')
    except ValueError:        
        if os.name == 'posix':
            handleCleanTerminal('clear')
        elif os.name == 'nt':
            handleCleanTerminal('cls')
        print('Algo deu errado tente novamente \n')
        handleStartingApplication()
        

def handleCleanTerminal(commandLine):
    os.system(commandLine)

handleStartingApplication()