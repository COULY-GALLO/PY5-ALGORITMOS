import py5


cosa1 = [6490,123,54,567,8,567,1,34,5,75,98,23]  


def bubble_sort(num1):
    num = len(num1) 
    for i in range(num - 1):  
        for j in range(num - 1 - i):  
           num2 = num1[j + 1] 
           if num1[j] < num2:
              continue  
           if num1[j] > num2:  
            num1[j], num1[j + 1] = num1[j + 1], num1[j]
           if num1[j] == num2:
            continue  
    return num1  



def setup():
    py5.size(600, 400)  # Tamaño de la ventana
    py5.background(255)  
    py5.no_stroke()  
    for i, tamaño in enumerate(cosa1):
        
        diametro_circulo = tamaño * 30 
        x_pos = (i + 3)
        y_pos = py5.height / 2  
        
        py5.fill(100, 150, 250) 
        py5.circle(x_pos, y_pos, diametro_circulo)





def draw():
    py5.background(255)  # Limpiar la pantalla en cada frame
    for i, tamano in enumerate(bubble_sort(cosa1)):
        
        diametro_circulo = tamano * 30 
        x_pos = (i + 3)  # Posición X de cada círculo
        y_pos = py5.height / 2  
        
        py5.fill(100, 150, 250) 
        py5.circle(x_pos, y_pos, diametro_circulo)

# Ejecutar el sketch
py5.run_sketch()
