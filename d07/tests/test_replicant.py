import json
import pytest
import sys
import os
import io

from _pytest import monkeypatch

sys.path.append('..')

from d07.models import ReplicantTest, VariableMeasurements

@pytest.fixture
def test_replicant_instance():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    questions_file = os.path.join(current_dir, "../questions.json")
    return ReplicantTest(questions_file)


def test_load_questions(test_replicant_instance):
    assert len(test_replicant_instance.questions) > 0


def test_valid_responses(test_replicant_instance, monkeypatch):
    test_input = "1"
    monkeypatch.setattr('builtins.input', lambda _: test_input)
    test_replicant_instance.ask_question({"question": "Question", "responses": ["Option1", "Option2"]})
    assert len(test_replicant_instance.responses) == 1
    assert test_replicant_instance.responses[0] == "Option1"
    assert test_replicant_instance.score == 1


def test_ask_question_valid_response(monkeypatch):
    test_input = "1"
    test_question = {"question": "Question", "responses": ["Option1", "Option2"]}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_replicant_instance = ReplicantTest(os.path.join(current_dir, "../questions.json"))

    with io.StringIO(test_input) as user_input:
        monkeypatch.setattr("sys.stdin", user_input)

        test_replicant_instance.ask_question(test_question)

    assert len(test_replicant_instance.responses) == 1
    assert test_replicant_instance.responses[0] == "Option1"
    assert test_replicant_instance.score == 1