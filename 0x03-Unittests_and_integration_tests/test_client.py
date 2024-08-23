#!/usr/bin/env python3
"""
Familiarize yourself with the client.GithubOrgClient class.
In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class and implement
 the test_org method.

This method should test that GithubOrgClient.org returns the
correct value.
Use @patch as a decorator to make sure get_json is called
 once with the expected argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize the test
 with a couple of org examples to pass to GithubOrgClient, in this order:
google
abc
Of course, no external HTTP calls should be made.
"""
import unittest
from typing import Mapping
from parameterized import parameterized
from unittest.mock import patch, MagicMock

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Mapping, mocked_fxn: MagicMock) -> None:
        """Tests the `org` method."""
        mocked_fxn.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_fxn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
