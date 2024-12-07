import requests
import argparse
import os

# Function to handle the challenge submission
def submit_challenge(api_url, github_token, file_path, payload):
    try:
        # Open the file in binary mode
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f, "application/zip")}
            
            # Set headers, including the Authorization header
            headers = {
                "Authorization": f"Bearer {github_token}"
            }
            
            # Perform the POST request
            response = requests.post(api_url, data=payload, files=files, headers=headers)

            # Check the response status code
            if response.status_code == 200:
                print("Challenge submitted successfully!")
                print("Response:", response.json())
            else:
                print(f"Failed to submit challenge. Status code: {response.status_code}")
                print("Response:", response.text)

    except FileNotFoundError:
        print("The specified file was not found. Please check the file path.")
    except requests.RequestException as e:
        print(f"An error occurred during the request: {e}")

# Main function to parse arguments and call the submission function
def main():
    parser = argparse.ArgumentParser(description="Submit a challenge to the API.")
    parser.add_argument("url", help="The API endpoint URL.")
    parser.add_argument("github_token", help="The GitHub authorization token.")
    parser.add_argument("file_path", help="The path to the ZIP file to upload.")
    parser.add_argument("--title", required=True, help="The title of the challenge.")
    parser.add_argument("--link", required=True, help="The repository link for the challenge.")
    parser.add_argument("--points", type=int, required=True, help="The points for the challenge.")
    parser.add_argument("--total_test_case", type=int, required=True, help="The total test cases for the challenge.")
    parser.add_argument("--tags", nargs="+", required=True, help="A list of tags for the challenge.")

    args = parser.parse_args()

    # Prepare the payload
    payload = {
        "title": args.title,
        "link": args.link,
        "points": args.points,
        "total_test_case": args.total_test_case,
        "tags": args.tags
    }

    # Call the submission function
    submit_challenge(args.url, args.github_token, args.file_path, payload)

main()