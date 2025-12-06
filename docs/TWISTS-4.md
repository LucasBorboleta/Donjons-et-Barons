# TWISTS-4

## Introduction

Ce mémo recueille des idées de "twists" comme tentatives de réponses aux manques ou faiblesses rapportés par le jury de la sélection au concours de LudiNord 2025.

## Nouvelles mécaniques

### Mise en place

En début de partie, après que la désignation du premier joueur et le choix des couleurs des joueurs, mais avant le premier tour, les cartes de positions, autres que celles des montagnes, sont mélangées faces cachées. Chaque joueur en reçoit une face cachée, mais qu'il peut consulter. Cette carte, appelée "carte personnelle", pourra être jouée une seule fois, soit verso pour le "trésor", soit verso pour la "chevauchée".

### Trésor

Après avoir lancer le dé de bonus en début de tour, le joueur peut jouer sa carte personnelle pour forcer le dé à la valeur de son choix. La carte personnelle est ensuite défaussée face cachée.

Cet usage de "trésor" n'est pas compté dans les deux actions possibles de son tour de jeu.

### Chevauchée

Un officier est déplacé à la position indiquée par la carte personnelle, qui est ensuite défaussée face cachée. Si le baron est déplacé vers une tuile contenant un baron adverse, alors les deux barons échangent leurs positions.

Autre option à envisager : défausse face cachée d'un carte tactique et déplacement d'officier jusqu'à 3 tuiles :

- C'est cohérence avec le dé de bonus de valeur 1 qui à permet de collecter au trésor (pioche d'une carte tactique). C'est un usage différent du dé de bonus pour un déplacement long d'officier.
- C'est aussi une option qui procure plus de flexibilité.
- Faut-il introduire deux qualificatifs au terme "chevauchée" pour distinguer ces deux types de chevauchée ?
  - Chevauchée éclair => au plus 3 tuiles
  - Chevauchée lointaine => saut à la position indiquée sur la carte tactique

Cet usage de la "chevauchée" est compté comme "déplacement d'officier" ; c'est donc une des deux actions possibles du tour de jeu.

## Révision de la mécanique de capture de donjon

Le coût de la "capture de donjon" a été jugée trop faible par certains testeurs. Une évaluation plus juste conduit à la mécanique suivante :

