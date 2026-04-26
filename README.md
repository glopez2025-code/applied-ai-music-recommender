# Applied AI Music Recommender

## Original Project Overview

The original project was a music recommender simulation built in Python. It used song data like genre, mood, and energy along with user preferences to calculate a score and suggest songs. The system followed a simple content-based approach, meaning it recommended songs based on how similar they were to what the user liked.

---

## AI Enhancement

This project was extended into an Applied AI System by adding a Retrieval-Augmented Generation (RAG) component.

The system now:
- Takes user input
- Validates input using guardrails
- Classifies it into a music category
- Retrieves relevant information from a knowledge base file
- Returns a structured recommendation with explanation

---

## How It Works

1. User enters a request (e.g., "chill music")
2. The system validates the input
3. The system identifies a category (Chill / Study, Workout, etc.)
4. It searches a knowledge base file
5. It returns the matching section with details

---

## Architecture Overview

The system follows a simple flow:

User Input → Input Validation → Category Detection → Knowledge Base Retrieval → Output Response

This shows how data moves through the system from the user’s request to the final recommendation.

---

## Guardrails

The system includes input validation:
- Prevents empty input
- Prevents vague requests (e.g., "music", "song")
- Prompts the user for clearer input

---

## Sample Interactions

### Example 1

Input:
chill music

Output:
Category: Chill / Study

Chill / Study
- Usually has low energy and a calm mood
- Often instrumental or soft vocals
- Examples: Lo-fi, acoustic, ambient

---

### Example 2

Input:
gym playlist

Output:
Category: Workout

Workout
- High energy and fast tempo
- Strong beats and motivating lyrics
- Examples: Hip-hop, EDM, pop

---

### Example 3 (Guardrail)

Input:
music

Output:
Guardrail: Please describe the mood, activity, or type of music you want.

---

## Evaluation

The system was tested using multiple inputs to ensure consistent behavior:

- Test 1: "chill music" → Correct category and knowledge retrieval
- Test 2: "gym playlist" → Correct category and output
- Test 3: "music" → Guardrail triggered correctly

All tests passed, showing that the system responds consistently and handles both valid and invalid inputs.

---

## Setup Instructions

1. Clone the repository
2. Navigate to the project folder
3. Run:

```bash
python main.py

---

## Reflection

This project showed how AI systems can combine user input with external knowledge to generate useful results. It also demonstrated the importance of guardrails to improve reliability and user experience.

During development, AI tools like Copilot were used to assist with writing functions and improving code structure. One helpful suggestion was generating a function to safely load files with exception handling. One limitation is that the system relies on simple keyword matching, which may not always fully understand complex user requests. Future improvements could include more advanced natural language processing or expanding the knowledge base.

---

## Portfolio Reflection

This project reflects my ability to build a complete AI system from scratch, including input processing, retrieval from a knowledge base, and reliability through guardrails. It shows that I can take a basic concept and extend it into a structured, working system. I focused on keeping the design simple, understandable, and functional, which is important when building real-world AI tools.

---

## Video Walkthrough

Loom Video: [PASTE YOUR LINK HERE]