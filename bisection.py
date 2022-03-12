#!/usr/bin/env python
import sys
import math

def func(x):
    return math.cos(x) - x

def equa(x):
    # 3x^4 - 2x^3 - x^2 + x + 8
    return 3*x**4 - 2*x**3 - x**2 + x + 8

def main():
    a = -1 #1
    b = 1 #2
    tolerance = 0.000001
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print 'Usage : bisection.py <maximum iterations>'
        sys.exit(0)

    
    print 'iteracao\t a\t\t b\t\t media\t\t f(a)\t\t f(media)\t sinal\t\t error(b-a)\t'
    print '---------\t --------\t --------\t --------\t --------\t --------\t --------\t --------\t'
    i = 0
    while i <= int(sys.argv[1]):

        fa = equa(a)
        c = (a + b)/2.0 #3
        fc = equa(c)
        error = (b - a)

        if(i == 0):
            s = "+"
            error = 0

        print "%d\t\t %.6f\t %.6f\t %.6f\t %.6f\t %.6f\t %s\t\t %.6f\t" %(i ,a ,b ,c, fa , fc, s, error)

        if (equa(a) * equa(c)) < 0:
            b = c
            s = "-"
        else:
            a = c
            s = "+"

        i = i + 1 


#agora saimos do loop e imprimimos o valor da media final
    if abs((a-b)/2.0) < tolerance:
        print 'A raiz depois de %d iteracoes e %.10f.'%(i-1,c) 
    else:
        print 'Nao foi possivel atender a tolerancia em determinadas iteracoes.'
    


if __name__ == '__main__':
    main()
    
