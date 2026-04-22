# Responsive Klijent

 

**Ekrani koji se prilagođavaju svakom ekranu — bez fiksnih koordinata, bez ručnog prilagođavanja.**

 

Do sada je iscrtavanje ekrana u inView platformi funkcionisalo na principu apsolutnog pozicioniranja — svaki element imao je fiksne koordinate i dimenzije, bez prilagođavanja različitim veličinama ekrana. Responsive klijent menja taj pristup iz osnova.

---

### Kako funkcioniše?

 

Osnova novog sistema je **flex raspored**, poznat iz modernog web dizajna. Umesto da svaki element zna tačno gde stoji na ekranu, elementi znaju samo kako se odnose jedni prema drugima.

Ekran se gradi u slojevima. U pozadini se postavljaju **kontejneri** — nevidljive kutije koje definišu zone i smerove rasporeda. Kontejner može da slaže decu horizontalno ili vertikalno, da ih ravnomerno raspoređuje ili da ih gurne uz jedan kraj. Kontejneri se mogu ugnježdavati — kontejner unutar kontejnera — čime se gradi složena mreža bez ijedne fiksne koordinate.

Na vrhu te mreže dolaze **komponente** — vrednosti, grafici, dugmad, alarmi. Svaka komponenta zauzima prostor koji joj kontejner dodeli. Kada se ekran proširi, kontejner to primeti i preraspodeli prostor. Kada se ekran smanji, isti princip radi u suprotnom smeru.

Rezultat: isti ekran, iscrtavan na industrijskom panelu od 10 inča i monitoru od 27 inča, izgleda uredno na oba — bez intervencije aplikativca.

> Više o flex principu možete pročitati na: [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

![Responsive screen](responsive-screen.png)
