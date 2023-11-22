import re
import csv

def extract_contacts(text):
    # Regular expression for extracting mobile numbers
    mobile_pattern = re.compile(r'\b\d{10}\b|\b\d{5}[-\.\s]?\d{5}\b')

    # Regular expression for extracting email addresses
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    # Find all matches for mobile numbers and email addresses
    mobile_numbers = mobile_pattern.findall(text)
    email_addresses = email_pattern.findall(text)

    return mobile_numbers, email_addresses

def write_to_csv(filename, mobile_numbers, email_addresses):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Mobile Numbers', 'Email Addresses'])
        for mobile, email in zip(mobile_numbers, email_addresses):
            writer.writerow([mobile, email])

if __name__ == "__main__":
    # Read the text data from the file
    with open('data.txt', 'r') as file:
        data = file.read()

    # Extract mobile numbers and email addresses
    mobile_numbers, email_addresses = extract_contacts(data)

    # Write the results to a CSV file
    write_to_csv('contacts.csv', mobile_numbers, email_addresses)

    print("Extraction completed. Check 'contacts.csv' for results.")
