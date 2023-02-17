<h1 align="center">LIBRERÍA DE COMPLEJOS</h1>
<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjKO_u5IerRydQSZu4WdilrqjAwnip2QaOQdgfOvDVXQTB7BgENjbcn9e4SG__pSQ0j-mKDLE4GIxlFluVEsM8bBHxyhL7bI5_VXiIpUacA2Lr-TOgen4MN12WSYV07Za1miunMWrzUFdR9QUThaGSdDiNNHULHL6w0Pjd34gpLsWnrjKr1flQPyA/s16000/Complex.png" alt="" class="Complex">

`Esta librería de números complejos evidencia algunas de las operaciones fundamentales de este conjunto de números y sus notaciones.` <br>
`Algunos de los aspectos más relevantes de este trabajo son:` <br><br>
✔️ Órden secuencial de las operaciones (prelación de operaciones). <br>
✔️ Utilización de tuplas modificables a cualquier caso de prueba. <br>
✔️ Archivo de pruebas que certifica el correcto funcionamiento de la calculadora.
<hr>

<h2 align="left">Código Fuente</h2>

    import math

    def sumacomplex(c1,c2):
        real=c1[0]+c2[0]
        img=c1[1]+c2[1]
        resultado=(real,img)
        return resultado

    def multcomplex(c1,c2):
        real=((c1[0]*c2[0])-(c1[1]*c2[1]))
        img=(c1[0]*c2[1])+(c1[1]*c2[0])
        resultado=(real,img)
        return resultado

    def restacomplex(c1,c2):
        real=c1[0]-c2[0]
        img=c1[1]-c2[1]
        resultado=(real,img)
        return resultado

    def divcomplex(c1,c2):
        c3=(c2[0],-c2[1])
        realnum=(c1[0]*c3[0])-(c1[1]*c3[1])
        imgnum=(c1[0]*c3[1])+(c1[1]*c3[0])
        realdenom=(c2[0]*c3[0])-(c2[1]*c3[1])
        resultadodiv=(realnum,imgnum,realdenom)
        return resultadodiv

    def modulocomplex(c):
        modu=round((c[0]**2+c[1]**2)**(0.5),6)
        return modu

    def conjugadocomplex(c):
        return (c[0],-c[1])

    def fasecomplex(c):
        if(c[0]!=0):
            fase=math.degrees(math.atan((c[1])/(c[0])))
            if(c[0]<0 and c[1]>0):
                fase+=180
            if(c[0]<0 and c[1]<0):
                fase-=180
            fase=round(fase,6)
        else:
            if(c[1]==0):
                fase=0
            elif(c[1]>0):
                fase=90
            elif(c[1]<0):
                fase=270
        return fase

    def polarcomplex(c):
        modu=modulocomplex(c)
        fase=fasecomplex(c)
        resultado=(modu,fase)
        return resultado

    def printpolarcomplex(modu,fase):
        print(f'{modu} ({fase}°)')

    def printcomplex(c):
        print("{} + {}i".format(c[0],c[1]))

    def printdivcomplex(c):
        print(f"({c[0]} / {c[2]}) + ({c[1]} / {c[2]}) i")

    if __name__ == '__main__':
        printcomplex((7,-4))
        printcomplex(sumacomplex((3,-8),(4,6)))
        printcomplex(multcomplex((2,-3),(-1,1)))
        printcomplex(restacomplex((1,-1),(-2,-5)))
        print(modulocomplex((-2,-3)))
        printdivcomplex(divcomplex((3,2),(-1,2)))
        print(conjugadocomplex((7,-4)))
        fase=fasecomplex((7,-4))
        print(f'{fase}°')
        print(polarcomplex((7,-4)))
    
`Trabajo realizado por el estudiante Cristian David Polo Garrido.`
