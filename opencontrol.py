import compliancelib
from github import Github, RateLimitExceededException
import os
import requests_cache
import sys

requests_cache.install_cache("requests_cache")


def opencontrol_files(github_client):
    # only pull in top-level opencontrol.yaml files for now, for simplicity
    return github_client.search_code("path:/ filename:opencontrol.yaml components")


def opencontrol_system(file_result):
    sp = compliancelib.SystemCompliance()
    repo = file_result.repository
    try:
        sp.load_system_from_opencontrol_repo(repo.html_url)
    except Exception as err:
        print("Failed to import {}.".format(repo.full_name), file=sys.stderr)
        return None

    return sp


def opencontrol_systems(github_client):
    results = opencontrol_files(github_client)
    systems = []
    for result in results:
        print(result.path)
        print(result.repository.html_url)

        system = opencontrol_system(result)
        if system:
            systems.append(system)

    return systems


if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    systems = opencontrol_systems(g)
    print(len(systems))
