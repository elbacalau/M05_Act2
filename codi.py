class Treballador:
   """Classe per a guardar les dades d'un treballador"""
   DIRECTOR = 0
   SUBDIRECTOR = 1
   BASE = 2


   def __init__(self, nom, tipus, nomina, hores):
       #Constructor amb arguments, alternatiu al constructor per defecte
       self.nomTreballador = nom
       self.tipusTreballador = tipus
       self.nominaTreballador = nomina
       self.horesExtresTreballador = hores


   def setNom(self, nom):
       #Si la longitud del nou nom es inferior a tres caracters llença excepcio
       if len(nom) < 3:
           raise Exception("El nom ha de tenir 3 o més caracters")
       #En cas contrari assign a el nom
       self.nomTreballador = nom


   def getNom(self):
       return self.nomTreballador


   def setNomina(self, euros):
        # Si la nomina es un numero negatiu salta exepcio
        if euros < 0:
            raise Exception("La nomina no pot ser un numero negatiu")

        
        self.nominaTreballador = euros




   def getNomina(self):
       return self.nominaTreballador


   def setHoresExtres(self, hores):
       # Les hores extra poden ser zero sense problema
       self.horesExtresTreballador = hores

       
       # Si les hores extra son un numero negatiu salta exepcio
       if hores < 0:
           raise Exception("Les hores extres no poden ser un numero negatiu")
    


   def getHoresExtres(self):
       return self.horesExtresTreballador


   def setTipusTreballador(self, tipus):
       # Aqui no és recomanable estalviar-se les comprovacions perquè el tipus de
       # treballador només pot ser DIRECTOR, SUbDIRECTOR o BASE
       if (tipus == self.DIRECTOR) or (tipus == self.SUBDIRECTOR) or (tipus == self.BASE):
           #Si el tipus és vàlid, l'assignem
           self.tipusTreballador = tipus
       else:
           #Si el tipus no és valid, creem excepció
           raise Exception("Tipus de treballador no valid")


   def getTipusTreballador(self):
       return self.tipusTreballador
