# Applied AI Music Recommender

## Original Project Overview

The original project was a music recommender simulation built in Python. It used song data like genre, mood, and energy along with user preferences to calculate a score and suggest songs. The system followed a simple content-based approach, meaning it recommended songs based on how similar they were to what the user liked.

---

## AI Enhancement

This project was extended into an Applied AI System by adding a Retrieval-Augmented Generation (RAG) component.

The system now:
- Takes user input
- Classifies it into a music category
- Retrieves relevant information from a knowledge base file
- Returns a structured recommendation with explanation

---

## How It Works

1. User enters a request (e.g., "chill music")
2. The system identifies a category (Chill / Study, Workout, etc.)
3. It searches a knowledge base file
4. It returns the matching section with details

---

## Architecture Overview

The system follows a simple flow:

User Input → Input Validation → Category Detection → Knowledge Base Retrieval → Output Response

The architecture diagram is included in the project to show how data moves through the system from the user’s request to the final recommendation.

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

See evaluation.txt for test cases and results.

---

## Setup Instructions

1. Clone the repository
2. Navigate to the project folder
3. Run:

```bash
python main.py