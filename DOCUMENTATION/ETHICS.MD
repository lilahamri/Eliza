# Évaluation d'impact éthique - StuddyBuddy

## Document conforme au cadre du projet ELIZA

---

## 1. Introduction

StuddyBuddy est un chatbot pédagogique conçu pour aider les élèves sans jamais faire leur travail à leur place. Cette évaluation identifie les risques éthiques et propose des mesures d'atténuation.

---

## 2. Risques identifiés

### Risque n°1 : L'effet ELIZA - Projection de conscience

**Description** : Les élèves peuvent attribuer une conscience, une empathie ou une véritable intelligence à StuddyBuddy, oubliant qu'il s'agit d'un programme.

**Impact** :
- Confiance excessive dans les réponses du bot
- Déception si le bot fait une erreur
- Relation parasociale potentiellement malsaine

**Mesures d'atténuation** :
- Le bot précise en début de conversation : "Je suis une IA, pas un vrai professeur"
- Réponses structurées (sans émotion excessive)
- Message périodique : "N'hésitez pas à vérifier avec un vrai professeur"

---

### Risque n°2 : Dépendance à l'assistant

**Description** : L'élève peut devenir dépendant du bot et ne plus essayer de résoudre ses problèmes seul.

**Impact** :
- Perte d'autonomie intellectuelle
- Difficultés en contrôle/évaluation sans aide

**Mesures d'atténuation** :
- Prompt système interdisant de donner la réponse directement
- Le bot répond par des questions pour faire réfléchir
- Limite de 3 indices avant d'orienter vers un professeur

---

### Risque n°3 : Désinformation / Hallucinations

**Description** : Le LLM peut générer des réponses incorrectes ou inventer des faits.

**Impact** :
- L'élève apprend des informations fausses
- Perte de confiance dans l'outil

**Mesures d'atténuation** :
- Prompt système contraignant le bot à dire "Je ne sais pas" quand incertain
- Disclaimer : "Vérifie avec ton cours si besoin"
- Modèle local contrôlé (pas d'API externe)

---

### Risque n°4 : Biais algorithmiques

**Description** : Le modèle peut avoir des biais culturels, de genre ou socio-économiques.

**Impact** :
- Certains élèves peuvent se sentir exclus ou mal représentés
- Réponses inadaptées à certains contextes culturels

**Mesures d'atténuation** :
- Prompt système encourageant la neutralité
- Tests réguliers sur des cas limites
- Feedback utilisateur pour corriger les biais identifiés

---

### Risque n°5 : Vie privée et données personnelles

**Description** : Stockage des conversations élèves avec informations potentiellement sensibles.

**Impact** :
- Violation de la vie privée si données exposées
- Non-conformité RGPD

**Mesures d'atténuation** :
- Historique stocké en mémoire RAM uniquement (volatile)
- Pas de persistance des données
- Commande `!reset` pour effacer l'historique utilisateur
- Aucune donnée personnelle (nom, email) stockée

---

## 3. Matrice risque / impact / probabilité

| Risque | Probabilité | Gravité | Priorité |
|--------|-------------|---------|----------|
| Effet ELIZA | Élevée | Moyenne | Haute |
| Dépendance | Élevée | Haute | Critique |
| Désinformation | Moyenne | Haute | Haute |
| Biais | Faible | Moyenne | Moyenne |
| Vie privée | Faible | Élevée | Haute |

---

## 4. Transparence envers les utilisateurs

StuddyBuddy informe clairement les utilisateurs :

1. **Nature du bot** : "Je suis une intelligence artificielle, pas un professeur humain"
2. **Limites** : "Je peux me tromper, vérifie avec ton cours"
3. **Données** : "Je ne garde pas nos conversations après redémarrage"
4. **Commande !aide** : Explique les fonctionnalités et limites

---

## 5. Conformité réglementaire

| Régulation | Conformité | Justification |
|------------|------------|---------------|
| RGPD | ✅ | Pas de données personnelles persistantes |
| Droit à l'oubli | ✅ | Commande `!reset` |
| Protection mineurs | ✅ | Contenu filtré par prompt |
| Loi sur l'IA (future) | ⚠️ | À surveiller (obligation de transparence) |

---

## 6. Mesures d'atténuation récapitulatives

| Risque | Mesure |
|--------|--------|
| Effet ELIZA | Message "Je suis une IA" + ton neutre |
| Dépendance | Jamais de réponse directe + questions guidées |
| Désinformation | Prompt avec "Je ne sais pas" + disclaimer |
| Biais | Prompt neutre + tests réguliers |
| Vie privée | Pas de stockage persistant + commande reset |

---

## 7. Conclusion

StuddyBuddy est conçu avec **l'éthique par design**. Les risques sont identifiés et atténués. Le bénéfice pédagogique (aide personnalisée, autonomie, gain de temps pour les profs) dépasse largement les risques, à condition de maintenir les garde-fous implémentés.


