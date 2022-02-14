from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTeglalapKetPozitiv(TestCase):
    def test_teglalap_van(self):
        aktualis = feladatok.teglalap_kerulet(5.3,7.4)
        elvart = 25.4
        self.assertEqual(elvart, aktualis, "A teglalap_kerulet függvény létező téglalap területét nem jól határozza meg!")






