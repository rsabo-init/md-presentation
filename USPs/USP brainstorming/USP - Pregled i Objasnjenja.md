# USP — Pregled, Objašnjenja i Zaključci
**InView Web SCADA / inVIEW IIoT platforma**

> Ovaj dokument predstavlja sažetak brainstorminga na temu USP-eva, sa kontekstom, obrazloženjem i zaključcima za svaki USP.
> Osnova: brainstorming sastanak 11.03.2026., zapisnik, transkript i tehnički kontekst platforme.
> Nakon brainstorminga, sprovedena je dodatna radionica sa Product Development Managerom koji je aktivno učestvovao u analizi. Tokom te radionice utvrđene su veze sličnosti između pojedinih USP-ova — grupe koje se međusobno nadopunjuju i koje se u prodajnoj komunikaciji trebaju tretirati zajedno.
****
---

## O grupisanju i metodologiji

### Kako je nastala ova lista

Na brainstorming sastanku (11.03.2026.) tim od **9 osoba** bio je podeljen u **3 grupe** (G1, G2, G3 — po 3 člana). Svaka grupa je nezavisno i paralelno pisala USP-ove na sticker papiriće — **jedan sticker = jedan USP**. Nakon toga, voditelj je prikupio sve stickere i tim je zajedno diskutovao, deduplicirao i grupisao rezultate koristeći **Affinity dijagram** metodu.

### Šta znači broj pored USP-a

Pored nekih USP-ova u originalnoj tabeli (`from table.txt`) stoji broj:

| Oznaka | Značenje |
|---|---|
| *(nema broja)* | Samo **1 tim** je taj USP naveo |
| `2/3` | **2 od 3 tima** su nezavisno navela taj USP |
| `3/3` | Sva **3 tima** su nezavisno navela taj USP |
| `+` (npr. `2+/3`) | BDM je **samostalno, pre brainstorming sastanka**, predložio isti USP — dodatna eksterna potvrda relevantnosti |

Ovaj broj je **indikator konsenzusa** — što je veći, to je šira saglasnost unutar tima da je taj USP stvarno relevantan i prepoznatljiv. USP-ovi sa brojem 2 ili 3 imaju veći prioritet jer nisu bili samo ideja jedne osobe. Oznaka `+` predstavlja dodatnu potvrdu van grupe — BDM je nezavisno i pre sastanka identifikovao isti USP kao relevantan.

### Grupe po ciljnoj publici

USP-ovi su podeljeni u 4 grupe na osnovu toga **kome se prodaje / ko donosi odluku**:

| Grupa | Ciljna publika | Logika |
|---|---|---|
| 🟩 **Top Level Management** | Direktori, C-level, finansijski odlučioci | Govore o brzini, ceni, pouzdanosti investicije i reputaciji vendora |
| 🌐 **Zajedničko (sve grupe)** | Svi — operateri, tehničari, menadžment | Horizontalne vrednosti koje su relevantne bez obzira na ulogu |
| 🔵 **Technical** | Sistemski arhitekti, tehnički evaluatori | Govore o arhitekturi, protokolima, skalabilnosti i integrabilnosti |
| 🟧 **Operational** | Operateri, inženjeri na terenu, IT timovi klijenta | Govore o svakodnevnom korišćenju, UX-u i praktičnim workflow-ovima |
| ⬜ **Manje relevantno** | — | Validne ideje, ali nisu primarni USP-ovi u ovoj fazi |

---

## Pregled svih USP-ova

Kompletna lista svih 25 USP-ova sa konsenzus skorom, grupisana po ciljnoj publici. Detaljna razrada svakog USP-a nalazi se u nastavku dokumenta.

> ⭐ = sva 3 tima su nezavisno navela ovaj USP (pun konsenzus)

| # | USP | Konsenzus |
|---|---|---|
| **🌐 Zajedničko (sve grupe)** | | |
| 1 | High level support | ⭐ 3+/3 |
| **🟩 Top Level Management** | | |
| 2 | Veoma brza implementacija | 2+/3 |
| 3 | Pricing | 2+/3 |
| 4 | Brz razvoj feature-ova | 2/3 |
| 5 | Dokazan AI u industriji | 1/3 |
| 6 | Pay-as-you-go model | 1/3 |
| 7 | Duga prisutnost u industriji | 1/3 |
| **🔵 Technical** | | |
| 8 | Edge computing | ⭐ 3/3 |
| 9 | Dokazana skalabilnost | ⭐ 3/3 |
| 10 | Otvorenost za integracije | 2+/3 |
| 11 | AI & ML integracija | 2+/3 |
| 12 | Store and Forward | 2/3 |
| 13 | Kontrola distribuiranih sistema | 1+/3 |
| 14 | Cloud agnostičan + hybrid deployment | 1/3 |
| 15 | Lifetime history | 1/3 |
| 16 | High security standard | 1/3 |
| 17 | Real-time podaci | 1/3 |
| 18 | Push mehanizam orjentisanost | 1/3 |
| **🟧 Operational** | | |
| 19 | Remote Control | 1+/3 |
| 20 | No-Code konfigurator i IDE | 2+/3 |
| 21 | No-Code mobilna aplikacija | 1+/3 |
| 22 | Templating | 2/3 |
| 23 | Batch device management | 1/3 |
| 24 | Intuitivan UI | 2/3 |
| 25 | Raznovrsnost komponenti | 1/3 |

