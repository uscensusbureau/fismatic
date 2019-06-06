import compliancelib
from fismatic.control import Control
from fismatic.control_set import ControlSet
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
    """A generator that yields instances of compliancelib.SystemCompliance."""
    results = opencontrol_files(github_client)
    for result in results:
        print(result.path)
        print(result.repository.html_url)

        system = opencontrol_system(result)
        if system:
            yield system


def controls_for(system):
    """A generator that yields instances of compliancelib.nist800_53.NIST800_53."""
    control_ids = compliancelib.NIST800_53.get_control_ids()
    for control_id in control_ids:
        try:
            control = system.control(control_id)
        except Exception:
            # control not present, or some other issue
            continue
        yield control


def cl_to_fm_controls(cl_controls):
    """Converts compliancelib controls into FISMAtic ones."""
    for cl_control in cl_controls:
        fm_control = Control(name=cl_control.id)
        # TODO handle multiple parts
        fm_control.implementation = {"": cl_control.implementation_narrative}
        yield fm_control


if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)

    systems = opencontrol_systems(g)
    for system in systems:
        cl_controls = controls_for(system)
        fm_controls = cl_to_fm_controls(cl_controls)
        control_set = ControlSet(fm_controls)
        print(control_set.top_entities())
