import unittest
from codi import Treballador

class TreballadorTest(unittest.TestCase):
        #Aquest test prova si el programa detecta que volem assignar un nom
        #incorrecte i llença l'excepció que toca
        #Noteu que per als objectes individuals de la classe Treballador i
        #Exception podem triar els noms que ens done la gana,
        #no cal fer-los coincidir amb els de les classes"""
    
    def test_nom_ko(self):
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setNom("d")
        
        self.assertEqual(str(cm.exception), 'El nom ha de tenir 3 o més caracters')
    

    def test_set_nomina_invalid(self):
        
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setNomina(-1)
        
        self.assertEqual(str(cm.exception), 'La nomina no pot ser un numero negatiu')


    def test_set_nomina_valid(self):
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setNomina(1000)
        self.assertEqual(treballador_meu.getNomina(), 1000)



    def test_set_hores_extres(self):
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setHoresExtres(10)
        self.assertEqual(treballador_meu.getHoresExtres(), 10)


    def test_set_tipus_treballador(self):
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setTipusTreballador(1)
        self.assertEqual(treballador_meu.tipusTreballador, 1)

    def test_set_tipus_treballador_invalid(self):
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setTipusTreballador(3)
        
        self.assertEqual(str(cm.exception), 'Tipus de treballador no valid')

if __name__ == '__main__':
    unittest.main()

    


