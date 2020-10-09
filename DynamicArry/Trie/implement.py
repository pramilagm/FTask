class Test:
    def __init__(self, test_name="", print_tests=False):
        self.total_count = 0
        self.problem_count = 0
        self.total_score = 0
        self.problem_score = 0
        self.current_problem = ""
        self.failed_problems = []
        self.printTests = print_tests
        print(f"Beginning Test: {test_name}")

    # Test Helpers
    def test(self, expected_outcome, outcome, case_num=0):
        if expected_outcome == outcome:
            if self.printTests:
                print(f"\n   Test Case {case_num} Passed!")
            return self.passed(case_num)
            return True
        if self.printTests:
            print(f"\n   Test Case {case_num} Failed.")
        return self.failed(case_num)

    def testMultipleCases(self, possible_outcomes, outcome, case_num=0):
        for possible_outcome in possible_outcomes:
            if possible_outcome == outcome:
                if self.printTests:
                    print(f"\n   Test Case {case_num} Passed!")
                return self.passed(case_num)
                return True
        if self.printTests:
            print(f"\n   Test Case {case_num} Failed.")
        return self.failed(case_num)

    # Test Logistics
    def startProblem(self, problemName):
        self.current_problem = problemName
        self.problem_score = 0
        self.problem_count = 0
        self.failed_problems = []

    def passed(self, case_num):
        self.total_score += 1
        self.problem_score += 1
        self.problem_count += 1
        self.total_count += 1

    def failed(self, case_num):
        self.problem_count += 1
        self.total_count += 1
        self.failed_problems.append(case_num)

    def endProblem(self):
        print(
            f"\n   {self.current_problem} Score: {self.problem_score} / {self.problem_count}")
        if len(self.failed_problems) > 0:
            print(f"   ** Failed Test Cases: {self.failed_problems}")

    def printFinal(self):
        print(f"\nTotal Score: {self.total_score} / {self.total_count}")


test = Test("Algo Practice")


class Trie:
    # Write your code here.

    # Initialize your data structure here.
    def __init__(self):
        self.letters = {}
        self.end = False

    def __repr__(self):
        return f"<Trie: Letters: {self.letters} End: {self.end}>"
    # Inserts a word into the trie.

    def insert(self, word: str) -> None:
        # Write your code here.
        current = self
        for letter in word:
            if letter not in current.letters:
                current.letters[letter] = Trie()
            current = current.letters[letter]
        current.end = True
    # Returns if the word is in the trie.

    def search(self, word: str) -> bool:
        current = self
        for letter in word:
            if letter not in current.letters:
                return False
            current = current.letters[letter]
        return current.end
    # Returns if there is any word in the trie that starts with the given prefix.

    def startsWith(self, prefix: str) -> bool:
        current = self
        for letter in prefix:
            if letter not in current.letters:
                return False
            current = current.letters[letter]
        return True


# Test Cases
test.startProblem("Trie")
trie = Trie()
trie.insert("apple")
test.test(True, trie.search("apple"), 1)
test.test(False, trie.search("app"), 2)
test.test(True, trie.startsWith("app"), 3)
trie.insert("app")
test.test(True, trie.search("app"), 4)
test.test(True, trie.startsWith("a"), 5)
test.test(False, trie.startsWith("ple"), 6)
test.endProblem()


class Trie:
    # Write your code here.

    # Initialize your data structure here.
    def __init__(self):
        self.c = {}

        # Inserts a word into the trie.
    def insert(self, word: str) -> None:
            # Write your code here.
        node = self.c
        for i in word:
            if i not in node:
                node[i] = {}
            node = node[i]
        node['#'] = True

        # Returns if the word is in the trie.

    def search(self, word: str) -> bool:
        # Write your code here.
        node = self.c
        for i in word:
            if i in node:
                node = node[i]
            else:
                return False
        return '#' in node

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        # Write your code here.
        node = self.c
        for i in prefix:
            if i in node:
                node = node[i]
            else:
                return False
        return True


    # Test Cases
test.startProblem("Trie")
trie = Trie()
trie.insert("apple")
test.test(True, trie.search("apple"), 1)
test.test(False, trie.search("app"), 2)
test.test(True, trie.startsWith("app"), 3)
trie.insert("app")
test.test(True, trie.search("app"), 4)
test.test(True, trie.startsWith("a"), 5)
test.test(False, trie.startsWith("ple"), 6)
test.endProblem()
