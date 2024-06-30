# Compilateur C

Un compilateur est un programme qui convertie le code source d'un langage dans un autre langage (Généralement en langage machine). Cette transformation permet l'éxécution du programme compilé sur un ordinateur.

Cette compilation ce découpe en plusieurs étapes. 

## Étape 1: Le Lexing
Le lexing est une méthode qui permet de décomposer le code source en tokens (">", "if", "else", etc). Il va permettre principalement de définir les mots clés du langage.


## Étape 2: Le Parsing
Le parsing est une technique qui permet la detection grammaticale du langage, elle va utilisers les tokens précédemment récuperer et vérifier la syntaxe du langage.


## Etape3: l'analyse sémantique

L'analyse sémantique est un mécanisme qui va vérifier la cohérence du code source. Une variable ne peux pas être utilisé si elle n'est pas déclaré. L'objectif est de détecter d'éventuelle incohérence dans le code.

## Étape 4: Génération du code

A cette étape, on va générer le code machine compatible. Cela va permettre d'éxécuté en envoyant les instruction au processeurs notre programme. Un if va devenir un (CMP, JNE) par example.

## Étape 5: Optimisation
La dernière étape consiste à optimiser les ressources utilisé par le programme compilé, par exemple il n'y a pas besoin de prendre un QWORD (64 bits)  pour écrire un caractère (8 bits).

# Auteurs
Yohann MALEY, Samuel NUEZ, Florent LEBORGNE
