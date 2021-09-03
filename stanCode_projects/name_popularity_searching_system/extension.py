"""
File: extension.py
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        ##################
        #                #
        #      TODO:     #
        #                #
        ##################
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html)
        items = soup.find('table', {'class': 't-stripe'}).find('tbody').find_all('tr')
        items.pop()         # remove the last item, because the last item is the note of the ranking
        male_total = 0      # total of male
        female_total = 0    # total of female
        for item in items:
            info = item.find_all('td')
            male = info[2].text.split(",")       # remove ',' in the numbers
            male_num = male[0]+male[1]
            female = info[4].text.split(",")     # remove ',' in the numbers
            female_num = female[0]+female[1]
            male_total += int(male_num)
            female_total += int(female_num)
        print("Male Number: "+str(male_total))
        print("Female Number: "+str(female_total))


if __name__ == '__main__':
    main()
