class Produite:
    def __init__(self,nom_produite,quantite_dispo,prix_unite):
        self.__nom_produite = nom_produite
        self.__quantite_dispo = quantite_dispo
        self.__prix_unite = prix_unite
        


    
    def set_nom(self):
        new_nom = input("saisi le nouveau nom du se produire: ")
        self.__nom_produite = new_nom

    def set_prix(self):
        try:
            new_prix_unite = int(input("saisi le neveau prix par unite: "))
        except:
            print("saisi une valeure numirique!!")

        self.__prix_unite = new_prix_unite

    def set_quantite(self):
        try:
            new_quantite = int(input("saisi la nouvlel quantite: "))
        except:
            print("saisi une vlaleure numirique et positif!!")
            quit()

        self.__quantite_dispo = new_quantite

    def get_nom(self):
        print(f"le nom de ce produite est {self.__nom_produite}")

    def ajouter_stock(self):
        try:
            new_quantite = int(input("saisi la quantite du produite a ajouter: "))
        except:
            print("saisi une valeure numirique")
            quit()
        
        if new_quantite > 0:
            self.__quantite_dispo += new_quantite
        else:
            print("saisi une valeure de quantite positif")

    def vendre(self):
        quantite_vendu = int(input("saisi la quantite a ete vendu: "))
        if self.__quantite_dispo >= quantite_vendu and quantite_vendu > 0:
            self.__quantite_dispo -= quantite_vendu
        
        else:
            print("cette quantite est pas disponible")

    def afiche_detail(self):
        print(f"==> nom: {self.__nom_produite}, quantite: {self.__quantite_dispo}, prix unitaire: {self.__prix_unite}")

    def abondance(self):
        if self.__quantite_dispo >= 1000:
            abondance = True
        elif self.__quantite_dispo < 1000:
            abondance = False
        print(f"ce produite est abandante: {abondance}")
        

produite1 = Produite("ordinateur",10,8000)
produite1.afiche_detail()
while True:
    changer_info = input("voulez vous changer les informations actuelle (oui/non): ")
    if changer_info == "oui":
        produite1.set_nom()
        produite1.set_quantite()
        produite1.set_prix()
        break
    elif changer_info == "non":
        break
    else:
        print("votre choix n'exeste pas!! ")
    



produite1.get_nom()
produite1.ajouter_stock()
produite1.vendre()
produite1.afiche_detail()
produite1.abondance()


