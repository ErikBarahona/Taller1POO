class computadora:
  def __init__(self):
    pass
  def tipo(self,mensaje):
    print (mensaje)


class hp(computadora):
  def procesador(self):
    Desktop.tipo('Soy un Desktop')
    print ("Procesador Marca Intel")
class lenovo(computadora):
  def procesador(self):
    Desktop.tipo('Soy un Desktop')
    print ("Procesador Marca AMD Ryzen") 

for computadora in hp(), lenovo():
  computadora.procesador()