### Veze sličnosti (affinity grupe)

Nakon brainstorminga, radionica sa Product Development Managerom identifikovala je USP-ove koji su konceptualno usko vezani i koji se trebaju komunicirati kao grupisana priča, a ne izolovane tačke:

| Affinity grupa | USP-ovi |
|---|---|
| **Brzina isporuke** | #2 Veoma brza implementacija + #4 Brz razvoj feature-ova |
| **Cenovni model** | #3 Pricing + #6 Pay-as-you-go model |
| **No-Code ekosistem** | #20 No-Code konfigurator i IDE + #22 Templating + #21 No-Code mobilna aplikacija |

Kod svakog USP-a iz gore navedenih grupa naznačena je veza sa ostalim članovima grupe.

---

## 🌐 Zajedničko za sve grupe

---

### 1. High level support (konsenzus: 3/3 tima) ⭐

**Šta znači:**
INIT tim pruža direktnu, ekspertsku podršku — bez niova tierova, posrednika, ili offshore help deska. Klijent komunicira direktno sa timom koji je napravio sistem.

**Kontekst iz diskusije:**
Jedini USP koji je tim konsenzusom svrstao u sve tri grupe — što govori o tome da je ovo horizontalna vrednost relevantna za svakoga. Sva 3 tima su ga nezavisno navela, što ga čini jedinim USP-om sa punim konsenzusom (3/3).

**Zaključak:**
Jak i dokaziv USP koji se posebno ističe u poređenju sa velikim vendorima (Siemens, AVEVA) gde support prolazi kroz nivoe, ticketing sisteme i offshore timove. Treba ga komunicirati konkretno: reaction time, dedicated kontakt, direktan pristup razvojnom timu.

**+ Plusevi:**
- Direktan pristup razvojnom timu = brže rešavanje problema
- Timezone i kulturna bliskost (za EU i balkansko tržište)
- Jak diferencijator od enterprise vendora
- Pun timski konsenzus (3/3) — najjači signal iz brainstorminga

**- Minusi / Rizici:**
- Skalabilnost podrške može biti izazov sa rastom baze klijenata
- Needs SLA formalizaciju da postane prodajni argument

---

## 🟩 Top Level Management
> *Ciljna publika: direktori, C-level, finansijski odlučioci*

---

### 2. Veoma brza implementacija (konsenzus: 2/3 tima)

> 🔗 *Affinity grupa — Brzina isporuke: usko vezano za **#4 Brz razvoj feature-ova***

**Šta znači:**
Projekti idu u produkciju u sedmicama, a ne godinama. Tim INIT-a je lokalno dostupan, bez outsourcing-a i timezone problema.

**Kontekst iz diskusije:**
Navedeno na prezentaciji kao *"Projekti u nedeljama, ne godinama"*. Potkrepljeno iskustvom tima u industriji. Na sastanku je pomenuto i pitanje *"Koliko brzo je najbrža implementacija otišla od kickoffa do live-a?"* — što ukazuje da postoji konkretan primer koji se može koristiti.

**Zaključak:**
Jedan od najjačih USP-ova za Top Management publiku jer direktno govori o troškovima i riziku projekta. Mora biti potkrepljen konkretnim brojevima i primerima.

**+ Plusevi:**
- Direktno se prevodi u novac (kraća implementacija = manji projektni trošak)
- Smanjuje rizik dugih projekata
- No-code + templating direktno podržava ovaj claim

**- Minusi / Rizici:**
- "Brzo" bez definicije je prazan claim — potrebni su konkretni primeri ("implementacija u 3 nedelje za X klijenta")
- Ovaj USP mora biti konzistentno isporukan — loše iskustvo ga uništava

---

### 3. Pricing (konsenzus: 2/3 tima)

> 🔗 *Affinity grupa — Cenovni model: usko vezano za **#6 Pay-as-you-go model***

**Šta znači:**
Cenovni model platforme je konkurentan u poređenju sa enterprise SCADA rešenjima poput Siemensa ili Wonderwarea.

**Kontekst iz diskusije:**
Na sastanku je otvorena diskusija o tome da je *"jeftino relativno"* — jer se uvek može dati popust, ali onda kvalitet percepcije opada. Tim nije stigao do konkretnog zaključka oko pricing strategije.

**Zaključak:**
Pricing sam po sebi je slab USP — lako ga je kopirati i može da degradira brendiranje. Treba ga komunicirati kroz vrednost (ROI), ne kroz apsolutnu cenu. Pay-as-you-go model je konkretnije i jače od generičke "povoljna cena" poruke.

**+ Plusevi:**
- Niži entry cost u poređenju sa Siemens/AVEVA/GE
- Fleksibilni modeli

**- Minusi / Rizici:**
- Race to the bottom rizik
- Snižavanje cene može negativno uticati na percepciju kvaliteta
- Bez ROI kalkulacije, "jeftino" ne govori dovoljno

---

### 6. Pay-as-you-go model (konsenzus: 1/3 tima)

> 🔗 *Affinity grupa — Cenovni model: usko vezano za **#3 Pricing***

**Šta znači:**
Klijenti plaćaju prema stvarnoj upotrebi ili na pretplatničkoj osnovi, a ne veliku licencu unapred. Niži barrier to entry.

**Kontekst iz diskusije:**
Na sastanku je naglašeno da je ovaj model bolji USP od same "jeftine cene" — jer govori o fleksibilnosti i smanjenju inicijalnog rizika za klijenta.

