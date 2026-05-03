import re

def extract_year(file_path, text):
    # 1️⃣ filename
    match = re.search(r"(20\d{2})", file_path)
    if match:
        return match.group(1)

    # 2️⃣ content
    match = re.search(r"(20\d{2})", text)
    if match:
        return match.group(1)

    return "Unknown"