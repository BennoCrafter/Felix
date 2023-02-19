import requests


def show_commits():
    repo_owner = input("What's the name of the repo owner?:")
    repo_name = input("What's the name of the repo?:")

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"

    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print("Commit message:", commit["commit"]["message"])
            print("Author:", commit["commit"]["author"]["name"])
            print("---")
    else:
        print("Failed to retrieve commits. Response status code:", response.status_code)
