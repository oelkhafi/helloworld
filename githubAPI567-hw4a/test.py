
import unittest
from github_api import get_repo_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        """Test that a valid user returns a non-empty list."""
        user_id = "richkempinski"
        result = get_repo_and_commits(user_id)
        self.assertTrue(len(result) > 0, "Expected at least one repository")

    def test_repo_format(self):
        """Test that the returned strings follow the desired format."""
        user_id = "richkempinski"
        result = get_repo_and_commits(user_id)
        for item in result:
            self.assertIn("Repo: ", item)
            self.assertIn("Number of commits: ", item)

    def test_invalid_user(self):
        """Test passing a non-existent user, expecting 404 or request failure."""
        invalid_user_id = "thisuserdoesnotexistandhopefullyneverwill123456789"
        with self.assertRaises(Exception):
            get_repo_and_commits(invalid_user_id)

    def test_empty_string(self):
        """Test passing an empty string as user_id."""
        with self.assertRaises(ValueError):
            get_repo_and_commits("")

    def test_non_string(self):
        """Test passing a non-string type."""
        with self.assertRaises(ValueError):
            get_repo_and_commits(1234)

if __name__ == '__main__':
    unittest.main()
