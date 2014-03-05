from ajay3yrs2 import return_max
import unittest
class TestReturnMax(unittest.TestCase):
    
    def setUp(self):
        self.return_max = return_max()
        self.result_correct = [['1995', 'apl', 'comp_1', '99'], ['2003', 'nov', 'comp_2', '99'], ['2001', 'apl', 'comp_3', '99'], ['1998', 'apl', 'comp_4', '99'], ['1996', 'jun', 'comp_5', '99'], ['1996', 'jun', 'comp_6', '99']]
        self.result_incorrect = [['1995', 'apl', 'comp_1', '9'], ['2003', 'nov', 'comp_2', '99'], ['2001', 'apl', 'comp_3', '99'], ['1998', 'apl', 'comp_4', '99'], ['1996', 'jun', 'comp_5', '99'], ['1996', 'jun', 'comp_6', '99']]
    
    def test_equality(self):
        self.assertEqual(self.return_max, self.result_correct) 
        
        
    def test_inequality(self):
        self.assertNotEqual(self.return_max, self.result_incorrect) 
        

if __name__ == '__main__':
    unittest.main()