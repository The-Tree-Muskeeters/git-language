from requests import get
from bs4 import BeautifulSoup
import os
import re
from env import github_token, github_username
import pandas as pd


headers = {"Authorization": f"token {github_token}", "User-Agent": github_username}

if headers["Authorization"] == "token " or headers["User-Agent"] == "":
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )

g_url = ['https://github.com/search?o=desc&p=1&q=stars%3A%3E1&s=forks&type=Repositories', ' https://github.com/search?o=desc&p=2&q=stars%3A%3E1&s=forks&type=Repositories'\
         'https://github.com/search?o=desc&p=3&q=stars%3A%3E1&s=forks&type=Repositories', 'https://github.com/search?o=desc&p=4&q=stars%3A%3E1&s=forks&type=Repositories',\
         'https://github.com/search?o=desc&p=5&q=stars%3A%3E1&s=forks&type=Repositories','https://github.com/search?o=desc&p=6&q=stars%3A%3E1&s=forks&type=Repositories',\
        'https://github.com/search?o=desc&p=7&q=stars%3A%3E1&s=forks&type=Repositories','https://github.com/search?o=desc&p=8&q=stars%3A%3E1&s=forks&type=Repositories',\
        'https://github.com/search?o=desc&p=9&q=stars%3A%3E1&s=forks&type=Repositories','https://github.com/search?o=desc&p=10&q=stars%3A%3E1&s=forks&type=Repositories']


def get_repos(urls):
    """ Function that gives address of github repos in a list for given list if urls """
    repo = []
    for url in urls:    
        response = get(url, headers=headers)
        soup = BeautifulSoup(response.text)
        text = soup.find_all(attrs={"f4 text-normal"})
        for i in text:
            repo.append(i.find('a')['href'])
    return repo









# def git_1(url):
#     """ Function to get url info for single url from github"""
#     d1 =[]
#     response = get(url, headers=headers)
#     soup = BeautifulSoup(response.text)
#     text = soup.find_all(attrs={"f4 text-normal"})
#     d1 = text
#     print('\n')
#     return d1

# def git_repos(urls):
#     """ Master url to get github info from list of urls"""
#     d =[]
#     for url in urls:
#         d.append(git_1(url))
                 
#     return d

# def get_repo_list(urls):
#     text = str(git_repos(urls))
#     text1 = re.findall(r'Repository","url*":"https:\/\/github.com\/.*"}', text)
#     text1 = str(text1)
#     lines = pd.Series(text1.strip().split(','))

#     count = 0
#     line1 = []
#     for line in lines:
#         if count%2 !=0:
#             line1.append(line)
#             print('\n')
#         count = count+1

#     line1 = pd.Series(line1)

#     regex = r'(?P<ip>url.+.com\/)(?P<repo>.+)(?P<comma>")'
#     regex = re.compile(regex,re.VERBOSE)

#     line1.str.extract(regex)

#     return line1.str.extract(regex)['repo'].tolist()

