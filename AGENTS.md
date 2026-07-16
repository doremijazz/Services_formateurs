# AGENTS.md

## Présentation du projet

Le projet consiste à répartir les services de levé, du midi et de veillée entre
les formateurs pour une année scolaire.

L’application est destinée à la personne responsable des plannings. Elle doit
permettre de générer une répartition équilibrée des services tout en laissant
la possibilité de modifier manuellement les contraintes.

La personne responsable doit notamment pouvoir :

- ajouter ou supprimer un formateur ;
- renseigner les indisponibilités des formateurs ;
- prendre en compte l’arrivée ou le départ d’un formateur en cours d’année ;
- saisir des préférences de jours et de services ;
- exclure certaines semaines de la planification ;
- saisir les périodes de vacances scolaires ;
- contrôler le nombre de services attribués à chaque formateur ;
- modifier manuellement un planning généré.

---

## Objectifs actuels

La première version de l’application doit permettre de :

- enregistrer les initiales des formateurs ;
- ajouter, modifier ou supprimer un formateur ;
- enregistrer la date d’arrivée d’un formateur ;
- enregistrer la date de départ d’un formateur ;
- saisir les dates de début et de fin de l’année scolaire ;
- saisir les périodes de vacances ;
- exclure certaines semaines de la planification ;
- exclure certaines semaines uniquement pour un formateur ;
- saisir les indisponibilités des formateurs ;
- saisir les préférences de service ;
- générer automatiquement un planning ;
- afficher le nombre de services attribués à chaque formateur ;
- contrôler l’équilibre de la répartition.

---

## Types de services

L’application doit gérer les services suivants :

- `morning` : service de levé ;
- `lunch` : service du midi ;
- `evening` : service de veillée.

Les identifiants internes sont écrits en anglais. Les intitulés affichés dans
l’interface sont écrits en français.

---

## Demandes et préférences

Pour chaque formateur, il doit être possible d’enregistrer les demandes
suivantes :

- souhaite effectuer un type de service certains jours ;
- ne souhaite pas effectuer un type de service certains jours ;
- est totalement indisponible certains jours ;
- est indisponible pendant une ou plusieurs semaines ;
- souhaite éviter certains services ;
- souhaite prioritairement effectuer certains services.

Exemples :

- souhaite faire les services du midi uniquement le lundi et le mardi ;
- ne souhaite pas faire de veillée le vendredi ;
- est indisponible pendant la semaine 42 ;
- ne peut effectuer aucun service le mercredi.

Une indisponibilité obligatoire doit être prioritaire sur une préférence.

---

## Règles métier obligatoires

Le planning généré doit respecter les règles suivantes :

- un formateur ne peut pas effectuer deux services le même jour ;
- un formateur peut effectuer au maximum deux services par semaine ;
- parmi ces deux services hebdomadaires, il ne peut pas avoir plus d’un service
  du midi et d’un service de veillée ;
- un service ne peut être attribué qu’à un formateur présent et disponible ;
- aucun service ne doit être créé pendant une semaine exclue ;
- un formateur ne doit recevoir aucun service avant sa date d’arrivée ;
- un formateur ne doit recevoir aucun service après sa date de départ ;
- les indisponibilités obligatoires doivent toujours être respectées ;
- les services doivent être répartis aussi équitablement que possible.

> La règle concernant le nombre maximal de services de levé par semaine doit
> être confirmée avant son implémentation.

---

## Équilibrage de la répartition

La répartition doit être équilibrée :

- sur l’ensemble de l’année scolaire ;
- pour chaque type de service ;
- pour chaque période comprise entre deux vacances ;
- en fonction de la période réelle de présence de chaque formateur.

Un formateur arrivé en cours d’année ne doit pas avoir le même objectif annuel
qu’un formateur présent toute l’année.

L’écart entre deux formateurs comparables doit être aussi faible que possible.

Les contraintes obligatoires sont prioritaires sur l’équilibrage.

Les préférences doivent être respectées autant que possible, mais elles ne
doivent pas rendre la génération du planning impossible.

---

## Priorité des contraintes

Les règles doivent être appliquées dans l’ordre suivant :

1. dates de présence du formateur ;
2. semaines et vacances exclues ;
3. indisponibilités obligatoires ;
4. impossibilité d’avoir deux services le même jour ;
5. nombre maximal de services par semaine ;
6. couverture de tous les services ;
7. équilibrage entre les formateurs ;
8. préférences personnelles.

Si toutes les contraintes ne peuvent pas être respectées, l’application doit
signaler clairement le problème au lieu de produire silencieusement un planning
incorrect.

---

## Données à gérer

### Formateur

Un formateur possède au minimum :

```python
trainer = {
    "id": str,
    "initials": str,
    "start_date": str | None,
    "end_date": str | None,
    "active": bool
}
```
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


