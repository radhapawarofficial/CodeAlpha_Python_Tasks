# automation_toolkit.py

import os
import shutil
import re
import requests

# ----------------------------
# 1️⃣ Move all .jpg files
# ----------------------------
def move_jpg_files(source_folder="images", destination_folder="images/moved_images"):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_count = 0
    for file in os.listdir(source_folder):
        if file.lower().endswith(".jpg"):
            shutil.move(
                os.path.join(source_folder, file),
                os.path.join(destination_folder, file)
            )
            moved_count += 1

    print(f"All JPG files moved successfully. Total moved: {moved_count}")


# ----------------------------
# 2️⃣ Extract emails from a file
# ----------------------------
def extract_emails(input_file="sample_data/emails.txt", output_file="sample_data/output_emails.txt"):
    # Ensure sample_data folder exists
    if not os.path.exists("sample_data"):
        os.makedirs("sample_data")

    # Create sample input file if it doesn't exist
    if not os.path.exists(input_file):
        with open(input_file, "w", encoding="utf-8") as f:
            f.write("contact@example.com\nsupport@company.in\nhr@organization.org\n")
        print(f"Sample input file created at '{input_file}'")

    # Read file and extract emails
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    # Save emails to output file
    with open(output_file, "w", encoding="utf-8") as file:
        for email in set(emails):
            file.write(email + "\n")

    print(f"Email extraction completed. Total emails found: {len(emails)}")
    print(f"Extracted emails saved to '{output_file}'")


# ----------------------------
# 3️⃣ Extract title from URL or local HTML file
# ----------------------------
def scrape_title(source="https://example.com", output_file="webpage_title.txt"):
    try:
        if os.path.exists(source):  # local HTML file
            with open(source, "r", encoding="utf-8") as f:
                html = f.read()
        else:  # URL
            response = requests.get(source)
            if response.status_code != 200:
                print(f"Failed to fetch webpage. Status code: {response.status_code}")
                return
            html = response.text

        # Extract title
        title_match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)
        title = title_match.group(1) if title_match else "Title not found"

        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(title)

        print(f"Title saved to '{output_file}': {title}")

    except Exception as e:
        print(f"Error: {e}")


# ----------------------------
# 4️⃣ Main Menu
# ----------------------------
def main():
    print("=== Python Task Automation Toolkit ===")
    print("1. Move JPG files")
    print("2. Extract Email Addresses")
    print("3. Extract Title from URL or HTML file")

    choice = input("Select an option (1-3): ")

    if choice == "1":
        move_jpg_files()
    elif choice == "2":
        extract_emails()
    elif choice == "3":
        source = input("Enter URL or local HTML file path: ")
        scrape_title(source)
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
