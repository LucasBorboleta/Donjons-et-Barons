# TWISTS-6

## Introduction

Ce mémo recueille une nouvelle vague d'idées de "twists".

## Nouvelles mécaniques

### Infortunes

Dépendant le **dé de bonus** et sur défausse de **1 carte tactique** :

- Dé 1 ou 2 => **Peste** dit aussi "**Malédiction Noire**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **troupes** sont envoyées en **défausse**.
- Dé 3 ou 4 => **Révolte** dit aussi "**Vent de Sédition**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **troupes** sont envoyées en **réserve**.
- Dé 5 ou 6 => **Séisme** dit aussi "**Le Courroux de la Terre**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **donjons** sont envoyées **détruits**.

Il y a 37 tuiles, dont 4 pour les montagnes; ce qui laisse 33 tuiles. Les simulations indiquent qu'en moyenne 10 donjons sont construits en fin de partie.

Si une position est tirée, alors la probabilité de toucher un donjon est 10/33 = 30%.

Si deux positions sont tirées, alors la probabilité de toucher au moins un donjon est 1 - 23x22/(33x32) = 52%.

Si trois positions sont tirées, alors la probabilité de toucher au moins un donjon est 1 - 23x22x21/(33x32x31) = 67.5%.

Dans le tour de jeu, le tirage d'une infortune :

- Nécessite d'utiliser le dé de bonus ET une défausse de carte tactique.
- Est jouée à la place d'une action d'officier.

## Révision de mécaniques existantes

### Recrutement sur un donjon adverse

Actuellement, la présence d'un donjon adverse dans une tuile de commandement empêche le recrutement. Cependant, la présence de troupes adverses n'empêche pas le recrutement, mais seulement oblige à un combo spécial/forcé "recrutement + attaque de troupes". Idem pour la déconstruction en présence de troupes adverses. Cette situation complique les règles par maque d'uniformité.

Il est donc suggéré de rendre **possible le recrutement en présence d'un donjon adverse**, avec un combo spécial/forcé "recrutement + attaque forcée". Si aucune "attaque forcée" (des éventuelles troupes adverses ou du donjon adverse) n'a lieu, alors une seconde action du joueur est possible.

Examinons divers cas particuliers :

- Présence d'un donjon adverse seul + dé de 6 qui recrute 3 troupes : le donjon adverse est détruit ; fin du tour
- Présence d'un donjon adverse et de 2 troupes adverses dans une tuile T1 + dé de 6 qui recrute 4 troupes : d'abord les 2 troupes adverses sont détruites, puis le donjon adverse est détruit ; fin du tour.
- Présence d'un donjon adverse seul + dé de 1 qui recrute 1 troupe : le donjon adverse n'est pas détruit ; une autre action est possible dans le tour.
