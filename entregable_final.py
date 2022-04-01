class trabajador:
    def __init__(self, nombre, categoria,horas_x,tardanzas):
      self.nombre = nombre
      self.categoria = categoria
      self.horas_x = horas_x
      self.tardanzas = tardanzas

print("")
print("*** DATOS DE ENTRADA ***")
nombre = input ("TRABAJADOR                   : ")
categoria = input("CATEGORIA                    : ")
horas_x = int(input("HORAS EXTRAS                 : "))
tardanzas = int(input("TARDANZAS: (minutos)         : "))

class boleta(trabajador):
    
    if categoria == ("A"):
        sueldo_b = (3000)
    elif categoria == ("a"):
        sueldo_b = (3000)    
    elif categoria == ("B"):
        sueldo_b = (2500)
    elif categoria == ("b"):
        sueldo_b = (2500)    
    elif categoria == ("C"):
        sueldo_b = (2000)
    elif categoria == ("c"):
        sueldo_b = (2000)
    
    descuento = round((((sueldo_b / 240)*tardanzas)/60),2)
    pago_h = (sueldo_b / 240)
    phe = round((pago_h * horas_x),2)
    sueldo_n = round(((sueldo_b + phe)- descuento),2)
    
    
    print("")    
    print("*** BOLETA DE PAGO ***")
    print("NOMBRE:                       ",nombre)
    print("CATEGORIA:                    ",categoria)
    print("SUELDO BASICO:                ",sueldo_b)
    print("DESCUENTO TARDANZAS:          ",descuento)
    print("PAGO HORAS EXTRAS:            ",phe)
    print("SUELDO NETO:                  ",sueldo_n) 
    
    
    
    
    
    
           
            
            
       
            
                  
            
              
    
    
              
            
                

      
    