import json
import pytest
import sys
import os
import io
from _pytest import monkeypatch

sys.path.append('..')

from src.models import ReplicantTest, VariableMeasurements, is_replicant

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


def test_run_test_1(monkeypatch):
    test_input = "1\n2\n3\n4\n1\n2\n3\n4\n1\n2\n1\n2\n3\n4"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_replicant_instance = ReplicantTest(os.path.join(current_dir, "../questions.json"))

    with io.StringIO(test_input) as user_input:
        monkeypatch.setattr("sys.stdin", user_input)

        variable_measurements, score = test_replicant_instance.run_test()

    assert isinstance(variable_measurements, VariableMeasurements)
    assert variable_measurements.respiration == 1
    assert variable_measurements.heart_rate == 2
    assert variable_measurements.blushing_level == 3
    assert variable_measurements.pupillary_dilation == 4
    assert score == 23


def test_run_test_2(monkeypatch):
    test_input = "4\n4\n4\n4\n4\n4\n4\n4\n4\n4\n1\n2\n3\n4"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    test_replicant_instance = ReplicantTest(os.path.join(current_dir, "../questions.json"))

    with io.StringIO(test_input) as user_input:
        monkeypatch.setattr("sys.stdin", user_input)

        variable_measurements, score = test_replicant_instance.run_test()

    assert isinstance(variable_measurements, VariableMeasurements)
    assert variable_measurements.respiration == 1
    assert variable_measurements.heart_rate == 2
    assert variable_measurements.blushing_level == 3
    assert variable_measurements.pupillary_dilation == 4
    assert score == 40


def test_is_replicant():
    assert is_replicant(20, threshold_score=15)
    assert not is_replicant(25, threshold_score=30)
    assert is_replicant(40)
