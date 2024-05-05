# Projet RAM
Aymeric GOUDOUT
Cyriac THIBAUDEAU

1. Simulation de l'exécution d'une machine RAM 
2. La pile dans la RAM
3. Optimisation de machine RAM

## Simulation de l'exécution d'une machine RAM {#part1}

    1. Notre programme prend en entrée un fichier text .ram représentant le programme voulu, qui doit être écrit tel qu'il le serait sur papier. En utilisant lex et yacc, on met en place un language et une grammaire qui nous permet d'analyser ligne par ligne le contenu de celui-ci. Grâce aux règles de la grammaire, on écrit la suite des opérations dans une liste en python pour garder un indexage de celles-ci. Ayant créée des fonctions python pour chaque fonctions RAM possibles, il ne reste au programme plus que d'évaluer une à une les instructions à suivre.

## La pile de la RAM {#part2}

    1. Pseudo Code:

        Initialisation : 

            R0 = I1 : longueur de w
            R1 = I2 : nombre de transi
            R2 = 3 : pointeur de début du mot
            R3 = 0 : état initial
            R4 = 0 : contient le caractère courant du mot
            R5 = 0 : taille de la pile
            R6 ... = 0 : utilisé pour empiler/dépiler les symboles de la pile

        Boucle principale :

            tant que R2 < R0:

                adresse = R2
                R4 = I@R2

                pour i de 0 à R1-1

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

## Optimisation de machine RAM {#part3}

