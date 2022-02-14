from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class Testosszeg10(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.osszeg(10)
        elvart = 55
        self.assertEqual(elvart, aktualis, "A osszeg nem jól határozta meg!")