**Zaključak:**
Jak USP u modernom B2B SaaS kontekstu. Direktno odgovara na prigovor *"preskupo za početak"*. Posebno relevantan za SMB klijente ili prve deploymente.

**+ Plusevi:**
- Niski inicijalni trošak = lakša odluka za klijenta
- Skalira se sa rastom klijenta
- Moderno i u skladu sa SaaS trendovima

**- Minusi / Rizici:**
- Mora biti jasno definisan cenovni model (po uređaju? po korisniku? po podatku?)
- Potrebno razjasniti da li je ovaj model formalizovan ili je to fleksibilnost u pregovorima

---

### 4. Brz razvoj feature-ova (konsenzus: 2/3 tima)

> 🔗 *Affinity grupa — Brzina isporuke: usko vezano za **#2 Veoma brza implementacija***

**Šta znači:**
INIT tim kontinuirano i brzo isporučuje nove funkcionalnosti. Klijenti ne čekaju godine na feature koji im treba.

**Kontekst iz diskusije:**
Pomenuto u kontekstu dugoročne vrednosti platforme vs. inicijalnog takmičenja sa konkurencijom. *"Izgubili smo bid, ali na duži rok smo bili bolji."* Brzina feature razvoja direktno doprinosi tom argumentu.

**Zaključak:**
Jak USP ali ga je teško dokazati bez konkretnih referenci (changelog, roadmap, release frequency). Interno svakodnevna realnost — eksterno treba biti vidljiv.

**+ Plusevi:**
- In-house R&D = nema zavisnosti od vendora za nove feature-ove
- Agilan razvoj — klijentski feedback se brzo implementira
- Kompetitivna prednost nad legacy sistemima koji rade godišnje release cikluse

**- Minusi / Rizici:**
- Bez javnog changelog-a ili roadmap-a, ovaj claim je nevidljiv
- Potreban je mehanizam za prikaz release historije prema klijentima

---

### 7. Duga prisutnost u industriji (konsenzus: 1/3 tima)

**Šta znači:**
INDAS Group postoji od 1992. (30+ godina), a komercijalna SCADA platforma od 2011. (15+ godina). To nije startup — to je dokazano rešenje sa realnim deploymentima.

**Kontekst iz diskusije:**
Na sastanku naglašeno više puta. Direktan citat: *"Imamo prefix 'proven' — već smo to uradili u industriji, kod nekog drugog."* Tim se složio da je ovo jak argument posebno u industrijama gde je poverenje ključno (kritična infrastruktura, energetika).

**Zaključak:**
Jedan od najjačih USP-ova za konzervativne klijente u regulisanim industrijama. Direktno adresira prigovor *"ko je vaš referentni klijent?"*. Uprkos samo jednom timu koji ga je eksplicitno naveo, bio je snažno podržan u plenarnoj diskusiji.

**+ Plusevi:**
- Trust signal koji startup konkurencija ne može kopirati
- Relevantno za government, utility i critical infrastructure sektor
- Dokazano preživljavanje tržišnih ciklusa (30 godina)

**- Minusi / Rizici:**
- Može stvoriti percepciju "starog" rešenja — treba balansirati sa modernim tehničkim USP-ovima
- Zahteva vidljivu referencu listu klijenata za maksimalni efekat

---

### 5. Dokazana AI u industriji (konsenzus: 1/3 tima)

**Šta znači:**
AI/ML funkcionalnosti platforme nisu laboratorijski proof-of-concept — postoje realni klijenti koji koriste anomaly detection i predictive analytics u produkciji.

**Kontekst iz diskusije:**
Na sastanku pomenuto kao dopuna dugoj prisutnosti u industriji. Kombinirani argument: iskustvo + moderne AI sposobnosti = jedinstven spoj.

**Zaključak:**
Jak USP kada je potkrepljen konkretnim primerima. Kombinacija "legacy credibility + AI modernity" je posebno efikasna u razgovoru sa C-levelom.

**+ Plusevi:**
- Direktno adresira trend AI adoptije u industriji
- Razlikuje od legacy SCADA vendora koji nemaju native AI
- Visoka percipirana vrednost kod menadžmenta

**- Minusi / Rizici:**
- "AI" kao termin je infliran — treba konkretizovati: anomaly detection, prediction, OEE optimization
- Potrebni su konkretni klijentski primeri i izmereni rezultati

---

## 🔵 Technical
> *Ciljna publika: sistemski arhitekti, tehnički evaluatori*

---

### 14. Cloud agnostičan + podrška za hybrid deployment (konsenzus: 1/3 tima)

**Šta znači:**
Platforma ne zahteva specifičan cloud provider — može se deployovati na AWS, Azure, GCP, private cloud, on-premise serveru, ili u hibridnoj kombinaciji. Isti product, iste funkcionalnosti, bez obzira na deployment model.

**Kontekst iz diskusije:**
Jedan od jasnih tehničkih diferencijatora. Platforma podržava sve modele: on-premise, cloud (SaaS), hybrid (miks), i edge + cloud. Ovo je direktan odgovor na potrebe klijenata u regulisanim industrijama (energetika, kritična infrastruktura) koji ne mogu ili ne žele da idu u public cloud.

**Zaključak:**
Jak USP u B2B industrijskom segmentu. Posebno relevantan za klijente u EU koji imaju data sovereignty zahteve, i za klijente u kritičnoj infrastrukturi.

