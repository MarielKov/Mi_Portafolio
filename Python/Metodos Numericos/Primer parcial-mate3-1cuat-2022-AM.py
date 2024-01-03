
#!/usr/bin/env python
# coding: utf-8

# # Datos

# ```
# De 1000 televidentes encuestados se obtiene la siguiente información:
# 
# a)
#     391 ven programas deportivos y los datos se han recolectado en un diccionario: 
#         
#     
#     230 ven programas cómicos y los datos se han recolectado en una tupla:
#         (41,29,58,4,45,37,9,7)
#     
#     545 ven programas sobre mundo animal y los datos se han recolectado en una lista:
#         [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
# 
# b) 
# Por otra parte, se sabe que:
#     98 ven programas cómicos y deportivos
#     152 ven programas cómicos y de mundo animal
#     88 ven programas deportivos y de mundo animal
#     90 no ven ninguno de esos programas
# 
# c)
# Resolver y responder:
#     1. Cuántos entrevistados ven los 3 tipos de programas?
#     2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
#     3. Cuántos entrevistados ven sólo cómicos y mundo animal?
#     4. Cuántos entrevistados ven sólo deportivos y mundo animal
#     5. Cuántos entrevistados ven sólo deportes?
#     6. Cuántos entrevistados ven sólo cómicos?
#     7. Cuántos entrevistados ven sólo mundo animal? 
#     8. Cuántos entrevistados ven 2 de las 3 categorías?
# 
# d) Graficar con matplotlib_venn
# 
# Nota: 
# 
# El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y del lenguaje, etc. No se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones de variables.
# 
# Una vez resuelto el ejercicio, sube la solución a la carpeta del campus con nombre y apellido como nombre de archivo.
# 
# ```

# # Solución

import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn3_circles
deportesdic = {"Voleybol": 10, "Hockey": 87,  "Equitacion":23, "Ciclismo":81, "Esqui":11, "Futbol": 45, "Tenis": 37,
               "Rugby": 9, "Basquetbol": 7, "Boxeo": 6, "Natacion":75}
comicotupla =   (41,29,58,4,45,37,9,7)
animallista= [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]

univ = 1000
ning = 90
def sumastotal(x):
    sum=0 
    for elm in x:
       sum = sum + elm
    return (sum)

def sumastotaldep(deportesdic):
    sum=0 
    for elm in deportesdic.values():
       sum = sum + elm
    return (sum) 

totalcomico = sumastotal(comicotupla)
totalanimal = sumastotal(animallista)
totaldeportes = sumastotaldep(deportesdic)



d = totaldeportes - (98 + 88 + 90)
c = totalcomico - (98 + 152 + 90)
a = totalanimal - (152 + 88 + 90)



print(totaldeportes)
print(totalcomico)
print(totalanimal)

def conjuntodep (deportesdic):
    deportes = set()
    for elm in deportesdic.values():
        deportes.add(elm)
    return (deportes)

comico = set(comicotupla)
animal = set(animallista)
deportes = conjuntodep(deportesdic)
def soloDCA(x ,y, z):
    return (x & y & z)

DCA = soloDCA(deportes, animal, comico)

sumadca = sumastotal(DCA)
print(sumadca)

# In[ ]:
setdeportes = {d , 98, 88, sumadca}
setcomico = {c, 98, 152, sumadca}
setanimal = {a, 152, 88, sumadca}

def solo2 (x,y):
    return (x & y)



#     2. Cuántos entrevistados sólo lo ven deportivos y cómicos?
#     3. Cuántos entrevistados ven sólo cómicos y mundo animal?
#     4. Cuántos entrevistados ven sólo deportivos y mundo animal

DC = solo2(setdeportes, setcomico)
CA = solo2(setcomico, setanimal)
DA = solo2(setdeportes, setanimal)

def solo1 (x, y,z):
    return (x-y) & (x-z)

#     5. Cuántos entrevistados ven sólo deportes?
#     6. Cuántos entrevistados ven sólo cómicos?
#     7. Cuántos entrevistados ven sólo mundo animal? 

D = solo1(setdeportes, setanimal, setcomico)
C = solo1(setcomico, setanimal, setdeportes)    
A = solo1(setanimal, setcomico, setdeportes)
#     1. Cuántos entrevistados ven los 3 tipos de programas?
DCA2 = soloDCA(setdeportes, setanimal, setcomico)

# # Gráficos
diag = venn3(subsets=(1,1,1,1,1,1,1), set_labels= ("Deportes", "Comicos", "Mundo animal"))

diag.get_label_by_id('100').set_text(D)
diag.get_label_by_id('010').set_text(C)
diag.get_label_by_id('001').set_text(A)
diag.get_label_by_id('110').set_text(DC)
diag.get_label_by_id('011').set_text(CA)
diag.get_label_by_id('101').set_text(DA)
diag.get_label_by_id('111').set_text(DCA2)

#plt.text(-0.50, -1,10, s=(f"Universal = " + str(univ))
#plt.text(-0.60, -1,10, s= (f"Ninguno de los tres = " + str(ning))
# plt.text(-0.70, -1,10, s= (f"Solo deportes = " + str(D))
# plt.text(-0.80, -1,10, s= (f"Solo comico =  " + str(C))
#plt.text(-0.90, -1,10, s= (f"Solo mundo animal = " + str(A))
#plt.text(-1.0, -1,10, s= (f"Solo deportes y comico = " + str(DC))
#plt.text(-1.10, -1,10, s=( f"Solo comico y mundo animal= " + str(CA))
#plt.text(-1.20, -1,10, s= (f"Solo deportes y mundo animal =  " + str(DA))
#plt.text(-1.30, -1,10, s= (f"Los tres =  " + str(DCA2)
plt.show()
# In[ ]: