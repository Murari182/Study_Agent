import os
import json
from agents.reader import ReaderAgent
from agents.flashcard import FlashcardAgent
from agents.quiz import QuizAgent
from agents.planner import PlannerAgent


class DummyLLM:
    """A tiny deterministic LLM-like object with a predict(prompt) method.
    It returns simple heuristic outputs suitable for demo/testing without real API calls.
    """
    def predict(self, prompt: str) -> str:
        # Very small heuristics to produce Q/A or MCQs depending on prompt keywords
        text = prompt.lower()
        if "flashcard" in text or "flashcard generator" in text or "produce" in text:
            # return a small JSON array
            return json.dumps([
                {"question": "What is the main topic?", "answer": "The main topic is X."},
                {"question": "Define X.", "answer": "X is defined as ..."}
            ])
        if "multiple-choice" in text or "mcq" in text or "quiz" in text:
            return json.dumps([
                {"question": "What does X stand for?", "options": ["A", "B", "C", "D"], "answer": "A"}
            ])
        # fallback: echo a simplified answer
        return "[DEMO] Generated content based on input chunk."


def save_json(obj, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def main():
    base = os.path.dirname(__file__)
    outputs = os.path.join(base, "outputs")
    os.makedirs(outputs, exist_ok=True)

    reader = ReaderAgent()
    llm = DummyLLM()
    flash = FlashcardAgent(llm=llm)
    quiz = QuizAgent(llm=llm)
    planner = PlannerAgent()

    sample_pdf = os.path.join(base, "sample.pdf")
    if os.path.exists(sample_pdf):
        print("Using sample PDF at", sample_pdf)
        chunks = reader.read_pdf(sample_pdf)
    else:
        print("No sample PDF found — using built-in sample text for demo.")
        sample_text = (
            "Topic: Photosynthesis\n"
            "Photosynthesis is the process by which plants convert light into chemical energy.\n"
            "Key steps include light absorption, water splitting, and carbon fixation.\n"
            "Definitions: Chlorophyll — pigment that captures light.\n"
        )
        chunks = reader.splitter.split_text(sample_text)

    print(f"Reader produced {len(chunks)} chunks; showing first chunk:\n{chunks[0][:300]}\n")

    flashcards = flash.generate_from_chunks(chunks)
    print(f"Generated {len(flashcards)} flashcards (sample):", flashcards[:3])
    save_json(flashcards, os.path.join(outputs, "flashcards.json"))

    quizzes = quiz.generate_from_chunks(chunks)
    # Ensure quizzes have a difficulty field (demo assigns 'Easy' by default)
    for i, q in enumerate(quizzes):
        if isinstance(q, dict) and "difficulty" not in q:
            q["difficulty"] = "Easy"
    print(f"Generated {len(quizzes)} quizzes (sample):", quizzes[:2])
    save_json(quizzes, os.path.join(outputs, "quizzes.json"))

    topics = [c.split("\n")[0][:80] for c in chunks]
    plan = planner.plan_topics(topics)
    print(f"Planner produced {len(plan)} items (sample):", plan[:3])
    save_json(plan, os.path.join(outputs, "planner.json"))

    print("Demo run complete. Outputs saved to backend/outputs/")


if __name__ == "__main__":
    main()
