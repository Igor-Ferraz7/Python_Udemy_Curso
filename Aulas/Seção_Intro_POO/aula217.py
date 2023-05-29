# Composição: ser DONO de outro objeto (Se o obj é deletado, no DONO também será)
# Para ser dono de um objeto, basta apenas criá-lo dentro de sua classe/objeto
# Um objeto PRECISA de outro objeto

class Client:
    def __init__(self, name):
        self.name = name
        self.adresses = []

    def insert_adress(self, street, number):
        self.adresses.append(Adress(street, number))
    
    def insert_external_adress(self, adress):
        self.adresses.append(adress)

    def list_adresses(self):
        for adress in self.adresses:
            print(adress.street, adress.number)
    
    def __del__(self):
        print(f'Del {self.name}')

class Adress:
    def __init__(self, street, number):
        self.street = street
        self.number = number
    
    def __del__(self):
        print(f'Del {self.street} {self.number}')

client1 = Client('Igor')
client1.insert_adress('Manhattan', '37')
external_adress = Adress('Brooklyn', '09')

client1.insert_external_adress(external_adress)
client1.list_adresses()

del client1

print(external_adress.street, external_adress.number)
print('-----------Fim de codigo-----------')
