from utils.user_agents import get_random_user_agent

headers = {
    "User-Agent": get_random_user_agent(
        # os="windows",
        # browser="chrome",
    )
}

print(headers)
