# Import Statements
import requests
from bs4 import BeautifulSoup

# !!!----------------------------------------------------------------------------------------------------------------!!!
# !!!---------This is taken from the realpython.com beautifulsoup tutorial, this is not entirely my work-------------!!!
# !!!----------------------------------------------------------------------------------------------------------------!!!

# Finds the URL and then gets the website info for the website variable
url = "https://realpython.github.io/fake-jobs/"
website = requests.get(url)

# Parses through the website's info with html parser to clean it up
parsed = BeautifulSoup(website.content, "html.parser")
# Finds the resultscontainer in the website's html code
results = parsed.find(id="ResultsContainer")
# Finds all the card contents (In this case, each card represents a job)4
"""
job_elements = results.find_all("div", class_="card-content")
# Use this to find the job title, company, and location for all jobs
for i in range(0, len(job_elements)):
    job = job_elements[i]
    job_title = job.find("h2", class_="title").text.strip()
    job_company = job.find("h3", class_="subtitle").text.strip()
    job_location = job.find("p", class_="location").text.strip()
    print(job_title)
    print(job_company)
    print(job_location + "\n")
"""

"""
# Finds all the job titles with the word "python" in it
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# Since the above python_jobs only looks for the job names, we need to go back up to card-content in order to get all
# the info for the job. In this case, we do this by calling .parent.parent.parent, or the job name's great-grandparents
python_job_info = [
    job.parent.parent.parent for job in python_jobs
]

# Same as previous for loop but looking for only python jobs
for job in python_job_info:
    job_title = job.find(class_="title").text.strip()
    job_company = job.find(class_="subtitle").text.strip()
    job_location = job.find(class_="location").text.strip()
    print(job_title)
    print(job_company)
    print(job_location)
"""

"""
# This part finds the application links for every job and prints them out

# finds all the jobs
jobs = results.find_all(class_="card-content")

# For each job
for job in jobs:
    # Finds the links
    links = job.find_all("a")
    # For each link
    for link in links:
        # If it is the application link
        if link.text.lower() == "apply":
            # Prints it out
            link_url = link["href"]
            print(link_url)
"""
