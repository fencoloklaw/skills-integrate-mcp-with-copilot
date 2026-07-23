import unittest

from src.app import activities


class ActivityCatalogTests(unittest.TestCase):
    def test_github_skills_activity_is_present(self):
        self.assertIn("GitHub Skills", activities)


if __name__ == "__main__":
    unittest.main()
