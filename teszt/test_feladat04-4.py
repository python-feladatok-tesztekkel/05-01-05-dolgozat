from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok



class TestLottoszamE91(TestCase):
    def test_feladat04(self):
        aktualis = feladatok.lottoszam_e(91)
        elvart = False
        self.assertEqual(elvart, aktualis, "Az lottoszam_e függvény nem megfelelően működik")

