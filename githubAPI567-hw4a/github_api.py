
import requests
import json

def get_repo_and_commits(user_id):
    """
    Given a GitHub username, returns a list of strings where each string
    contains the repo name and the number of commits.
    Format: "Repo: <repo_name> Number of commits: <commit_count>"
    """

    if not isinstance(user_id, str) or not user_id.strip():
        raise ValueError("Invalid GitHub user ID provided")

    # 1. Get all repos for the user
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    repos_response.raise_for_status()
    repos_data = repos_response.json()

    results = []

    for repo in repos_data:
        repo_name = repo['name']

        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        commits_response.raise_for_status()
        commits_data = commits_response.json()

        commit_count = len(commits_data)

        # 3. Create the output string
        results.append(f"Repo: {repo_name} Number of commits: {commit_count}")

    return results

def main():
    user_id = input("Enter a GitHub user ID: ")
    try:
        repo_commits_list = get_repo_and_commits(user_id)
        for item in repo_commits_list:
            print(item)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
