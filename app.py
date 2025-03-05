from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de réponses pour le chatbot
responses = {
    "bonjour": "Salut, comment puis-je t'aider ?",
    "comment ça va": "Ça va bien, merci ! Et toi ?",
    "qui es-tu": "Je suis un chatbot simple, comment puis-je t'aider ?",
    "au revoir": "Au revoir et à bientôt !"
}

# Route pour le chatbot
@app.route('/chatbot', methods=['POST'])
def chatbot():
    # Récupérer les données JSON envoyées dans la requête
    user_message = request.get_json().get('message', '').lower()
    
    # Vérifier si le message existe dans notre base de données de réponses
    response = responses.get(user_message, "Désolé, je ne comprends pas cette question.")
    
    # Retourner la réponse sous forme de JSON
    return jsonify({"response": response})

if __name__ == '__main__':
    # Lancer l'application Flask
    app.run(debug=True, host="0.0.0.0", port=5000)

