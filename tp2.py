# -*- coding: utf-8 -*-
"""TP2 ML2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12URRtLSsNX18gsoJRVVkaNE1V4eDSMYG
"""

import gymnasium as gym
env = gym.make("CartPole-v1", render_mode="human")
env.reset()

print (f"Espace d'actions: {env.action_space}")
print (f"Espace d'observations {env.observation_space}")

for _ in range (100):
  action = env.action_space.sample()

  observation, reward, done,_,_ = env.step(action)

  print (f"Action: {action}, Observation: {observation}, Reward :{reward}")

  if done:
    env.reset()

env.close()

#Exe2
import gymnasium as gym

# Création de l'environnement
env = gym.make("CartPole-v1", render_mode="human")

# Réinitialisation de l'environnement
observation, info = env.reset()

# Exécuter une action et observer les valeurs retournées
action = env.action_space.sample()  # Choix d'une action aléatoire
observation, reward, terminated, truncated, info = env.step(action)

# Affichage des résultats
print(f"Action choisie : {action}")
print(f"Observation reçue : {observation}")
print(f"Récompense obtenue : {reward}")
print(f"L'épisode est-il terminé ? {'Oui' if terminated or truncated else 'Non'}")

# Fermer l'environnement
env.close()

#Exe3
import gymnasium as gym
import numpy as np

#maximiser la récompense totale accumulée à long terme

# L'équation complète du Q-learning est :

# Q(s, a) = Q(s, a) + alpha [ R + gamma max Q(s', a') - Q(s, a)]

# Hyperparamètres
alpha = 0.1  # Taux d'apprentissage
gamma = 0.99  # Facteur de réduction (discount factor)
epsilon = 0.1  # Facteur d'exploration epsilon-greedy

# Création de l'environnement
env = gym.make("CartPole-v1")
state, info = env.reset()

# Discrétisation de l'état (si nécessaire)
def discretize(state):
    return tuple(np.digitize(s, bins=np.linspace(-2.4, 2.4, 10)) for s in state)

# Initialisation de la table Q
q_table = {}

# Boucle d'épisodes
for episode in range(100):  # Nombre d'épisodes
    state, _ = env.reset()
    state = discretize(state)

    episode_length = 0

    while True:
        # Choisir une action avec epsilon-greedy
        if np.random.rand() < epsilon:  # Exploration
            action = np.random.choice([0, 1])
        else:  # Exploitation
            action = np.argmax(q_table.get(state, [0, 0]))  # Par défaut [0, 0]

        # Appliquer l'action et récupérer les nouvelles valeurs
        next_state, reward, terminated, truncated, _ = env.step(action)
        next_state = discretize(next_state)

        # Initialiser la table Q pour les nouveaux états
        if state not in q_table:
            q_table[state] = [0, 0]
        if next_state not in q_table:
            q_table[next_state] = [0, 0]

        # Mise à jour de Q(s, a)
        best_next_action = np.argmax(q_table[next_state])
        q_table[state][action] += alpha * (reward + gamma * q_table[next_state][best_next_action] - q_table[state][action])

        # Mise à jour de l'état
        state = next_state
        episode_length += 1

        # Vérifier si l'épisode est terminé
        if terminated or truncated:
            print(f"Épisode {episode} terminé en {episode_length} étapes.")
            break

# Fermer l'environnement
env.close()

#EXe4
import gymnasium as gym
import numpy as np

# Création de l'environnement
env = gym.make("CartPole-v1")

num_episodes = 10  # Nombre d'épisodes à exécuter
episode_durations = []  # Liste pour stocker les durées

for episode in range(num_episodes):
    observation, info = env.reset()
    episode_length = 0

    while True:
        action = env.action_space.sample()  # Action aléatoire
        observation, reward, terminated, truncated, info = env.step(action)
        episode_length += 1

        if terminated or truncated:
            break

    episode_durations.append(episode_length)
    print(f"Épisode {episode + 1} terminé en {episode_length} étapes.")

# Calcul de la durée moyenne des épisodes
average_duration = np.mean(episode_durations)
print(f"Durée moyenne des épisodes : {average_duration:.2f} étapes.")

# Fermer l'environnement
env.close()