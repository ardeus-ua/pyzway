import unittest
import zway.controller


class TestZwayController(unittest.TestCase):

    def test_create_controller(self):
        zwc = zway.controller.Controller(baseurl="http://localhost")


if __name__ == '__main__':
    unittest.main()
