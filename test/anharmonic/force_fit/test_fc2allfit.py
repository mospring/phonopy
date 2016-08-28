import unittest
import numpy as np

from phonopy.interface.phonopy_yaml import get_unitcell_from_phonopy_yaml
from phonopy.structure.cells import get_supercell
from phonopy.structure.symmetry import Symmetry
from anharmonic.force_fit.fc2 import FC2allFit

class TestFC2allFit(unittest.TestCase):

    def setUp(self):
        filename = "POSCAR.yaml"
        symprec = 1e-5

        self._cell = get_unitcell_from_phonopy_yaml(filename)
        self._scell = get_supercell(self._cell,
                                    np.diag([2, 2, 2]),
                                    symprec=symprec)
        self._symmetry = Symmetry(self._scell, symprec=symprec)
        self._fc2allfit = FC2allFit(self._scell,
                                    None,
                                    None,
                                    self._symmetry)
    
    def tearDown(self):
        pass
    
    def test_search_operations(self):
        self.assertTrue(self._fc2allfit._search_operations())

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFC2allFit)
    unittest.TextTestRunner(verbosity=2).run(suite)
    # unittest.main()
