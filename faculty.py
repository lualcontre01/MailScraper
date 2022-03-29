from bs4 import BeautifulSoup
import requests

end_link = []
fixed_url="https://www.arch.columbia.edu/faculty"
fixed_html_content = requests.get(fixed_url).text
fixed_soup = BeautifulSoup(fixed_html_content, "lxml")
for link in fixed_soup.find_all('a', {"class":"faculty__name link--blank"}):
    end_link.append(link.get('href'))

mails = []
for end in end_link[:50]:
    end_url = 'https://www.arch.columbia.edu{}'.format(end)
    end_html_content = requests.get(end_url).text
    end_soup = BeautifulSoup(end_html_content, "lxml")
    for mail in end_soup.find_all('div', {"class": "faculty-sidebar__email"}):
        if '@' in mail.get_text():
            mails.append(mail.get_text())

with open('mails.txt', 'w') as f:
    for mail in set(mails[:50]):
        f.write(mail)
        f.write('\n')
    f.close()
