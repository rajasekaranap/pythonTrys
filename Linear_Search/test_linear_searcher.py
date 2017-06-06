import LinearSearcher
import unittest

class TestLinearSearcher(unittest.TestCase):

#Test 1
    def test_list_element_is_available(self):
        '''find the element 5 in list'''
        list = [3, 1, 5, 2, 4]
        expected = True
        actual = LinearSearcher.isAvailable(list, 5)
        self.assertEqual(expected, actual)    

#Test 2
    def test_list_element_is_not_available(self):
        '''find the element 5 in list'''
        list = [3, 1, 5, 2, 4]
        expected = False
        actual = LinearSearcher.isAvailable(list, 6)
        self.assertEqual(expected, actual)

#Test 3
    def test_list_list_is_mono_type_true(self):
        '''Expected list is mono type'''
        list = [3, 1, 5, 2, 4]
        expected = True
        actual = LinearSearcher.isMonoTypeList(list)
        self.assertEqual(expected, actual)

#Test 4
    def test_list_list_is_mono_type_false(self):
        '''Expected list is non mono type'''
        list = [3, 1, 5, 2, 4, "Six"]
        expected = False
        actual = LinearSearcher.isMonoTypeList(list)
        self.assertEqual(expected, actual)

#Test 5    
    def test_list_list_is_empty(self):
        '''Expected list is Empty'''
        list = []
        expected = True
        actual = LinearSearcher.isEmptyList(list)
        self.assertEqual(expected, actual)

#Test 6   
    def test_list_list_is_non_empty(self):
        '''Expected list is Non_Empty'''
        list = [1]
        expected = False
        actual = LinearSearcher.isEmptyList(list)
        self.assertEqual(expected, actual)

#Test 7
    def test_list_find_size_of_list(self):
        '''Expected Size is 5'''
        list = [3, 1, 5, 2, 4]
        expected = 5
        actual = LinearSearcher.sizeOfList(list)
        self.assertEqual(expected, actual)

#Test 8    
    def test_list_for_single_element(self):
        '''Expected isSilgleElementList is True'''
        list = [3]
        expected = True
        actual = LinearSearcher.isSingleElementList(list)
        self.assertEqual(expected, actual)

#Test 9   
    def test_list_search_for_element_in_empty_list(self):
        '''Searching for element 3 in empty list'''
        list = []
        expected = "Empty List"
        actual = LinearSearcher.searcher(list,3)
        self.assertEqual(expected, actual)

#Test 10    
    def test_list_finding_max_element_in_list(self):
        '''List has max element is 10'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 0]
        expected = 10
        actual = LinearSearcher.findMaxElement(list)
        self.assertEqual(expected, actual)

#Test 11    
    def test_list_finding_max_element_in_list_empty_list(self):
        '''Empty list but we trying to find element 10'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.findMaxElement(list)
        self.assertEqual(expected, actual)

#Test 12    
    def test_list_finding_min_element_in_list(self):
        '''List has max element is 10'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 0]
        expected = 0
        actual = LinearSearcher.findMinElement(list)
        self.assertEqual(expected, actual)
#Test 13    
    def test_list_finding_min_element_in_list_empty_list(self):
        '''Empty list but we trying to find element 10'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.findMinElement(list)
        self.assertEqual(expected, actual)

#Test 14    
    def test_list_finding_first_element_in_list(self):
        '''List has first element is 1'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 0]
        expected = 1
        actual = LinearSearcher.findFirstElement(list)
        self.assertEqual(expected, actual)

#Test 15    
    def test_list_finding_first_element_in_list_empty_list(self):
        '''Empty list but we trying to find first element'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.findFirstElement(list)
        self.assertEqual(expected, actual)

#Test 16    
    def test_list_finding_last_element_in_list(self):
        '''List has last element is 1'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 20]
        expected = 20
        actual = LinearSearcher.findLastElement(list)
        self.assertEqual(expected, actual)

#Test 17    
    def test_list_finding_last_element_in_list_empty_list(self):
        '''Empty list but we trying to find last element'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.findLastElement(list)
        self.assertEqual(expected, actual)

#Test 18
    def test_list_finding_position_of_element_in_list(self):
        '''List has last element is 1'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 20]
        expected = 3
        actual = LinearSearcher.findPositionOfElement(list,10)
        self.assertEqual(expected, actual)

#Test 19
    def test_list_finding_position_of_element_not_available_in_list(self):
        '''List has last element is 1'''
        list = [1, 2, 3, 10, 4, 7, 5, 9, 20]
        expected = "Can't Find an Element in List"
        actual = LinearSearcher.findPositionOfElement(list,50)
        self.assertEqual(expected, actual)

#Test 20
    def test_list_finding_the_list_is_sorted_in_assending_order(self):
        '''This is Sorted List'''
        list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected = True
        actual = LinearSearcher.isSortedList(list)
        self.assertEqual(expected, actual)

#Test 21
    def test_list_finding_the_list_is_sorted_in_desending_order(self):
        '''This is Sorted List'''
        list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = True
        actual = LinearSearcher.isSortedList(list)
        self.assertEqual(expected, actual)

#Test 22
    def test_list_finding_the_list_is_not_sorted(self):
        '''This is Non Sorted List'''
        list = [1, 7, 3, 4, 9, 6, 2, 8, 5]
        expected = False
        actual = LinearSearcher.isSortedList(list)
        self.assertEqual(expected, actual)

#Test 23
    def test_list_finding_the_list_is_sorted_but_list_is_empty(self):
        '''This is Non Sorted List'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.isSortedList(list)
        self.assertEqual(expected, actual)

#Test 24
    def test_list_finding_the_element_in_position_of_list(self):
        '''List has Element 7 in 5th position'''
        list = [1, 10, 3, 4, 9, 7, 2, 8, 10]
        expected = 7
        actual = LinearSearcher.findTheElementInPosition(list, 5)
        self.assertEqual(expected, actual)

#Test 25
    def test_list_finding_the_element_in_position_of_list_position_outbound(self):
        '''List has Element 7 in 5th position'''
        list = [1, 10, 3, 4, 9, 7, 2, 8, 10]
        expected = "Position is OutBound"
        actual = LinearSearcher.findTheElementInPosition(list, 20)
        self.assertEqual(expected, actual)

#Test 26
    def test_list_finding_the_element_in_position_of_list_but_list_is_empty(self):
        '''Empty List but tyring to find element in 5th position'''
        list = []
        expected = "Invalid List"
        actual = LinearSearcher.findTheElementInPosition(list, 5)
        self.assertEqual(expected, actual)
if __name__ == '__main__':
    unittest.main()
