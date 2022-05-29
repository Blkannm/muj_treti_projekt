# POPIS PROJEKTU

data_colector.py dokaze skrapovat data ze stranky volby.cz. Idealne z teto stranky https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ z vybranych okresu.
data pote ulozi do CVS souboru. prijima 2 parametry: 
1. Link ktery chcete pouzit napr.:https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2102
2. Nazev souboru


# INSTALACE KNIHOVEN
na to aby fungoval program potrebujete nezabudovane knihovny


### pip install beautifulsoup4

### pip install requests



# SPOUSTENI PROJEKTU

spusteni souboru data_colector.py vyzaduje 2 parametry:

###  python .\data_colector.py <odkaz-uzemniho-celku> <nazev-souboru.csv>
  
# UKAZKA PROJEKTU
  
  argument 1: 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
  argument 2: 'nazev_souboru.csv'
  
# STAHOVANI
  
  STAHUJI DATA ZE STRANKY!
  DATA ULOZENA V UKOL3.CSV

# CASTECNY VYSTUP
  
![image](https://user-images.githubusercontent.com/96025406/170860719-f62afc9c-959e-44ce-bd07-539bc080169f.png)

