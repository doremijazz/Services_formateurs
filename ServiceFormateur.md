# Projet application web django/aws ServiceFormateur

## Création du projet

1. Création du dossier dans le répertoire utilisatuer
2. Créartion de l'environement virtuel et activation
3. Installation de Django
4. création et ajout du fichier .gitignore
5. Intialisation du projet avec git
6. Création du répertoire github
7. Liaison dépot local et distant


## Implémentation des models 

### 19/11/2026 :
---------
Choix d'utiliser `models.IntegerChoices` pour les status et les types. J'ai aussi pris bien soint de mettre les clés étrangéres.

|Relation | Code|
|---|---|
|Un à plusieurs (1,N)	|ForeignKey|
|Un à un (1,1) |	OneToOneField|
|Plusieurs à plusieurs (N,N)	|ManyToManyField |

19/11/2026 : Les méthodes compléxes non pas encore été développées

### / / :

## Implémentation du formulaire de demande

### 19/11/2026 :







































## Sources

### Source pour le calendrier Django

#### Installer et afficher le calendrier

- [Documentation FullCalendar](https://fullcalendar.io/docs)
- [Mettre FullCalendar dans le HTML](https://fullcalendar.io/docs/initialize-globals)
- [Exemple de calendrier](https://fullcalendar.io/demos)

#### Modifier l'affichage du calendrier

- [Afficher les semaine et les heures](https://fullcalendar.io/docs/timegrid-view)
- [Afficher le mois](https://fullcalendar.io/docs/daygrid-view)
- [Les bouton pour changer de semaine ou de mois](https://fullcalendar.io/docs/headerToolbar)
- [Mettre le calendrier en français](https://fullcalendar.io/docs/locale)
- [Choisir les heures afficher](https://fullcalendar.io/docs/slotMinTime)

#### Afficher les réservation

- [Comment sont fait les evenement](https://fullcalendar.io/docs/event-object)
- [Récupérer les réservation avec du JSON](https://fullcalendar.io/docs/events-json-feed)
- [Format des date et heures](https://fullcalendar.io/docs/date-parsing)
- [Changer la couleur des evenement](https://fullcalendar.io/docs/eventColor)

#### Autre tuto

- [Tuto Django avec FullCalendar](https://tutorial101.blogspot.com/2022/05/python-django-ajax-fullcalender-crud.html)
- [Documentation FullCalendar version 6](https://legacy.fullcalendar.io/v6/)
