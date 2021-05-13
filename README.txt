Johdatus datatieteeseen k2021
Etuovi.com'n kohteiden hinnan ennustaminen ja haluttujen tuloksien rajaaminen

Harjoitustyössä kerätään dataa omakoti- ja erillistaloista etuovi.com-sivustolta. Dataa esikäsitellään, ja 
opetetaan muutamaa koneoppimismallia ennustamaan asuntojen hintoja. Opetusdata on Turusta, Jyväskylästä ja Oulusta.
Työn tuloksena on raportti, jossa näytetään kartalla kaikki valitut kriteerit täyttävät Tampereen 
omakoti- ja erillistalot, sekä tietoja niistä.

Tiedostot:
- joda_ht.ipynb sisältää varsinaisen harjoitustyön kaikkine vaiheineen
- etuovi_scraper.py on raapija, jolla kerätään tiedot etuovi.com-sivustolta
- TreTurkuJklOulu.json sisältää kerätyn datan

- joda.ipynb sisältää vain työn tuloksen eli käyttäjää varten tehdyn raportin, sekä käyttöohjeet raportin käyttämiseen
- mlModel.pkl- tiedsotoon on talennettu käyttäjäversiota varten koneoppimismalli asuntojen hintojen ennustamiseen 
- dfTampere.json sisältää dataa Tampereen omakoti- ja erillistaloista käyttäjäversiota varten