**+ Plusevi:**
- Nema vendor lock-in na cloud nivo
- Pokriva i konzervativne klijente (on-premise) i moderne (cloud-first)
- EU data sovereignty — relevantno za GDPR i regulisane industrije

**- Minusi / Rizici:**
- Kompleksnija podrška i testiranje (više deployment scenarija)
- Neke funkcionalnosti mogu biti ograničenije u određenim deployment modelima

---

### 15. Lifetime history (trajno čuvanje istorije podataka) (konsenzus: 1/3 tima)

**Šta znači:**
Platforma čuva kompletnu istoriju svih procesnih podataka bez automatskog brisanja. Klijent ima pristup podacima od prvog dana implementacije — godinama ili decenijama unazad.

**Kontekst iz diskusije:**
Pomenuto kao feature koji je teško naći kod konkurencije u istoj formi. Podržano tehnički kroz `IwsHistory` mikroservis i konfigurabilan data retention policy.

**Zaključak:**
Relevantan USP za industrije sa regulatornim zahtevima (energetika, farmaceutika, prehrambena industrija) gdje je čuvanje podataka obavezno. Treba ga komunicirati uz napomenu o konfigurabilnosti retention politike.

**+ Plusevi:**
- Direktno adresira regulatorne zahteve
- Audit trail i forenzička analiza incidenata
- Osnova za ML/prediktivnu analitiku (potrebni su dugi istorijski nizovi)

**- Minusi / Rizici:**
- Trošak storage-a raste s vremenom — treba jasna politika upravljanja podacima
- "Lifetime" treba precizno definisati (da li je stvarno neograničeno, ili konfigurabilan period?)

---

### 16. High security standard (verifikovan) (konsenzus: 1/3 tima)

**Šta znači:**
Platforma implementira moderne bezbednosne standarde: granularna kontrola pristupa, audit log, modernu autentifikaciju, i enkriptovanu komunikaciju.

**Kontekst iz diskusije:**
Pomenuto na sastanku uz komentar: *"Mislim da imamo kontrolu nad tim."* — što znači da tim ima poverenje u bezbednost, ali bez jakog konkretnog dokaza (certifikat, penetration test, itd.) koji bi se mogao koristiti u prodaji.

**Zaključak:**
Neophodan uslov (hygiene factor) za svaku ozbiljnu industrijsku platformu — ali bez eksternog verifikovanog dokaza teško ga je koristiti kao USP. Preporuka: investirati u formalnu verifikaciju (ISO 27001, penetration testing, ili sličan certifikat) koji bi dao dokazivost.

**+ Plusevi:**
- Granularna kontrola pristupa (svaki korisnik vidi samo što mu treba)
- Audit log svih promena
- GDPR-svesna arhitektura (EU kompanija)

**- Minusi / Rizici:**
- Bez eksternog certifikata ili pentest izveštaja, teško je dokaziv prema zahtevnim klijentima
- Sigurnost industrijskog softvera je pod povećalom — ranjivost bi imala veliku reputacionu štetu

---

### 11. AI & ML integracija (konsenzus: 2/3 tima)

**Šta znači:**
Platforma ima nativan AI/ML sloj — anomaly detection (Z-Score, IQR, Rate-of-Change, Timeout algoritmi), self-prediction modul (LSTM i Random Forest), feature selection (Pearson, Spearman, Mutual Information) i MLflow integraciju za upravljanje ML lifecycle-om.

**Kontekst iz diskusije:**
Pomenuto više puta na sastanku. Naglašeno je i kao USP za top menadžment ("Proven AI in industry") i kao tehnički diferencijator. Ujedno je pomenuto i kao *tehnički izazov* — ML i distribuirani sistemi su kompleksni za implementaciju.

**Zaključak:**
Jedan od najsnažnijih USP-ova platforme jer je AI/ML nativan deo arhitekture, a ne third-party add-on. Ključno je imati konkretne industrijske primere korišćenja (npr. "detektovali smo anomaliju X dana pre kvara").

**+ Plusevi:**
- Native, nije bolt-on — ugrađen u arhitekturu od samog početka
- Više algoritama + ensemble detekcija povećava tačnost
- Model versioning i inkrementalni update (ne treba pun re-training)
- MLflow integracija govori o profesionalnom ML lifecycle managementu

**- Minusi / Rizici:**
- ML zahteva kvalitetne istorijske podatke — klijenti bez njih ne mogu koristiti pun potencijal
- Kompleksnost implementacije i tumačenja rezultata — potrebna edukacija klijenata
- "AI" je trenutno overused marketing termin — treba biti konkretan, ne generički

---

### 10. Otvorenost za integracije (konsenzus: 2/3 tima)

**Šta znači:**
Platforma nudi multiple protokole i interfejse za integraciju sa eksternim sistemima: REST API, WebSocket, MQTT, i pre-pripremljene konektore za česte scenarije.

**Kontekst iz diskusije:**
Na sastanku je naveden konkretan primer: klijent koji je hteo da šalje podatke kroz protokol — tim je uzeo pre-pripremljeni konektor, minimalno prilagodio, i pustio u produkciju. Ovo je odličan prodajni primer koji ilustruje USP.

**Zaključak:**
Jak USP posebno za System Integrator segment koji mora da poveže inView sa postojećim ERP, MES ili SCADA sistemima klijenta. Konkretni primeri integracija su ključni za kredibilitet.

