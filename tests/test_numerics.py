import ast
import unittest

import numpy as np

from lgs.anysplat_wrap import apply_sim3, sim3_from_cams
from lgs.compat import Annotations
from lgs.metrics import auc


class NumericsTests(unittest.TestCase):
    def test_auc_ties_and_order(self):
        labels = np.array([False, False, True, True])
        self.assertAlmostEqual(auc(np.ones(4), labels), 0.5)
        scores = np.array([0., 1., 1., 2.])
        self.assertAlmostEqual(auc(scores, labels), 0.875)
        order = np.array([3, 1, 0, 2])
        self.assertAlmostEqual(auc(scores[order], labels[order]), 0.875)
        self.assertAlmostEqual(auc(np.arange(4), labels), 1.)

    def test_sim3_known_transform(self):
        src = np.repeat(np.eye(4)[None], 3, axis=0)
        src[:, 0, 3] = [0, 1, 2]
        rotation = np.array([[0., -1., 0.], [1., 0., 0.], [0., 0., 1.]])
        dst = apply_sim3(src, 2.5, rotation, np.array([3., 4., 5.]))
        transform = sim3_from_cams(src, dst)
        np.testing.assert_allclose(apply_sim3(src, *transform), dst, atol=1e-10)

    def test_python39_type_backport_preserves_bitwise(self):
        code = 'ViewSamplerCfg = int | str\nx: int | None = None\ny = 1 | 2\ndef f(a: int | str) -> int | None: return 1\n'
        tree = ast.fix_missing_locations(Annotations().visit(ast.parse(code)))
        scope = {}
        exec(compile(tree, '<compat-test>', 'exec'), scope)
        self.assertEqual(scope['y'], 3)
        self.assertEqual(scope['f'](1), 1)


if __name__ == '__main__':
    unittest.main()
