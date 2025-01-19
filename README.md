# Job Search Script Using Twitter API

This script helps you search for job postings related to DevOps roles and internships posted on Twitter within a specified time frame (default is the last 24 hours). It uses the Twitter API v2 via the Tweepy library.

---

# Features

- Searches for tweets containing keywords like "DevOps," "Engineer," "Internship," "Junior," "Fresher," "Hiring," and "Entry Level."
- Filters out retweets programmatically to show only original tweets.
- Retrieves tweet details, including the text, author ID, creation time, and a direct URL.
- Handles rate limits and retries automatically.

---

# Prerequisites

1. **Python Environment**: Install Python 3.7 or higher.
2. **Tweepy Library**: Install the Tweepy library for interacting with the Twitter API.
3. **dotenv Library**: Install the dotenv library to load environment variables from a `.env` file.
4. **Twitter Developer Account**: Obtain a Bearer Token by creating a Twitter developer account and setting up a project in the Twitter Developer Portal.

---

# Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Chirag-S-Kotian/jobify.git
   cd jobify
   ```

2. **Create a Virtual Environment**:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install tweepy python-dotenv
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the project directory.
   - Add your Twitter Bearer Token to the `.env` file:
     ```plaintext
     TWITTER_BEARER_TOKEN=your_twitter_bearer_token
     ```

5. **Run the Script**:
   ```bash
   python job.py
   ```

---

# Script Workflow

1. **Load Configuration**:
   The script uses the `dotenv` library to load the Twitter Bearer Token from the `.env` file.

2. **Define the Search Query**:
   - The query is set to search for DevOps-related jobs, internships, and entry-level roles.
   - Keywords include: `DevOps`, `Engineer`, `Internship`, `Junior`, `Fresher`, `Hiring`, and `Entry Level`.

3. **Call Twitter API v2**:
   - The `search_recent_tweets` method fetches tweets matching the query within the last 24 hours.
   - Filters out retweets and non-English tweets programmatically.

4. **Handle Rate Limits**:
   - Automatically waits and retries when rate limits are exceeded.

5. **Display Results**:
   - Outputs relevant job postings in a user-friendly format, including:
     - Tweet text
     - Author ID
     - Timestamp
     - Direct tweet URL

---

# Example Output

When run successfully, the script outputs something like this:

```plaintext
Searching Twitter jobs using API v2...

Found 2 relevant tweets:

1. Tweet: "We're hiring a Junior DevOps Engineer! Exciting opportunity for freshers. #DevOps #Hiring"
   Author ID: 12345678
   Created At: 2025-01-18T15:30:45+00:00
   URL: https://twitter.com/user/status/987654321

2. Tweet: "Looking for a DevOps intern to join our team. Apply now! #Internship"
   Author ID: 87654321
   Created At: 2025-01-18T18:20:30+00:00
   URL: https://twitter.com/user/status/123456789
```

---

# Customization

1. **Time Frame**:
   - Adjust the `start_time` in the `search_twitter_jobs_v2` function to change the time window.
     ```python
     start_time = (datetime.now() - timedelta(days=<number_of_days>)).isoformat("T") + "Z"
     ```

2. **Query**:
   - Modify the `query` variable in the `main()` function to include additional keywords or phrases.

3. **Max Results**:
   - Adjust the `max_results` parameter in the `search_recent_tweets` call (default is 20).

---

# Troubleshooting

1. **Rate Limits**:
   - If you encounter a rate limit error, the script will automatically wait and retry.

2. **Invalid Token**:
   - Ensure the Bearer Token in your `.env` file is correct and active.

3. **Query Errors**:
   - Ensure your query is supported by the Twitter API v2. Avoid unsupported operators like `-filter:retweets`.

---

# License

This project is open-source and available under the MIT License. Feel free to modify and use it for your own purposes.

---

# Contributions

Contributions are welcome! If you have suggestions or enhancements, feel free to submit a pull request.

---

# Disclaimer

This script is for educational purposes only. Ensure compliance with Twitter's API usage policies when using this script.

