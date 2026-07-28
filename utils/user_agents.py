"""
User-Agent Generator

Generate random User-Agent strings using fake-useragent.

Supported operating systems:
    - windows
    - macos
    - linux
    - android
    - ios

Supported browsers:
    - chrome
    - firefox
    - edge
    - safari
"""

import random
from typing import Optional

from fake_useragent import UserAgent


class UserAgentGenerator:
    """
    Generate random User-Agent strings using fake-useragent.
    """

    SUPPORTED_OS = {
        "windows": "Windows",
        "macos": "Mac OS X",
        "linux": "Linux",
        "android": "Android",
        "ios": "iOS",
    }

    SUPPORTED_BROWSERS = {
        "chrome": "Chrome",
        "firefox": "Firefox",
        "edge": "Edge",
        "safari": "Safari",
    }

    def __init__(self):
        self.ua = UserAgent()

    def get(
        self,
        os: Optional[str] = None,
        browser: Optional[str] = None,
    ) -> str:
        """
        Generate one random User-Agent.

        Examples:

            get()

            get(os="windows")

            get(
                os="windows",
                browser="chrome"
            )
        """

        # If no filters are provided,
        # use fake-useragent's built-in random selection.
        if os is None and browser is None:
            return self.ua.random

        # Get User-Agent database.
        agents = self.ua.data_browsers

        # Normalize OS.
        os_name = None

        if os is not None:
            os = os.lower().strip()

            if os not in self.SUPPORTED_OS:
                raise ValueError(
                    f"Unsupported OS: {os}. "
                    f"Supported OS: "
                    f"{list(self.SUPPORTED_OS.keys())}"
                )

            os_name = self.SUPPORTED_OS[os].lower()

        # Normalize browser.
        browser_name = None

        if browser is not None:
            browser = browser.lower().strip()

            if browser not in self.SUPPORTED_BROWSERS:
                raise ValueError(
                    f"Unsupported browser: {browser}. "
                    f"Supported browsers: "
                    f"{list(self.SUPPORTED_BROWSERS.keys())}"
                )

            browser_name = self.SUPPORTED_BROWSERS[browser].lower()

        # Filter User-Agents.
        filtered_agents = []

        for agent in agents:

            # fake-useragent returns dictionaries.
            if not isinstance(agent, dict):
                continue

            agent_os = str(agent.get("os", "")).lower()

            agent_browser = str(agent.get("browser", "")).lower()

            # Check OS.
            if os_name is not None:
                if os_name not in agent_os:
                    continue

            # Check browser.
            if browser_name is not None:
                if browser_name not in agent_browser:
                    continue

            filtered_agents.append(agent)

        # No matching User-Agent.
        if not filtered_agents:
            raise ValueError(
                "No matching User-Agent found for " f"os={os!r}, browser={browser!r}"
            )

        # Pick random entry.
        selected = random.choice(filtered_agents)

        # Extract User-Agent string.
        return selected["useragent"]

    def get_many(
        self,
        count: int,
        os: Optional[str] = None,
        browser: Optional[str] = None,
    ) -> list[str]:
        """
        Generate multiple random User-Agent strings.

        User-Agents can repeat.

        Example:

            get_many(10)

            get_many(
                10,
                os="windows",
                browser="chrome"
            )
        """

        if count < 1:
            raise ValueError("count must be greater than 0")

        return [
            self.get(
                os=os,
                browser=browser,
            )
            for _ in range(count)
        ]


# ============================================================
# Global generator instance
# ============================================================

user_agents = UserAgentGenerator()


# ============================================================
# Public helper functions
# ============================================================


def get_random_user_agent(
    os: Optional[str] = None,
    browser: Optional[str] = None,
) -> str:
    """
    Generate one random User-Agent.
    """

    return user_agents.get(
        os=os,
        browser=browser,
    )


def get_random_user_agents(
    count: int,
    os: Optional[str] = None,
    browser: Optional[str] = None,
) -> list[str]:
    """
    Generate multiple random User-Agent strings.
    """

    return user_agents.get_many(
        count=count,
        os=os,
        browser=browser,
    )
