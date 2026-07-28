# User-Agent Generator

A reusable Python module for generating random User-Agent strings using the [`fake-useragent`](https://pypi.org/project/fake-useragent/) library.

The module provides a simple API for generating one or multiple User-Agent strings and allows filtering by operating system and browser.

## Features

* Generate a single random User-Agent
* Generate multiple random User-Agents
* Filter User-Agents by operating system
* Filter User-Agents by browser
* Uses `fake-useragent` for User-Agent generation
* Reusable from any Python file in your project
* Simple functional API
* Optional object-oriented API
* Input validation for unsupported operating systems and browsers

## Supported Operating Systems

The following operating systems are supported:

| Input     | Operating System |
| --------- | ---------------- |
| `windows` | Windows          |
| `macos`   | macOS            |
| `linux`   | Linux            |
| `android` | Android          |
| `ios`     | iOS              |

## Supported Browsers

The following browsers are supported:

| Input     | Browser |
| --------- | ------- |
| `chrome`  | Chrome  |
| `firefox` | Firefox |
| `edge`    | Edge    |
| `safari`  | Safari  |

## Installation

Install the required dependency using pip:

```bash
pip install fake-useragent
```

Or upgrade to the latest available version:

```bash
pip install -U fake-useragent
```

If you are using a `requirements.txt` file, add:

```text
fake-useragent
```

Then install the project dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

A recommended project structure is:

```text
your_project/
│
├── utils/
│   ├── __init__.py
│   └── user_agents.py
│
├── main.py
│
└── requirements.txt
```

The `user_agents.py` file contains the User-Agent generator module.

---

# Basic Usage

Import the functions from the module:

```python
from utils.user_agents import (
    get_random_user_agent,
    get_random_user_agents,
)
```

## Generate One Random User-Agent

To generate a completely random User-Agent:

```python
from utils.user_agents import get_random_user_agent

ua = get_random_user_agent()

print(ua)
```

Example output:

```text
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/...
```

The returned User-Agent is generated using `fake-useragent`.

---

# Generate a User-Agent for a Specific Operating System

You can specify the operating system using the `os` parameter.

## Windows

```python
ua = get_random_user_agent(
    os="windows"
)

print(ua)
```

## macOS

```python
ua = get_random_user_agent(
    os="macos"
)

print(ua)
```

## Linux

```python
ua = get_random_user_agent(
    os="linux"
)

print(ua)
```

## Android

```python
ua = get_random_user_agent(
    os="android"
)

print(ua)
```

## iOS

```python
ua = get_random_user_agent(
    os="ios"
)

print(ua)
```

---

# Generate a User-Agent for a Specific Browser

You can also specify a browser using the `browser` parameter.

## Chrome

```python
ua = get_random_user_agent(
    browser="chrome"
)

print(ua)
```

## Firefox

```python
ua = get_random_user_agent(
    browser="firefox"
)

print(ua)
```

## Edge

```python
ua = get_random_user_agent(
    browser="edge"
)

print(ua)
```

## Safari

```python
ua = get_random_user_agent(
    browser="safari"
)

print(ua)
```

---

# Combine Operating System and Browser Filters

You can specify both `os` and `browser`.

For example, to generate a Chrome User-Agent for Windows:

```python
ua = get_random_user_agent(
    os="windows",
    browser="chrome"
)

print(ua)
```

Chrome on macOS:

```python
ua = get_random_user_agent(
    os="macos",
    browser="chrome"
)

print(ua)
```

Firefox on Linux:

```python
ua = get_random_user_agent(
    os="linux",
    browser="firefox"
)

print(ua)
```

Safari on iOS:

```python
ua = get_random_user_agent(
    os="ios",
    browser="safari"
)

print(ua)
```

---

# Generate Multiple User-Agents

Use `get_random_user_agents()` when you need multiple User-Agent strings.

The first argument is the number of User-Agents to generate.

```python
from utils.user_agents import get_random_user_agents

agents = get_random_user_agents(10)

for ua in agents:
    print(ua)
```

This generates 10 random User-Agent strings.

---

# Generate Multiple User-Agents for a Specific OS

For example, generate 10 User-Agents for Windows:

```python
agents = get_random_user_agents(
    count=10,
    os="windows"
)

for ua in agents:
    print(ua)
```

Generate 20 Linux User-Agents:

```python
agents = get_random_user_agents(
    count=20,
    os="linux"
)
```

Generate 15 Android User-Agents:

```python
agents = get_random_user_agents(
    count=15,
    os="android"
)
```

---

# Generate Multiple User-Agents for a Specific Browser

For example, generate 10 Chrome User-Agents:

```python
agents = get_random_user_agents(
    count=10,
    browser="chrome"
)

for ua in agents:
    print(ua)
```

Generate 10 Firefox User-Agents:

```python
agents = get_random_user_agents(
    count=10,
    browser="firefox"
)
```

---

# Generate Multiple User-Agents with OS and Browser Filters

You can combine both filters.

For example, generate 10 Chrome User-Agents for Windows:

```python
agents = get_random_user_agents(
    count=10,
    os="windows",
    browser="chrome"
)

for ua in agents:
    print(ua)
```

Generate 5 Firefox User-Agents for Linux:

```python
agents = get_random_user_agents(
    count=5,
    os="linux",
    browser="firefox"
)
```

Generate 10 Safari User-Agents for iOS:

```python
agents = get_random_user_agents(
    count=10,
    os="ios",
    browser="safari"
)
```

---

# Using the Module with Requests

The module can be used with the Python `requests` library.

```python
import requests

from utils.user_agents import get_random_user_agent


headers = {
    "User-Agent": get_random_user_agent(
        os="windows",
        browser="chrome"
    )
}

response = requests.get(
    "https://example.com",
    headers=headers
)

print(response.status_code)
```

You can also generate a new User-Agent for every request:

```python
import requests

from utils.user_agents import get_random_user_agent


url = "https://example.com"

for _ in range(10):

    headers = {
        "User-Agent": get_random_user_agent()
    }

    response = requests.get(
        url,
        headers=headers
    )

    print(
        response.status_code,
        headers["User-Agent"]
    )
```

> Use this functionality responsibly and make sure your requests comply with the target website's Terms of Service and applicable laws.

---

# Using a Session

For projects that make multiple HTTP requests, you can use a `requests.Session`.

```python
import requests

from utils.user_agents import get_random_user_agent


session = requests.Session()

session.headers.update({
    "User-Agent": get_random_user_agent(
        os="windows",
        browser="chrome"
    )
})

response = session.get(
    "https://example.com"
)

print(response.status_code)
```

---

# Object-Oriented API

The module also provides a reusable `UserAgentGenerator` class.

```python
from utils.user_agents import UserAgentGenerator


generator = UserAgentGenerator()

ua = generator.get()

print(ua)
```

Generate a User-Agent for Windows:

```python
ua = generator.get(
    os="windows"
)

print(ua)
```

Generate Chrome on Windows:

```python
ua = generator.get(
    os="windows",
    browser="chrome"
)

print(ua)
```

Generate multiple User-Agents:

```python
agents = generator.get_many(
    count=10
)

for ua in agents:
    print(ua)
```

Generate multiple Chrome User-Agents for Windows:

```python
agents = generator.get_many(
    count=10,
    os="windows",
    browser="chrome"
)
```

---

# Complete Example

The following example demonstrates a complete workflow:

```python
import requests

from utils.user_agents import get_random_user_agent


def make_request(url: str):

    user_agent = get_random_user_agent(
        os="windows",
        browser="chrome"
    )

    headers = {
        "User-Agent": user_agent
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    return response


response = make_request(
    "https://example.com"
)

print("Status:", response.status_code)
print("User-Agent:", response.request.headers["User-Agent"])
```

---

# API Reference

## `get_random_user_agent()`

Generate a single random User-Agent.

### Signature

```python
get_random_user_agent(
    os: str | None = None,
    browser: str | None = None,
) -> str
```

### Parameters

#### `os`

Optional operating system filter.

Available values:

```text
windows
macos
linux
android
ios
```

#### `browser`

Optional browser filter.

Available values:

```text
chrome
firefox
edge
safari
```

### Returns

```python
str
```

A randomly generated User-Agent string.

### Example

```python
ua = get_random_user_agent(
    os="windows",
    browser="chrome"
)
```

---

## `get_random_user_agents()`

Generate multiple random User-Agent strings.

### Signature

```python
get_random_user_agents(
    count: int,
    os: str | None = None,
    browser: str | None = None,
) -> list[str]
```

### Parameters

#### `count`

Number of User-Agent strings to generate.

Must be greater than `0`.

#### `os`

Optional operating system filter.

#### `browser`

Optional browser filter.

### Returns

```python
list[str]
```

A list containing the requested number of User-Agent strings.

### Example

```python
agents = get_random_user_agents(
    count=20,
    os="windows",
    browser="chrome"
)
```

---

## `UserAgentGenerator`

Reusable class for generating User-Agent strings.

### Create an instance

```python
from utils.user_agents import UserAgentGenerator

generator = UserAgentGenerator()
```

### Generate one User-Agent

```python
generator.get()
```

### Generate one filtered User-Agent

```python
generator.get(
    os="windows",
    browser="chrome"
)
```

### Generate multiple User-Agents

```python
generator.get_many(
    count=10,
    os="linux",
    browser="firefox"
)
```

---

# Error Handling

The module validates the provided operating system and browser.

For example:

```python
get_random_user_agent(
    os="unknown"
)
```

will raise:

```text
ValueError: Unsupported OS: unknown
```

Similarly:

```python
get_random_user_agent(
    browser="unknown"
)
```

will raise:

```text
ValueError: Unsupported browser: unknown
```

The `count` parameter must also be greater than zero:

```python
get_random_user_agents(
    count=0
)
```

will raise:

```text
ValueError: count must be greater than 0
```

---

# Recommended Usage

For most applications, the functional API is the simplest approach:

```python
from utils.user_agents import get_random_user_agent


user_agent = get_random_user_agent(
    os="windows",
    browser="chrome"
)
```

For larger applications where you want to maintain a dedicated generator instance, use:

```python
from utils.user_agents import UserAgentGenerator


generator = UserAgentGenerator()

user_agent = generator.get(
    os="windows",
    browser="chrome"
)
```

---

# Requirements

* Python 3.9+
* `fake-useragent`

Install the dependency with:

```bash
pip install fake-useragent
```
