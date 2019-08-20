registro = []
caminhoes = []
registro_cli = []
clientes=[]
registro_fre = []
fretes = []
registro_ma = []
manutencoes = []

while True:
    print("--------------- Menu Principal ------------------")
    menu = int(input("O que deseja fazer? \n1 - Caminhão \n2 - Cliente \n3 - Fretes \n4 - Manutenção \n5 - Financeiro \n0 - Sair \n"))
    if menu == 0:
        break
    if menu > 5:
        print("\n Comando inválido! \n")
        menu

         ## Caminhões


    def menu1():

                            ## Menu secundário
        while True:
            caminhao = []
            print("\n----------- Menu Caminhão ------------")
            menu_s = int(input("1- Cadastrar caminhão \n2- Editar caminhão \n3- Remover caminhão \n4- Exibir caminhões cadastrados \n0- Voltar "))
            if menu_s == 0:
                print("")
                break


            if menu_s == 1:  ## Cadastrando Caminhão

                x = 1
                import random
                for x in range(x):
                    cod = (random.randint(10, 300))
                    print("\nO código do caminhão será: %d" % cod)
                    at = x + 1

                    caminhao.append(cod)
                    capa = int(input("Qual a capacidade do caminhão (Em kg): " ))
                    caminhao.append(capa)
                    manu = input("Qual a data da ultima manutenção do caminhão (DD/MM/AA): " )
                    caminhao.append(manu)
                    frete = int(input("Qual o valor do frete do caminhão? " ))
                    caminhao.append(frete)
                    caminhoes.append(caminhao)

                    print("\n--------- Caminhão %i----------" %cod)
                    regis = ("Código do caminhão: %i \nCapacidade: %i \nData de ultima manutenção: %s \nFrete a ser cobrado: %i" % (cod, capa, manu, frete))
                    registro.append(regis)
                    print(regis)


            elif menu_s == 2:  ## Editando Caminhão
                print("\n----------- Caminhões --------------")
                for p, e in enumerate(registro):
                    print("%d - %s\n" % (p+1, e))
                edit = int(input("Qual código do caminhão que deseja editar? "))

                for p, e in enumerate(caminhoes):

                    if e[0] == edit:
                        print("Caminhão encontrado! \n")
                        print(registro[p])

                        capa = int(input("\nQual a capacidade da nova carga? "))
                        manun = input("Qual a nova data de manutenção? ")
                        frete = int(input("Qual o novo valor do frete? "))
                        caminhoes[p][1] = capa
                        caminhoes[p][2] = manun
                        caminhoes[p][3] = frete

                        registro[p] = ("Codigo do caminhão: %i \nCapacidade: %i \nData de ultima manutenção: %s \nFrete a ser cobrado: %i" % (cod, capa, manun, frete))
                        registro.append(registro[p])
                        break

                else:
                    print("Código não encontrado!")
                print(caminhoes)


            elif menu_s == 3:  ## Removendo Caminhão
                print("--------- Caminhões -------------")
                for p, e in enumerate(registro):
                    print("%d - %s\n" % (p+1, e))
                remover = int(input("\nQual código do caminhão que deseja remover? "))
                for p, e in enumerate(caminhoes):
                    if e[0] == remover:
                        del caminhoes[p]
                        del registro[p]
                        break

                else:
                    print("\nCódigo não encontrado!")
                print(caminhoes)


            elif menu_s == 4: ## Exibindo caminhões cadastrados
                print("\n----------- Caminhões -------------")
                for p, e in enumerate(caminhoes):
                    print("%d - %s\n" % (p+1, e))


    if menu == 1:
        menu1()


         ## Clientes

    def menu2 ():
                     ## Menu clientes
        while True:
            print("\n----------- Menu Cliente ------------")
            menu_c = int(input("1- Cadastrar cliente \n2- Editar cliente \n3- Remover cliente \n4- Exibir clientes cadastrados \n0- Voltar "))
            if menu_c ==0:
                print("")
                break

            if menu_c == 1:  ## Cadastrando clientes
                cliente = []
                cod_cli = int(input("\nQual o CPF do cliente?(Somente números!) "))
                cliente.append(cod_cli)
                nome = input("Qual o nome do cliente? ")
                cliente.append(nome)
                end = input("Qual o endereço do cliente? ")
                cliente.append(end)
                clientes.append(cliente)

                print("\n------------ Cliente %i-------------" % cod_cli)
                regis_cli = ("CPF do cliente: %i \nNome do cliente: %s \nEndereço do cliente: %s"%(cod_cli,nome,end))
                registro_cli.append(regis_cli)
                print(regis_cli)


            elif menu_c == 2:    ## Editando Cliente
                print("\n------------ Clientes ------------")
                for p, e in enumerate(registro_cli):
                    print("%d - %s\n" % (p+1, e))
                edit = int(input("Qual cpf do cliente que deseja editar? "))

                for p, e in enumerate(clientes):
                    if e[0] == edit:
                        print("Cliente encontrado! \n")
                        print(registro_cli[p])

                        cod_cli = int(input("\nQual o novo cpf? "))
                        nome = input("Qual o nome do novo cliente? ")
                        end = input("Qual o novo endereço? ")
                        clientes[p][0] = cod_cli
                        clientes[p][1] = nome
                        clientes[p][2] = end
                        registro_cli[p] = ("\nCPF do cliente: %i \nNome do cliente: %s \nEndereço do cliente: %s" % (cod_cli, nome, end))

                        print(registro_cli[p])
                        print(clientes)
                        break
                else:
                    print("CPF não encontrado!")



            elif menu_c == 3:        ## Removendo Cliente
                print("\n--------- Clientes ----------")
                for p, e in enumerate(registro_cli):
                    print("%d - %s\n" % (p+1, e))
                remover = int(input("Qual cpf do cliente que deseja remover? "))
                for p, e in enumerate(clientes):
                    if e[0] == remover:
                        del clientes[p]
                        del registro_cli[p]
                        break

                else:
                    print("\nCodigo não encontrado!")
                print(clientes)


            elif menu_c == 4:   ## Exibindo clientes cadastrados
                print("\n--------- Clientes ------------")
                for p, e in enumerate(registro_cli):
                    print("%d - %s" % (p+1, e))

    if menu == 2:
        menu2()

        ## Fretes


    def menu3 ():
        frete = []
                      ## Menu fretes
        while True:

            print("\n----------- Menu Fretes ------------")
            menu_f = int(input("1- Frete \n2- Total de fretes \n0- Voltar "))
            if menu_f == 0:
                print("")
                break
                            ## Fretes
            if menu_f == 1:
                for p, e in enumerate(registro):
                    print("\n%d - %s\n" % (p + 1, e))

                orig = input("Qual a origem? ")
                frete.append(orig)
                desti = input("Qual o destino? ")
                frete.append(desti)
                dist = int(input("Qual a distância em km? "))
                frete.append(dist)
                peso = int(input("Qual o peso? "))
                frete.append(peso)
                fretes.append(frete)

                for p, e in enumerate(caminhoes):
                    if peso <= e[1]:
                        c_usa = (caminhoes[p][0])
                        v_fre = (caminhoes[p][3])
                        frete.append(v_fre)
                        regis_fre = ("\nA carga vai de %s para %s \nO valor do frete é de: %i \nO caminhão melhor para levar a carga será o: %i" % (orig, desti, v_fre, c_usa,))
                        registro_fre.append(regis_fre)
                        print(regis_fre)
                        break
                else:
                    print("Não há caminhão cadastrado com essa capacidade")



            if menu_f == 2:  ## Total de fretes
                print("\n------------ Fretes -------------")
                for p, e in enumerate(registro_fre):
                    print("%d - %s\n" % (p+1, e))

    if menu == 3:
        menu3()


            ## Manutenções



    def menu4():

        print("\n----------- Manutenção --------------")
        for p, e in enumerate(caminhoes):
            print("%d - %s" % (p+1, e))

        manun = int(input("\nQual o código do caminhão que vai pra manutenção? "))

        for p, e in enumerate(caminhoes):
            if e[0] == manun:
                manuten = []
                new_manun = input("Qual a nova data de manutenção?(DD/MM/AA) ")
                manuten.append(new_manun)
                caminhoes[p][2] = new_manun
                manute = int(input("Qual o valor da manutenção? "))
                manuten.append(manute)
                manutencoes.append(manuten)

                print("\nManutenção feita no caminhão %d \nValor: %d \nData: %s " % (caminhoes[p][0], manute, new_manun))
                print("\nLista",caminhoes,"\n")

            else:
                print("")

    if menu == 4:
        menu4()


                ## Financeiro


    def menu5():
        soma_m = 0
        soma_f = 0
        print("\n----------- Financeiro --------------")
        if (len(fretes) != 0) and (len(manutencoes) != 0):

            for p, e in enumerate(fretes):
                fts = e[4]
                soma_f += fts
            for p, e in enumerate(manutencoes):
                man = e[1]
                soma_m += man

            print("O valor total de fretes é R$%1.2f \nO valor gasto em manutenções R$%1.2f" % (soma_f, soma_m))

            if soma_f > soma_m:
                lucro = soma_f - soma_m
                print("A empresa está com as finanças positivas, com o lucro de R$%1.2f" % lucro)

            elif soma_f < soma_m:
                preju = soma_m - soma_f
                print("A empresa está com as finanças negativas, com o prejuizo de R$%1.2f" % preju)

            print("")


    if menu == 5:
        menu5()
