# TreballadorTest - Documentació dels Tests

Aquest és un conjunt de tests per validar el comportament de la classe `Treballador` a través de la unitat `unittest` de Python.

## Test: `test_nom_ko`

Aquest test verifica si el programa detecta correctament quan es vol assignar un nom incorrecte a l'objecte `Treballador` i llença l'excepció corresponent. Es crea un objecte `Treballador` amb un nom de menys de 3 caràcters i s'intenta establir un nou nom amb menys de 3 caràcters. S'espera que el programa llençi una excepció amb el missatge 'El nom ha de tenir 3 o més caracters'.

## Test: `test_set_nomina_invalid`

Aquest test comprova si el programa detecta adequadament quan es vol establir una nòmina negativa per a l'objecte `Treballador`. Es crea un objecte `Treballador` amb una nòmina inicial i s'intenta establir una nova nòmina amb un valor negatiu. S'espera que el programa llençi una excepció amb el missatge 'La nomina no pot ser un numero negatiu'.

## Test: `test_set_nomina_valid`

Aquest test verifica si el programa pot establir correctament una nòmina vàlida per a l'objecte `Treballador`. Es crea un objecte `Treballador` i s'estableix una nova nòmina. S'espera que el valor de la nòmina de l'objecte sigui igual al valor establert.

## Test: `test_set_hores_extres`

Aquest test comprova si el programa pot establir correctament la quantitat d'hores extres per a l'objecte `Treballador`. Es crea un objecte `Treballador` i s'estableix un nombre d'hores extres. S'espera que el valor de les hores extres de l'objecte sigui igual al valor establert.

## Test: `test_set_tipus_treballador`

Aquest test verifica si el programa pot establir correctament el tipus de treballador per a l'objecte `Treballador`. Es crea un objecte `Treballador` i s'estableix un nou tipus de treballador. S'espera que el tipus de treballador de l'objecte sigui igual al valor establert.

## Test: `test_set_tipus_treballador_invalid`

Aquest test comprova si el programa detecta adequadament quan es vol establir un tipus de treballador no vàlid per a l'objecte `Treballador`. Es crea un objecte `Treballador` i s'intenta establir un tipus de treballador fora de l'interval permès. S'espera que el programa llençi una excepció amb el missatge 'Tipus de treballador no vàlid'.
