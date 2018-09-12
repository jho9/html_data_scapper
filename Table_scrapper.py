from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_columns(table):
    columns = table[0].text.split(sep = '\n')
    columns.remove('')
    return columns
    
def main():
    page = 'https://jobs.mo.gov/content/missouri-warn-notices-py-2017'
    html = urlopen(page)
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    company_info = soup.find(class_='field-item even')
    company_information = company_info.findAll('tr')
    list_of_company_data = []
    dataset = {}
    info_column = get_columns(company_information)

    for j in range(1,len(company_information)-1):
        for i in range(0, len(info_column)):
            rawdata = company_information[j].text.split(sep = '\n')
            rawdata.remove('')
            dataset[info_column[i]] = rawdata[i]
        print(dataset)
     
 if __name__ == "__main__":
    main()
   
