from github import Github

from datetime import datetime
import json
import logging
import time

from io_utils import write_to_json

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def search():
    """
    Search GitHub
    """
    with open('./config.json') as config_f:
        config = json.load(config_f)

    logging.info("Config file read successfully.")

    access_token = config['TOKEN']

    gh = Github(access_token)

    repos = gh.search_repositories("",sort='stars',order='desc',
                                   **{
                                       'archived': False,
                                       'fork': False,
                                       'is': 'public',
                                       'language': 'Python',
                                       '-topic': 'tutorial',
                                       'stars': '>500',
                                       'created': '2019-10-01..2022-12-31'
                                   })

    logging.info(f"Remaining requests: {gh.rate_limiting[0]}/{gh.rate_limiting[1]}")
    logging.info(
        f"Rate will reset on: {datetime.utcfromtimestamp(gh.rate_limiting_resettime).strftime('%Y-%m-%d %H:%M:%S')}"
    )

    logging.info(f"Total number of repos: {repos.totalCount}")

    list_of_repos = []

    # default page size is 30
    total_pages = (repos.totalCount // 30) + 1
    for i in range(total_pages):
        if gh.rate_limiting[0] == 1:
            time.sleep(60)
        page_repos = repos.get_page(i)  # returns a list of repos
        for repo in page_repos:
            tmp = {
                'full_name': repo.full_name,
                'url': repo.html_url,
                'contributors': repo.contributors_url,
                'issues': repo.issues_url,
                'stars': repo.stargazers_count,
                'size': repo.size
            }
            list_of_repos.append(tmp)

        logging.info(f"Remaining requests: {gh.rate_limiting[0]}/{gh.rate_limiting[1]}")
        logging.info(
            f"Rate will reset on: {datetime.utcfromtimestamp(gh.rate_limiting_resettime).strftime('%Y-%m-%d %H:%M:%S')}"
        )

    return {"repos": list_of_repos}


def main():
    repos = search()
    write_to_json(repos, "top1000_repos")

if __name__ == '__main__':
    main()