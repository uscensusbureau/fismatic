from github import Github, RateLimitExceededException
import os
import requests_cache
import sys

requests_cache.install_cache("requests_cache")

token = os.getenv("GITHUB_TOKEN")
g = Github(token)

# The GitHub code search API requires one or more org/user to be specified.
# https://developer.github.com/changes/2013-10-18-new-code-search-requirements/#new-validation-rule
# The following is a curated list. To find more, go to:
# https://github.com/search?utf8=%E2%9C%93&q=schema_version+satisfies+control_key+language%3Ayaml&type=Code
users = [
    "18F",
    "ComplianceAsCode",
    "corbaltcode",
    "docker",
    "GovReady",
    "GSA",
    "jenglish",
    "jmmcnj",
    "m3brown",
    "madhugilla",
    "nsagoo-pivotal",
    "opencontrol",
    "redhatrises",
    "SecurityCentral",
    "shawndwells",
    "superbrilliant",
    "weirdscience",
]
users_q = " ".join("user:{}".format(user) for user in users)
results = g.search_code("schema_version satisfies control_key language:yaml " + users_q)

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
