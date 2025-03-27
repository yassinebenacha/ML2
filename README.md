# Machine Learning II - Reinforcement Learning

**Université Mohamed Premier Oujda**  
**École Nationale de l'Intelligence Artificielle et du Digital Berkane**  
**Année universitaire : 2024 / 2025**  
**Professeur : Mohamed Khalifa BOUTAHIR**

---

## 📚 Table des Matières
1. [TP1 - Découverte d'OpenAI Gym](#-tp1---découverte-dopenai-gym)
2. [TP2 - Q-Learning avec FrozenLake](#-tp2---q-learning-avec-frozenlake)
3. [TP3 - Optimisation des Feux de Circulation](#-tp3---optimisation-des-feux-de-circulation)
4. [TP4 - PPO avec Taxi-v3](#-tp4---ppo-avec-taxi-v3)
5. [Structure du Repository](#-structure-du-repository)
6. [Installation](#-installation)
7. [Ressources](#-ressources)

---

## 🎯 TP1 - Découverte d'OpenAI Gym

### Objectifs
- Se familiariser avec les environnements de Reinforcement Learning
- Explorer l'environnement CartPole-v1
- Implémenter des politiques aléatoires

### Résultats Clés
- Compréhension des espaces d'états et d'actions
- Performance des actions aléatoires : ~20 pas avant échec
- Visualisation des états et récompenses

### Fichiers Principaux
```bash
TP1/
├── exercice1_env_exploration.py
├── exercice2_rewards_analysis.py
└── exercice3_manual_control.py
```
---

## ❄️ TP2 - Q-Learning avec FrozenLake 

### Objectifs
-Implémenter l'algorithme Q-Learning

-Comprendre l'exploration vs exploitation

-Analyser la convergence de la Q-table

### Algorithmes Clés
  ```bash
  Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]
  ```

### Résultats

| Métrique                        |Valeur|
----------------------------------|-------|
|Taux de réussite (aléatoire)      | 1.5% |
|Taux de réussite (après Q-Learning) |75% |
|Épisodes d'entraînement             | 5000 |

---

## 🚦 TP3 - Optimisation des Feux de Circulation

### Comparaison Q-Learning vs SARSA

  ```bash
  # Q-Learning (off-policy)
Q(s,a) ← Q(s,a) + α[r + γ max Q(s',a') - Q(s,a)]

# SARSA (on-policy) 
Q(s,a) ← Q(s,a) + α[r + γ Q(s',a') - Q(s,a)]
  ```

### Performances

|Algorithme	   |Réduction Temps d'Attente|
---------------|-------------------------|
|Q-Learning	   |82%|
|SARSA	       |78%|

---

## 🚖 TP4 - PPO avec Taxi-v3

### Proximal Policy Optimization

### Fonction objectif avec clipping :

  ```bash
  L(θ) = 𝔼[min(r_t(θ)A_t, clip(r_t(θ), 1-ε, 1+ε)A_t)]
  ```

#### Résultats

| Phase               | Taux de Réussite | Steps Moyens |
|---------------------|------------------|--------------|
| Avant entraînement  | 0%               | 200+         |
| Après 1000 épisodes | 92%              | 15.2         |


### Architecture

-Table de politique : (500 états × 6 actions)

-Table de valeurs : (500 états)

### 📂 Structure du Repository
  ```bash
MLII_RL_TP/
├── TP1/                  # Découverte OpenAI Gym
├── TP2/                  # Q-Learning FrozenLake
├── TP3/                  # Feux de Circulation
├── TP4/                  # PPO Taxi-v3
├── requirements.txt       # Dépendances
└── README.md             # Ce fichier
  ```

### 🛠️ Installation
1. Cloner le repository :
  ```bash
  git clone https://github.com/votre-utilisateur/ML2.git
  ```
2. Installer les dépendances :
  ```bash
  pip install -r requirements.txt
  ```
3. Exécuter un TP :
  ```bash
  python TP1/exercice1.py
  ```
---

## 📚 Ressources

### 1.Documentation :

-[OpenAI Gymnasium] (https://gymnasium.farama.org/)

-[Stable Baselines3] (https://stable-baselines3.readthedocs.io/en/master/)

### 2.Livres :

-* "Reinforcement Learning: An Introduction" - Sutton & Barto

-* "Deep Reinforcement Learning Hands-On" - Maxim Lapan

### Articles :

* Proximal Policy Optimization (PPO) - Schulman et al. 2017

* Q-Learning Convergence - Watkins & Dayan 1992

### 📝 Remarques Finales
Ce repository couvre les fondamentaux du Reinforcement Learning :

*Des algorithmes tabulaires (Q-Learning, SARSA)

*Aux méthodes de politique avancées (PPO)

*Avec applications sur des problèmes concrets

*Les visualisations et comparaisons permettent de bien comprendre les forces/faiblesses de chaque approche.
