from models import ReplicantTest
import pytest
import os


RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    questions_file = os.path.join(current_dir, "questions.json")
    test = ReplicantTest(questions_file)
    variable_measurements, score = test.run_test()

    threshold_score = 30
    is_replicant = score > threshold_score

    if is_replicant:
        print(RED + "Subject is identified as replicant." + RESET)
    else:
        print(GREEN + "Subject is identified as human." + RESET)

if __name__ == "__main__":
    main()
