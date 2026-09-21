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
- Choix d'une recette pour un repas (2026-09-21, demande de Maziar : filtrer d'abord, intégrer
  ensuite) : le repas ouvre un sélecteur avec la même recherche et les mêmes filtres que le
  carnet ; on filtre, on tape le plat, il est placé. Depuis le carnet filtré, « Mettre au menu »
  sur une recette demande le repas (jour + déjeuner/dîner, les libres en premier), le nombre
  de personnes et la case congélateur
- Bouton « Générer les courses »
- « Proposer une semaine » (2026-09-21) : remplit les repas vides avec des plats variés
  (pas deux fois la même catégorie de suite, au moins un végétarien), pour N personnes,
  en respectant un budget si on en donne un ; option « privilégier les plats à congeler »
  (portions doublées, marquées congélateur)
- Coût de la semaine affiché en haut (avec tes prix, sinon indicatif)
- Marquage « à congeler » pour les plats cuisinés en avance (à préciser)

### 2. Recette
- Vue par défaut de l'onglet (2026-09-21, demande de Maziar) : « Cette semaine », les recettes
  complètes des plats choisis dans le menu, dans l'ordre des repas, quantités ajustées au
  nombre de personnes, avec coût et boutons « Cuisiné », « Changer le repas », « Fiche ».
  « Tout le carnet » (recherche, filtres, 52 plats) reste à un tap. Si rien n'est planifié,
  l'onglet s'ouvre directement sur le carnet
- Catalogue de départ (2026-09-21) : 52 plats familiaux (classiques français + plats persans),
  chacun avec ingrédients pour N personnes, temps, catégorie, étiquettes et coût indicatif
- Recherche par nom ou ingrédient
- Filtres combinables (2026-09-21, demande de Maziar) : pays de cuisine (française, italienne,
  persane, asiatique, indienne, maghreb, orientale, mexicaine, américaine), protéine (bœuf, veau,
  agneau, volaille, porc, poisson, œufs, végétarien), type de plat, temps (≤ 20 / 21-45 / > 45 min),
  saison (été / hiver), pratique (rapide, à congeler, pas cher, enfants, au four, sans porc),
  origine (mes recettes / catalogue). OU à l'intérieur d'un groupe, ET entre les groupes ;
  chaque option affiche le nombre de plats qu'elle donnerait
- « Sans porc » se déduit des ingrédients (lardons, jambon, saucisse… comptent comme porc)
- « Proposer une semaine » peut se limiter aux plats du filtre actif
- « Rapide » (≤ 25 min) et « pas cher » (≤ 2 €/pers.) se déduisent automatiquement
- Coût d'une recette (règle du 2026-09-21, demande de Maziar) : un produit acheté sert de
  référence à tous les plats qui l'utilisent, au prorata de la quantité (300 g de riz = 30 %
  du sac de 1 kg). Prix de référence = moyenne du dernier prix relevé dans chaque enseigne.
  Les ingrédients sans prix restent sur l'estimation indicative, au prorata de leur part.
  Affichage : « avec tes prix » quand tout est connu, « n/N prix à toi » en cours de route,
  « indicatif » sinon. La fiche recette montre le montant vert de chaque ingrédient connu.
- Saison : l'app connaît la saison en cours (avril-septembre = printemps-été, sinon
  automne-hiver). Pastille « De saison » dans le carnet ; « Proposer une semaine » écarte
  les plats de la saison opposée et privilégie ceux de la saison en cours (coché par défaut)
- Déroulé détaillé (2026-09-21, demande de Maziar : « recettes trop bâclées ») : chaque plat du
  catalogue a 5 à 7 étapes précises avec temps, températures, repères de cuisson et astuces
  (repos, congélation). Les quantités ajustées sont arrondies façon cuisine (330 g, 1,5 oignon,
  1 pincée), jamais 333,33 g
- Ordre des onglets : Semaine, Courses, Recettes, Prix, Stock (Recettes après Courses)
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

### 3 bis. Stock de la maison (fait le 2026-09-21)
- Entrées : un article coché « dans le panier » au magasin entre dans le stock avec sa quantité ;
  un ticket enregistré ajoute ce qui a été acheté (quantité du ticket)
- Sorties : sur un repas de la semaine, « Cuisiné » retire les ingrédients au prorata des
  personnes (seulement ce qui est en stock) ; les portions mises au congélateur deviennent
  un « plat prêt » dans le stock
- « Proposer une semaine » place d'abord les plats prêts du congélateur (déjà payés)
- La liste de courses ne propose que ce qui manque : un article couvert par le stock passe en
  « déjà à la maison (en stock) », un article partiellement couvert voit sa quantité réduite
- Onglet Stock : frigo, congélateur, placard ; ajout et correction à la main ; date limite
  facultative avec alerte « à consommer vite » (3 jours)
- Règle de conception : tout s'accroche à des gestes déjà faits (cocher, enregistrer un ticket,
  cuisiner) pour que le stock ne dérive pas ; la correction manuelle reste à un tap

### Catalogue sans porc (2026-09-21, demande de Maziar)
- Plus aucun plat à base de porc dans le catalogue. Retirés : côtes de porc, sauté de porc,
  rôti de porc, quiche lorraine. Adaptés : bourguignon sans lardons, riz cantonais au poulet,
  gratin de pâtes au poulet, tomates farcies au bœuf, pizza aux poivrons, crêpes et
  croque-monsieur au jambon de dinde. Remplaçants : escalopes de poulet et pommes sautées,
  sauté de poulet au caramel, rôti de dinde aux carottes, quiche aux poireaux
- Le jambon de dinde ou de poulet ne compte pas comme porc pour le filtre « sans porc »
- Une recette du catalogue modifiée par l'utilisateur devient « mes recettes » et n'est plus
  resynchronisée par les mises à jour du catalogue

### À faire : filtres régime (demande du 2026-09-21)
- Souhait : sans glucides / pauvre en glucides, calories contrôlées, hyperprotéiné, sans farine
  (sans gluten), sans produit industriel, ingrédients controversés
- Approche prévue : table nutritionnelle intégrée des ingrédients courants (kcal, protéines,
  glucides pour 100 g) pour calculer par portion ; détection par mots-clés pour « sans
  farine », « sans produit industriel » ; liste des ingrédients controversés à définir avec Maziar

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
