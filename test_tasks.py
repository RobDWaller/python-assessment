import unittest
import websites
import test_inputs
import test_ans
import copy

# unittest.util._MAX_LENGTH=None
TEST_CASE1 = copy.deepcopy(test_inputs.TEST_CASE_ONE)
TEST_CASE2 = copy.deepcopy(test_inputs.TEST_CASE_TWO)
TEST_CASE3 = copy.deepcopy(test_inputs.TEST_CASE_THREE)
TEST_CASE4 = copy.deepcopy(test_inputs.TEST_CASE_FOUR)


class test_tasks(unittest.TestCase):

    def test_task_one(self):
        global TEST_CASE1
        global TEST_CASE2
        global TEST_CASE3
        global TEST_CASE4

        TEST_CASE1 = copy.deepcopy(test_inputs.TEST_CASE_ONE)
        TEST_CASE2 = copy.deepcopy(test_inputs.TEST_CASE_TWO)
        TEST_CASE3 = copy.deepcopy(test_inputs.TEST_CASE_THREE)
        TEST_CASE4 = copy.deepcopy(test_inputs.TEST_CASE_FOUR)

        task1_result1 = websites.task_one(test_inputs.TEST_CASE_ONE)
        self.assertEqual(task1_result1, test_ans.TASK_ONE_ANS_ONE)

        task1_result2 = websites.task_one(test_inputs.TEST_CASE_TWO)
        self.assertEqual(task1_result2, test_ans.TASK_ONE_ANS_TWO)

        task1_result3 = websites.task_one(test_inputs.TEST_CASE_THREE)
        self.assertEqual(task1_result3, test_ans.TASK_ONE_ANS_THREE)

        task1_result4 = websites.task_one(test_inputs.TEST_CASE_FOUR)
        self.assertEqual(task1_result4, test_ans.TASK_ONE_ANS_FOUR)


    def test_task_two(self):
        global TEST_CASE1
        global TEST_CASE2
        global TEST_CASE3
        global TEST_CASE4

        TEST_CASE1 = copy.deepcopy(test_inputs.TEST_CASE_ONE)
        TEST_CASE2 = copy.deepcopy(test_inputs.TEST_CASE_TWO)
        TEST_CASE3 = copy.deepcopy(test_inputs.TEST_CASE_THREE)
        TEST_CASE4 = copy.deepcopy(test_inputs.TEST_CASE_FOUR)

        websites.task_two(TEST_CASE1)
        self.assertEqual(TEST_CASE1, test_ans.TASK_TWO_ANS_ONE)

        websites.task_two(TEST_CASE2)
        self.assertEqual(TEST_CASE2, test_ans.TASK_TWO_ANS_TWO)

        websites.task_two(TEST_CASE3)
        self.assertEqual(TEST_CASE3, test_ans.TASK_TWO_ANS_THREE)

        websites.task_two(TEST_CASE4)
        self.assertEqual(TEST_CASE4, test_ans.TASK_TWO_ANS_FOUR)


    def test_task_three(self):
        global TEST_CASE1
        global TEST_CASE2
        global TEST_CASE3
        global TEST_CASE4

        TEST_CASE1 = copy.deepcopy(test_inputs.TEST_CASE_ONE)
        TEST_CASE2 = copy.deepcopy(test_inputs.TEST_CASE_TWO)
        TEST_CASE3 = copy.deepcopy(test_inputs.TEST_CASE_THREE)
        TEST_CASE4 = copy.deepcopy(test_inputs.TEST_CASE_FOUR)

        websites.task_three(TEST_CASE1)
        self.assertEqual(TEST_CASE1, test_ans.TASK_THREE_ANS_ONE)

        websites.task_three(TEST_CASE2)
        self.assertEqual(TEST_CASE2, test_ans.TASK_THREE_ANS_TWO)

        websites.task_three(TEST_CASE3)
        self.assertEqual(TEST_CASE3, test_ans.TASK_THREE_ANS_THREE)

        websites.task_three(TEST_CASE4)
        self.assertEqual(TEST_CASE4, test_ans.TASK_THREE_ANS_FOUR)


    def test_task_four(self):
        global TEST_CASE1
        global TEST_CASE2
        global TEST_CASE3
        global TEST_CASE4

        TEST_CASE1 = copy.deepcopy(test_inputs.TEST_CASE_ONE)
        TEST_CASE2 = copy.deepcopy(test_inputs.TEST_CASE_TWO)
        TEST_CASE3 = copy.deepcopy(test_inputs.TEST_CASE_THREE)
        TEST_CASE4 = copy.deepcopy(test_inputs.TEST_CASE_FOUR)

        task4_result1 = websites.task_four(test_inputs.TEST_CASE_ONE)
        self.assertEqual(task4_result1, 23)

        task4_result2 = websites.task_four(test_inputs.TEST_CASE_TWO)
        self.assertEqual(task4_result2, 0)

        task4_result3 = websites.task_four(test_inputs.TEST_CASE_THREE)
        self.assertEqual(task4_result3, 18)

        task4_result4 = websites.task_four(test_inputs.TEST_CASE_FOUR)
        self.assertEqual(task4_result4, 32)


if __name__ == '__main__':
    unittest.main()