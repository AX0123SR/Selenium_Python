'''
Assertions are used in python to check a validation point.
1) There are various methods-
  - AssertEqual
  - AssertNotEqual
  - AssertTrue
  - AssertFalse
  - AssertIsNone
  - AssertIsNotNone
  - AssertIn
  - AssertNotIn
  - AssertGreater
  - AssertGreaterEqual
  - AssertLess
  - AssertLessEqual
'''

import unittest
from selenium import webdriver
class Assertion(unittest.TestCase):
   def test_assert(self):
        driver = webdriver.Chrome(executable_path="C://Users//ayussriv//Downloads//chromedriver_win32 (1)//chromedriver.exe")
        driver.get("https://www.google.com/")
        title = driver.title
        #self.assertEqual("Google",title, "Webpages titles are not matched")
        #self.assertNotEqual("Google123", title, "Webpages titles are not matched")
        #self.assertTrue(title == "Google") # True
        #self.assertFalse(title == "google34")
        #self.assertIsNone(driver)
        #self.assertIsNotNone(driver)

        list1 = ["Ayush", "Amil", "Aman", "Akshat"]
        self.assertIn("Amil",list1)
        self.assertNotIn("Ruby",list1)
        self.assertGreater(100,10)
        self.assertGreaterEqual(100,100)
        self.assertLess(10,50)
        self.assertLessEqual(100,100)

# It means module that is being run is the main program.

if __name__ == "__main__":
    unittest.main()
