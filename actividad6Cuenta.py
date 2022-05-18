class Cuenta:
  #necesito un atributo de titular de la cuenta y uno para la cantidad
  def __init__(self,titular,cantidad):
    self.titular=titular
    self.cantidad=cantidad
  #necesito definir mostrar() como metodo
  def mostrar(self):
    print("El titular de la cuenta es Lucas y tiene $23.000,00 en su cuenta")
  def ingresar(self,cantidad):
    if (cantidad < 0):
      pass
    else:
      cantidad=23000+cantidad
      print(f"Ahora tiene: ${cantidad} en su cuenta")
  def retirar(self,cantidad):
    cantidad=31000-cantidad
    print(f"Ahora tiene: ${cantidad} en su cuenta")

cuenta1=Cuenta("Lucas",23000)
print(f"El titular de la cuenta es: {cuenta1.titular}")
print(f"El titular {cuenta1.titular} tiene ${cuenta1.cantidad} en su cuenta")
cuenta1.mostrar()
cuenta1.ingresar(8000)
cuenta1.retirar(5000)