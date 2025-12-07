# TWISTS-5

## Introduction

Ce mémo recueille une nouvelle vague d'idées de "twists".

## Nouvelles mécaniques

### Recrutement d'un troisième chevalier

En plus des deux chevaliers mis en place en début de partie, le joueur peut mettre en œuvre le recrutement d'un troisième chevalier :

- Le prix à payer est un **dé** de bonus de valeur **6** et la défausse de **2 cartes tactiques**.
- Le chevalier recruté est placé sur la tuile du baron ou sur une tuile avec un donjon allié.
- Cette manœuvre compte comme une action d'officier. 

### Cités et ville

Cette mécanique permet d'augmenter les points d'une tuile sur laquelle un donjon est construit.

Après la mise en place des montagnes, une carte tactique est piochée et retournée ; sa lettre et sa position sont exploitée :

- **Cité marchande** : sa **lettre** indique les tuiles qui bénéficient de **2 points supplémentaires** lorsqu'un donjon y est construit.
- **Ville franche** : sa **position** indique la tuile qui bénéficie de **4 points supplémentaires** lorsqu'un donjon y est construit.

La ville franche n'est pas compté comme "cité marchande".

Cette mécanique place sur le "marché" 4 + 2 + 2 + 2 = 10 points supplémentaires à partager entre les joueurs.

## Révision des points de défi

Compte tenu des remarques des joueurs qui trouvent les parties de "Terre de Barons" pas assez longues, et sachant que les simulations Python ne prennent pas en compte les affrontements, ni les points supplémentaires pour diversité (ni les suppléments de points pour cités marchandes et ville franche), envisageons d'augmenter les points de défi. Pour cela, la simulation est passée de 1_000 à 10_000 parties, et du joueur classé en meilleur position, ce sont ses quantiles 75% qui seront retenus, plutôt que ses quantiles 25%. Cela donne :
- **19 points** à 2 joueurs (soit +3 points)
- **14 points** à 3 joueurs (soit +2 points);
- **12 points** à 4 joueurs (soit +2 points).

