class CompareHelper:
    @staticmethod
    def isListMatch(value_list, ans_list):
        return len(list(set(value_list) - set(ans_list))) == 0
