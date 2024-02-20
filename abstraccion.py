class computadora:
  def __init__(self, color, pulgadas, velocidad, memoria):
    self.color = color
    self.pulgadas = pulgadas
    self.velocidad = velocidad
    self.memoria = memoria

    def caracteristicas(self):
      pass


class hp(computadora):
  def caracteristicas(self):
    print("Estoy usando la computadora laptop de color " + self.color + " de " + self.pulgadas + " pulgadas, con una velocidad de " +self.velocidad + " GHz y con un almacenamiento de " + self.memoria)


hp = hp("azul", "15", "560", "16" )


hp.caracteristicas()

    
