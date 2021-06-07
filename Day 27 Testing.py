def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues:
    @staticmethod
    def get_array():
        return [1,2,3,4,5,6]
    @staticmethod
    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        return [1,2,1,4,5,6]
    @staticmethod
    def get_expected_result():
        return 0