**+ Plusevi:**
- API-first pristup
- Pre-built konektori smanjuju integracionu kompleksnost
- Podržava i legacy i moderne protokole
- Relevantan za SI (System Integrator) kanal prodaje

**- Minusi / Rizici:**
- "Otvoren za integracije" je često prazan marketing claim — mora biti potkrepljen konkretnim primerima
- Kvalitet i kompletnost dokumentacije API-ja direktno utiče na ovu tvrdnju

---

### 12. Store and Forward (lokalni gateway history) (konsenzus: 2/3 tima)

**Šta znači:**
Edge gateway lokalno čuva podatke kada je konekcija sa cloud-om ili centralnim serverom prekinuta, i automatski šalje podatke čim se konekcija uspostavi. Nema gubitka podataka zbog mrežnih ispada.

**Kontekst iz diskusije:**
Nije eksplicitno duboko diskutovano na sastanku, ali je uvršteno kao tehnički USP. Direktno se nadovezuje na priču o reliability i kritičnoj infrastrukturi.

**Zaključak:**
Kritičan USP za klijente u industrijama sa nepouzdanom mrežnom konekcijom (terenske lokacije, udaljeni objekti, oil & gas, utility infrastruktura). Treba ga komunicirati uz primere scenarija u kojima dolazi do izražaja.

**+ Plusevi:**
- Zero data loss — kritično za regulisane industrije
- Autonomija edge lokacije od cloud dostupnosti
- Direktno adresira "što ako padne internet?" prigovor klijenata

**- Minusi / Rizici:**
- Zavisi od kapaciteta lokalnog storage-a na gateway uređaju
- Potrebno precizirati koji podaci se čuvaju lokalno i koji je maksimalni buffer period

---

### 9. Dokazana skalabilnost (konsenzus: 3/3 tima) ⭐

**Šta znači:**
Platforma je dizajnirana za horizontalno skaliranje kroz mikroservisnu arhitekturu i Kafka event streaming, i ima realne dokaze iz produkcije.

**Kontekst iz diskusije:**
Na sastanku je naveden konkretan primer: multitenant platforma sa **100.000 simultanih prikaza** na mikroservisnoj arhitekturi — i tim naglasio da su i sami bili iznenađeni koliko su daleko stigli. Ovo je odličan, dokaziv primer.

**Zaključak:**
Jak USP sa konkretnim dokazom. "Proven scalability" je puno snažnije od "scalable architecture" jer nije samo arhitekturna tvrdnja — ima produkcioni dokaz.

**+ Plusevi:**
- Konkretni produkcioni primer (100k simultanih prikaza)
- Mikroservisi + Kafka = arhitektura built for scale
- Relevantan za enterprise klijente i managed service providere

**- Minusi / Rizici:**
- Skalabilnost dolazi sa operativnom kompleksnošću (Kubernetes, Kafka, Zookeeper) — treba biti iskren oko operativnih zahteva

---

### 17. Real-time podaci (konsenzus: 1/3 tima)

**Šta znači:**
Platforma isporučuje procesne podatke u realnom vremenu kroz WebSocket stream — bez polling-a, bez kašnjenja. Korisnici vide žive podatke čim se pojave iz polja.

**Kontekst iz diskusije:**
Pomenuto više puta kao core capability. *"Imamo real-time, i možemo analizirati stvari u realnom vremenu."* Direktno se nadovezuje na USP iz Top menadžment grupe (brza reakcija = manji gubitak produkcije).

**Zaključak:**
Osnovna (hygiene) sposobnost za SCADA platformu — svaka ozbiljna platforma ovo ima. Treba je komunicirati u kombinaciji sa AI/ML (real-time anomaly detection) ili remote control (real-time reakcija), a ne kao izolovanu tačku.

**+ Plusevi:**
- WebSocket arhitektura — nema polling overhead-a
- Osnova za sve ostale real-time feature-ove (alarms, ML, dashboards)

**- Minusi / Rizici:**
- Samo po sebi nije diferencijator — svi to imaju
- Jača u kombinaciji sa drugim USP-ovima

---

### 8. Edge computing (konsenzus: 3/3 tima) ⭐

**Šta znači:**
Platforma može pokretati logiku, skripte i automatizaciju direktno na edge uređajima — bliže izvoru podataka, bez potrebe za slanjem svega na centralni server ili cloud.

**Kontekst iz diskusije:**
Na sastanku je diskutovano proširenje edge computing funkcionalnosti — od izvođenja skripti na jednom uređaju ka izvođenju na više uređaja simultano. Naglašeno je da je ovo kompleksna oblast i da lokalno ponašanje servisa utiče na ceo sistem. Sva 3 tima su ovaj USP navela nezavisno — što je uz "High level support" jedini drugi USP sa punim konsenzusom.

**Zaključak:**
Visok konsenzus (3/3) unutar tima potvrđuje da je ovo prepoznat diferencijator. Posebno relevantan za klijente sa distribuiranim postrojenjima, lošom konekcijom, ili latency-sensitive procesima. Trenutno u razvoju za proširene scenarije — treba precizno definisati šta je danas dostupno, a šta je roadmap.

**+ Plusevi:**
- Smanjuje latency (odluke se donose lokalno, odmah)
- Radi i bez cloud konekcije
- Smanjuje bandwidth troškove (filtriranje podataka na izvoru)
- Relevantan za IIoT deploymente sa stotinama senzora
- Pun timski konsenzus (3/3)

