import requests
from bs4 import BeautifulSoup

def get_corona_cases(country):

    api_address = "https://www.worldometers.info/coronavirus/country/"

    url = api_address + country

    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    pew = soup.findAll(['span'])

    data=[]
    for subs in pew:
        if subs.get_text()!='[source]':
            if subs.get_text()!='':
                if '\n'not in subs.get_text():
                    if not any([i in subs.get_text() for i in [i for i in 'aeiou']]):
                        data.append(subs.get_text())
    return data

if __name__ == "__main__":
    cases_num = get_corona_cases("Germany")
    print(cases_num)