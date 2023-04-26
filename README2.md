<<<<<<< HEAD
# INSEE DB 
## Configuration de la base de données
Dans [le fichier tools/db.py] (./tools/db.py), modifiez (DBNAME, USERNAME, PASS) dans votre base de données et ajoutez-la à [.gitignore](.gitignore)
## Sources des fichiers csv à télécharger
* region.csv , departement.csv, commune.scv [https://www.insee.fr/fr/information/6800675]
* dossier_complet.csv, [https://www.insee.fr/fr/statistiques/5359146]

##  Ou mettre les fichier csv dans le projet
* Ajoutez dossier_complet.csv dans [./csv/](./csv/)
>
* Ajoutez region.csv, departement.csv et commune.scv(comune.csv) [./csv/fill/](./csv/fill/) Et tous les fichier population et naissance se trouve dans [./csv/fill/pop](./csv/fill/pop) et [./csv/fill/naiss](./csv/fill/naiss)
## Generer les fichier dont on a bésoin pour l'application
* > $ cd tools
* > $ python3 generateCsv.py
## Lancement du programme
* > python3 main.py
*  Une fois fois que cette commande executé vous n'avez plus bésoin de l'exécuter à nouveau donc vous commenter la fonction (insertAll(conn , cur)) sur [./main.py](./main.py) dans main.py

*  et une fois cette commande lancer, on aura un menu qui va s'afficher pour permettre à l'utilisateur de voir c'est ce qu'il souhaite.

## Dans le dossier sql
* > Dans ce on a 5 fichier notes.sql et tables.sql qu'on trouve ici: [./sql/](./sql/) 
* Dans tables.sql on a toutes les tables crées ainsi que quleques insertions et aussi quelques requêtes simples
* Dans notes.sql on a la table statistique crée avec ses contraintes.

## Dans le dossier tools
* > Dans ce dossier on a 5 fichiers python db.py, display.py, generateCsv.py et insert.py qu'on trouve ici : [./tools/](./tools/)

    ## Dans db.py
    * C'est ici qu'on a définit les fonctions à la base de données
    * connexion, 
    * execution des requêtes, 
    * selection et affichage des requêtes notament avec des differentes couleurs pour une meilleur visibilité, 
    * créer une liste à partir de la demande du client,
    * Une requête pour créer une vue de région,
    * Une requête pour obtenir la plus petite région,
    * Une requête obtenir le département d'une région donnée,
    * Une requête pour créer une vue de département,
    * Une requête pour obtenir Commune d'un département donné,
    * Une requête pour obtenir le plus petit département.

    ## Dans display.py
    * Là c'est vraiment pour l'affichage de notre interface avec des actions(choix) que le client peut voir et consulter qu'il soit plus facile, lisible avec des couleurs différentes.

    ## Dans generateCsv.py
    * Tout d'abord les fichiers de population et naissance se trove dans csv/fill comme indiquer au dessus, donc on a mis les deux chemins dans 2 variables
      * la première variable contient le chemin ou se trouve le dossier_complet: ***DATA_PATH = '../csv/dossier_complet.csv'***
      * et la deuxième variable contient tout simplement le chemin dans le quel on place les fichiers de population et naissance générer ***FILL_PATH = '../csv/fill'***
      * Donc si vous voulais placer ces fichier à part que dans le chemin indiqué, vous avez juste à modifier le chemin dans ses 2 variables

    ## Dans insert.py
    * C'est ici qu'on a vraiment mis en ouevre pour générer des differentes fichiers population et naissance qu'on utliseras ensuite pour les statistiques.

## Dans le dossier note
* On retrouve ici le model relationnel du rendu précedent

    ## Dans request.py
    * Ici on effectue des fonctions qui permettent de faire des insertions sur la base de donnée avec les fichiers csv déjà disponible dans le dossier csv
=======
<h1>
INSEEDB app with python: 
</h1>

![home1](./images/icon.png)

## What is This

---

This is a Python application that maid to creat and manage [**INSEE**](https://www.insee.fr/fr/information/6800675) databases using ([psycopg2](https://www.psycopg.org/docs/index.html)).

## 🚀 Installation

Clone this repository by running this line :

```console
~$ git clone https://github.com/NiNejah/INSEEDB.git
```


## 📗 Usage
1. Go to [db config](./tools/dbConfig.py) and change it to your own values.

## RUN 
```console
~$ python3 main.py
```

**Important:** 
In [main.py](./main.py) 
*  uncomment this line if you don't have already all the tables **creatDB(conn,cur)** 
   (all the tables creation are in [tables](./sql/tables.sql))
*  comment this line after the first execution  **insertAll(conn , cur)**


## demostation :

![home1](./images/demo.gif)

I have already all the tables that's why we see the Warning message to comment  **insertAll(conn , cur)** 



### info 
* all the fill files in [./csv](./csv/) gentated by a python script from [dossier_complet.csv](https://www.insee.fr/fr/statistiques/6456192) and from [Official geographic code ](https://www.insee.fr/fr/information/6800675)

 
>>>>>>> 8129d5159614c9832fde2ed95a8c2e679190597a
