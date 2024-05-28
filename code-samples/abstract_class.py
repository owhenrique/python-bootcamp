from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    @property
    def marca(self):
        return "LG"

    def ligar(self):
        print("ligando tv...")
        print("LIGADA")
    
    def desligar(self):
        print("desligando tv...")
        print("DESLIGADA")

class ControleArCondicionado(ControleRemoto):
    @property
    def marca(self):
        return "SAMSUNG"

    def ligar(self):
        print("ligando o ar condicionado...")
        print("LIGADO")
    
    def desligar(self):
        print("desligando o ar condicionado...")
        print("DESLIGADAO")

# Métodos ligar e desligar são os contratos, que forçam as classes filhas à implementá-los
# controle = ControleRemoto() # Erro: não podemos instânciar por conta dos métodos abstratos
controle1 = ControleTv()
print(controle1.marca)
controle1.ligar()
controle1.desligar()

controle2 = ControleArCondicionado()
print(controle2.marca)
controle2.ligar()
controle2.desligar()