**- Minusi / Rizici:**
- Kompleksnost upravljanja distribuiranom logikom raste sa brojem edge čvorova
- Potrebno precizno definisati scope tekuće implementacije vs. roadmap

---

### 18. Push mehanizam orjentisanost (konsenzus: 1/3 tima)

**Šta znači:**
Platforma šalje podatke prema klijentima (web browsers, mobile aplikacije, third-party sistemi) čim se dogode promene — umesto da klijenti moraju stalno pitati za podatke (polling). Zasniva se na WebSocket i Kafka arhitekturi.

**Kontekst iz diskusije:**
Pomenuto kao arhitekturni princip koji podržava real-time pristup i skalabilnost.

**Zaključak:**
Više arhitekturni princip nego direktno prodajni USP. Najkorisnije ga je komunicirati kroz efekte koje donosi (real-time dashboards, instant alarmi, manje opterećenja servera) a ne kroz tehničku terminologiju.

**+ Plusevi:**
- Efikasno korišćenje resursa (nema polling overhead-a)
- Osnova za instant alarm notifikacije
- Skalabilnost — server ne mora odgovarati na hiljade simultanih upita

**- Minusi / Rizici:**
- Tehnički koncept koji nije direktno razumljiv non-tehničkoj publici — treba ga prevesti u benefit

---

### 13. Kontrola distribuiranih sistema (konsenzus: 1/3 tima)

**Šta znači:**
Platforma može upravljati i nadgledati procese raspoređene na više fizičkih lokacija, objekata ili fabrika — iz jednog centralnog interfejsa.

**Kontekst iz diskusije:**
Na sastanku pomenuto uz napomenu da su *"distribuirani sistemi tvrdi za computing"* — što je bio iskren komentar o kompleksnosti. Ujedno naglašeno da platforma to podržava.

**Zaključak:**
Visoka vrednost za klijente sa multi-site operacijama (npr. lanci fabrika, distributivne mreže, komunalna preduzeća sa više objekata). Kombinuje se sa multitenancy i cloud-agnostic USP-om.

**+ Plusevi:**
- Single pane of glass za multi-site operacije
- Relevantan za enterprise i critical infrastructure klijente
- Direktno se nadovezuje na cloud agnostic + hybrid USP

**- Minusi / Rizici:**
- Kompleksnost implementacije i podrške raste eksponencijalno sa brojem lokacija
- Potrebno imati reference implementacije za kredibilitet

---

## 🟧 Operational
> *Ciljna publika: operateri, inženjeri na terenu, IT timovi klijenta*

---

### 24. Intuitivan UI (konsenzus: 2/3 tima)

**Šta znači:**
Korisnički interfejs platforme je dizajniran da bude razumljiv osobama koje nisu IT stručnjaci — operaterima u pogonu, inženjerima na lokaciji, tehničarima. Platforma nudi responsive dizajn koji radi na PC-u, tabletu i mobilnom telefonu iz istog sistema.

**Kontekst iz diskusije:**
Na sastanku je naglašeno da UI mora biti prilagođen korisniku "u/na pogonu/lokaciji" — dakle osobi čiji je posao praćenje procesa, a ne rad sa softverom. Responsive dizajn (isti program na PC, tablet, telefon) direktno adresira ovaj zahtev.

**Zaključak:**
Solidan USP, posebno u segmentu industrijskog tržišta gde je konkurencija često kompleksna za korišćenje. Treba potkrepiti konkretnim primerima ili korisničkim feedbackom.

**+ Plusevi:**
- Smanjuje potrebu za treningom korisnika
- Širi krug potencijalnih korisnika sistema (nije potreban IT background)
- Responsive dizajn je redak u tradicionalnim SCADA sistemima

**- Minusi / Rizici:**
- "Intuitivan UI" je subjektivna ocena — potrebni su konkretni dokazi (user testing, feedback klijenata)
- Editor (Configurator) je na sastanku ocenjen kao donekle zastareo — ovo treba razlikovati od runtime UI-a

---

### 19. Remote Control (konsenzus: 1/3 tima)

**Šta znači:**
Mogućnost upravljanja fizičkim uređajima, aktuatorima i procesima direktno sa web ili mobilnog interfejsa, sa bilo koje lokacije u svetu — bez fizičkog prisustva na lokaciji.

**Kontekst iz diskusije:**
Ovo je jedna od najsnažnije naglašenih tačaka na sastanku, uprkos tome što je samo jedan tim naveo na stickeru. Direktni citat iz diskusije: *"Zašto bi top level menadžment uzeo naš proizvod ako nema remote control?"* — što govori da ovaj USP nije samo operativna pogodnost, već faktor koji utiče na odluku o kupovini na višem nivou.

**Zaključak:**
Jak USP koji se proteže kroz sve grupe publike — uprkos niskom sticker konsenzusu (1/3), bio je snažno podržan u plenarnoj diskusiji kao kritičan faktor. Funkcionalno prisutan u platformi. Ključno ga je jasno komunicirati i demonstrirati jer diferencira inView od čistih IoT monitoring platformi koje nude samo pregled podataka, bez mogućnosti kontrole.

**+ Plusevi:**
- Direktna distinkcija od "read-only" IoT platformi
- Visoka percipirana vrednost za menadžment (smanjuje potrebu za terenskim timovima)
- Relevantno za kritičnu infrastrukturu, udaljene lokacije, oil & gas