- **engager 9 troupes** pour capturer un donjon adverse (soit le double d'une opération en deux temps) ;
- **défausser 3 troupes** (qui correspondent à la construction du nouveau donjon) ;
- **renvoyer 6 troupes en réserve**.
- La justification est que 3 troupes sont nécessaires pour détruire le donjon adverse et qui 3 troupes sont nécessaires pour construire le nouveau donjon, mais que cette opération de capture en 1 seul ordre aux troupes fait économiser au Baron en moyenne de l'ordre de 3.15 tours de jeu (pour un scénario moyen de capture depuis le centre vers un bord de plateau, soit 3 tuiles de distance) qui aurait permis de recruter en moyenne 2*3.15 = 6.3 troupes. Lors de ces opérations d'aller-retour et de construction, le Baron aurait pu recruter 0.84 troupes en moyenne. La différence de recrutement de troupes est donc 6.3 - 0.84 = 5.46 troupes. Donc, en demandant d'engager 3 troupes supplémentaires, le coût de capture d'un donjon reste bon marché, sachant que la distance de 3 tuiles entre le Baron et le donjon est un scénario moyen.

## Révision de la limitation de recrutement

La limitation à 6 troupes dans une tuile qui empêche de passer un ordre de recrutement est artificielle. Il est donc suggérée de supprimer cette limitation. Ceci est encouragé par la révision de la mécanique de capture de donjon, qui réclame une accumulation accrue de troupes. En effet, 6 tours de jeu sont nécessaire pour accumuler 12 troupes nécessaires à une capture.

## Révision des confrontations de chevaliers

Dans une tuile, les chevaliers se neutralisent mutuellement par mêlées chromatiques :

- Chaque mêlée regroupe automatiquement le maximum de couleurs distinctes et non répétées de chevaliers d'une tuile.
- La couleur bloquante d'une tuile est celle du chevalier hors d'une mêlée (sachant qu'il faut être au moins deux pour faire une mêlée !)

Pour une partie à 2 joueurs, rien n'est changé. 

Mais les parties à 3 et 4 joueurs sommes impactées. Par exemple, dans une tuile, 2 ou 3 chevaliers adverses de couleurs distincts se neutralisent tous seuls sans nécessiter de chevaliers alliés, et adjoindre 2 chevaliers alliés a pour effet, que le premier chevalier se joint à la mêlée et que le second, hors de la mêlée, bloque la tuile pour les ordres aux troupes des adversaires.

## Révision du blocage par les troupes

Dans les règles anciennes, la présence de troupes adverses sur une case de commandement bloque le recrutement et la déconstruction. Dans les nouvelles règles, il y a obligation de "combo forcé" : recrutement en 1ère action + attaque sans déplacement (qui n'existe pas autre part dans le gameplay).

Analysons les conséquences d'une suppression de ces deux blocages.

Conséquence pour la **déconstruction** : 

- Puisqu'un donjon existe sur la tuile de commandement, cela implique qu'au plus 2 troupes adverses sont présentes, sinon le donjon serait automatiquement détruit. Donner la possibilité de déconstruire, donc de convertir le donjon en 3 troupes, impliquerait de faire combattre immédiatement ces troupes troupes contre les 2 troupes adverses, avec un résultat net d'envoyer 3 troupes adverses à la défausse et de renvoyer 3 troupes alliées à la réserve. 
- Jugement : 
  - Du point de vue du thème, les troupes défendant le donjon sont prêtes à sacrifier le donjon pour un bénéfice au combat ; 
  - Au plus ce mécanisme cause une perte de 2 troupes adverses ; ce n'est pas un levier si énorme que ça.
  - Cela évite une règle d'interdiction, et procure plus de flexibilité. Les joueurs devraient apprécier.

Conséquence pour le **recrutement** :

- Cela permet une forme d'auto-défense de la tuile de commandement lorsque le tuile de commandement est de type "donjon + chevalier" ; la menace étant la destruction du donjon. Cela implique que l'attaque d'un donjon doit engager directement au moins 3 troupes adverses, plutôt que d'envoyer 2 troupes dans un premier tour, puis 1 troupe fatale dans un second tour. C'est en général un engagement en 1 tour qui est pratiqué. Donc l'auto-défense de la tuile "donjon + chevalier" ne devrait être utilisée que marginalement.
- S'agissant de la libération du recrutement pour la tuile de commandement de type "baron", les conséquences sont différentes. En effet, le baron n'a pas à se défendre en soi, puisqu'il ne peut pas être pris. L'auto-défense, cependant, se conçoit pour une configuration "baron + donjon", dans laquelle le baron défend le donjon qu'il occupe en recrutant des troupes. Donc, là aussi l'auto-défense se justifie, et se n'est pas trop gênant, dans la mesure où, en pratique, la destruction de donjon se fait par engagement direct d'au moins 3 troupes adverses en un seule tour.
- Parlons maintenant d'une conséquence offensive par recrutement du baron. La tactique offensive du baron serait : déplacer le baron sur une tuile contenant des troupes adverses et recruter pour les attaquer. Un déplacement de 1 case rend possible l'utilisation du bonus pour recruter, donc en 1 tour, cela rend possible une attaque de troupes adverses (bonus 5 ou 6). Un déplacement par "chevauchée éclair" + usage du bonus permet là-encore une destruction de 3 troupes lointaines. Sinon, l'usage du bonus pour le déplacement permet l'attaque d'une troupe adverse distance de 3 tuiles.
- Jugement :
  - Cela simplifie les règles en supprimant des conditions d'interdiction.
  - Cela ouvre des combos intéressant.
  - A voir si les tests ne révèlent pas une trop grande puissance de ce mécanisme.
