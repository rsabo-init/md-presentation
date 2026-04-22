# R&D Project Definition

## 1. Identifikacija

| Polje | Vrednost |
|-------|----------|
| **Naziv projekta** | ChatBot Scripts - AI Chat for Scripting |
| **Izvor ideje** | 2025 not finished yet |
| **Target vreme zavrsavanja** | Q1 2026 (Mart) |

---

## 2. Problem i Cilj

| Polje | Opis |
|-------|------|
| **Problem** | Pisanje C# skripti u InView IwsScriptProcessing modulu zahteva tehnicko znanje. Korisnici bez programerskog iskustva ne mogu kreirati automatizacije, sto ogranicava upotrebljivost platforme. |
| **Business Value** | Demokratizacija automatizacije - i ne-programeri mogu kreirati skripte, brzi time-to-value za klijente, smanjeno opterecenje support tima. |
| **Success Criteria** | Korisnici mogu kroz chat opisati zeljenu automatizaciju i dobiti funkcionalan C# kod za IwsScriptProcessing koji se moze direktno primeniti u Scripting editoru. |

**Napomene o integraciji sa Konfiguratorom (Scripting) — Overview 3 faze i outputi:**

**Faza 1 – Chatbot u Konfiguratoru (Read/Generate)**
- **Opis:** U konfigurator se dodaje dugme koje otvara iframe chatbota. Chatbot prima koding-orijentisane promptove i generiše C# kod u formatu kompatibilnom sa Scripting editorom.
- **Output:** Generisani C# snippet spreman za lepljenje u Scripting editor; jasna napomena da se placeholder varijable zamene stvarnim sistemskim varijablama vidljivim u editoru.
- **Ograničenja:** Ne-koding pitanja se odbijaju. Validacija formata output-a pre prikaza.

**Faza 2 – APPLY (Write/Sync)**
- **Opis:** U chat se dodaje APPLY dugme koje sinhronizuje generisani kod direktno u Scripting editor u istom kontekstu. Podržane su iteracije (korisnik traži izmene dok kod ne bude ispravan).
- **Output:** Kod je primenjen u editoru (default replace; opcioni append). Povratna informacija o validaciji/kompajliranju (success/error).
- **Fallback:** Ako se compile radi iz editora, zadržava se isti kontekst u chatu za brze ispravke.

**Faza 3 – Varijable (Context-Aware)**
- **Opis:** Varijable iz konfiguratora se drag&drop-uju u chatbot kontekst. Model generiše kod isključivo koristeći dostupne varijable.
- **Output:** Kod sa konzistentnim referencama na stvarne sistemske varijable; validaciona poruka ako nešto nedostaje.
- **UX/Validacija:** Ako nedostaju obavezne varijable ili je schema nevalidna, APPLY je disable-ovan uz jasnu poruku greške.


---

## 3. Scope

| Polje | Opis |
|-------|------|
| **In Scope** | AI chat u Configurator-u (iframe), generisanje C# skripti, validacija koda, APPLY mehanizam, varijable (drag&drop), kontekst sesije po userId:scriptId (Konfigurator salje identifikatore pri otvaranju iframe-a kroz postMessage) |
| **Out of Scope** | Automatsko deployment skripti, debugging kroz chat, istorija konverzacija, perzistentno cuvanje konteksta van in-memory pristupa (npr. Redis, baza), treniranje ili fine-tuning modela na internim skriptama ili primerima, uvodjenje novih LLM provajdera ili zamena primarnog modela, promene u osnovnoj prompt strategiji van dogovorenih ogranicenja za ne-koding upite, uvodjenje multi-agent logike ili autonomnog planiranja koraka, poboljsanja "razumevanja domena" kroz dodatne modele ili eksterno znanje, internacionalizacija chata (vise jezika), napredna UX poboljsanja |
| **Dependencies** | IwsScriptProcessing, Docs AI (RAG), LLM API, FE integracija, server resources |

---

## 4. OKR

| Tip | Opis |
|-----|------|
| **Objective** | Kreiranje InView skripti kroz prirodni jezik iz konfiguratora |
| **KR1** | Chat frame je dostupan klikom na dugme u Scripts ekranu u konfiguratoru i daje odgovore na pitanja o kreiranju skripti |
| **KR2** | APPLY flow stabilan - transport skripte iz chat dijaloga u Scripts IDE |
| **KR3** | Mogucnost drag&drop-ovanja varijabli |
| **KR4** | Ne-koding upiti pravilno odbijeni (100%) |

---

## 5. Effort i Alokacija

| Tim | Dani |
|-----|------|
| FE | 4 |
| AI | 14 |

---

## 6. Funkcionalnosti i Taskovi

### 6.1 Dugme + iframe chatbot (Konfigurator)
- FE: dugme + iframe
- AI (5-7 dana): ogranicenja za ne-koding pitanja, streaming UX, input/output schema, iterativni kontekst (1 skripta = 1 kontekst), deploy stage/prod

### 6.2 APPLY dugme
- FE: sync funkcija (chat -> editor)
- AI (2-3 dana): APPLY u chatbotu, fallback compile, append vs replace (default replace)

### 6.3 Varijable (Drag & Drop)
- FE: drag&drop varijabli
- AI (4 dana): hendlovanje drop-a, kontekst samo sa tim varijablama, error handling + disable APPLY ako fali

---

## 7. Rizici
- Nesiguran kod → validation + sandbox
- Halucinacije API-ja → validacija
- Neuskladjen format → strogi formatter
- UX streaming → optimizacija

---

## 8. Deliverables
- Chat UI (iframe + dugme)
- APPLY mehanizam
- AI backend (C# generation)
- Validacija koda
- Varijable (drag&drop)
- Dokumentacija
- Stage/Prod deploy

---

## Jira Goal

> **Sta radimo?**
> Gradimo AI chat asistenta za generisanje C# skripti direktno iz konfiguratora. Korisnici ce moci kroz prirodni jezik da opisu zeljenu automatizaciju i dobiju funkcionalan kod.
>
> **Zasto radimo?**
> Da demokratizujemo automatizaciju - i ne-programeri mogu kreirati skripte, brzi time-to-value za klijente, smanjeno opterecenje support tima.
>
> **Kako cemo znati da smo uspesno zavrsili?**
> Kada chat frame bude dostupan u konfiguratoru, APPLY flow bude stabilan, drag&drop varijabli radi, i 70% generisanih skripti radi bez korekcije.
