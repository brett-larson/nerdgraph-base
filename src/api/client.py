import requests


def execute_query(query: str, variables: dict = None, api_key: str = None) -> dict:
    """Execute a single GraphQL query"""
    headers = {
        "API-Key": api_key,
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api.newrelic.com/graphql",
        json={"query": query, "variables": variables},
        headers=headers
    )

    return response.json()