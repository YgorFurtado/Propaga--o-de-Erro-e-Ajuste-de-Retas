from colorama import Fore, Back, Style

n = int(input("Quantidade de Dados:"))
Eixo_X = []
Erro_X = []
Eixo_Y = []
Erro_Y = []

for i in range(0,n):
    Eixo_X.append(float(input(f"Inserir x{i+1}: ")))
for i in range(0,n):
    Erro_X.append(float(input(f"Inserir σx{i+1}: ")))
for i in range(0,n):
    Eixo_Y.append(float(input(f"Inserir y{i+1}: ")))
#for i in range(0,n):
#    Erro_Y.append(float(input(f"Inserir σy{i+1}: ")))


#Calcula <σ2>
Sig = 0
for i in range(0,n):
    Sig = Sig + (1/(Erro_X[i]**2))
    
#Calcula <x>
x = 0
for i in range(0,n):
    x = x + (Eixo_X[i]/Erro_X[i])
x = (1/Sig)*x

#Calcula <x²>
xsqr = 0
for i in range(0,n):
    xsqr = xsqr + ((Eixo_X[i]**2)/Erro_X[i])
xsqr = (1/Sig)*xsqr

#Calcula <y>
y = 0
for i in range(0,n):
    y = y + (Eixo_Y[i]/Erro_X[i])
y = (1/Sig)*y

#Calcula <xy>
xy = 0
for i in range(0,n):
    xy = xy + ((Eixo_X[i]*Eixo_Y[i])/Erro_X[i])
xy = (1/Sig)*xy

#Calcula a,b
a = ((x*y)-(xy)/(x**2)-(xsqr))
b = y - (a*x)

#Calcula Delta_a,Delta_b
Delta_a = ((1/Sig)/((xsqr)-(x**2)))**(1/2)
Delta_b = ((xsqr/Sig)/(xsqr)-(x**2))**(1/2)

print(f"a = {a}\nb = {b}")
print(f"∆a = {Delta_a}\n∆b = {Delta_b}")
input()