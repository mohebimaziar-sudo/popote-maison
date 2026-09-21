# App Repas et Courses — cahier des charges

Dernière mise à jour : 2026-09-21

## Objectif
Organiser la semaine, cuisiner en avance pour congeler (gain de temps),
et surtout maîtriser le budget alimentaire de la maison.

## Utilisateurs
Toute la famille, sur téléphone. Un seul lien partagé, données communes en direct.

## Écrans

### 1. Menu de la semaine (cœur de l'app)
- Une ligne par repas : jour + déjeuner / dîner
- Nombre de personnes par repas
- Choix d'une recette du carnet
- Bouton « Générer les courses »
- Marquage « à congeler » pour les plats cuisinés en avance (à préciser)

### 2. Recette
- Nom, nombre de personnes de base, temps
- Ingrédients avec quantités (recalculées selon le nombre de personnes du menu)
- Étapes
- Améliorations : plus tard

### 3. Liste de courses
- Générée à partir du menu, quantités additionnées
- Chaque article : « déjà à la maison » (exclu du total) ou « à acheter »
- Coché au magasin
- « Autres achats » : tout ce qui n'est pas dans une recette (lessive, papier toilette,
  croquettes…), ajouté à la main ; l'app mémorise les habitués et les propose en un tap
- Rayons ajoutés : Entretien et hygiène, Maison et divers
- Bouton « € » sur chaque article de la liste pour noter son prix (enseigne, quantité, date) :
  tout article de course, recette ou non, entre dans le suivi des prix

### 4. Carnet de prix et budget (version 2)
- Chaque ingrédient a un prix par enseigne, saisi à la main au départ
- Coût calculé par recette et pour la semaine
- Poser un budget pour la semaine : l'app ne propose que des combinaisons
  de plats qui tiennent dedans, en privilégiant les plats à congeler
- Comparaison entre enseignes : laquelle revient le moins cher pour la liste
- Photo du ticket de caisse (fait le 2026-09-21) : Claude lit les articles, quantités, prix,
  enseigne, date et total ; l'utilisateur vérifie dans un tableau puis enregistre ;
  les articles reconnus sont cochés dans la liste de la semaine
- Chaque ticket est gardé (date, enseigne, total, nb d'articles) : dépenses du mois affichées
- L'analyse passe par le compte Claude de la personne qui ouvre la page (autorisation
  demandée la première fois) ; hors application Claude, la saisie à la main reste disponible

### 5. Suivi de l'évolution des prix (version 2)
- Chaque saisie de prix est datée et rattachée à une enseigne : on garde tout l'historique
- Par produit : courbe du prix dans le temps, par enseigne
- Vue d'ensemble : ce qui a augmenté ou baissé depuis le mois dernier
- Alerte quand un produit courant a nettement augmenté
- Source des données : les prix saisis à la main, puis les tickets de caisse

## Pays et enseignes
- France, prix en euros
- Enseignes : Carrefour, Auchan, Leclerc, Monoprix, marché, supérette
- Fonction « regrouper » : à partir de la liste et des prix connus, l'app répartit
  les articles entre les enseignes (où acheter quoi pour payer le moins) et affiche
  aussi une vue consolidée, tous magasins confondus, avec le total
- Option « tout dans un seul magasin » pour comparer le coût du trajet unique

## Points ouverts
- Aucun pour l'instant

## Décisions
- 2026-09-21 (après-midi) : l'app doit être indépendante de Claude, installable sur le téléphone
  comme une vraie app. Choix : application web installable (PWA) hébergée sur une adresse à nous.
  Le fichier `app/popote.html` reste la source ; `python build.py` produit le dossier `site/`
  (index.html, manifest, service worker, icônes) prêt à déployer.
- Étapes pour l'indépendance complète :
  1. Hébergement : FAIT le 2026-09-21. Dépôt GitHub mohebimaziar-sudo/popote-maison
     (public : le code est visible, pas les données), GitHub Pages sur main, dossier /docs.
     Adresse de l'app : https://mohebimaziar-sudo.github.io/popote-maison/
     Mise à jour : modifier app/popote.html, `python build.py`, commit, `git push`.
  2. Données partagées famille : base en ligne gratuite (Supabase) : compte à créer par Maziar
  3. Lecture de ticket : petite fonction serveur qui appelle un service d'analyse d'image
     (clé API à payer à l'usage, quelques centimes par ticket)
  4. Facultatif plus tard : publication sur App Store / Play Store (comptes développeur payants)
- Technique : page web unique (HTML, sans serveur), fichier `app/popote.html`
- Version 1 publiée le 2026-09-21 : https://claude.ai/artifact/Jt5tu42P1vb9Ar4V1uXtMt
  Les données restent sur l'appareil qui ouvre la page (pas encore partagées entre téléphones)
- Contrainte découverte : la base partagée des artefacts Claude n'est ouverte qu'aux membres
  de l'organisation Claude du propriétaire, donc pas à la famille. Le partage familial
  passera par un hébergement à part (version 2), qui demandera de créer un compte gratuit
- Pas de connexion aux sites des enseignes (aucun accès officiel, aspiration fragile et interdite) :
  les prix viennent des saisies et des tickets de caisse
- Version 1 = carnet de recettes + menu + liste de courses. Prix, budget et suivi en version 2.
- Dès la version 1, chaque prix saisi est daté et conservé, pour que le suivi ait déjà des données
