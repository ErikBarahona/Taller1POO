class computadora:
  def __init__(self):
    print ("Tipo de computador")
  def tipo(self,mensaje):
    print (mensaje)
    
Desktop = computadora()
Desktop.tipo('soy un Desktop')
AIO = computadora()
AIO.tipo('soy un All in one')
Laptop = computadora()
Laptop.tipo('soy una Laptop')
Notebook = computadora()
Notebook.tipo('soy un Notebook')


