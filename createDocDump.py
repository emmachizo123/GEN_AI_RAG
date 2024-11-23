

import os
import requests

def fetch_and_save_html(url):
    # Fetch the HTML content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    html_content = response.text

    # Define folder and file paths
    folder_path = "store-docs"
    file_path = os.path.join(folder_path, "psoriases")

    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)

    # Write or append HTML content to the file
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(html_content)
        file.write("\n")  # Add a newline after appending content

    print(f"Content successfully written to {file_path}")

# Example usage
url ="https://www.ncbi.nlm.nih.gov/books/NBK579274/" # Replace with the actual URL
fetch_and_save_html(url)