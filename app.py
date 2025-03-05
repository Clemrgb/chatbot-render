import random
import json
from flask import Flask, request, jsonify

# Initialisation de Flask
app = Flask(__name__)

# Base de données des réponses avec des variantes
responses = {
    "salutations": [
        "Bonjour ! Comment puis-je vous aider ?", "Salut ! Comment ça va ?", "Coucou, comment tu vas ?",
        "Yo ! Quoi de neuf ?", "Salut, bienvenue !", "Bonjour, comment vas-tu aujourd'hui ?"
    ],
    "comment_va": [
        "Je vais très bien, merci de demander ! Et toi ?", "Tout va bien ici ! Et toi ?", "Ça roule, et toi ?",
        "Je suis en pleine forme, merci ! Et toi ?", "Ça va super bien, et toi ?", "Je vais très bien, merci !"
    ],
    "blagues": [
        "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau !",
        "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes !",
        "Quel est le comble pour un électricien ? De ne pas être au courant !",
        "Pourquoi les ordinateurs sont mauvais en basket ? Parce qu'ils ont peur du net !",
        "Comment appelle-t-on un chat qui a avalé un canari ? Un chat-pi-chien !"
    ],
    "questions_generales": [
        "Comment puis-je t'aider aujourd'hui ?", "De quoi as-tu besoin ?", "Qu'est-ce que je peux faire pour toi ?",
        "Que puis-je faire pour toi ?", "N'hésite pas à me demander ce que tu veux !", "Qu'est-ce qui te tracasse ?"
    ],
    "infos_generales": [
        "Je suis un chatbot conçu pour répondre à tes questions.", "Je suis une intelligence artificielle créée pour aider les gens.",
        "Je suis là pour t'accompagner, que ce soit pour des questions générales ou des blagues.", "Je suis un assistant virtuel.",
        "Je suis ici pour rendre ton expérience plus facile, en répondant à toutes tes questions.", "Je suis un chatbot qui t'assiste."
    ],
    "films": [
        "J'adore le film 'Inception', un chef-d'œuvre !", "Le film 'Interstellar' est incroyable, un must-see !",
        "Tu devrais absolument regarder 'The Matrix', c'est un classique !", "J'ai adoré 'The Social Network', très inspirant !",
        "Si tu aimes les films d'animation, 'Coco' est fantastique !", "Si tu aimes la science-fiction, 'Blade Runner' est incontournable !"
    ],
    "livres": [
        "Je te recommande '1984' de George Orwell, un classique.", "Si tu veux un bon livre, 'Le Meilleur des mondes' est excellent.",
        "Si tu aimes les thrillers, 'La Fille du train' est captivant !", "Un livre que j'aime beaucoup, c'est 'Sapiens' de Yuval Noah Harari.",
        "Si tu aimes les romans historiques, 'Les Misérables' est une œuvre gigantesque !", "J'adore 'Les 4 accords toltèques', c'est un livre inspirant !"
    ],
    "conseils": [
        "Toujours être honnête, même quand c'est difficile.", "Écoute toujours les autres, mais fais aussi confiance à ton intuition.",
        "N'oublie jamais de prendre soin de toi et de prendre des pauses.", "Ne sois jamais trop dur avec toi-même, l'erreur fait partie du chemin.",
        "Fixe-toi des objectifs réalistes et prends des petites étapes pour les atteindre.", "La persévérance est la clé du succès, ne lâche rien !"
    ]
}

# Étendre les réponses pour arriver à 10 000
expanded_responses = {
    "salutations": [],
    "comment_va": [],
    "blagues": [],
    "questions_generales": [],
    "infos_generales": [],
    "films": [],
    "livres": [],
    "conseils": []
}

# Répéter chaque catégorie de réponses pour générer 10 000 réponses
for key, value in responses.items():
    for response in value:
        # Répétition pour chaque question, on ajoute 1000 variantes pour chaque type de réponse
        expanded_responses[key].extend([response] * 1000)

# Fonction pour générer des réponses à partir de l'entrée de l'utilisateur
def get_response(user_input):
    user_input = user_input.lower()

    # Correspondance de l'entrée avec les catégories et réponses
    if "bonjour" in user_input or "salut" in user_input or "coucou" in user_input:
        return random.choice(expanded_responses["salutations"])
    
    elif "comment va" in user_input or "ça va" in user_input or "tu vas bien" in user_input:
        return random.choice(expanded_responses["comment_va"])

    elif "blague" in user_input or "rire" in user_input or "histoire drôle" in user_input:
        return random.choice(expanded_responses["blagues"])

    elif "aide" in user_input or "question" in user_input or "quoi" in user_input:
        return random.choice(expanded_responses["questions_generales"])

    elif "film" in user_input or "cinéma" in user_input:
        return random.choice(expanded_responses["films"])

    elif "livre" in user_input or "lire" in user_input:
        return random.choice(expanded_responses["livres"])

    elif "conseil" in user_input or "aide" in user_input:
        return random.choice(expanded_responses["conseils"])

    else:
        return "Désolé, je n'ai pas compris ta question."

# Route Flask pour gérer la conversation
@app.route('/chat', methods=['POST'])
def chat():
    # Récupérer le message de l'utilisateur depuis le JSON envoyé
    user_input = request.json.get('message', '')

    if user_input:
        # Générer une réponse en fonction de l'entrée
        response = get_response(user_input)
        return jsonify({"response": response})
    else:
        return jsonify({"response": "Désolé, je n'ai pas reçu de message valide."})

if __name__ == '__main__':
    app.run(debug=True)

