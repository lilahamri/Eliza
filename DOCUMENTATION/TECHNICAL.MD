# Documentation technique - StuddyBuddy

## Architecture détaillée

### Structure du projet
studdybuddy/
├── bot.py # Point d'entrée principal
├── config.py # Configuration (URL, tokens)
├── prompts.py # Prompts pour élève et professeur
├── roles.py # Gestion des rôles Discord
├── history.py # Gestion de l'historique
├── ollama_client.py # Appel HTTP à Ollama
├── discord_bot.py # Événements et commandes Discord
├── requirements.txt # Dépendances Python
└── .env # Variables d'environnement

### Flux de données
[Message Discord]
│
▼
[discord_bot.py - on_message()]
│
├── Commande (!aide, !reset, etc.) → réponse directe
│
└── Message normal
│
▼
[lm_client.py - ask_lm_studio()]
│
├── Récupère historique user
├── Ajoute question
├── Appel HTTP à LM Studio (POST /v1/chat/completions)
├── Sauvegarde réponse
└── Retourne réponse
│
▼
[Discord - envoi de la réponse]

---

## Système de réponse

### Prompt système (dans `prompts.py`)

Deux prompts distincts selon le rôle :

**STUDENT_SYSTEM_PROMPT** : Pour les élèves
- Interdit de donner la réponse directement
- Guide par des questions et indices
- Refuse poliment les demandes de réponse directe
- Refuse les questions non scolaires (cuisine, météo, etc.)

**TEACHER_SYSTEM_PROMPT** : Pour les professeurs
- Donne des réponses complètes et détaillées
- Explique la méthodologie pas à pas
- Propose des exercices corrigés pour les élèves

### Appel à LM Studio

```python
def ask_lm_studio(user_id: int, question: str, is_teacher_mode: bool) -> str:
    url = f"{LM_STUDIO_URL}/v1/chat/completions"
    payload = {
        "model": "local-model",
        "messages": history_dict[user_id],
        "temperature": 0.7,
        "max_tokens": max_tokens,
    }
    response = requests.post(url, json=payload, timeout=60)
    return response.json()["choices"][0]["message"]["content"]


Gestion de l'historique

L'historique est stocké dans des dictionnaires séparés pour élèves et professeurs :

student_conversation_history: dict[int, list[dict]] = {}
teacher_conversation_history: dict[int, list[dict]] = {}

Chaque entrée contient :

    user_id : ID Discord de l'utilisateur

    messages : Liste des messages (système, user, assistant)

Commande !reset : Supprime l'historique d'un utilisateur.

Gestion des rôles

Les professeurs sont détectés automatiquement via leurs rôles Discord :

TEACHER_ROLES = ["professeur", "profeseur", "teacher", "prof", "admin", "administrateur", "staff"]

def is_teacher(member) -> bool:
    for role in member.roles:
        if role.name.lower() in TEACHER_ROLES:
            return True
    return False

Commandes admin :

    !addrole <nom> : Ajoute un rôle à la liste

    !removerole <nom> : Retire un rôle de la liste

    !listroles : Liste tous les rôles professeurs



git clone https://github.com/yourusername/studdybuddy.git
cd studdybuddy

python -m venv venv
source venv/bin/activate  

pip install -r requirements.txt

echo "TOKEN=votre_token_discord" > .env

python bot.py