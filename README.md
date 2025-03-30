# Project-AIChatBot

A web-based intelligent chatbot application built with Flask that provides knowledge retrieval and calculation capabilities.

## Features
- **Knowledge Retrieval**: Answers questions about various topics using Wikipedia and DuckDuckGo.
- **Mathematical Calculations**: Solves basic arithmetic operations.
- **Natural Language Processing**: Analyzes sentiment and responds accordingly.
- **Responsive Design**: Works seamlessly on both desktop and mobile devices.
- **Real-time Interaction**: Provides immediate responses with typing indicators.

## Technical Stack
- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript (jQuery)
- **NLP Processing**: TextBlob for sentiment analysis
- **Knowledge Sources**: Wikipedia API and DuckDuckGo API
- **Styling**: CSS with animations and responsive design

## How It Works
The AI ChatBot uses a combination of techniques to understand and respond to user queries:

1. **Query Classification**: Identifies if the user is asking a knowledge question or requesting a calculation.
2. **Knowledge Retrieval**: For informational queries, it searches Wikipedia first, then falls back to DuckDuckGo.
3. **Mathematical Processing**: Parses and evaluates mathematical expressions.
4. **Sentiment Analysis**: Detects the emotional tone of messages and responds appropriately.
5. **Context Management**: Maintains conversation history for more coherent interactions.

## Usage Examples
### Knowledge Queries
- "What is quantum physics?"
- "Tell me about the Eiffel Tower"
- "Who is Marie Curie?"

### Mathematical Operations
- "What is 125 + 37?"
- "Calculate 15 times 8"
- "Solve 144 divided by 12"

## Installation

### Clone the repository:
```bash
git clone https://github.com/flowstxte/ai-chatbot.git
```

### Navigate to the project directory:
```bash
cd ai-chatbot
```

### Install the required dependencies:
```bash
pip install flask textblob wikipedia requests beautifulsoup4
```

### Run the application:
```bash
python app.py
```

### Open your browser and navigate to:
```
http://localhost:5000
```

## Future Enhancements
- Voice input and output capabilities
- Integration with more knowledge sources
- Support for more complex mathematical operations
- User authentication and personalized responses
- Multi-language support

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- **Wikipedia API** for knowledge retrieval
- **DuckDuckGo API** for supplementary information
- **TextBlob** for natural language processing capabilities

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or feature requests.
