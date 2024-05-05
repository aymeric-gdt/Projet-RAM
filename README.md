# Projet RAM
Aymeric GOUDOUT
Cyriac THIBAUDEAU

#### Prérequis
Les librairies networkx et matplotlib sont utilisées pour la partie graphe. Pour les installer :
```
pip install networkx
pip install matplotlib
```

1. Simulation de l'exécution d'une machine RAM 
2. La pile dans la RAM
3. Optimisation de machine RAM

## Simulation de l'exécution d'une machine RAM {#part1}

    1. Notre structure de données prend en entrée un fichier text .ram représentant le programme voulu, qui doit être écrit tel qu'il le serait sur papier, et une liste de données sur lequel ce code ram sera executé.

    La classe RegistreManager est utilisée pour gérer trois types de registres : lr_input, lr_main et lr_output. Voici ses méthodes et son fonctionnement :

        Initialisation (__init__) : Crée des listes vides pour chaque type de registre.
        Méthodes get_registre et set_registre : Permettent d'accéder et de modifier les valeurs des registres à un indice donné, spécifié par une chaîne comme "I5" pour lr_input ou "R3" pour lr_main.
        Méthodes privées (__extend, __in_lr, __select_lr, __getset) : Gèrent les opérations internes comme l'extension des listes de registres, la vérification de l'existence d'indices, et la sélection des registres appropriés.
        Représentation (__repr__) : Fournit une représentation sous forme de chaîne de l'état actuel de chaque registre.

    La classe MachineUniverselle est une représentation en python d'une Machine Universelle comme son nom l'indique. Elle est la base de notre code. Voici ses méthodes et son fonctionnement :

        Initialisation (__init__) : Instance des registres à partir de la classe précédente, une liste de tâches, une position, et un graphe.
        Méthodes (load_input, get_config, set_config, next, start, build, show_graph, dead_code_detector, code_optimize) : Utilisées pour charger des données, obtenir les registres et modifier la configuration des registres, implementer le fonctionnement pas à pas, executer la machine puis donner l'entièreté des étapes dans un fichier output.txt, construire la machine à partir de l'input, dessiner le graphe tel qu'il est demandé dans la question 8, détecter du code mort et enfin optimiser la machine construite.
        Méthodes privées (__get_value, __ADD, __SUB, __MULT, __DIV, __MOD, __JUMP, __JE, __JLT, __JGT, __build_graph) : Correspondent à des opérations mathématiques que l'on va trouver dans les codes ram, en plus de fonctions nous permettant d'obtenir la valeur d'un registre par une chaine de caractère et d'un constructeur de graphe. 

    Pour cette question, la méthode build fait exactement cela.

    2. En reprenant ces classes, nous utiliserons cette fois-ci la méthode next pour afficher la configuration à chaque étape de l'execution de la machine universelle. On peut spécifier le nombre d'étapes que l'on veut executer, mais si ce chiffre dépasse le maxmimum de tâches à effectuer, une erreur est retournée.

    5. Les deux machines correspondent au fichiers apowb.ram et triabulle.ram. Vous pouvez les tester dans le fichier main.py. 


## La pile de la RAM {#part2}

    6. Nous avons fait le choix pour le codage des symboles de pile des transitions de toujours attribuer 2 registres : si il faut juste dépiler, les deux seront égaux à 0, sinon si il faut empiler, le premier doit être égal au symbole du haut de pile actuel et le second sera empilé par dessus.
    
    
    Pseudo Code:

        Initialisation : 

            R0 = I1 : longueur de w
            R1 = I2 : nombre de transi
            R2 = 3 : pointeur de début du mot
            R3 = 0 : état initial
            R4 = 0 : contient le caractère courant du mot
            R5 = 0 : taille de la pile
            R6 ... = 0 : utilisé pour empiler/dépiler les symboles de la pile

        Boucle principale :

            tant que R2 < I1:

                adresse = R2
                R4 = I@R2

                pour i de 0 à I2-1

                    i_transi = 3 + I1 + i * 6
                    q = I@i_transi

                    si R3 == q :

                        a = I@(i_transi + 1)

                        si R4 == a :

                            A = I@(i_transi + 2)
                            sommet = R@(6 + R5)

                            si A == sommet

                                R5 -= 1
                                w1 = I@i_transi + 3
                                w2 = I@i_transi + 4

                                si w1 vaut 1 ou 2 :
                                    R@(6 + R5) = w1
                                    R5 += 1

                                si w2 vaut 1 ou 2 :
                                    R@(6 + R5) = w2
                                    R5 += 1
                                
                                R3 = I@(i_transi + 5)
                                R2 += 1
                                break la boucle pour
                            
                            sinon :
                                boucle suivante

                        sinon :
                            boucle suivante

                    sinon : 
                        boucle suivante

                Fin Pour

            Fin Tant que

            Si R3 == 1:
                O0 = 0
            sinon :
                O0 = 1

    7. Pour tester le fonctionnement de cette machine RAM sur l'automate à pile reconnaissant {a^nb^n | n ∈ N}, exectuez la fonction test dans le fichier main.py.
    Les transitions de l'automate sont les suivantes : (q0​,0,0,11,q1​), (q1​,0,1,11,q1​), (q1​,1,1,ϵ,q2​), (q2​,1,1,ϵ,q2​), (q2​,1,0,ϵ,qf​).
    Sont équivalent que l'on donnera en entrée sera : [0,0,0,1,1,2,2,0,1,1,1,2,2,1,1,0,0,3,3,1,1,0,0,3,3,1,0,0,0,1].
    Le premier état atteint est nommé 2 puisque l'état final doit être nommé 1.

## Optimisation de machine RAM {#part3}

    8. Dans la classe MachineUniverselle nous avons implémentés la fonction show_graph() permettant de visualiser à l'aide de matplotlib et networkx le graph orienté du code ram.

    9. Pour différencier le code mort du reste du code nous avons implémenté la fonction dead_code_detector() qui se base sur la graph orienté du code ram et sur une recherche en profondeur pour trouver les sommet jamais explorés et par extension le code mort. 

