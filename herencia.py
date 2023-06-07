#Herencia
class carro:
    def __init__(self,nom,mod,color,precio):#CONSTRUCTOR CLASE PADRE
        self.nom=nom
        self.mod=mod
        self.color=color
        self.precio=precio
    def descripcion(self):  #FUNCION QUE MUESTRA LOS VALORES DE LOS ATRIBUTOS
        print(f"Nombre{self.nom} Modelo:{self.mod} color:{self.color} precio:{self.precio}")
class Chevrolet(Carro):#CLASE HIJA QUE  HEREDA ATRIBUTOS Y COMPORTAMIENTO DE LA CLASE PADRE
    def __init__(self, nom, mod, color, precio, marca):#constructor clase hija
        super().__init__(nom, mod, color, precio, marca)#le digo que el constructor de le clase hija hereda del constructor de que padre
        self.marca=marca
    def descripcion(self):  #hereda la funcion descripcion de la clase padre y le agrega especificidad
        super().descripcion()
        print(f"marca {self.marca}")

c1=carro("Versa",2021,"Negro","150000")#creamos o instanciamos el objeto c1 y le indicamos que es de la clase carro
#llamado