from bs4 import BeautifulSoup
import requests
import pandas as pd



def scrap_etenders(link='https://etenders.gov.in/eprocure/app'):
    link = requests.get('https://etenders.gov.in/eprocure/app').text
    src_code = BeautifulSoup(link, 'html.parser')

    # print(src_code.prettify())
    table = src_code.find('table', {'class': "list_table"})
    table_row = table.find('tr', {'class': 'list_header'})
    print(f' table column are :  {table_row.text}')
    count = 0
    for inside in table.find_all('tr', {'class': ['even', 'odd']}):
        count += 1
        print(f'{count} -->> {inside.text}')
        print('========' * 10)

# scrap_etenders() # default link passed



def cpppc_scraper(link='https://www.cpppc.org/en/PPPyd.jhtml'): #China Public Private Partnerships Center
    link_to_scrape = requests.get(link).text
    src_code = BeautifulSoup(link_to_scrape, 'html.parser')
    title = []
    content = []
    ul_data = src_code.find('ul', {'class': "new-content ppp-list"})
    for li_data in ul_data.find_all('li'):
        a = li_data.a.text
        title.append(a)
        for div_data in li_data.find_all('div'):
            b = div_data.text
            content.append(b)
        # print(li_data.a.text)

    # print(one)

    data_dict = {'titles': title, 'Content': content}

    # print(data_dict)
    csv_file = pd.DataFrame(data_dict)
    csv_file.to_csv('results.csv', index=False)


# cpppc_scraper() # default link passed



def wbg_screper(link='https://ieg.worldbankgroup.org/data'):
    link_to_scrape  = requests.get(link)
    src_code = BeautifulSoup(link_to_scrape.text, 'html.parser')

    div_content = src_code.find('div', {'class': 'views-field views-field-body'})

    for table_data in div_content.find_all('tr'):
        print(table_data.text, end='')
        print('====' * 10)



wbg_screper() # default link passed