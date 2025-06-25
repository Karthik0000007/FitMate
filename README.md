# FitMate 💪🧠

**FitMate** is an intelligent chatbot assistant built with NLP and deep learning to help users with **fitness**, **nutrition**, and **injury recovery** guidance. It features a responsive graphical interface, context-aware responses, and customizable intents for expanding its domain knowledge.

---

## 🌟 Features

- 🧠 Trained with TensorFlow on custom intents for fitness & health.
- 💬 GUI-based chatbot with `Tkinter` for interactive use.
- 🕒 Built-in commands like time, web search, and session save.
- 📁 Saves your chat logs to review fitness advice later.
- 🔄 Easily extendable through `intents.json`.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Karthik0000007/FitMate.git
cd FitMate
```
### 2. Install the required libraries
```bash
pip install nltk tensorflow keras
```
### 3. Download NLTK data
```bash
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```
### 4. Run the following to train the model using your custom intents:
```bash
python main.py
```
### This will generate:
- chatbot_model.h5
- words.pkl
- classes.pkl
### 5. Launch the chatbot
```bash
python Graphical_UI.py
```
## Customize Intents
- You can edit intents.json to expand FitBot’s knowledge. Here’s an example intent:
```bash
  {
  "tag": "nutrition_tips",
  "patterns": ["What should I eat?", "Best post-workout food?", "Nutrition advice?"],
  "responses": [
    "Make sure to consume protein and complex carbs after a workout.",
    "Lean meats, veggies, and whole grains are great for fitness nutrition!"
  ]
}
```
- After editing intents.json, re-run main.py to retrain the model.
### 6. Future Plans

- Voice input and text-to-speech responses.
- Integration with fitness trackers and APIs.
- Injury-specific rehab protocols.
- Personalized meal and workout suggestions.

### 7. Special Commands in Chat

- search <query> – Opens a Google search for the query.
- time – Shows the current time.
- exit / quit / bye – Ends the conversation.
- Clear Chat – Clears the current session.
- Save Chat – Saves chat history as a timestamped .txt file.
- Help – Opens a help message box.
