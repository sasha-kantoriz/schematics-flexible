# -*- coding: utf-8 -*-

import unittest
import tests.test_schematics_flexible


def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(
        test_schematics_flexible.TestSchematicsFlexible
    )
    return suite
