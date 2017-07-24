import unittest

from snapstack import Plan, Setup, Step

class SnapstackTest(unittest.TestCase):

    def test_snapstack(self):
        '''
        _test_snapstack_

        Run a basic smoke test, utilizing our snapstack testing harness.

        '''
        # snapstack already installs neutron. Override the 'neutron'
        # step with a locally built snap. keystone, nova, etc. will still
        # be installed as normal from the store.
        setup = Setup()
        setup.add_steps(('neutron', Step(
            snap='neutron',
            script_loc='./tests/',
            scripts=['neutron.sh'],
            snap_store=False)))

        # Execute the snapstack tests
        plan = Plan(base_setup=setup.steps())
        plan.run()
