# StuddyBuddy - Chatbot Éducatif

**Plateforme :** Discord | **Langage :** Python 3.10+ | **LLM :** Ministral-3:3b (via LM Studio - 100% local)

---

## Présentation du projet

StuddyBuddy est un chatbot pédagogique conçu pour les collèges et lycées, intégré à Discord. Il aide les élèves à comprendre leurs cours plutôt qu'à obtenir des réponses toutes faites.

**Problématique :** Les élèves utilisent ChatGPT pour obtenir des réponses sans effort. Les professeurs manquent de temps pour répondre à toutes les questions.

**Solution :** StuddyBuddy guide l'élève vers la solution par des questions et des indices, sans jamais donner la réponse directement.

---

## Audience cible

| Type | Description |
|------|-------------|
| Élèves | Collège (6ème→3ème) et Lycée (2nde→Terminale) |
| Professeurs | Mode admin pour créer des évaluations |
| Établissements | Collèges et lycées cherchant une solution d'aide aux devoirs |

---

## Personas utilisateurs

| Persona | Profil | Besoin principal |
|---------|--------|------------------|
| Lucas | Élève de 3ème en difficulté | Aide immédiate sans jugement |
| Sophie | Professeure de maths débordée | Gagner du temps, suivre les élèves |
| Philippe | Principal de collège | Améliorer les résultats avec ROI prouvé |
| Marie | Investisseuse EdTech | Scalabilité et modèle rentable |

---

## Trois besoins réels identifiés

1. **Aide aux devoirs personnalisée** - Élèves bloquent sans accès immédiat à un professeur
2. **Préparation aux examens** - Besoin de générer des quiz adaptés au niveau
3. **Suivi pédagogique** - Visibilité sur les difficultés des élèves

---

## Objectifs du chatbot

- **Automatisation** - Répondre 24h/24 et 7j/7
- **Accompagnement** - Guider sans donner la réponse
- **Évaluation** - Générer des quiz via `!examen`
- **Suivi** - Mode admin pour recevoir les réponses

---

## Indicateurs clés de performance (KPIs)

| Indicateur | Cible | Justification |
|------------|-------|---------------|
| Temps de réponse moyen | 10-30 secondes | Modèle local (dépend machine) |
| Taux d'automatisation | 85% | Élèves résolvent seuls avec indices |
| Score de satisfaction | 4.5/5 | Feedback utilisateurs |
| Taux de complétion | 70% | Questions menées jusqu'à la solution |

---

## Accessibilité

L'accessibilité est prise en charge directement par Discord, ce qui rend le chatbot utilisable par des personnes sourdes, malentendantes, aveugles ou malvoyantes. Discord propose le sous-titrage automatique des messages vocaux, la compatibilité avec les synthèses vocales, les commandes clavier et les thèmes à fort contraste. Notre bot hérite donc de ces paramètres sans configuration additionnelle.

## Retour sur investissement (ROI) - Collège de 500 élèves

### Sans StuddyBuddy

| Poste | Coût annuel |
|-------|-------------|
| 20h/semaine × 35€ × 36 semaines | 25 200 € |
| Manuels de soutien (500 × 10€) | 5 000 € |
| Plateforme concurrente | 3 000 € |
| **Total** | **33 200 €** |

### Avec StuddyBuddy

| Poste | Coût annuel |
|-------|-------------|
| 5h/semaine × 35€ × 36 semaines | 6 300 € |
| Manuels de soutien réduits | 1 000 € |
| Hébergement (local) | 0 € |
| **Total** | **7 300 €** |

**Calcul :** 33 200 € - 7 300 € = 25 900 € économisés par an  
**ROI :** (25 900 / 7 300) × 100 = **355%**  
**Temps de retour :** Moins de 4 mois

---

## Chaîne de valeur

Élève pose une question → StuddyBuddy analyse → Réponse guidée → Élève progresse → Impact : meilleure compréhension, autonomie, gain de temps profs.

---

## Fonctionnalités et commandes

| Commande | Fonction | Public |
|----------|----------|--------|
| `!aide` | Affiche l'aide | Tout le monde |
| `!mode` | Affiche le mode (élève/professeur) | Tout le monde |
| `!reset` | Réinitialise la conversation | Tout le monde |
| `!roles` | Liste les rôles professeurs | Tout le monde |
| `!examen` | Génère un examen/quiz | Tout le monde |
| `!exercice` | Génère un exercice | Tout le monde |
| `!addrole` | Ajoute un rôle professeur | Admin serveur |
| `!removerole` | Retire un rôle professeur | Admin serveur |

**Mode professeur :** Détection automatique via le rôle Discord → réponses complètes et détaillées  
**Mode élève :** Réponses guidées avec questions et indices, jamais de solution directe

---

## Modèle économique

| Offre | Prix | Inclus |
|-------|------|--------|
| Gratuit | 0€ | Questions illimitées, toutes commandes, mode élève/professeur |
| Établissement (future) | 1 500-4 000€/an | Dashboard, support dédié, hébergement cloud |

**Projections :**
- Année 1 : 42 500 € CA, 38 680 € bénéfice
- Année 2 : 218 500 € CA, 187 880 € bénéfice
- Année 3 : 1 030 000 € CA, 947 880 € bénéfice

---

## Architecture technique

**Technologies :** Python 3.10+, discord.py, LM Studio, Ministral-3:3b, Requests

**Flux de données :** Message Discord → Bot → LM Studio (localhost:1234) → Réponse → Discord

**Pourquoi LM Studio plutôt qu'une API externe ?**

| Solution | Type | Coût | Conforme projet |
|----------|------|------|-----------------|
| ChatGPT API | Externe | Payant | ❌ Interdit |
| Mistral API | Externe | Payant | ❌ Interdit |
| **LM Studio** | **Local** | **Gratuit** | **✅ Autorisé** |

---

## Installation locale

### Prérequis
- Python 3.10+
- Token Discord Bot
- LM Studio installé
- 8 Go RAM minimum (16 Go recommandé)

### Étapes

```bash

git clone https://github.com/yourusername/studdybuddy.git
cd studdybuddy
python -m venv venv
source venv/bin/activate 
pip install -r requirements.txt
echo "TOKEN=votre_token_discord" > .env

python bot.py