**- Minusi / Rizici:**
- Zahteva pažljiv pristup sigurnosti — remote control je i bezbednosni rizik ako nije dobro implementiran
- Treba biti jasno koji nivo kontrole je podržan i koji uređaji

---

### 25. Raznovrsnost komponenti (konsenzus: 1/3 tima)

**Šta znači:**
Platforma nudi bogat skup gotovih vizuelnih i funkcionalnih komponenti (grafovi, merači, tabele, alarmi, mape, itd.) koji se koriste za izgradnju SCADA ekrana i aplikacija.

**Kontekst iz diskusije:**
Pomenuto u kontekstu templating-a i no-code konfiguracije — raznovrsnost komponenti direktno doprinosi brzini razvoja novih ekrana i aplikacija.

**Zaključak:**
Dopunski USP koji jača No-Code priču. Teško ga je prodati kao standalone USP bez demonstracije, ali u kombinaciji sa No-Code IDE-om postaje konkretan argument.

**+ Plusevi:**
- Ubrzava implementaciju kod novih klijenata
- Smanjuje potrebu za custom razvojem

**- Minusi / Rizici:**
- Relativno teško porediti sa konkurencijom bez direktnog prikaza
- Zavisi od kvaliteta i aktuelnosti komponenti — stare komponente slabe argument

---

### 20. No-Code konfigurator i IDE (konsenzus: 2/3 tima)

> 🔗 *Affinity grupa — No-Code ekosistem: usko vezano za **#22 Templating** i **#21 No-Code mobilna aplikacija***

**Šta znači:**
Platforma omogućava izgradnju SCADA ekrana, workflow automatizacija i aplikacija bez pisanja koda — vizuelnim drag-and-drop editorom. IT tim klijenta ili sistem integrator mogu sami kreirati i menjati ekrane bez angažovanja programera.

**Kontekst iz diskusije:**
Jasno definisan kao USP na sastanku. Direktan citat: *"Novi ekrani bez kodiranja — mogu razviti vlastitu aplikaciju bez pomoći naučnika."* Međutim, otvorena je i kritika: trenutni editor je od strane nekih učesnika ocenjen kao *"malo zasteo"* u poređenju sa aktuelnim standardima. Configurator v3 je u aktivnom razvoju.

**Zaključak:**
Jak USP kada se komunicira u kontekstu brzine implementacije i nezavisnosti klijenta. Treba biti pažljiv u komunikaciji — istaknuti da je novi Configurator u razvoju, kako se ne bi stvorila pogrešna očekivanja kod potencijalnih klijenata.

**+ Plusevi:**
- Značajno smanjuje trošak i trajanje implementacije
- Klijent dobija autonomiju — može sam proširivati sistem
- Diferencijator od legacy SCADA sistema koji zahtevaju programere za svaku promenu

**- Minusi / Rizici:**
- Trenutna verzija editora je prepoznata kao zastarela — risk pri demo situacijama
- Configurator v3 još nije gotov — treba pažljivo upravljati komunikacijom

---

### 22. Templating (konsenzus: 2/3 tima)

> 🔗 *Affinity grupa — No-Code ekosistem: usko vezano za **#20 No-Code konfigurator i IDE** i **#21 No-Code mobilna aplikacija***

**Šta znači:**
Mogućnost kreiranja šablona za SCADA ekrane, konfiguracije uređaja i procese koji se mogu višekratno koristiti i instancirati — bez ponovnog kreiranja od nule.

**Kontekst iz diskusije:**
Pomenuto eksplicitno kao feature koji *"omogućava da se više stvari uradi brže"*. Direktno podržava USP "Veoma brza implementacija" iz Top Level grupe.

**Zaključak:**
Solidan operativni USP koji se najjasnije izražava kroz konkretne primere (npr. klijent sa 50 istih mašina — konfigurišete jednu, ostalo je template). Treba ga uvek pratiti brojevima ili primerima.

**+ Plusevi:**
- Dramatično ubrzava implementaciju kod klijenata sa ponavljajućim procesima ili uređajima
- Smanjuje greške (isti template = isti standard)

**- Minusi / Rizici:**
- Manje relevantan za klijente sa visoko individualizovanim procesima

---

### 21. No-Code mobilna aplikacija (konsenzus: 1/3 tima)

> 🔗 *Affinity grupa — No-Code ekosistem: usko vezano za **#20 No-Code konfigurator i IDE** i **#22 Templating***

**Šta znači:**
Platforma omogućava kreiranje mobilnih aplikacija (iOS/Android) bez razvoja zasebne native aplikacije — koristeći isti no-code alat i iste podatke kao web verzija.

**Kontekst iz diskusije:**
Pomenuto na sastanku uz neizvesnost oko nekih detalja: *"Postoji mobilna aplikacija na istoj platformi, možete promeniti ekran, promeniti prikaz... nisam siguran kako tačno funkcioniše na native nivou."* — što ukazuje da ovaj USP treba tehnički precizirati pre nego što se snažno komunicira prema van.

**Zaključak:**
Potencijalno jak USP (mobilni pristup SCADA-i je tražen), ali treba interno razjasniti granice funkcionalnosti i deploymeneta pre nego što postane deo standardnog prodajnog narrativa.

**+ Plusevi:**
- Visoka vrednost za klijente koji imaju terenske timove
- Jedna platforma = jedan alat za web i mobile

