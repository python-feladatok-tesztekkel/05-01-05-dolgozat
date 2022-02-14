from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok


class TestKisebbEgyenlo(TestCase):
    def test_egyenloek(self):
        aktualis = feladatok.kisebb(5,5)
        elvart = 5
        self.assertEqual(elvart, aktualis, "kisebb(5,5) visszatérési értéke nem 5")
