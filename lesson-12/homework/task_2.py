

from bs4 import BeautifulSoup
import requests
import sqlite3
import csv

# Define the URL
url = 'https://realpython.github.io/fake-jobs'

# Fetch the content of the page
response = requests.get(url)
html_content = response.text

# Parse the content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract job titles, company names, and locations
job_titles = soup.find_all("h2")
company_names = soup.find_all("h3")
locations = [location.text.strip() for location in soup.find_all("p", class_="location")]

# Extract the apply links
base_urls = [x.get("href") for x in soup.find_all("a") if x.text == "Apply"]

# Get job descriptions by visiting each apply URL
job_descriptions = []
for base_url in base_urls:
    res = requests.get(base_url)
    soup2 = BeautifulSoup(res.text, "html.parser")
    raw_info = BeautifulSoup(str(soup2.find_all("div", class_="content")), "html.parser")
    job_descriptions.append(raw_info.find("p").text if raw_info.find("p") else "No description available")

# Establish a connection to the SQLite database
with sqlite3.connect("lesson-12/homework/jobs.db") as connection:
    cursor = connection.cursor()

    # Create the jobs table if it doesn't already exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jobs (
        JobTitle TEXT,
        CompanyName TEXT,
        Location TEXT,
        Description TEXT,
        ApplicationLink TEXT,
        UNIQUE(JobTitle, CompanyName, Location)
    );
    """)

    # Prepare job data
    jobs = []
    for i in range(len(job_titles)):
        job = { 
            "jobTitle": job_titles[i].text.strip(),
            "companyName": company_names[i].text.strip(),
            "Location": locations[i],
            "Description": job_descriptions[i],
            "ApplicationLink": base_urls[i]
        }
        jobs.append(job)

    # Insert or update job listings into the database
    for job in jobs:
        job_title = job["jobTitle"]
        company_name = job["companyName"]
        location = job["Location"]
        description = job["Description"]
        application_link = job["ApplicationLink"]

        # Check if the job already exists in the database
        cursor.execute("SELECT COUNT(*) FROM jobs WHERE JobTitle = ? AND CompanyName = ? AND Location = ?", (job_title, company_name, location))
        existing_job = cursor.fetchone()[0]

        if existing_job > 0:
            # If job exists, update the record
            update_query = """
            UPDATE jobs
            SET Description = ?, ApplicationLink = ?
            WHERE JobTitle = ? AND CompanyName = ? AND Location = ?
            """
            cursor.execute(update_query, (description, application_link, job_title, company_name, location))
            print(f"Updated job: {job_title}")
        else:
            # If job doesn't exist, insert it
            insert_query = """
            INSERT INTO jobs (JobTitle, CompanyName, Location, Description, ApplicationLink)
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (job_title, company_name, location, description, application_link))
            print(f"Inserted new job: {job_title}")
        
        connection.commit()

# Function to filter job listings by location or company name
def filtering_jobs():
    prompt = input("Location or Company-based filtering? (Enter 'company' or 'location'): ").strip().lower()
    flag = None
    prompt2 = ""

    if prompt == "company":
        prompt2 = input("Enter company name: ").strip()
        flag = 1
    elif prompt == "location":
        prompt2 = input("Enter the location: ").strip()
        flag = 2
    else:
        raise ValueError("Invalid input. Please enter 'company' or 'location'.")

    # Filter jobs based on the user input
    filtered_jobs = []
    with sqlite3.connect("lesson-12/homework/jobs.db") as connection:
        cursor = connection.cursor()
        
        if flag == 1:
            cursor.execute("SELECT * FROM jobs WHERE CompanyName LIKE ?", ('%' + prompt2 + '%',))
        elif flag == 2:
            cursor.execute("SELECT * FROM jobs WHERE Location LIKE ?", ('%' + prompt2 + '%',))
        
        filtered_jobs = cursor.fetchall()
    
    return filtered_jobs

# Function to export filtered results into a CSV file
def convert2CSV():
    filtered_jobs = filtering_jobs()

    if filtered_jobs:
        with open("lesson-12/homework/filtered_jobs.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["JobTitle", "CompanyName", "Location", "Description", "ApplicationLink"])
            writer.writerows(filtered_jobs)
        print("Filtered jobs exported to filtered_jobs.csv.")
    else:
        print("No jobs found for the given filter.")

# Example: Filtering and exporting jobs
convert2CSV()