**- Minusi / Rizici:**
- Nejasnoće oko native deploymeneta treba razjasniti
- Potencijalno ograničena funkcionalnost u poređenju sa full native mobilnom aplikacijom

---

### 23. Batch device management (konsenzus: 1/3 tima)

**Šta znači:**
Mogućnost dodavanja, konfiguracije i upravljanja većim brojem uređaja odjednom — umesto individualnog, jednog po jednog.

**Kontekst iz diskusije:**
Eksplicitno navedeno na sastanku kao *"nismo potpuno rešili"* — trenutni workflow zahteva posetu jednoj lokaciji u jednom trenutku za dodavanje uređaja. Neko je napomenuo: *"Zaista ne znam jesam li to video negde drugde"* — što sugeriše da je to diferencijator, ali koji još nije u potpunosti implementiran.

**Zaključak:**
Visoka potencijalna vrednost kao USP, posebno za klijente sa distribuiranim mrežama (npr. 200 senzora na 50 lokacija). Trenutno je to više roadmap item nego dovršen feature — komunikacija prema klijentima mora to uzeti u obzir.

**+ Plusevi:**
- Značajna ušteda vremena za klijente sa velikim brojem uređaja
- Redak u industriji ako je dobro implementiran

**- Minusi / Rizici:**
- Još nije potpuno implementirano — rizik od preuranjene prodajne komunikacije
- Potrebno definisati scope: šta sve batch management pokriva

---

## ⬜ Manje relevantno (parkirano)
> *Validne ideje, ali nisu primarni USP-ovi u ovoj fazi*

---

### Custom software development (dostupan od INIT-a)

**Zaključak:**
Vredna usluga, ali nije USP platforme — to je profesionalna usluga. Može biti relevantan argument kod klijenata koji imaju specifične zahteve izvan standardnih mogućnosti platforme, ali se ne sme koristiti kao osnovna prodajna tačka jer može izazvati percepciju da platforma nije dovoljno kompletna.

---

### Fleksibilni custom reporti

**Zaključak:**
Reporting je prisutan u platformi (`IwsReport` servis), ali sam po sebi nije diferencirajući. Vredniji je kada se komunicira u kombinaciji sa AI uvidima ili automatskim izvršavanjem. Na sastanku je pomenuto kao potencijalna oblast za dalji razvoj.

---

### Role-based access control (RBAC)

**Zaključak:**
Neophodan feature za svaku enterprise platformu — hygiene factor, ne diferencirajući USP. Vredniji je kao deo šire "Security & Compliance" priče nego kao samostojna tačka. Na sastanku je pomenuto da je tim u aktivnom razvoju custom roles funkcionalnosti.

---

## BDM izbor — ključni USP-ovi

Nakon prateće radionice, BDM je izdvojio skup USP-ova koje smatra **stvarno ključnim** za prodajnu komunikaciju. Ovo nije finalna lista za sve situacije — već predlog fokusiranih USP-ova koji imaju najveći potencijal u razgovoru sa klijentima.

> 💡 *Oznaka `+` uz konsenzus znači da je BDM taj USP samostalno predložio i pre brainstorming sastanka — što je dodatna eksterna potvrda relevantnosti, van grupne dinamike.*

| # | USP | (Konsenzus) | Napomena |
|---|---|---|---|
| 1 | High level support | (⭐ 3+/3) | Jedini USP sa punim timskim konsenzusom + BDM potvrdom |
| 8 | Edge computing | (⭐ 3/3) | Pun timski konsenzus; jak tehnički diferencijator |
| 9 | Dokazana skalabilnost | (⭐ 3/3) | Pun timski konsenzus; ima konkretan produkcioni dokaz |
| 10 | Otvorenost za integracije | (2+/3) | Visok konsenzus + BDM potvrda |
| 19 | Remote Control | (1+/3) | BDM potvrda; kritičan faktor za Top Management odluku |
| 13 | Kontrola distribuiranih sistema | (1+/3) | BDM potvrda; visoka vrednost za multi-site klijente |
| 2 + 4 | Veoma brza implementacija + Brz razvoj feature-ova | (2+/3 + 2/3) | Affinity grupa — komunicirati zajedno kao *brzina isporuke* |
| 3 + 6 | Pricing + Pay-as-you-go model | (2+/3 + 1/3) | Affinity grupa — komunicirati zajedno kao *fleksibilan cenovni model* |
| 20 + 22 + 21 | No-Code konfigurator + Templating + No-Code mobilna aplikacija | (2+/3 + 2/3 + 1+/3) | Affinity grupa — komunicirati zajedno kao *No-Code ekosistem* |

Affinity grupe (parovi/trojke) se tretiraju kao **jedna prodajna priča**, a ne izolovane tačke — u ukupnom broju to je **9 USP-ova, grupisanih u 6 tematskih celina**.

---

## Napomena

Sledeći korak je **prioritizacija** ovih USP-ova po kriterijumima:
1. Važnost za klijente (1–5)
2. Jedinstvenost u odnosu na konkurenciju (1–5)
3. Dokazivost — imamo li konkretan dokaz? (Da / Ne / U razvoju)

Follow-up sastanak: **22.03.2026.** (TLS meet, posle GOAL-ova)
Deadline za radnu verziju USP dokumenta: **kraj marta 2026.**

---

*Dokument pripremio: R. Sabo | 12. mart 2026.*
*inVIEW IIoT Platform — INIT Technologies*
