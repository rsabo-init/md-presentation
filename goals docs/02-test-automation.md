# R&D Project Definition

## 1. Identifikacija

| Polje | Vrednost |
|-------|----------|
| **Naziv projekta** | Test Automation - Automatizacija testiranja |
| **Izvor ideje** | Brainstorming notes |
| **Target vreme zavrsavanja** | !!! @MZ correct: Q1 2026 (Mart) |

---

## 2. Problem i Cilj

| Polje | Opis |
|-------|------|
| **Problem** | Manuelno testiranje InView platforme je sporo i podlozno greškama. Nedostaje automatizovani test suite koji bi omogucio brzu validaciju regresija i novih funkcionalnosti. |
| **Business Value** | Brzi release ciklusi, manje bugova u produkciji, smanjeno vreme QA tima na repetitivnim zadacima. |
| **Success Criteria** | !!! @MZ correct: Automatizovani test suite pokriven za kljucne user journeys, integrisan u CI/CD pipeline. |


> podsetnik: 
> podeliti po celinama:
> A. trenutno postojece procedure; Q1
> B. widely used nepokrivene komponente ; Q2
> C. continues covering; Definisati u Q2, praitit u Q3

---

## 3. Scope

| Polje | Opis |
|-------|------|
| **In Scope** | E2E testovi svih postojecih procedura regularnog deploya |
| ? **In Scope** | E2E well known komponenti |
| ? **In Scope** | Continues test writing |
| **Out of Scope** | Performance testiranje (zasebna inicijativa), testiranje edge uredaja |
| **Dependencies** | Stabilna test environment, pristup test podacima |

---

## 4. OKR (Objectives and Key Results)

| Tip | Opis |
|-----|------|
| **Objective** | Uspostaviti robustan automatizovani test framework za InView platformu |
| **Key Result 1** | 80% pokrivenost kriticnih user journeys automatizovanim testovima |
| **Key Result 2** | Testovi integrisani u CI/CD - svaki commit prolazi kroz test suite |
| **Key Result 3** | Vreme manuelnog regresijskog testiranja smanjeno za 60% |

---

## 5. Effort i Alokacija Timova

| Polje | Vrednost |
|-------|----------|
| **Total Days** | 30 |
| **Parallel Teams** | NE |

| Tim | Dani |
|-----|------|
| FE | - |
| BE | - |
| AI | - |
| QA | 30 |
| DevOps | - |
| TL | - |

---

## 6. Rizici

| Rizik | Mitigation |
|-------|------------|
| Flaky testovi zbog async operacija | Implementacija robust wait strategija, retry mehanizama |
| Test environment nestabilnost | Dedicated test environment sa izolovanim podacima |
| Odrzavanje test suite-a postaje skupo | Modularni test dizajn, page object pattern |

---

## 7. Deliverables
!!! @MZ correct:
- [ ] Automatizovani E2E test suite (Cypress/Playwright)
- [ ] API test suite (Postman/Newman ili custom)
- [ ] CI/CD integracija (GitLab/Jenkins pipeline)
- [ ] Test reporting dashboard
- [ ] Dokumentacija za pisanje novih testova

>Za Robija chckLista:
> A. trenutno postojece procedure; Q1
> B. widely used nepokrivene komponente ; Q2
> C. continues covering; Definisati u Q2, praitit u Q3
---

## Jira Goal

> **Sta radimo?**
> Gradimo automatizovani test framework za InView platformu sa E2E i API testovima.
>
> **Zasto radimo?**
> Da ubrzamo release cikluse i smanjimo broj bugova u produkciji kroz automatsku validaciju.
>
> **Kako cemo znati da smo uspesno zavrsili?**
> Kada 80% kriticnih user journeys bude pokriveno automatizovanim testovima integrisanim u CI/CD.
