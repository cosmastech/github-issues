import os

from dotenv import load_dotenv
from github import (Github, Auth)


def _get_github_client() -> Github:
    load_dotenv()
    if not (github_token := os.getenv('GITHUB_ISSUES_API_TOKEN', None)):
        raise Exception("You must set GITHUB_ISSUES_API_TOKEN as an env variable")

    auth = Auth.Token(github_token)

    return Github(auth=auth, per_page=100)


def _get_lang() -> str | None:
    return 'python'


def main() -> None:
    github: Github = _get_github_client()

    """
    label = Label.Label(attributes={
        "name": "good first issue"
    })
    issues = github.get_user().get_issues(
        filter="all",
        sort="created",
        direction="desc",
        labels=[label]
        #state="open",
        #labels=["good first issue"],
    )
    """

    issues = github.search_issues(
        query=f'is:issue state:open language:{_get_lang()} label:"good first issue" -linked:pr no:assignee',
        sort="created",
        order="desc",
    )

    print('number of issues: ' + str(issues.totalCount))
    for issue in issues:
        print(
            f"""
Title: {issue.title}
URL: {issue.html_url}
""")
    pass


if __name__ == '__main__':
    main()
