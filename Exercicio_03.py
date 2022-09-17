dias_do_mes = [ 31, 28, 31, 30, 31, 30, 31 , 31 , 30, 31, 30, 31, 30, 31]

qual_mes = int(input("Informe o número do mës: "))
ano = int(input("Informe qual o ano: "))
print("O mês", qual_mes, "tem", dias_do_mes[qual_mes+1] , "dias", "no ano de", ano) 
