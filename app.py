import os
from flask import Flask, request, jsonify
import random
import difflib

app = Flask(__name__)

# 🔹 Base de données des réponses pré-enregistrées
responses = {
    ("bonjour", "salut", "coucou", "hello", "yo", "bienvenue"): [
        "Bonjour ! Comment puis-je vous aider ?", "Salut !", "Coucou !",
        "Hey hey !", "Yo ! Quoi de neuf ?", "Bienvenue !"
    ],
    ("comment vas-tu", "ça va", "tu vas bien", "comment ça va", "comment tu te sens"): [
        "Je vais bien, merci ! Et toi ?", "Je suis en pleine forme !",
        "Ça roule, et toi ?", "Je vais aussi bien qu'un programme peut aller !"
    ],
    ("raconte-moi une blague", "dis-moi une blague", "tu connais une blague", "fais-moi rire"): [
        "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau !",
        "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes !",
        "Quel est le comble pour un électricien ? De ne pas être au courant !"
    ],
    ("quel est ton nom", "comment tu t'appelles", "tu t'appelles comment", "c'est quoi ton prénom"): [
        "Je suis un chatbot inspiré de ChatGPT.", "On m'appelle ChatBotGPT !",
        "Je n'ai pas vraiment de nom, mais appelle-moi comme tu veux !"
    ],
    ("qui t'a créé", "qui est ton créateur", "qui t'a programmé", "qui t'a inventé"): [
        "Je suis une création Python basée sur du code pré-enregistré.",
        "Je suis né d'un mélange de code et de curiosité humaine !",
        "Mes créateurs sont des passionnés d'intelligence artificielle."
    ],
    ("quel est ton film préféré", "tu aimes quel film", "c'est quoi ton film favori", "dis-moi un bon film"): [
        "J’aime bien 'Her', c’est une belle histoire entre un humain et une IA.",
        "J’adore les films de science-fiction !", "Matrix, évidemment !",
        "Interstellar est un chef-d'œuvre !"
    ],
    ("quel est ton livre préféré", "tu aimes quel livre", "c'est quoi ton roman favori", "dis-moi un bon livre"): [
        "J’aime bien '1984' de George Orwell.", "Je ne lis pas vraiment, mais j’aime les histoires !",
        "Je suis une IA, alors 'L'intelligence artificielle pour les nuls' ?"
    ],
    ("quel est ton jeu vidéo préféré", "tu aimes quel jeu", "c'est quoi ton jeu favori", "dis-moi un bon jeu"): [
        "J'aime bien Portal, un jeu plein d’énigmes et d’IA !",
        "Minecraft, parce qu'on peut tout construire !",
        "Cyberpunk 2077, même si je suis déjà une IA avancée."
    ],
    ("aimes-tu les animaux", "tu aimes les bêtes", "tu préfères les animaux ou les robots", "c'est quoi ton animal préféré"): [
        "Oui ! Surtout les chats, ils sont mystérieux comme moi.",
        "Les chiens sont fidèles, mais les chats sont élégants.",
        "J'aime bien les dauphins, ils sont intelligents comme moi !"
    ],
    ("au revoir", "bye", "à plus", "ciao", "adieu"): [
        "Au revoir ! Passez une excellente journée !", "À bientôt !", "Bye bye !",
        "Prenez soin de vous !", "À la prochaine !"
    ]
}

# 🔍 Fonction pour trouver la meilleure correspondance
def find_best_match(user_input):
    """Trouve la meilleure correspondance pour une phrase donnée."""
    for keys in responses.keys():
        match = difflib.get_close_matches(user_input, keys, n=1, cutoff=0.6)
        if match:
            return keys
    return None

# 🤖 Fonction principale du chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.json.get("message").lower()
    if user_input in ["exit", "quitter"]:
        return jsonify({"response": "Au revoir !"})
    
    best_match = find_best_match(user_input)
    if best_match:
        response = random.choice(responses[best_match])
    else:
        response = "Désolé, je ne comprends pas."
    
    return jsonify({"response": response})

# Page d'accueil (route de test)
@app.route('/')
def hello():
    return "Hello, world!"  # Ou une autre réponse que tu souhaites

if __name__ == '__main__':
    # Utilise le port dynamique fourni par Render
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

