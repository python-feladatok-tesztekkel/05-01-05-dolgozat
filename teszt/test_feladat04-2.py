from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok



class TestLottoszamE90(TestCase):
    def test_feladat02(self):
        aktualis = feladatok.lottoszam_e(90)
        elvart = True
        self.assertEqual(elvart, aktualis, "Az lottoszam_e függvény nem megfelelően működik")
