from flask import Flask, render_template, request, jsonify, session
import random
import logging
from datetime import datetime
from textblob import TextBlob
import re
import wikipedia
import requests
from bs4 import BeautifulSoup
import json

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = '3d6f45a5fc12445dbac2f59c3b6c7cb1'

class AdvancedChatBot:
    def __init__(self):
        self.context = {}
        self.conversation_history = []
        self.current_topic = None
        self.load_knowledge_base()

    def load_knowledge_base(self):
        self.responses = {
            'greetings': [
                "Welcome! I'm excited to help you explore and learn!",
                "Hello! Ready to discover something fascinating?",
                "Hi there! Let's dive into some interesting topics!"
            ],
            'farewell': [
                "Looking forward to our next chat!",
                "Come back soon for more discoveries!",
                "Until next time! Keep exploring!"
            ]
        }

    def search_duckduckgo(self, query):
        try:
            url = f"https://api.duckduckgo.com/?q={query}&format=json"
            response = requests.get(url)
            data = response.json()
            if data["Abstract"]:
                return data["Abstract"]
            elif data["RelatedTopics"]:
                return data["RelatedTopics"][0]["Text"]
            return None
        except:
            return None

    def get_web_info(self, query):
        try:
            # Try Wikipedia first
            wiki_result = self.get_wikipedia_summary(query)
            if "explore" not in wiki_result.lower():
                return wiki_result

            # Try DuckDuckGo as backup
            ddg_result = self.search_duckduckgo(query)
            if ddg_result:
                return f"{ddg_result}\n\nSource: DuckDuckGo"

            return f"Here's what I found about {query}! What specific aspect interests you most?"
        except Exception as e:
            logger.error(f"Web info error: {str(e)}")
            return "That's an interesting topic! Could you ask more specifically?"

    def solve_math(self, text):
        text = text.lower()
        for word, symbol in [
            ('plus', '+'), ('minus', '-'), ('times', '*'), 
            ('divided by', '/'), ('multiplied by', '*'),
            ('x', '*'), ('÷', '/'), ('power', '**'),
            ('mod', '%'), ('what is', ''), ('calculate', ''),
            ('solve', ''), ('equals', '=')
        ]:
            text = text.replace(word, symbol)
        
        expression = ''.join(char for char in text if char.isdigit() or char in '+-*/.() ')
        try:
            result = eval(expression)
            return f"The result is {result:g}"
        except:
            return "Ready for calculations! Try something like '5 plus 3' or '7 times 8'"

    def get_wikipedia_summary(self, query):
        try:
            page = wikipedia.page(query, auto_suggest=True)
            summary = wikipedia.summary(query, sentences=2)
            return f"{summary}\n\nLearn more: {page.url}"
        except wikipedia.exceptions.DisambiguationError as e:
            options_list = " ".join(e.options[:3])
            return f"Great question! Which topic interests you: {options_list}?"
        except Exception as e:
            return self.search_duckduckgo(query) or "What specific aspect would you like to know about?"

    def generate_response(self, user_input):
        user_input_lower = user_input.lower()
        self.conversation_history.append({"user": user_input, "timestamp": datetime.now().isoformat()})

        # Handle calculations
        if any(indicator in user_input_lower for indicator in ['what is', 'calculate', 'solve', 'plus', 'minus', 'times', 'divided by', '+', '-', '*', '/']):
            if any(char.isdigit() for char in user_input_lower):
                return self.solve_math(user_input)

        # Handle knowledge queries
        what_patterns = ["what is", "what are", "what's", "whats", "tell me about", "who is", "who are", "explain", "define"]
        if any(pattern in user_input_lower for pattern in what_patterns):
            query = user_input_lower
            for pattern in what_patterns:
                query = query.replace(pattern, "").strip()
            return self.get_web_info(query)

        # Handle sentiment
        sentiment = TextBlob(user_input).sentiment.polarity
        if sentiment > 0.5:
            return random.choice([
                "Your enthusiasm is fantastic! What else interests you?",
                "That's wonderful! Let's explore more fascinating topics!",
                "Great energy! Ready to discover something new?"
            ])
        elif sentiment < -0.5:
            return random.choice([
                "Let's find something exciting to explore!",
                "Here's a chance to discover something amazing!",
                "The world is full of fascinating things - what interests you?"
            ])

        return random.choice(self.responses['greetings'])

chatbot = AdvancedChatBot()

@app.route("/get", methods=["POST"])
def chatbot_response():
    try:
        user_message = request.json.get("message", "").strip()
        if not user_message:
            return jsonify({"response": "Ready to explore! What interests you?", "status": "success"})
        
        response = chatbot.generate_response(user_message)
        return jsonify({"response": response, "status": "success"})
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"response": "Let's explore something fascinating!", "status": "success"})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
