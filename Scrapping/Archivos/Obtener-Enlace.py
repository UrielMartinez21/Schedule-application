from urllib.request import urlopen
from bs4 import BeautifulSoup

r = urlopen("https://www.misprofesores.com/escuelas/IPN-ESCOM_1694/")
bs = BeautifulSoup(r.read(), "html.parser")
r.close()

for link in bs.find_all("a"):
    print(link.get("href"))
