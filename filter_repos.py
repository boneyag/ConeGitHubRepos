import re
import logging
import json
import time
from datetime import datetime

from github import Github

from io_utils import read_from_json, write_to_json

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def filter_repos(repo_list):
    with open('./config.json') as config_f:
        config = json.load(config_f)

    logging.info("Config file read successfully.")

    access_token = config['TOKEN']

    gh = Github(access_token)

    list_of_repos = []

    for list_item in repo_list:
        # comply with secondary rate limit
        if gh.rate_limiting[0] == 1:
            time.sleep(60)

        repo = gh.get_repo(list_item['full_name'])
        # analyze the repo information to see if it is a candidate
        if repo.has_issues: # check if the repo has issues as we need to analyze issues to find API misuse
            topics = repo.get_topics() # analyze the topics to filter tutorials and educational projects
            logging.info(f"Topics: {topics}")
            for topic in topics:
                if re.search(r'.*tutorial.*', topic):
                    break
                if re.search(r'.*education.*', topic):
                    break

            tmp = {
                'full_name': list_item['full_name'],
                'url': list_item['url'],
                'topics': topics,
                'contributors': list_item['contributors'],
                'issues': list_item['issues'],
                'stars': list_item['stars'],
                'size': list_item['size']
            }
            list_of_repos.append(tmp)

        logging.info(f"Remaining requests: {gh.rate_limiting[0]}/{gh.rate_limiting[1]}")
        logging.info(
            f"Rate will reset on: {datetime.utcfromtimestamp(gh.rate_limiting_resettime).strftime('%Y-%m-%d %H:%M:%S')}"
        )

    logging.info(f"Total number of repos after secondary filtering: {len(list_of_repos)}")

    return {"repos": list_of_repos}


def main():
    repos = read_from_json("top1000_repos")
    filtered_repos = filter_repos(repos['repos'])
    write_to_json(filtered_repos, "filter_repos")


if __name__ == '__main__':
    main()
