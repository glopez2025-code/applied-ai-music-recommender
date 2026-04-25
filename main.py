def load_text_file(file_path):
    """
    Safely loads a text file and handles exceptions.
    """
    try:
        with open(file_path, "r") as file:
            data = file.read()
        return data

    except FileNotFoundError:
        print(f"Exception: File '{file_path}' not found.")
        return None

    except IOError as e:
        print(f"Exception while reading file '{file_path}': {e}")
        return None

    except Exception as e:
        print(f"Unexpected exception while loading '{file_path}': {e}")
        return None


def load_knowledge_base():
    return load_text_file("knowledge_base/music_recommendation_guide.txt")


def get_user_input():
    """Gets music preference from user."""
    return input("What kind of music are you looking for? ").strip()


def get_knowledge_section(knowledge, section_title):
    """Finds and returns the matching section from the knowledge base."""

    sections = knowledge.split("\n\n")

    for section in sections:
        if section_title.lower() in section.lower():
            return section.strip()

    return None


def process_recommendation(user_input, knowledge):
    """Matches user input and pulls explanation from knowledge base."""

    if not validate_user_input(user_input):
        print("Guardrail: Please describe the mood, activity, or type of music you want.\n")
        return

    user_input = user_input.lower()

    print(f"\n✓ Searching for '{user_input}' recommendations...")
    print("(Matching against knowledge base...)\n")

    category = None
    if "chill" in user_input or "study" in user_input:
        category = "Chill / Study"
    elif "workout" in user_input or "gym" in user_input:
        category = "Workout"
    elif "sad" in user_input or "emotional" in user_input:
        category = "Sad / Emotional"
    elif "happy" in user_input or "upbeat" in user_input:
        category = "Happy / Upbeat"
    elif "focus" in user_input:
        category = "Focus"
    else:
        print("No clear category found. Try being more specific.\n")
        return

    print(f"Category: {category}\n")

    # 🔥 RAG retrieval
    section = get_knowledge_section(knowledge, category)

    if section:
        print(section)
        print("\n")
    else:
        print(f"No recommendations found for {category} category.\n")


def validate_user_input(user_input):
    if not user_input or len(user_input) < 4:
        return False
    vague_words = ["music", "song", "songs", "playlist"]
    if user_input.lower().strip() in vague_words:
        return False
    return True


def main():
    knowledge = load_knowledge_base()
    
    if knowledge is None:
        print("System could not start")
        return

    print("=== AI Music Recommender Assistant ===\n")
    
    while True:
        user_input = get_user_input()
        
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Thank you for using the AI Music Recommender. Goodbye!")
            break
        
        process_recommendation(user_input, knowledge)


if __name__ == "__main__":
    main()