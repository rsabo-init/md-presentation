# R&D Project Definition

## 1. Identifikacija

| Polje | Vrednost |
|-------|----------|
| **Naziv projekta** | WYSIWYG - WYSIWYG Editor |
| **Izvor ideje** | 2025 not finished yet |
| **Target vreme zavrsavanja** | Q1 2026 (Mart) |

---

## 2. Problem i Cilj

| Polje | Opis |
|-------|------|
| **Problem** | InView Editor za dizajniranje SCADA ekrana ima ogranicene WYSIWYG mogucnosti. Mobilni web client nema preview. Komponente trenutno ne primaju podatke u preview-u. Socket je otvoren ali se ne koristi optimalno. |
| **Business Value** | Brze kreiranje SCADA ekrana, mobilni preview, podaci na komponentama u preview-u, optimizovano koriscenje resursa (socket, getscreen). |
| **Success Criteria** | Mobilni preview radi kao web, komponente prikazuju podatke (ne live), socket i getscreen optimizovani. |

---

## 3. Scope

| Polje | Opis |
|-------|------|
| **In Scope** | Mobilni web client preview (isto kao web, prikaz mobile/desktop konfiguracije, top menu na editoru), podaci na komponentama (ne live values), provera socket-a za live podatke (gasenje ako nije potreban), optimizacija getscreen poziva za top menu (kesiraj posle prvog preview-a) |
| **Out of Scope** | Novi tipovi kontrola, responsive editor layout |
| **Dependencies** | Editor submodule, Client rendering engine, Socket infrastruktura |

---

## 4. OKR (Objectives and Key Results)

| Tip | Opis |
|-----|------|
| **Objective** | Omoguciti mobilni preview, podatke na komponentama i optimizovati socket/getscreen |
| **Key Result 1** | Mobilni web client ima preview identican web-u, sa prikazom mobile/desktop konfiguracije |
| **Key Result 2** | Komponente u preview-u prikazuju podatke (ne live values) |
| **Key Result 3** | getscreen poziv optimizovan (kesiran posle prvog preview-a), socket zatvoren ako nije potreban |

---

## 5. Effort i Alokacija Timova

| Polje | Vrednost |
|-------|----------|
| **Total Days** | 4 |
| **Parallel Teams** | NE |

| Tim | Dani |
|-----|------|
| FE | 4 |
| BE | - |
| AI | - |
| QA | - |
| DevOps | - |
| TL | - |

---

## 6. Rizici

| Rizik | Mitigation |
|-------|------------|
| Socket otvoren a ne koristi se za live podatke | Proveriti mogucnost live podataka, ako ne - gasiti socket kad nije potreban |
| getscreen poziv se poziva vise puta nepotrebno | Optimizovati - kesirati rezultat posle prvog preview-a |
| Komponente ne primaju podatke u preview-u | Obezbediti da podaci stizu (ne live values) |

---

## 7. Deliverables

- [ ] Mobilni web client preview (isto kao web, prikaz mobile/desktop konfiguracije, top menu na editoru)
- [ ] Podaci na komponentama u preview-u (ne live values)
- [ ] Provera socket-a za live podatke (gasenje ako nije potreban)
- [ ] Optimizacija getscreen poziva za top menu (kesiranje posle prvog preview-a)

---

## Jira Goal

> **Sta radimo?**
> Dodajemo mobilni web client preview, obezbedjujemo podatke na komponentama u preview-u, i optimizujemo socket i getscreen pozive.
>
> **Zasto radimo?**
> Mobilni web client trenutno nema preview. Komponente ne primaju podatke. Socket je otvoren ali se ne koristi optimalno, getscreen se poziva vise puta nego sto je potrebno.
>
> **Kako cemo znati da smo uspesno zavrsili?**
> Kada mobilni preview radi kao web, komponente prikazuju podatke (ne live), socket je optimizovan, i getscreen se kesira posle prvog preview-a.
