from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok



class Testosszeg3(TestCase):
    def test_feladat02(self):
        aktualis = feladatok.osszeg(3)
        elvart = 6
        self.assertEqual(elvart, aktualis, "A osszeg nem jól határozta meg!")

