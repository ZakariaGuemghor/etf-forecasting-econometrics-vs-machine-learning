![Image de couverture du projet](images/image_couverture.png)

# Prévision de la Performance des ETFs Sectoriels : Une Double Approche Machine Learning et Économétrique

## Introduction

La prévision de la performance des actifs financiers, et en particulier des ETFs sectoriels, est un exercice complexe qui se situe à l'intersection de l'analyse macroéconomique et de la modélisation statistique. Les mouvements de ces ETFs sont souvent influencés par des indicateurs économiques clés, mais leur dynamique temporelle présente également des caractéristiques (saisonnalité, volatilité changeante) qui peuvent être capturées par des modèles dédiés.

Ce projet propose une investigation comparative de la prévision de la performance d'un ETF sectoriel (Dans notre cas, on va se concentrer sur l'etf **XLI - Industrial Select Sector SPDR Fund**) en utilisant deux approches méthodologiques distinctes et complémentaires :
1.  **Une approche par Machine Learning (ML) :** axée sur la prédiction multivariée et autorégressive.
2.  **Une approche Économétrique :** fondée sur des modèles de séries temporelles classiques comme SARIMAX et GARCH-X.

L'objectif est d'évaluer les forces et les faiblesses de chaque méthode pour modéliser et anticiper les tendances et la volatilité de l'ETF en se basant sur un ensemble restreint d'indicateurs macroéconomiques.

---

## Objectif du Projet

L'objectif principal de ce projet est de construire, d'évaluer et de comparer deux pipelines de prévision distincts pour un ETF sectoriel. En utilisant les mêmes données d'entrée (prix de l'ETF et indicateurs macroéconomiques comme le PIB, l'inflation et les ventes au détail), nous cherchons à :
-   **Modéliser la trajectoire future du prix de l'ETF** en utilisant les deux approches.
-   **Quantifier l'incertitude et la volatilité** associées à ces prévisions.
-   **Comparer la performance et l'interprétabilité** des modèles issus du Machine Learning et de l'Économétrie.

Le projet vise à fournir un cadre d'analyse complet, de la collecte des données à la génération de prévisions et de simulations, illustrant comment différentes philosophies de modélisation peuvent être appliquées au même problème financier.

---

## Structure du Projet et Méthodologie

Le projet est organisé en deux notebooks Jupyter distincts, chacun représentant une approche de modélisation.

### 📂 `01_machine_learning_forecast.ipynb`

Ce notebook implémente un pipeline de prévision basé sur le Machine Learning. L'approche est multivariée : le modèle apprend à prédire simultanément l'ETF et les indicateurs macroéconomiques.

**Étapes clés :**
1.  **Collecte des Données :** Téléchargement des données mensuelles pour l'ETF (XLI) et les indicateurs macroéconomiques (PIB, Inflation, Ventes au Détail) depuis les APIs de Yahoo Finance et FRED.
2.  **Préparation et Ingénierie des Caractéristiques :**
    -   Synchronisation et nettoyage des séries temporelles.
    -   Normalisation des données (StandardScaler).
    -   Transformation des séries en séquences `(look_back)` pour l'apprentissage supervisé.
3.  **Optimisation et Entraînement du Modèle :**
    -   Recherche du meilleur ratio entraînement/test pour optimiser la performance prédictive (MSE).
    -   Entraînement d'un modèle de **Régression Bayésienne** pour prédire la valeur de chaque variable au pas de temps suivant, en se basant sur les valeurs passées de toutes les variables.
4.  **Génération de Prévisions Futures :**
    -   Mise en œuvre d'une boucle de prédiction autorégressive pour générer des prévisions sur un horizon de plusieurs mois. Le modèle utilise ses propres prédictions comme entrées pour les étapes suivantes.
5.  **Analyse des Résultats :**
    -   Visualisation des performances du modèle sur les ensembles d'entraînement et de test.
    -   Affichage du tableau des prévisions futures dé-normalisées.

### 📂 `02_econometric_forecasting_(sarimax_garchx).ipynb`

Ce notebook adopte une approche économétrique classique, en modélisant séparément la tendance (rendements) et la volatilité.

**Étapes clés :**
1.  **Collecte et Préparation des Données :** Mêmes sources que le notebook ML, avec un accent sur le calcul des rendements et de la volatilité historique.
2.  **Modélisation de la Tendance (SARIMAX) :**
    -   Recherche des meilleurs paramètres `(p,d,q)(P,D,Q)` pour un modèle **SARIMAX** via une validation croisée sur séries temporelles, en utilisant un indicateur macroéconomique comme variable exogène.
    -   Entraînement du meilleur modèle et analyse des prévisions sur l'ensemble de test.
    -   Génération des prévisions de rendements futurs.
3.  **Modélisation de la Volatilité (GARCH-X) :**
    -   Recherche des meilleurs ordres `(p,q)` pour un modèle **GARCH-X**, en utilisant également une variable exogène.
    -   Entraînement du meilleur modèle et génération des prévisions de volatilité future.
4.  **Synthèse et Simulation (Monte Carlo) :**
    -   Les prévisions de rendements (SARIMAX) sont converties en une trajectoire de prix.
    -   Les prévisions de volatilité (GARCH-X) sont utilisées comme mesure de l'incertitude.
    -   Une **simulation de Monte Carlo** est lancée pour générer de multiples trajectoires de prix possibles autour de la prévision centrale, fournissant une distribution des résultats potentiels.
5.  **Analyse des Résultats :**
    -   Visualisation des prévisions de rendements, de prix, et de volatilité.
    -   Affichage du "cône" des simulations de Monte Carlo.