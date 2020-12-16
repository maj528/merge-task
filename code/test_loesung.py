import unittest
import loesung
import time

class TestMerge(unittest.TestCase):

    def test_merge(self):
        """Merge Function"""
        self.assertEqual(loesung.merge([[1,2],[2,2]]), [[1,2]])
        print "Test passed!"
        self.assertEqual(loesung.merge([[1,50],[1,100]]), [[1,100]])
        print "Test passed!"
        self.assertEqual(loesung.merge([[-1,2],[-5,3]]), [[-5,3]])
        print "Test passed!"
        self.assertEqual(loesung.merge([[-10,-7], [-4,-3], [-5,-1]]), [[-10,-7],[-5,-1]])
        print "Test passed!"
        self.assertEqual(loesung.merge([[25,30], [2,19], [14, 23], [4,8]]), [[2,23], [25,30]])
        print "Test passed!"
        
        with self.assertRaises(ValueError):
            loesung.merge([[0]])
        with self.assertRaises(ValueError):
            loesung.merge([[30,0]])
        with self.assertRaises(ValueError):
            loesung.merge([[0,1,2,3,4,5]])            
        with self.assertRaises(ValueError):
            loesung.merge([])

    #hier koennte eine genaure Laufzeit des Programmes gerechnet werden - nuetzlich fuer zukuenftige Leistungstests
    #def test_performance(list_input):
        #start = time.time()
        #loesung.merge(list_input)
        #end = time.time()
        #return end - start

if __name__ == '__main__':
    unittest.main()
