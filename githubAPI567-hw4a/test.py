
import unittest
from unittest.mock import patch, MagicMock
from github_api import get_repo_and_commits

class TestGitHubAPIMocking(unittest.TestCase):

    @patch('github_api.requests.get') 
    def test_valid_user_mocked(self, mock_get):
        """
        Test using a mock response to simulate a valid user with multiple repos.
        No actual calls to GitHub are made.
        """

        mock_repos_response = [
            {"name": "MockRepo1"},
            {"name": "MockRepo2"}
        ]

        mock_commits_response_1 = [{}, {}, {}]  # e.g., 3 commits
        mock_commits_response_2 = [{}, {}]      # e.g., 2 commits

        mock_response_1 = MagicMock()
        mock_response_1.json.return_value = mock_repos_response
        mock_response_1.raise_for_status = MagicMock()

        mock_response_2 = MagicMock()
        mock_response_2.json.return_value = mock_commits_response_1
        mock_response_2.raise_for_status = MagicMock()

        mock_response_3 = MagicMock()
        mock_response_3.json.return_value = mock_commits_response_2
        mock_response_3.raise_for_status = MagicMock()

        mock_get.side_effect = [mock_response_1, mock_response_2, mock_response_3]

        result = get_repo_and_commits("someuser")

        self.assertEqual(len(result), 2)  # should be 2 repos
        self.assertIn("Repo: MockRepo1 Number of commits: 3", result[0])
        self.assertIn("Repo: MockRepo2 Number of commits: 2", result[1])

    @patch('github_api.requests.get')
    def test_invalid_user_mocked(self, mock_get):
        """
        Test using a mock response to simulate an invalid user (e.g., 404 error).
        """

        # Mock a response that raises an HTTP error
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_repo_and_commits("invaliduser")

if __name__ == "__main__":
    unittest.main()
