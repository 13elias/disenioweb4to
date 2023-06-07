class proveedor:
    def __init__ (self, marca, id_provedor, nombre,id_precio_provedor):
      self.nombre=nombre
      self.id_precio_provedor=id_precio_provedor
      self.marca=marca
      self.id_provedor=id_provedor
    def mostras (self):
      print ("nombre:",self.nombre)
      print("id_precio_provedor:",self.id_precio_provedor)
      print("marca:",self.marca)
      print("id_provedor:",self.id_provedor)
p1=proveedor("Distribuidora Tijuano","google","martin ricardo",2000)
p1.mostrar()