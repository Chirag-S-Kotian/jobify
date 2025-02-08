import tweepy
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os

load_dotenv()

# Twitter Configuration
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Function to fetch Twitter job postings using API v2
def search_twitter_jobs_v2(query):
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    # Define time window (last 24 hours)
    start_time = (datetime.now() - timedelta(days=4)).isoformat("T") + "Z"
    
    try:
        # Search for tweets
        response = client.search_recent_tweets(
            query=query,
            start_time=start_time,
            max_results=10,  # Adjust based on your API plan
            tweet_fields=['created_at', 'text', 'author_id', 'lang']
        )
        
        # Process the results
        jobs = []
        if response.data:
            for tweet in response.data:
                # Skip retweets (tweets starting with "RT @")
                if not tweet.text.startswith("RT @"):
                    # Filter relevant tweets based on content
                    if tweet.lang == 'en' and "devops" in tweet.text.lower():
                        if any(keyword in tweet.text.lower() for keyword in ["hiring", "internship", "entry level", "junior"]):
                            jobs.append({
                                'text': tweet.text,
                                'author_id': tweet.author_id,
                                'created_at': tweet.created_at,
                                'url': f"https://twitter.com/user/status/{tweet.id}"
                            })
        return jobs
    
    except tweepy.TooManyRequests as e:
        # Handle rate limits
        reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 60))
        wait_time = reset_time - int(time.time())
        print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
        time.sleep(wait_time + 1)  # Wait and retry
        return search_twitter_jobs_v2(query)
    except tweepy.BadRequest as e:
        print(f"Bad Request Error: {e}")
        return []
    except tweepy.TweepError as e:
        print(f"Tweepy Error: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Main function
def main():
    # Search query for DevOps-specific roles and internships
    query = "DevOps (Engineer OR Internship OR Junior OR Fresher OR Hiring OR Entry Level)"
    
    print("\nSearching Twitter jobs using API v2...")
    twitter_jobs = search_twitter_jobs_v2(query)
    
    # Display the results in a readable format
    if twitter_jobs:
        print(f"\nFound {len(twitter_jobs)} relevant tweets:\n")
        for i, job in enumerate(twitter_jobs, 1):
            print(f"{i}. Tweet: {job['text']}")
            print(f"   Author ID: {job['author_id']}")
            print(f"   Created At: {job['created_at']}")
            print(f"   URL: {job['url']}\n")
    else:
        print("No relevant job postings found in the last 24 hours.")

if __name__ == "__main__":
    main()