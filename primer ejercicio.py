# 1. crea un programa que con dos puntos cardinales  donde pasa una linea recta en el plano cartesiano,
# se obtenga la ecuación lineal que representa la recta.
print ('Empecemos con la primera coordenada')
x1=float(input('digite el valor de X de la primera coordenada'))
y1=float(input('digite el valor de Y de la primera coordenada'))
print ('Continuemos con la segunda coordenada coordenada')
x2=float(input('digite el valor de X de la segunda coordenada'))
y2=float(input('digite el valor de Y de la segunda coordenada'))

m=(y2-y1)/(x2-x1)
b=y1-m*x1
print('La ecuación de la recta es: y = '+str(m)+' x + '+str(b))

