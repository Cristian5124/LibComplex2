import numpy as np
import Libcomplex2 as lc

passed =0
failed =0

a = np.array([2j,4+1j,3])
b = np.array([1+2j,-2+1j,3.5j])
c = np.array([[2j,4+1j,3],[1+2j,-2+1j,3.5j]])
d = np.array([[7-4j,4+5j,4],[10-3j,-1+2j,4-3j]])
e = np.array([[1+3j,2j-1],[-3j+8,7-1j]])
f = np.array([[1+1j,2j-2,3j+1],[1j-6,3-2j,-1j+2],[2j,0,1+3j]])
g = np.array([[2-3j,1j+3],[4+8j,2j-1]])
h = np.array([1-3j,0+1j,-2-5j])
k1 = 2+3j
k2 = -3-1j

#pruebasumavectcomplex
resp = lc.sumavectcomplex(a,b)
 
if resp==([(1+4j), (2+2j), (3+3.5j)]):
    passed += 1
else:
    failed+=1

#prueba2sumavectcomplex
resp = lc.sumavectcomplex(a,h)
 
if resp==([(1-1j), (4+2j), (1-5j)]):
    passed += 1
else:
    failed+=1

#pruebainversoaddvect
resp = lc.inversoaddvect(a)
 
if resp==([(-0-2j), (-4-1j), -3]):
    passed += 1
else:
    failed+=1

#prueba2inversoaddvect
resp = lc.inversoaddvect(b)
 
if resp==([(-1-2j), (2-1j), (-0-3.5j)]):
    passed += 1
else:
    failed+=1

#pruebaescalarxvector
resp = lc.escalarxvector(k1,a)

if resp==([(-6+4j), (5+14j), (6+9j)]):
    passed += 1
else:
    failed+=1

#prueba2escalarxvector
resp = lc.escalarxvector(k2,b)

if resp==([(-1-7j), (7-1j), (3.5-10.5j)]):
    passed += 1
else:
    failed+=1

#pruebaaddmatrizvcomplex
resp = lc.addmatrizvcomplex(c,d)

if resp==([[(7-2j), (8+6j), 7], [(11-1j), (-3+3j), (4+0.5j)]]):
    passed += 1
else:
    failed+=1

#prueba2addmatrizvcomplex
resp = lc.addmatrizvcomplex(e,g)

if resp==([[(3+0j), (2+3j)], [(12+5j), (6+1j)]]):
    passed += 1
else:
    failed+=1

#pruebainvaddmatrizcomplex
resp = lc.invaddmatrizcomplex(e)

if resp=="[[ 0.57241379-0.13103448j  0.06896552-0.17241379j] /n [-0.64137931+0.30344828j  0.10344828+0.24137931j]]":
    passed += 1
else:
    failed+=1


#Impresión de los resultados de las pruebas
print("Passed: ",passed," | Failed: ",failed)