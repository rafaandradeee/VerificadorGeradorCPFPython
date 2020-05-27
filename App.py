# Created by Rafaandradeee

import random

flag = 1

# Criação do menu -------------------------
while flag != 0:
    try:
        flag = int(input("\n|---------------------------------|"
                         "\n\nEscolha uma opção para prosseguir: \n"
                         "1. Validar CPF\n"
                         "2. Gerar CPF Aleatório\n\n"
                         "0. Sair\n\n"
                         "Digite: "))
    except:
        print("\nOpção inválida, tente novamente!")

    if flag == 1:      # Validação de CPF --------------------------
        try:
            testCPF = input("\nDigite o número do CPF a ser verificado, sem pontos ou traços: ")
            isReal1 = False
            isReal2 = False
            sum1 = 0
            sum2 = 0
            verified = False
            location = 11

            if len(testCPF) < 11 or len(testCPF) > 11:
                print("\nCPF digitado de forma inválida. Por favor digite os 11 números sem pontos ou traços.")
            else:
                # Verificação do primeiro dígito ------------------------
                auxList = [0] * 11
                for i in range(9):
                    auxList[i] = int(testCPF[i]) * range(10, 0, -1)[i]
                sum1 = sum(auxList)
                firstDigitModule = sum1 % 11
                if firstDigitModule < 2:
                    firstDigit = 0
                else:
                    firstDigit = 11 - firstDigitModule

                if firstDigit == int(testCPF[9]):
                        isReal1 = True
                        # Verificação do segundo dígito --------------------
                        auxList = [0] * 11
                        for i in range(10):
                            auxList[i] = int(testCPF[i]) * range(11, 0, -1)[i]
                        sum2 = sum(auxList)
                        secondDigitModule = sum2 % 11
                        if secondDigitModule < 2:
                            secondDigit = 0
                        else:
                            secondDigit = 11 - secondDigitModule

                        if secondDigit == int(testCPF[10]):
                            isReal2 = True
                            verified = True
                            location = int(testCPF[8])
                        else:
                            print("\nO CPF informado é inválido.")
            # Resultado de verificação
            if isReal1 == True and isReal2 == True and verified == True:
                print("\nO CPF digitado é válido.")
                if location == 0:
                    print("UF de emissão: Rio Grande do Sul")
                elif location == 1:
                    print("UF de emissão: Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
                elif location == 2:
                    print("UF de emissão: Acre, Amapá, Amazonas, Pará, Rondônia ou Roraima")
                elif location == 3:
                    print("UF de emissão: Ceará, Maranhão ou Piauí")
                elif location == 4:
                    print("UF de emissão: Alagoas, Paraíba, Pernambuco ou Rio Grande do Norte")
                elif location == 5:
                    print("UF de emissão: Bahia ou Sergipe")
                elif location == 6:
                    print("UF de emissão: Minas Gerais")
                elif location == 7:
                    print("UF de emissão: Espirito Santo ou Rio de Janeiro")
                elif location == 8:
                    print("UF de emissão: São Paulo")
                elif location == 9:
                    print("UF de emissão: Paraná ou Santa Catarina")

        except:
            print("\nCPF digitado de forma inválida. Por favor digite os 11 números sem pontos ou traços.")
    elif flag == 2:    # Geração de CPF ----------------------------
        auxList = [0] * 11
        generateCPF = str(random.randint(100010001, 489898989))
        for i in range(9):
            auxList[i] = int(generateCPF[i]) * range(10, 0, -1)[i]
        sum1 = sum(auxList)
        firstDigitModule = sum1 % 11
        if firstDigitModule < 2:
            firstDigit = 0
        else:
            firstDigit = 11 - firstDigitModule

        generateCPF += str(firstDigit)

        # Criação do segundo dígito --------------------
        auxList = [0] * 11
        for i in range(10):
            auxList[i] = int(generateCPF[i]) * range(11, 0, -1)[i]
        sum2 = sum(auxList)
        secondDigitModule = sum2 % 11
        if secondDigitModule < 2:
            secondDigit = 0
        else:
            secondDigit = 11 - secondDigitModule

        generateCPF += str(secondDigit)
        print(generateCPF[0:3] + "." + generateCPF[3:6] + "." + generateCPF[6:9] + "-" + generateCPF[9:11])

        location = int(generateCPF[8])
        if location == 0:
            print("UF de emissão: Rio Grande do Sul")
        elif location == 1:
            print("UF de emissão: Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
        elif location == 2:
            print("UF de emissão: Acre, Amapá, Amazonas, Pará, Rondônia ou Roraima")
        elif location == 3:
            print("UF de emissão: Alagoas, Paraíba, Pernambuco ou Rio Grande do Norte")
        elif location == 4:
            print("UF de emissão: Ceará, Maranhão ou Piauí")
        elif location == 5:
            print("UF de emissão: Bahia ou Sergipe")
        elif location == 6:
            print("UF de emissão: Minas Gerais")
        elif location == 7:
            print("UF de emissão: Espirito Santo ou Rio de Janeiro")
        elif location == 8:
            print("UF de emissão: São Paulo")
        elif location == 9:
            print("UF de emissão: Paraná ou Santa Catarina")
    elif flag == 0:    # Sair --------------------------------------
        print("\n\nEncerrando aplicação...\n"
              "Aplicação encerrada com sucesso.\n")
        break
    else:
        print("\nOpção inválida, tente novamente!")
