class Notebook:
    def __init__(self):
        print('Notebook creado ')

    def caracteristicas(self, marca, pulgadas, SO):
      self.marca = marca
      self.pulgadas = pulgadas
      self.SO = SO

    def __del__(self):
        print('Se llamo al destructor y el Notebook fue destruido')

Linux = Notebook() 
Linux.caracteristicas("Chormebook", "11" , "Chrome")
print("Tengo un computador " + Linux.marca + " de " + Linux.pulgadas + " pulgadas y con sistema operativo " + Linux.SO)
del Linux
