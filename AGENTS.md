# Présentation du projet

Le but est de répartir les services (levé, midi, veillée) entre tous les formateurs
pour une année scolaire

Le logiciel permet a la personne responsable des plannings de repartir les services tout
en gardant la main pour signifier au logiciel une indisponibilité d'un formateur, 
ou encore l'arrivée ou le départ d'un formateur. Avoir un contrôle du nombre de services
programmer par personne. Mais aussi d'exclure des semaines de la plannification comme 
par exemple pour les vacances qui bouges chaque année.


## Objectif actuel

- Pouvoir intégrer les initiales des formateurs et en supprimer
- Intégrer des demandes :
    - une demande de service X que les (jours précis)
    - une demande de service X pas les (jours précis)
- Possible d’exclure des semaines dans la planification pour certains
formateurs
- Possible de saisir les dates de vacances 
- Entrer le nombre de services total et le nombre de service à faire par
personne
- Avoir un contrôle du nombre de services programmer par personne


## Contraintes algotihmique

- 2 services par personnes par semaines max : 1 midi, 1 veillée
- Impossible de faire 2 services la même journée
- Equilibrer le nombre de service par période (vacances à vacances)

## Technologies utilisées

- Python 3.14
- CSV
- Tkinter
- etc au besoin

## Structure du projet


## Conventions de programmation

- Respecter la norme PEP 8 pour Python.
- Utiliser des noms de variables explicites en anglais.
- Utiliser `snake_case` pour les fonctions et variables.
- Utiliser `PascalCase` pour les classes.
- Ajouter des annotations de type aux nouvelles fonctions.
- Limiter chaque fonction à une responsabilité.
- Éviter la duplication de code.
- Ne pas utiliser de variable globale sans nécessité.
- Documenter les fonctions publiques.

## Format des docstrings

Utiliser le format suivant :

```python
def factorisation(n, nombres_premiers):
    """
    Calcule les facteurs premiers d’un nombre.

    : parameter
        n: nombre à factoriser
        nombres_premiers: liste des nombres premiers disponibles

    : type
        n: int
        nombres_premiers: list[int]

    : return
        facteurs: liste des facteurs premiers

    : rtype
        list[int]
    """
```

## Git et commits

Utiliser des commits courts et explicites :

- `feat: ajoute la connexion des élèves`
- `fix: corrige le chargement des fichiers MusicXML`
- `test: ajoute les tests de l’analyse harmonique`
- `docs: complète la documentation d’installation`
- `refactor: sépare l’accès S3 de la logique métier`

Ne pas créer de commit sauf si l’utilisateur le demande.
Ne jamais utiliser `git push --force` sans autorisation.

## Contraintes technique

- Le projet doit fonctionner sous Windows 11.
- Le code doit rester compatible avec Python 3.11.
- L’application doit pouvoir être utilisée par des personnes non techniques.

## Définition de terminé

Une tâche est terminée lorsque :

- la fonctionnalité demandée fonctionne ;
- le code respecte les conventions du projet ;
- les erreurs importantes sont gérées ;
- les tests associés sont présents et réussissent ;
- la documentation est mise à jour si nécessaire ;
- aucune fonctionnalité existante n’est cassée ;
- Codex résume les fichiers modifiés et les vérifications réalisées.

## En cas de doute

Codex doit demander confirmation avant de :

- modifier l’architecture générale ;
- changer le format d’une base de données ;
- ajouter une dépendance de production ;
- supprimer une fonctionnalité ;
- modifier une API publique ;
- effectuer une opération Git destructive ;
- choisir entre plusieurs comportements métier possibles.


