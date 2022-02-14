from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestKisebbKisebb(TestCase):
    def test_kisebb_elso(self):
        aktualis = feladatok.kisebb(3,5)
        elvart = 3
        self.assertEqual(elvart, aktualis, "kisebb(3,5) visszatérési értéke nem 3")

