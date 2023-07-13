class Key:
    def __init__(self):
        self.key = [0] * 1337
        self.passphrase = "zax2rulez"
        self.key[404] = 3

    def __len__(self):
        return 1337

    def __gt__(self, other):
        return True

    def __str__(self):
        return "GeneralTsoKeycard"


def run_key_tests():
    key = Key()

    assert len(key) == 1337
    assert key.key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"

    print("All tests passed!")

if __name__ == '__main__':
    run_key_tests()
