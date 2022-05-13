import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(executable_path='C:/Users/Carmen/Desktop/chromeDriver/chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
driver.quit()


for a in soup.findAll(attrs='blog-card__content-wrapper'):
    name = a.find('a')
    if name not in results:
        results.append(name.txt)
print(results)
for b in soup.findAll(attrs='blog-card__date-wrapper'):
    date = b.find('p')
    if date not in other_results:
        other_results.append(date.txt)
print(other_results)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')
