# Plan - Flashbac A18 - NLP

* Mise en contexte

* Pourquoi le NLU?
* China room
* Turing test
* Représentation des mots (ascii, bag of words, word embeddings)
    - Représentation des caractères en mémoire (ASCII, UTF-8)
    - Représentation one-hot d'un mot
    - Bag-of-words
    - Limitations : tous les mots sont indépendants les uns des autres!
    - word embeddings (CBOW, Skip-Gram)
* Introduction rapide aux réseaux de neurones
    - MLP
        + Apprentissage supervisé
        + Modèles linéaires
        + Ajout d'une couche
        + Backprop
    - RNN
    - Modèles séquence à séquence
        + beaucoup d'applications en NLP (Q&A, NMT, Conversational agents)
* Tâches en NLU (Question answering, Machine translation, chatbots, ...)
    - Sentiment Analysis
        + Review de films (positif ou négatif)
    - Modèles de langue
    - Traduction automatique
    - Question Réponse
        + IBM Watson à Jeopardy
    - Résumés automatiques de texte
    - Agents conversationnels
        + Test de Turing
        + Exemples
* Librairies python pour le NLP et le deep learning
    - PyTorch, Tensorflow
    - OpenNMT-py
    - NLTK, spaCy
    - 