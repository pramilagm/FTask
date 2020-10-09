from typing import List


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


def sm(matrix: List[List[int]]) -> List[int]:
    # Write your code here.
    res = []
    if len(matrix) == 0:
        return res
    rowBegin, rowEnd = 0, len(matrix)-1
    colBegin, colEnd = 0, len(matrix[0])-1
    while rowBegin <= rowEnd and colBegin <= colEnd:
        for i in range(colBegin, colEnd+1):
            res.append(matrix[rowBegin][i])
        rowBegin += 1
        for i in range(rowBegin, rowEnd+1):
            res.append(matrix[i][colEnd])
        colEnd -= 1
        if rowBegin <= rowEnd:
            for i in range(colEnd, colBegin-1, -1):
                res.append(matrix[rowEnd][i])
            rowEnd -= 1
        if colBegin <= colEnd:
            for i in range(rowEnd, rowBegin-1, -1):
                res.append(matrix[i][colBegin])
            colBegin += 1
    return res


# Test Cases
test.startProblem("Spiral Matrix")
test.test([1, 2, 3, 6, 9, 8, 7, 4, 5], sm(
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 1)
test.test([1, 2, 3, 3, 3, 2, 1, 1, 2], sm(
    [[1, 2, 3], [1, 2, 3], [1, 2, 3]]), 2)
test.test([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], sm(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), 3)
test.test([], sm([]), 4)
test.test([1], sm([[1]]), 5)
test.endProblem()
