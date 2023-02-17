<h1 align="center">LIBRERÍA DE MATRICES Y VECTORES COMPLEJOS</h1>
<img src="[https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKO_u5IerRydQSZu4WdilrqjAwnip2QaOQdgfOvDVXQTB7BgENjbcn9e4SG__pSQ0j-mKDLE4GIxlFluVEsM8bBHxyhL7bI5_VXiIpUacA2Lr-TOgen4MN12WSYV07Za1miunMWrzUFdR9QUThaGSdDiNNHULHL6w0Pjd34gpLsWnrjKr1flQPyA/s16000/Complex.png](https://blogger.googleusercontent.com/img/a/AVvXsEggS7Aj9h4uMSKmUpqERD0VevEgV6XIiSJLMrjFjWFi19A9Hsa7-jEo8a72DQXebw6xLE6Vh315e0Juba2hFkWYVcrfiRV6TrmAXf6xXUkeWG6H0RNrgn_sZi3mvpTeP1isfhgUvlHtAFS8ArSFA9LgNXfLYNbT2OKuYuQiOggxoO9U8daQk-l1LQ=s16000)" alt="" class="Complex">

`Esta librería de números complejos evidencia algunas de las operaciones fundamentales de este conjunto de números y sus notaciones.` <br>
`Algunos de los aspectos más relevantes de este trabajo son:` <br><br>
✔️ Órden secuencial de las operaciones (prelación de operaciones). <br>
✔️ Utilización de tuplas modificables a cualquier caso de prueba. <br>
✔️ Archivo de pruebas que certifica el correcto funcionamiento de la calculadora.
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

    def escalarxvector(k,a):
        tam=len(a)
        mult=[ 0+0j for i in range(tam)]
        cont=0

        while(cont<tam):
            mult[cont]=a[cont]*k
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

    def prodintvect(a,b):
        return np.dot(a,b)

    def normavector(a):
        return round(np.linalg.norm(a),5)

    def dist2vectores(a,b):
        a = np.array(a)
        b = np.array(b)
        return round(np.linalg.norm(a-b),5)

    def matrizunit(g):
        for i in range(len(g)):
            for j in range (len(g[0])):
                if i==j and (g[i][j]!=1 or g[i][j]!=j):
                    return 'No es una matriz unitaria.'
                elif i!=j and g[i][j]!=0:
                    return 'Si es una matriz unitaria.'
        return True

    def valpropmatriz(g):
        g=np.array(g)
        valpropio = np.linalg.eigvals(g)
        print(f'Valores propios: {valpropio}')
        print("")
        vectorpropio = np.linalg.eig(g)
        print(f'Vectores propios: {vectorpropio}')

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

        print(sumavectcomplex(a,b))
        print("")
        print(inversoaddvect(a))
        print("")
        print(escalarxvector(2+3j,a))
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
        print(prodintvect(a,b))
        print("")
        print(normavector(a))
        print("")
        print(dist2vectores(a,b))
        print("")
        print(matrizunit(g))
        print("")
        valpropmatriz(g)
        print("")
        print(prodtensor(a,b))
        print("")

    main()
    
`Trabajo realizado por el estudiante Cristian David Polo Garrido.`
