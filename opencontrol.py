import compliancelib
from github import Github, RateLimitExceededException
import os
import requests_cache
import sys

requests_cache.install_cache("requests_cache")

token = os.getenv("GITHUB_TOKEN")
g = Github(token)

results = g.search_code("path:/ filename:opencontrol.yaml components")
# get as many as we can before hitting the rate limit
repos = set()
try:
    for result in results:
        repos.add(result.repository.full_name)
except RateLimitExceededException as err:
    print(err, file=sys.stderr)

sorted_repos = list(repos)
sorted_repos.sort()
print(sorted_repos)

systems = []
for result in results:
    print(result.path)
    print(result.repository.html_url)

    sp = compliancelib.SystemCompliance()
    try:
        sp.load_system_from_opencontrol_repo(result.repository.html_url)
    except Exception as err:
        print(
            "Failed to import {}.".format(result.repository.full_name),
            err,
            file=sys.stderr,
        )
        continue

    systems.append(sp)

print(len(systems))
