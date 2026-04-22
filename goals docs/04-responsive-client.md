# R&D Project Definition

## 1. Identifikacija

| Polje | Vrednost |
|-------|----------|
| **Naziv projekta** | Responsive Client - Responsivni klijent |
| **Izvor ideje** | 2025 not finished yet |
| **Target vreme zavrsavanja** | Q1 2026 (Mart) |

---

## 2. Problem i Cilj

| Polje | Opis |
|-------|------|
| **Problem** | InView Client aplikacija nije potpuno responsivna. Na mobilnim uredajima i manjim ekranima, SCADA ekrani i kontrole se ne prikazuju optimalno, sto ogranicava upotrebljivost na terenu. |
| **Business Value** | Operateri mogu koristiti InView sa bilo kog uredaja, povecana produktivnost na terenu, konkurentska prednost (mobile-first SCADA). |
| **Success Criteria** | Responsive Client ode na produkciju bez uticaja na postojece projekte. Bugovi se popravljaju inkrementalno kako se bude koristilo. |

---

## 3. Scope

| Polje | Opis |
|-------|------|
| **In Scope** | Merge develop u responsive granu i obrnuto (bez uticaja na postojece projekte), prolazak kroz 10 kljucnih komponenti, verifikacija Top menu renderovanja po tipu ekrana, Editor grid selekcija (npr. 3x3 sa merge celija) |
| **Out of Scope** | Native mobilna aplikacija, mobilna konfiguracija sa GrapeJS-om (potrebna dodatna analiza), Button akcija Hide element (nije vezano za responsive - zasebna inicijativa) |
| **Dependencies** | Client submodule, Bootstrap 5 framework, develop grana |

---

## 4. OKR (Objectives and Key Results)

| Tip | Opis |
|-----|------|
| **Objective** | Pustiti Responsive Client na produkciju bez uticaja na postojece projekte |
| **Key Result 1** | Merge develop <-> responsive grana zavrsen bez konflikata, postojeci projekti rade normalno |
| **Key Result 2** | 10 kljucnih komponenti provereno i prilagodjeno za responsive |
| **Key Result 3** | Top menu se ispravno iscrtava na osnovu tipa ekrana (verifikovano) |

---

## 5. Effort i Alokacija Timova

| Polje | Vrednost |
|-------|----------|
| **Total Days** | 7 |
| **Parallel Teams** | NE |

| Tim | Dani |
|-----|------|
| FE | 7 |
| BE | - |
| AI | - |
| QA | - |
| DevOps | - |
| TL | - |

---

## 6. Rizici

| Rizik | Mitigation |
|-------|------------|
| Merge utice na postojece projekte | Prvo merge develop u responsive granu, pa obrnuto - testirati da postojeci projekti rade normalno |
| Bugovi nakon pustanja na produkciju | Ocekivano - popravljaju se inkrementalno kako se bude koristilo |
| Performanse na mobilnim uredajima | Optimizacija renderovanja, lazy loading elemenata |

---

## 7. Deliverables

- [ ] Merge develop <-> responsive grana (bez uticaja na postojece projekte)
- [ ] Verifikacija Top menu renderovanja po tipu ekrana
- [ ] Prolazak kroz 10 kljucnih komponenti i prilagodjavanje
- [ ] Editor grid selekcija (npr. 3x3) sa mogucnoscu merge celija
- [ ] Button akcija Hide/Show element sa id-jem elementa (zasebno od responsive-a)

---

## Jira Goal

> **Sta radimo?**
> Pustamo Responsive Client na produkciju kroz merge sa develop granom, prolazimo kroz 10 kljucnih komponenti i dodajemo Editor grid selekciju.
>
> **Zasto radimo?**
> Da responsive funkcionalnost ode na produkciju bez uticaja na postojece projekte. Bugovi se popravljaju inkrementalno.
>
> **Kako cemo znati da smo uspesno zavrsili?**
> Kada responsive grana bude mergovana sa develop-om, postojeci projekti rade normalno, i 10 kljucnih komponenti je verifikovano.
>
> **Napomena:**
> U ovom kvartalu NIJE cilj napraviti mobilnu konfiguraciju sa GrapeJS-om (potrebna dodatna analiza). Poenta je pustiti na produkciju i vremenom poboljsavati.
