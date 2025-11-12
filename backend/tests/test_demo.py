import os
import json
import tempfile
import sys

import pytest

from fastapi.testclient import TestClient

# Add backend to path and import app
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

from demo_runner import main as demo_main


def test_demo_runner_creates_outputs(tmp_path):
    # Run demo runner which writes to backend/outputs
    demo_main()
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs")
    out_dir = os.path.normpath(out_dir)
    assert os.path.exists(out_dir)
    # Check that expected files exist
    for name in ("flashcards.json", "quizzes.json", "planner.json"):
        p = os.path.join(out_dir, name)
        assert os.path.exists(p), f"{name} missing"
        # Each file should be valid JSON
        with open(p, encoding="utf-8") as f:
            data = json.load(f)
            assert data is not None


def test_run_demo_endpoint():
    client = TestClient(app)
    resp = client.post("/run_demo")
    assert resp.status_code == 200
    body = resp.json()
    assert body.get("status") == "ok"
    summary = body.get("summary")
    assert isinstance(summary, dict)
