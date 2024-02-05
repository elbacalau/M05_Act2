import unittest
from codi import Treballador

class TreballadorTest(unittest.TestCase):
    """
    Conjunt de tests per validar el comportament de la classe `Treballador`.

    Aquesta classe utilitza la unitat `unittest` de Python per a les proves.

    Noteu que per als objectes individuals de la classe Treballador i
    Exception podem triar els noms que ens doni la gana,
    no cal fer-los coincidir amb els de les classes.
    """

    def test_nom_ko(self):
        """
        Aquest test verifica si el programa detecta correctament
        quan es vol assignar un nom incorrecte a l'objecte `Treballador`
        i llença l'excepció corresponent. Es crea un objecte `Treballador`
        amb un nom de menys de 3 caràcters i s'intenta establir un nou
        nom amb menys de 3 caràcters. S'espera que el programa llençi
        una excepció amb el missatge 'El nom ha de tenir 3 o més caracters'.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setNom("d")
        
        self.assertEqual(str(cm.exception), 'El nom ha de tenir 3 o més caracters')
    

    def test_set_nomina_invalid(self):
        """
        Aquest test comprova si el programa detecta adequadament quan es vol
        establir una nòmina negativa per a l'objecte `Treballador`.
        Es crea un objecte `Treballador` amb una nòmina inicial i s'intenta
        establir una nova nòmina amb un valor negatiu. S'espera que el programa
        llençi una excepció amb el missatge 'La nomina no pot ser un numero negatiu'.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setNomina(-1)
        
        self.assertEqual(str(cm.exception), 'La nomina no pot ser un numero negatiu')


    def test_set_nomina_valid(self):
        """
        Aquest test verifica si el programa pot establir correctament una
        nòmina vàlida per a l'objecte `Treballador`. Es crea un objecte
        `Treballador` i s'estableix una nova nòmina. S'espera que el valor
        de la nòmina de l'objecte sigui igual al valor establert.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setNomina(1000)
        self.assertEqual(treballador_meu.getNomina(), 1000)


    def test_set_hores_extres(self):
        """
        Aquest test comprova si el programa pot establir correctament la
        quantitat d'hores extres per a l'objecte `Treballador`. Es crea un
        objecte `Treballador` i s'estableix un nombre d'hores extres.
        S'espera que el valor de les hores extres de l'objecte sigui igual al valor establert.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setHoresExtres(10)
        self.assertEqual(treballador_meu.getHoresExtres(), 10)


    def test_set_tipus_treballador(self):
        """
        Aquest test verifica si el programa pot establir correctament el
        tipus de treballador per a l'objecte `Treballador`. Es crea un
        objecte `Treballador` i s'estableix un nou tipus de treballador.
        S'espera que el tipus de treballador de l'objecte sigui igual al valor establert.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        treballador_meu.setTipusTreballador(1)
        self.assertEqual(treballador_meu.tipusTreballador, 1)

    def test_set_tipus_treballador_invalid(self):
        """
        Aquest test comprova si el programa detecta adequadament quan es vol
        establir un tipus de treballador no vàlid per a l'objecte `Treballador`.
        Es crea un objecte `Treballador` i s'intenta establir un tipus de treballador
        fora de l'interval permès. S'espera que el programa llençi una excepció
        amb el missatge 'Tipus de treballador no vàlid'.
        """
        treballador_meu = Treballador("pepa",0,2500,10)
        with self.assertRaises(Exception) as cm:
            treballador_meu.setTipusTreballador(3)
        
        self.assertEqual(str(cm.exception), 'Tipus de treballador no valid')
