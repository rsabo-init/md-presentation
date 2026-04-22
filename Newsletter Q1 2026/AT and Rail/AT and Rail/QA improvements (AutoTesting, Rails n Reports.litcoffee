# QA Unapređenja — Automatsko Testiranje i Izveštavanje
 

![Izvršavanje automatskih testova u Cypress-u](testovi.png)
 
**Svaki deploy automatski verifikovan. Svaki rezultat dokumentovan.**
 
Ručno testiranje nakon svakog deploya oduzimalo je vreme i bilo podložno greškama ili propuštenim slučajevima. Da bismo osigurali konzistentan kvalitet i brže reagovanje, uveli smo strukturirani sistem automatskog testiranja zasnovan na **Cypress** framework-u, a dokumentovan izveštajem u **Testrail-u**.

- Tri procedure pokrivaju ključne oblasti: Wells CRUD, Advanced Configurator i Editor/Client
- Svi test case-evi su dokumentovani i organizovani po procedurama u Testrail-u
- Nakon svakog deploya generišemo PDF izveštaj koji se šalje na željene mejlove

---

### Šta se testira?

**Tri procedure, sistematska pokrivenost.**
 
**Wells CRUD — Boomerang projekat:** Pokriva osnovne operacije nad Well-ovima — dodavanje novog Well-a, preimenovanje, retire i brisanje. Ovo su kritične operacije čiji kvar direktno utiče na svakodnevni rad klijenata.

<img src="BasicTestingCRUDWells.png" width="600"/>
 
**Advanced Configurator:** Pokriva najčešće korišćene komponente unutar Advanced Konfiguratora. Testovi verifikuju da su komponente funkcionalne i da se ponašaju očekivano nakon svake izmene na platformi.
 
**Editor/Client:** Pokriva komponente koje se konfigurišu u Editoru i prikazuju krajnjem korisniku u Clientu — verifikujući konzistentnost između onoga što se konfiguriše i onoga što korisnik vidi.

---

### Izveštavanje nakon deploya
 
**Automatski PDF izveštaj — uvek spreman, uvek dostavljen.**
 
Nakon izvršavanja testova, generišemo strukturirani izveštaj sa rezultatima svih test case-eva. Izveštaj je dostupan u PDF formatu i može se automatski slati na definisane mejl adrese.

![Primer izveštaja](Report.png)
 
- Jasan prikaz prošlih i palih testova po procedurama
- Mogućnost slanja na email-ove
- Istorija izveštaja omogućava praćenje kvaliteta kroz vreme

