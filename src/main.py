from dotenv import load_dotenv
import os
from api import execute_query, RateLimiter
from data import write_csv, read_csv


def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv('NEW_RELIC_API_KEY')

    # Initialize rate limiter
    rate_limiter = RateLimiter(calls_per_minute=60)

    # Execute your core logic
    try:
        # Fetch data (possibly with pagination)
        results = fetch_all_data(rate_limiter)

        # Process and save results
        write_csv("output.csv", results)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()