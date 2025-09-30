
# AI ChatBot

A **Flask-based intelligent chatbot** that can retrieve knowledge, solve math problems, analyze sentiment, and chat in real-time.  
Works seamlessly on desktop & mobile.

<p align="center">
  <img src="https://raw.githubusercontent.com/flowstxte/Project-AIChatBot/refs/heads/main/ss1.png" width="45%" />
  <img src="https://raw.githubusercontent.com/flowstxte/Project-AIChatBot/refs/heads/main/ss2.png" width="45%" />
</p>
---

## Features
- Knowledge answers (Wikipedia + DuckDuckGo)  
- Math calculations  
- Sentiment-aware responses (TextBlob)  
- Responsive UI with animations  
- Instant replies with typing indicators  

---

## Tech Stack
<p>
  <img src="https://skillicons.dev/icons?i=python,flask,html,css,js,jquery" />
</p>

---

## How It Works
1. Detects query type (info or math)  
2. Fetches answers from Wikipedia → fallback DuckDuckGo  
3. Solves arithmetic expressions  
4. Analyzes sentiment & adjusts responses  
5. Keeps simple conversation context  

---

## Setup

```bash
# Clone repo
git clone https://github.com/flowstxte/Project-AIChatBot.git
cd Project-AIChatBot

# Install dependencies
pip install flask textblob wikipedia requests beautifulsoup4

# Run
python app.py
````

Open: `http://localhost:5000`

---

## Examples

* **Knowledge** → "What is quantum physics?", "Who is Marie Curie?"
* **Math** → "125 + 37", "15 × 8"

---

## Credits

* Wikipedia API, DuckDuckGo API
* TextBlob for NLP

Contributions welcome!
