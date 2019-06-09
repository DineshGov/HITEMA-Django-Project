# hitema-django-project
Projet développé dans le cadre de l'évaluation du module Django par Dinesh GOVINDARADJANE.

L'application permet d'intéragir avec trois modèles:
  -Sport
  -Équipe
  -Joueur
  
Une équipe pratique un seul et unique sport.
Un sport peut être pratiqué par plusieurs équipes.

Une équipe est composée de joueurs, elle est initialement vide.
Un joueurs peut être affecté à une ou plusieurs équipe. Il peut ne pas avoir d'équipe.

L'accès à l'application se fait via l'url: http://127.0.0.1:8000
Elle redirige vers http://127.0.0.1:8000/academy/ qui est la page d'accueil du site. Il est donc aussi possible d'y accèder via cette URL.

Les modèles ont toutes les fonctions CRUD. Les URLS sont similaires pour chaque modèles:

http://127.0.0.1:8000/academy/<NOM_MODELE>s/
permet de lister toutes les entités du modèle.

http://127.0.0.1:8000/academy/create/<NOM_MODELE>/
permet de créer une entité du modèle.

http://127.0.0.1:8000/academy/read/<NOM_MODELE>/<INT>/
permet d'afficher les détails d'une entité.

http://127.0.0.1:8000/academy/update/<NOM_MODELE>/<INT>/
permet de mettre à jour une entité.

http://127.0.0.1:8000/academy/delete/<NOM_MODELE>/<INT>/
permet de supprimer une entité.
