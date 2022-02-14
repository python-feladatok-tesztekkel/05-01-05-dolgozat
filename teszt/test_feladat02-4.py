from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestTeglalapMindkettoNulla(TestCase):
    def test_teglalap_nincs_3(self):
        aktualis = feladatok.teglalap_kerulet(0, 0)
        elvart = None
        self.assertEqual(elvart, aktualis,"Ha mindkét oldal nulla, a teglalap_kerulet függvény nem jól határozza meg az értéket")




