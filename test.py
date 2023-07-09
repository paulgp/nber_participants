
# This script goes through each conference on the NBER website for the summer institute and
# downloads the list of participants on each page, and saves it as a CSV file.
# It then counts the number of participants for each conference and prints it out

import requests
from bs4 import BeautifulSoup
import csv
import re

# This function takes in a URL and returns a list of participants
def get_participants(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # find all names after the "Participants" text header
    participants = soup.find_all(string=re.compile('Participants'))[0].parent.parent.find_all('span')
    i = 0
    participant_list = []
    for p in participants:
        if i % 2 == 0:
            name = p.text
        else:
            institution = p.text
            participant_list.append([name, institution])
        i = i + 1
    return(participant_list)
url = 'https://www.nber.org/conferences/si-2023-international-asset-pricing'


# this function finds every url with the word "conferences/si" in it and  then
# returns the list of urls
def get_conference_urls(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a')
    conference_urls = []
    for l in links:
        try: 
            if 'conferences/si' in l['href']:
                conference_urls.append([l.string, l['href']])
        except KeyError:
            print(l)
    return(conference_urls)

url = 'https://www.nber.org/conferences/summer-institute-2023'
url_list = get_conference_urls(url)

# we now loop over each url in url_list, and construct the lenght of the get_participants
# function for each url, and combine the first entry in the url_list with the length,
# then write to a csv file
with open('participants.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for url in url_list:
        writer.writerow([url[0], len(get_participants('https://www.nber.org' + url[1]))])



