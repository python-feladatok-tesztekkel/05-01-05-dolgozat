from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestParatlenEIgen(TestCase):
    def test_feladat01(self):
        aktualis = feladatok.paratlan_e(5)
        elvart = True
        self.assertEqual(elvart, aktualis, "A paratlan_e függvény nem megfelelően működik")

