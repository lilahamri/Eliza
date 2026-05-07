# Personas - StuddyBuddy

## Méthodologie

Trois personas représentant les trois cibles principales :
1. Élève (B2C)
2. Professeur (B2B)
3. Établissement / Décideur (B2B)
4. Investisseur / Chef de produit

---

## Persona 1 : Lucas - L'élève en difficulté

### Identité

| Attribut | Valeur |
|----------|--------|
| Nom | Lucas Martin |
| Âge | 14 ans |
| Classe | 3ème |
| Établissement | Collège Victor Hugo, Paris |
| Matières difficiles | Maths, Physique-Chimie |

### Comportement

- Passe 2 heures par jour sur Discord
- Bloque souvent sur les exercices à la maison
- Pose des questions sur des serveurs Discord mais se fait parfois troller
- A déjà utilisé ChatGPT mais a eu la réponse sans comprendre

### Besoins

1. Aide disponible immédiatement
2. Explications adaptées à son niveau de 3ème
3. Ne pas avoir honte de poser une question dite bête
4. Progresser par lui-même sans qu'on lui donne la solution

### Freins

- Peu d'argent de poche
- Manque de temps entre les devoirs

### Parcours utilisateur

Lucas bloque sur un exercice de maths. Il ouvre Discord. Il mentionne StuddyBuddy. Le bot le guide par questions. Lucas trouve la solution seul. Il comprend mieux qu'avec ChatGPT.

### Citation

> "J'ai peur de poser des questions en classe, les autres vont se moquer. Là sur Discord, personne ne me juge."

---

## Persona 2 : Madame Legrand - La professeure débordée

### Identité

| Attribut | Valeur |
|----------|--------|
| Nom | Sophie Legrand |
| Âge | 42 ans |
| Matière | Mathématiques |
| Établissement | Lycée Jean Renoir, Lyon |
| Expérience | 18 ans |

### Comportement

- Reçoit plus de 30 emails d'élèves par semaine disant "Je n'ai pas compris l'exercice 3"
- Consacre 5 heures par semaine à répondre individuellement
- Utilise Pronote mais trouve l'outil limité
- Épuisée par les mêmes questions redondantes

### Besoins

1. Gagner du temps sur les questions répétitives
2. Suivre les difficultés de ses élèves avec des statistiques par matière
3. Créer des évaluations personnalisées rapidement
4. Recevoir les réponses des élèves de façon structurée

### Freins

- Sécurité des données des mineurs
- Validation de la direction pour tout nouvel outil
- Manque de temps pour se former à un outil complexe

### Parcours utilisateur

Sophie donne un devoir maison pour vendredi. Dix élèves bloquent sur le même exercice. Elle crée une évaluation via la commande `!eval`. Les élèves répondent dans Discord. Elle reçoit toutes les réponses en CSV. Elle gagne 4 heures par semaine.

### Citation

> "Je n'ai pas le temps de répondre à chaque élève individuellement. Mais je ne veux pas non plus qu'ils se tournent vers ChatGPT pour avoir la réponse sans réfléchir."

---

## Persona 3 : Monsieur Dubois - Le chef d'établissement

### Identité

| Attribut | Valeur |
|----------|--------|
| Nom | Philippe Dubois |
| Âge | 54 ans |
| Poste | Principal du Collège Jean Moulin |
| Taille établissement | 650 élèves |
| Budget annuel innovation | 15 000 euros |

### Comportement

- Piloté par les indicateurs comme le taux de réussite au brevet et le climat scolaire
- Sensible au retour sur investissement et aux économies réalisables
- Très attentif à la conformité RGPD
- Ouvert aux innovations si elles sont prouvées et simples

### Besoins

1. Améliorer les résultats sans embaucher
2. Réduire les inégalités avec une aide accessible à tous
3. Solution simple à déployer sans former toute l'équipe
4. Rester dans le budget avec un maximum de 3000 euros par an

### Freins

- Risque de gaspillage budgétaire si l'outil n'est pas utilisé
- Responsabilité légale sur les données des mineurs
- Lenteur administrative avec validation par la mairie

### Parcours utilisateur

Monsieur Dubois cherche à améliorer le taux de réussite au brevet qui est actuellement de 82 pourcent. Il teste StuddyBuddy avec deux classes volontaires pendant un mois. Il constate une augmentation de 15 pourcent de l'autonomie et moins de demandes aux professeurs. Il décide un abonnement établissement à 2000 euros par an. Il déploie à tout le collège. Le taux de réussite passe à 89 pourcent en un an.

### Citation

> "Je n'ai pas 50 000 euros pour embaucher un prof de soutien. Si une solution numérique à 2000 euros par an peut m'aider à faire progresser mes élèves, je suis preneur."

---

## Persona 4 : Marie - La cheffe de produit investisseur

### Identité

| Attribut | Valeur |
|----------|--------|
| Nom | Marie Chen |
| Âge | 31 ans |
| Poste | Chef de Produit EdTech |
| Structure | Fonds d'investissement éducation |
| Objectif | Trouver des startups EdTech scalables |

### Comportement

- Analyse la taille du marché adressable
- Calcule la valeur vie client et le coût d'acquisition client
- Cherche un avantage concurrentiel durable
- Veut un produit qui passe à l'échelle

### Besoins pour investir

1. Modèle économique clair comme abonnement ou freemium
2. Traction avec nombre d'utilisateurs actifs et croissance
3. Différenciation par rapport à ChatGPT
4. Équipe capable d'exécuter

### Citation

> "Le marché de l'éducation en France c'est 12 millions d'élèves et 800 000 professeurs. Si tu captes ne serait-ce que 1 pourcent, c'est énorme."

---

## Synthèse des personas

| Persona | Rôle | Besoin principal | Budget max | Canal d'acquisition |
|---------|------|------------------|------------|---------------------|
| Lucas | Élève | Aide immédiate sans jugement | 5 euros par mois | Discord, TikTok |
| Sophie | Professeur | Gagner du temps, suivre les élèves | 10 euros par mois | Réseaux professeurs, ENT |
| Philippe | Principal | Améliorer les résultats, ROI prouvé | 2000 euros par an | Salons éducation |
| Marie | Investisseur | Scalabilité, modèle rentable | 100 000 euros ou plus | Pitch deck |

---

## Stratégie de priorisation

**Stratégie recommandée** : 
- Commencer par Lucas pour la validation B2C
- Puis Sophie pour l'upsell B2B
- Enfin Philippe et Marie pour le passage à l'échelle et l'investissement