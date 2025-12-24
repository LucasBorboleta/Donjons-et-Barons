# TWISTS-6

## Introduction

Ce mémo recueille une nouvelle vague d'idées de "twists".

## Nouvelle mécanique : Infortunes

Dans le tour de jeu, le tirage d'une infortune :

- Est jouée à la place d'une action d'officier.
- Nécessite d'utiliser le dé de bonus ET la défausse d'une carte tactique.

L'infortune est déterminé par le dé de bonus :

- Dé 1 ou 2 => **Peste** dit aussi "**Malédiction Noire**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **troupes** sont envoyées en **défausse**.
- Dé 3 ou 4 => **Révolte** dit aussi "**Vent de Sédition**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **troupes** sont envoyées en **réserve**.
- Dé 5 ou 6 => **Séisme** dit aussi "**Le Courroux de la Terre**" : Piocher 3 cartes tactiques dont les positions indiquent les tuiles dont les **donjons** sont envoyées **détruits**.

Discussion :

- Il y a 37 tuiles, dont 4 pour les montagnes; ce qui laisse 33 tuiles sélectionnables. Les simulations indiquent qu'en moyenne 10 donjons sont construits en fin de partie, et que par conséquent 23 tuiles ne sont pas des cibles. Typiquement, il y a donc 10 tuiles cibles parmi 33 tuiles sélectionnables.

- Si une position est tirée, alors la probabilité de toucher un donjon est 10/33 = 30%.

- Si deux positions sont tirées, alors la probabilité de toucher au moins un donjon est 1 - 23x22/(33x32) = 52%.

- Si trois positions sont tirées, alors la probabilité de toucher au moins un donjon est 1 - 23x22x21/(33x32x31) = 67.5%.

En fonction du nombre de tuiles cibles, le tableau suivant montre la probabilité de toucher au moins une tuile cible en tirant 3 cartes tactiques d'infortune. En fin de partie à 2 joueurs, si un des joueurs est sur le point de stopper la partie par pénurie de troupes et en même temps de gagner, alors ce joueur aurait typiquement 4 ou 5 tuiles à cibler. La probabilité de toucher une de ses tuiles cibles est alors entre 33% et 40%. C'est assez faible, mais pas trop. Par contre, dans ce genre de situation. Ce mécanisme ne serait en général pas suffisant pour renverser le cours de la partie.

Conclusion : oui, le matériel du jeu permettrait de mettre en place un mécanisme d'infortunes. Mais ce n'est pas l'esprit du jeu. Donc on garde cette idée est réserve pour l'instant.

| Tuiles  sélectionnables                          | 33   | 33   | 33   | 33   | 33   | 33   | 33   | 33   | 33   | 33   | 33   |
| ------------------------------------------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Tuiles cibles                                    | 10   | 9    | 8    | 7    | 6    | 5    | 4    | 3    | 2    | 1    | 0    |
| Tuiles hors  cibles                              | 23   | 24   | 25   | 26   | 27   | 28   | 29   | 30   | 31   | 32   | 33   |
| Probabilité de  toucher au moins une tuile cible | 68%  | 63%  | 58%  | 52%  | 46%  | 40%  | 33%  | 26%  | 18%  | 9%   | 0%   |

## Mécanique révisée : Recrutement sur donjon adverse

Actuellement, la présence d'un donjon adverse dans une tuile de commandement empêche le recrutement. Cependant, la présence de troupes adverses n'empêche pas le recrutement, mais seulement oblige à un combo spécial/forcé "recrutement + attaque de troupes". Idem pour la déconstruction en présence de troupes adverses. Cette situation complique les règles par maque d'uniformité.

Il est donc suggéré de rendre **possible le recrutement en présence d'un donjon adverse**, avec un combo spécial/forcé "recrutement + attaque forcée". Si aucune "attaque forcée" (des éventuelles troupes adverses ou du donjon adverse) n'a lieu, alors une seconde action du joueur est possible.

Examinons divers cas particuliers :

- Présence d'un donjon adverse seul + dé de 6 qui recrute 3 troupes : le donjon adverse est détruit ; fin du tour
- Présence d'un donjon adverse et de 2 troupes adverses dans une tuile T1 + dé de 6 qui recrute 4 troupes : d'abord les 2 troupes adverses sont détruites, puis le donjon adverse est détruit ; fin du tour.
- Présence d'un donjon adverse seul + dé de 1 qui recrute 1 troupe : le donjon adverse n'est pas détruit ; une autre action est possible dans le tour.
