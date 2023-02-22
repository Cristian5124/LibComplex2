<h1 align="center">LIBRERÍA DE MATRICES Y VECTORES COMPLEJOS</h1>
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhra9fSfv5wMAxy4hyGbJXLrjLgnuPH2Y3kPRgSrP-4pymm5t5kJPuMKBKGUrxdhzkZXA9SCjag53faV7a_KkxM6gtaLJSlelo4so7d4zJtJg4BAcqzR9isV9MhT0dbJdMlWhplGO_S0RB8T97v-feUAEErvUVtJIorVlX0xUN3_pXINDH49aETig/s16000/a.png" alt="" class="Complex">

`Esta librería de matrices y vectores de números complejos contiene una cantidad considerable de operaciones entre ellos.` <br>
`Algunos de los aspectos más relevantes de este trabajo son:` <br><br>
✔️ Órden secuencial de las operaciones (prelación de operaciones). <br>
✔️ Posibilidad de modificar las matrices o vectores para cualquier caso de prueba. <br>
✔️ Interfaz amigable y respuesta rápida en pantalla al usuario.
<hr>

<h2 align="left">Código Fuente</h2>

    import numpy as np

    def sumavectcomplex(a,b):
        tam=len(a)
        suma=[ 0+0j for i in range(tam)]
        cont=0

        while(cont<tam):
            suma[cont]=a[cont]+b[cont]
            cont+=1
        return suma

    def inversoaddvect(a):
        tam=len(a)
        inv=[ 0+0j for i in range(tam)]
        cont=0

        while(cont<tam):
            inv[cont]=-a[cont]
            cont+=1
        return inv

    def escalarxvector(k1,a):
        tam=len(a)
        mult=[ 0+0j for i in range(tam)]
        cont=0

        while(cont<tam):
            mult[cont]=a[cont]*k1
            cont+=1
        return mult

    def addmatrizvcomplex(c,d):
        if(len(c)==len(d) and len(c[0])==len(d[0])):
            suma=[]
            filas=len(c)
            columnas=len(c[0])
            for x in range(filas):
                suma.append( [0] * columnas)
            for h in range(filas):
                for k in range(columnas):suma[h][k]+=c[h][k]+d[h][k]
        return suma

    def invaddmatrizcomplex(e):
        matriz = np.matrix(e)
        invadd = np.linalg.inv(matriz)
        return invadd

    def escxmatrizcomplex(k,c):
        matriz = np.matrix(c)
        return matriz*k

    def traspmatriz(f):
        traspmatriz = np.transpose(f)
        return traspmatriz

    def conjugmatriz(f):
        return np.conj(f)

    def adjmatriz(f):
        trasp = traspmatriz(f)
        adj = conjugmatriz(trasp)
        return adj

    def prod2matrices(e,g):
        return np.matmul(e,g)

    def accionmatvec(f,a):
        if len(f[0])!=len(a):
            print("No es posible hacer la multiplicación.")
        return np.dot(f,a)

    def prodintvect(a,b):
        return np.dot(a,b)

    def normavector(a):
        return round(np.linalg.norm(a),5)

    def dist2vectores(a,b):
        a = np.array(a)
        b = np.array(b)
        return round(np.linalg.norm(a-b),5)

    def valpropmatriz(g):
        g=np.array(g)
        valpropio = np.linalg.eigvals(g)
        print(f'Valores propios: {valpropio[0]}')
        print("")
        vectorpropio = np.linalg.eig(g)
        print(f'Vectores propios: {vectorpropio[0][1]}')

    def matrizunit(g):
        for i in range(len(g)):
            for j in range (len(g[0])):
                if i==j and (g[i][j]!=1 or g[i][j]!=j):
                    return False
                elif i!=j and g[i][j]!=0:
                    return False
        return True

    def matrizhermitiana(g):
        return np.allclose(g, np.conjugate(np.transpose(g)))

    def prodtensor(a,b):
        a = np.array(a).reshape(3,1)
        b = np.array(b).reshape(3,1)
        return (np.kron(a,b))

    def main():
        a = [2j,4+1j,3]
        b = [1+2j,-2+1j,3.5j]
        c = [[2j,4+1j,3],[1+2j,-2+1j,3.5j]]
        d = [[7-4j,4+5j,4],[10-3j,-1+2j,4-3j]]
        e = [[1+3j,2j-1],[-3j+8,7-1j]]
        f = [[1+1j,2j-2,3j+1],[1j-6,3-2j,-1j+2],[2j,0,1+3j]]
        g = [[2-3j,1j+3],[4+8j,2j-1]]
        h = [1-3j,0+1j,-2-5j]
        k1 = 2+3j
        k2 = -3-1j

        print(sumavectcomplex(a,b))
        print("")
        print(inversoaddvect(b))
        print("")
        print(escalarxvector(k1,a))
        print("")
        print(addmatrizvcomplex(c, d))
        print("")
        print(invaddmatrizcomplex(e))
        print("")
        print(escxmatrizcomplex(2,c))
        print("")
        print(traspmatriz(f))
        print("")
        print(conjugmatriz(f))
        print("")
        print(adjmatriz(f))
        print("")
        print(prod2matrices(e,g))
        print("")
        print(accionmatvec(f,a))
        print("")
        print(prodintvect(a,b))
        print("")
        print(normavector(a))
        print("")
        print(dist2vectores(a,b))
        print("")
        valpropmatriz(g)
        print("")
        print(matrizunit(g))
        print("")
        print(matrizhermitiana(g))
        print("")
        print(prodtensor(a,b))
        print("")

    main()
    
`Trabajo realizado por el estudiante Cristian David Polo Garrido.`
