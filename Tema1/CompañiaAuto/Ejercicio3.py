# Tenemos coches con su precio y con la comision que vamos ha llevar al fin del mes por cada coche vendido
# RBM Serie 1:
# precio: 20.000 EU, comisión: 3%

# RMB Serie plus:
# precio: 35.000 EU, comisión: 5%

# RBM todoterreno:
# precio: 60.000 EU, comisión: 7%

RMB1 = 20000
RMBPlus =  35000
RBMTT = 60000

# TT= TodoTerreno

# El usuario introduzca el numero de coches vendidos de cada tipo ese
# mes y que le devuelva la cantidad en euros a comisionar ese mes

NumVendidoRMB1St = input("Pon numero de coches RMB1 vendidos: ")
NumVendidoRMBPlusSt = input("Pon numero de coches RMBPlus vendidos: ")
NumVendidoRMBTTSt = input("Pon numero de coches RMBTT vendidos: ")

# Convierto a numero entero
NumVendidoRMB1 = int(NumVendidoRMB1St)
NumVendidoRMBPlus = int(NumVendidoRMBPlusSt)
NumVendidoRMBTT = int(NumVendidoRMBTTSt)

# Calculo comision
ComisionarRMB1 = NumVendidoRMB1 * RMB1 * 0.03  
ComisionarRMBPlus = NumVendidoRMBPlus * RMBPlus * 0.05
ComisionarRBMTT = NumVendidoRMBTT * RBMTT * 0.07

#Cantidad total
ComisionTotal = ComisionarRBMTT + ComisionarRMB1 + ComisionarRMBPlus

# Imprimo por pantalla
print("La comision por el RMB1 en este mes es: ", ComisionarRMB1)
print("La comision por el RMBPlus en este mes es: ", ComisionarRMBPlus)
print("La comision por el RMBTT en este mes es: ", ComisionarRBMTT)
print("La comision total es: ", ComisionTotal)


