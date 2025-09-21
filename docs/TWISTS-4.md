# TWISTS-4

### Introduction

Ce mémo recueille des idées de "twists" comme tentatives de réponses aux manques ou faiblesses rapportés par le jury de la sélection au concours de LudiNord 2025.

### Nouvelles mécaniques

#### Mise en place

En début de partie, après que la désignation du premier joueur et le choix des couleurs des joueurs, mais avant le premier tour, les cartes de positions, autres que celles des montagnes, sont mélangées faces cachées. Chaque joueur en reçoit une face cachée, mais qu'il peut consulter. Cette carte, appelée "carte personnelle", pourra être jouée une seule fois, soit verso pour le "trésor", soit verso pour la "chevauchée".

#### Trésor

Après avoir lancer le dé de bonus en début de tour, le joueur peut jouer sa carte personnelle pour forcer le dé à la valeur de son choix. La carte personnelle est ensuite défaussée face cachée.

Cet usage de "trésor" n'est pas compté dans les deux actions possibles de son tour de jeu.

#### Chevauchée

Un officier est déplacé à la position indiquée par la carte personnelle, qui est ensuite défaussée face cachée. Si le baron est déplacé vers une tuile contenant un baron adverse, alors les deux barons échangent leurs positions.

Cet usage de la "chevauchée" est compté comme "déplacement d'officier" ; c'est donc une des deux actions possibles du tour de jeu.

## Révision de la mécanique de capture de donjon

Le coût de la "capture de donjon" a été jugée trop faible par certains testeurs. Une évaluation plus juste conduit à :

- **engager 12 troupes** pour capturer un donjon adverse (soit le double d'une opération en deux temps) ;
- **renvoyer 9 troupes en réserve**.
- **défausser 3 troupes** (qui correspondent à la construction du nouveau donjon).

La justification est que 3 troupes sont nécessaires pour détruire le donjon adverse et qui 3 troupes sont nécessaires pour construire le nouveau donjon, mais que cette opération de capture en 1 seul ordre aux troupes fait économiser au Baron en moyenne de l'ordre de 3.5 tours de jeu, qui aurait permis de recruter en moyenne 2*3.5 = 7 troupes. Donc, en demandant d'engager 6 troupes supplémentaires, le coût de capture d'un donjon reste généreux.

Voici le raisonnement détaillé qui justifie ce coût .

- En partant d'une tuile de commandement avec 6 troupes (3 pour détruire le donjon adverse, et 3 pour construire le nouveau donjon), la mécanique de capture de donjon évite le déplacement du Baron, un premier ordre aux troupes pour les déplacer et un second pour construire le nouveau donjon. Cela économise donc:
  - un aller-et-retour ;
  - deux ordres aux troupes.
- Le case extrême : le baron est au centre (case 19)  et le donjon capturé est au bout de la diagonale (case 37), soit 12 cases pour un aller-et-retour. C'est juste une remarque, car on va s'en tenir au cas moyen.
- Le cas moyen: le baron est au centre (case 19)  et le donjon capturé est au bout de la diagonale (case 37)  : soit 6 cases pour un aller-et-retour.
- Evaluons le nombre moyen de tours nécessaire pour faire cet aller-retour et passer deux ordres :
  - Premier tour avec dé {1, 2} : dispersion des 3 troupes de construction + déplacement-aller du baron de 3 cases.
    - Second tour avec dé {1,2} : construction de donjon + déplacement-retour du baron de 3 cases => fin d'opération en **2 tours** avec la **probabilité 1/9** (occurrence 1)
    - Second tour avec dé {3, 4} : construction de donjon + déplacement-retour du baron de 2 cases
      - Troisième tour dé quelconque : requis pour le retour => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 1). 
    - Second tour avec dé {5, 6} : construction de donjon + déplacement-retour du baron de 1 case 
      - Troisième tour dé quelconque : requis pour le retour => fin d'opération en **3 tours** avec la **probabilité 1/9 **(occurrence 2).
  - Premier tour avec dé {3, 4} : dispersion des 3 troupes de construction + déplacement-aller du baron de 2 cases.
    - Second tour avec dé quelconque : déplacement-aller du baron de 1 case + construction de donjon 
      - Troisième tour avec dé {1,2} : déplacement-retour du baron de 3 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 3). 
      - Troisième tour avec dé {3, 4} : déplacement-retour du baron de 2 + 1 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 4).
      - Troisième tour avec dé {5, 6} : déplacement-retour du baron de 2  cases
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 case => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 1).
  - Premier tour avec dé {5, 6} : dispersion des 3 troupes de construction + déplacement-aller du baron de 1 case.
    - Second tour avec dé {1,2} : déplacement-retour du baron de 2 cases + construction de donjon
      - Troisième tour avec dé {1,2} : déplacement-retour du baron de 3 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 5).
      - Troisième tour avec dé {3, 4} : déplacement-retour du baron de 2 + 1 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 6).
      - Troisième tour avec dé {5, 6} : déplacement-retour du baron de 1 + 1 cases.
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 case => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 2).
    - Second tour avec dé {3, 4} : déplacement-retour du baron de 2 +  1 cases 
      - Troisième tour avec dé {1,2} : construction de donjon + déplacement-retour du baron de 3 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 7).
      - Troisième tour avec dé {3, 4} : construction de donjon + déplacement-retour du baron de 2 cases 
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 case => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 3).
      - Troisième tour avec dé {5, 6} : construction de donjon + déplacement-retour du baron de 1 case
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 +1 cases => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 4).
    - Second tour avec dé {5, 6} : déplacement-retour du baron de 1 + 1 cases 
      - Troisième tour avec dé {1,2} : construction de donjon + déplacement-retour du baron de 3 cases => fin d'opération en **3 tours** avec la **probabilité 1/9** (occurrence 8).
      - Troisième tour avec dé {3, 4} : construction de donjon + déplacement-retour du baron de 2 cases 
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 case => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 5).
      - Troisième tour avec dé {5, 6} : construction de donjon + déplacement-retour du baron de 1 case
        - Quatrième tour avec dé quelconque : déplacement-aller du baron de 1 + 1 cases => fin d'opération en **4 tours** avec la **probabilité 1/9** (occurrence 6). 
  - Bilan des scénarios qui chacun ont la même probabilité 1/9 :
    - Opération en 2 tours : 1
    - Opération en 3 tours : 8
    - Opération en 4 tours : 6
    - Nombre moyen = (3 + 24 + 24)/(1 + 8 + 6) = 51/15 = 3.4 ; que l'on arrondit à 3.5
    - Or pendant 3.5 tours, on aurait pu en moyenne recruter 3.5*2 = 7 troupes
    - Il serait donc raisonnable de disposer de 7 troupes en plus des 6 troupes nécessaires à détruire, puis construire ; soit donc un engagement de 13 troupes.
