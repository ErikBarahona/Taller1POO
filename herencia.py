class computadora:
  def __init__(self):
    print ("Tipo de computador")
  def tipo(self,mensaje):
    print (mensaje)


class hp(computadora):
  def procesador(self):
    print ("Procesador Marca Intel")

Desktop = hp()
Desktop.tipo('soy un Desktop')
Desktop.procesador()
