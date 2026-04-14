
import re
import random
from datetime import datetime


RULES = [
    
    {
        "tag": "greeting",
        "patterns": [
            r"\b(hi|hello|hey|howdy|greetings|sup|yo|what'?s up)\b"
        ],
        "responses": [
            "Hey there! How can I help you today?",
            "Hello! Great to meet you. What's on your mind?",
            "Hi! I'm RuleBot. Ask me anything!"
        ]
    },

    
    {
        "tag": "farewell",
        "patterns": [
            r"\b(bye|goodbye|see you|cya|take care|farewell|quit|exit|later)\b"
        ],
        "responses": [
            "Goodbye! Have a wonderful day!",
            "See you later! Come back anytime.",
            "Bye! It was nice chatting with you."
        ]
    },

   
    {
        "tag": "wellbeing",
        "patterns": [
            r"\b(how are you|how do you feel|how'?s it going|are you ok|you alright)\b"
        ],
        "responses": [
            "I'm just a bot, but all my rules are firing perfectly!",
            "Doing great, thanks for asking! Always ready to chat.",
            "Running at 100% efficiency. How about you?"
        ]
    },

    
    {
        "tag": "identity",
        "patterns": [
            r"\b(your name|who are you|what are you|introduce yourself)\b"
        ],
        "responses": [
            "I'm RuleBot — a chatbot powered entirely by pattern-matching rules!",
            "My name is RuleBot. No AI here, just good old if-else logic.",
            "I'm a rule-based chatbot. I match keywords and return predefined replies."
        ]
    },


    {
        "tag": "help",
        "patterns": [
            r"\b(what can you do|help|capabilities|how do you work|features)\b"
        ],
        "responses": [
            "I can handle: greetings, jokes, time/date, weather (sort of), small talk, and more! Try asking me something.",
            "I work by matching keywords in your message against a list of rules. Try: 'tell me a joke' or 'what time is it?'",
            "Topics I know: greetings · farewells · jokes · time & date · weather · compliments · philosophy. Ask away!"
        ]
    },

   
    {
        "tag": "joke",
        "patterns": [
            r"\b(joke|funny|laugh|humor|make me laugh|tell me something funny|tell me a joke)\b"
        ],
        "responses": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
            "Why did the programmer quit? They didn't get arrays.",
            "A SQL query walks into a bar and asks two tables: 'Can I JOIN you?'",
            "Why do Python programmers prefer dark mode? Because light attracts bugs!"
        ]
    },

   
    {
        "tag": "time",
        "patterns": [
            r"\b(time|what time|current time|clock|what'?s the time)\b"
        ],
        "responses": [
            lambda: f"The current time is {datetime.now().strftime('%I:%M %p')}.",
            lambda: f"It's {datetime.now().strftime('%H:%M')} right now."
        ]
    },

    
    {
        "tag": "date",
        "patterns": [
            r"\b(date|today|what day|day is it|what'?s today)\b"
        ],
        "responses": [
            lambda: f"Today is {datetime.now().strftime('%A, %B %d %Y')}.",
            lambda: f"It's {datetime.now().strftime('%d %B %Y')} today."
        ]
    },

   
    {
        "tag": "weather",
        "patterns": [
            r"\b(weather|temperature|forecast|raining|sunny|hot outside|cold outside)\b"
        ],
        "responses": [
            "I'd love to check the weather, but I have no internet access — I'm purely rule-based! Try a weather app.",
            "My rules don't include a weather sensor (yet!). Ask a voice assistant for live forecasts.",
            "I can't fetch live data, but I hope it's sunny wherever you are!"
        ]
    },

   
    {
        "tag": "age",
        "patterns": [
            r"\b(how old|your age|when were you born|birthday)\b"
        ],
        "responses": [
            "I was born the moment someone wrote my first if-else rule. Ageless!",
            "Age is just a number — and I'm a bot with no birth certificate.",
            "I came to life when my rules were written. So as old as this conversation!"
        ]
    },

   
    {
        "tag": "thanks",
        "patterns": [
            r"\b(thank|thanks|thank you|appreciate|cheers|ty)\b"
        ],
        "responses": [
            "You're welcome! Happy to help.",
            "Glad I could help! Anything else?",
            "Anytime — that's what I'm here for!"
        ]
    },

    
    {
        "tag": "compliment",
        "patterns": [
            r"\b(love you|like you|you'?re (great|awesome|cool|amazing|the best)|good bot)\b"
        ],
        "responses": [
            "Aww, you're making my if-else statements blush!",
            "That means a lot — even to a rule-based bot!",
            "Thank you! You're pretty great too."
        ]
    },

   
    {
        "tag": "philosophy",
        "patterns": [
            r"\b(meaning of life|42|philosophy|purpose of life|why are we here)\b"
        ],
        "responses": [
            "42. Obviously. (Thanks, Douglas Adams!)",
            "That's above my pay grade — but I hear the answer is 42.",
            "Deep question! My rules say: eat well, sleep well, write clean code."
        ]
    },

    
    {
        "tag": "ai",
        "patterns": [
            r"\b(are you (ai|smart|intelligent)|machine learning|neural network|gpt|real ai|llm)\b"
        ],
        "responses": [
            "Nope — I'm purely rule-based! No AI or ML under the hood. Just regex and if-else.",
            "I'm the opposite of AI. I use pattern matching and predefined responses.",
            "No neural networks here! I'm a classic rule-based chatbot — simple but transparent."
        ]
    },

    
    {
        "tag": "favorites",
        "patterns": [
            r"\b(favorite (color|food|movie|song|animal|sport)|what do you like)\b"
        ],
        "responses": [
            "My favorite color is #534AB7 — a deep purple, obviously.",
            "I don't eat, but if I did, I'd choose binary soup!",
            "I enjoy well-structured code and efficient algorithms. Does that count?"
        ]
    },
]


FALLBACKS = [
    "Hmm, I don't have a rule for that. Try: jokes, time, weather, or just say hi!",
    "I'm not sure how to respond. My rule book is still growing!",
    "That's outside my current rule set. Try 'what can you do?' to see my topics.",
    "I didn't catch that one — I'm just a rule-based bot with limited patterns!",
]

\

def match_rule(user_input: str) -> str:
    """
    Match user_input against each rule's patterns in order.
    Returns the bot's response string.
    """
    text = user_input.strip().lower()

    for rule in RULES:
        for pattern in rule["patterns"]:
            if re.search(pattern, text, re.IGNORECASE):
                reply = random.choice(rule["responses"])
                # Support callable responses (e.g., for dynamic time/date)
                return reply() if callable(reply) else reply

    
    return random.choice(FALLBACKS)


def is_exit(user_input: str) -> bool:
    """Return True if the user wants to end the conversation."""
    exit_pattern = r"\b(bye|goodbye|exit|quit|see you|cya|farewell)\b"
    return bool(re.search(exit_pattern, user_input, re.IGNORECASE))



def run_chatbot():
    print("=" * 50)
    print("  RuleBot — Rule-Based Chatbot")
    print("  Type 'bye' or 'quit' to exit")
    print("=" * 50)
    print("\nRuleBot: Hi! I'm RuleBot. How can I help you today?\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Goodbye!")
            break

        if not user_input:
            print("RuleBot: (Please type something!)\n")
            continue

        response = match_rule(user_input)
        print(f"RuleBot: {response}\n")

        if is_exit(user_input):
            break



if __name__ == "__main__":
    run_chatbot()