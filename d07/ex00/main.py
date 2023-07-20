from models import ReplicantTest


RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    questions_file = "questions.json"
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
