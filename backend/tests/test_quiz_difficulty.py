import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.quiz import QuizAgent


class DummyLLM:
    def predict(self, prompt: str) -> str:
        # Return a JSON with a question but no difficulty
        return json.dumps([
            {"question": "What is X?", "options": ["A","B","C","D"], "answer": "A"}
        ])


def test_quiz_agent_adds_difficulty():
    llm = DummyLLM()
    q = QuizAgent(llm=llm)
    chunks = ["Some sample text about X."]
    out = q.generate_from_chunks(chunks)
    assert isinstance(out, list)
    assert len(out) == 1
    assert "difficulty" in out[0]
    assert out[0]["difficulty"] == "Medium"
