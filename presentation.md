<!-- slide: 1/40 — Title -->
# inView IIoT Platform
## Newsletter Q1 2026

---

<!-- slide: 2/40 — Agenda -->
# Agenda

- Edge Scripts — Flows & Simulator
- inWise — LLM with InView
- Responsive Client
- App Improvements
- Quality Assurance with InView
- Highlights from 2025
- Q&A

---

<!-- slide: 3/40 — Edge Scripts: Background -->
# Edge Scripts

IWS scripts have always been a powerful tool — C#-like code that reads and writes variables, executes logic, automates processes. But everything runs **in the cloud**.

The **i3x gateway** sits on-site: reads devices, PLCs and sensors, sends variables to the cloud. It has processing power — and it's always there, regardless of internet connectivity.

**The question was:** why not push the script directly to the gateway?

- Location without stable internet → the script must run autonomously
- Real-time reaction to events → no cloud round-trip latency
- The gateway already knows all local variables — no need to go to the cloud


---

<!-- slide: 4/40 — Edge Scripts: How it works -->
# Edge Scripts

The developer writes a script **almost identically** to an IWS script — similar syntax, same variable access, same mental model.

The only difference: the script is deployed to the **i3x gateway**.

- Executes **locally** on the gateway — the user doesn't notice
- Works even when there is **no internet connection**
- Can read variables from the cloud — **remote locations** can communicate


**Result:** automation that lives at the network edge, independent of the cloud, but part of the same platform.

**Use case:** OFM wells monitoring, no operator action needed, only getting notified and next morning analyze what happened and why

![Edge Scripts — Architecture](images/q1-2026/edge-scripts-arch.svg)

---

<!-- slide: 5/40 — Edge Scripts: Architecture -->
# Edge Scripts — Architecture

![Edge Scripts — Architecture](images/q1-2026/edge-scripts-arch.png)

---

<!-- slide: 6/40 — Edge Scripts: Demo -->
# Edge Scripts — Demo

Demo

![Edge Scripts — Demo](images/q1-2026/edge-scripts-1.png)

---

<!-- slide: 7/40 — Edge Scripts: Flows -->
# Flows

No-Code IDE with scripts? Let's draw the script.

- Flow programming to draw scripts - **Visual presentation script**
- **Debug mode** - easily simulate your flow
- Same behavior as written edge scripts - you also can **switch to code** if you prefer


---

<!-- slide: 8/40 — Edge Scripts: Simulator Mode -->
# Simulator Mode

Demo

![Edge Scripts — Simulator](images/q1-2026/edge-scripts-2.png)

---

<!-- slide: 9/40 — AI & LLMs: The Opportunity -->
# InWise - LLMs with InView

![inView InWise](images/q1-2026/ai-icon.png)

**Large Language Models are transforming how we interact with software.**

LLMs can now understand context, generate code, and answer domain-specific questions — without retraining, without integration complexity.

Two immediately valuable use cases at InView, two **agents**:

- **Knowledge access** — the platform has rich documentation; let users query it conversationally
- **Script generation** —  scripts are powerfull tool; let AI write the them


To be continued...

---

<!-- slide: 10/40 — InView Docs Agent: Docs -->
# InView Docs Agent

![inView InWise](images/q1-2026/ai-icon.png)

**Ask the platform a question. Built on the documentation and user manual.**

The Docs Agent is trained on the official inView documentation — Editor, Configurator, drivers, components, properties...

Users ask questions in natural language and receive precise, contextual answers.

- No need to search through documentation pages manually
- Available directly inside the platform — no **context switching**
- Multilanguage supported

**Who benefits:** New team members, clients configuring independently, support engineers resolving tickets faster.

---

<!-- slide: 11/40 — InView Docs Agent: Docs — Demo -->
# InView Docs Agent

Demo

![InView Docs Agent — Documentation](images/q1-2026/docs-agent.png)

---

<!-- slide: 12/40 — Coding Agent -->
# Coding Agent

**Describe what the script should do — AI writes it.**

Writing Scripts **requires basic coding** knowledge. The Coding Agent removes that barrier — users describe the desired automation in plain language, and the agent generates ready-to-use code.

- **Analyze** — describe the script; identify potential problems
- **Write** — one click syncs the generated code directly into the Scripting editor; iterate in chat until correct
- **Variables Context** — drag variables from the Configurator into the chat; the agent understands the available resources and variable names — no broken references

Non-coding questions are automatically rejected — the agent stays focused on scripts.

---

<!-- slide: 13/40 — Coding Agent: Demo -->
# Coding Agent — Demo

Demo

![Coding Agent — Variables in context](images/q1-2026/coding-agent.png)

---

<!-- slide: 14/40 — Responsive: Web Positioning Concepts -->
# Responsive Client

**No more static absolute positioning needed while drawing in InView Editor**

**Absolute positioning** — every element has hardcoded pixel coordinates
- Works perfectly at the design resolution
- Manually create a separate layout for each target resolution: Desktop, Mobile

**Relative positioning** — elements are defined by their relationship to each other, not their exact position. Position while rendering

- One layout definition → correct on any screen
- The standard approach for modern web UIs since ~2015. Still new for SCADA

---

<!-- slide: 15/40 — Responsive Client: Flex Layout -->
# Responsive Client — Flex Layout

**Brand new InView's responsive client is built on CSS Flexbox — the web standard.**

Screens are structured in layers:

- **Containers** — invisible zones that define a layout direction (`flex-row →` or `flex-column ↕`)
- **Components** — occupy the space the container assigns them (`flex: 1`, `flex: 2` for proportional sizing)
- **Grid layout** - multiple containers present as view

When the screen expands or shrinks, the container redistributes space automatically. Components follow.

**Result:** The same screen definition renders correctly on a 10" industrial panel and a 27" monitor — without any manual adjustment.

---

<!-- slide: 16/40 — Responsive Client: Demo -->
# Responsive Client — Demo

Demo

![Absolute vs Flex Layout — Visual Comparison](images/q1-2026/responsive.png)

---

<!-- slide: 17/40 — Responsive Client: Flex Illustration -->
# Responsive Client — Flexbox

![Absolute vs Flex Layout — Visual Comparison](images/q1-2026/flexbox2.png)

---

<!-- slide: 18/40 — App UX: Intro -->
# App UX Improvements

**Continuously improving and adapting to make the everyday job easier.**

We work closely with the people who use inView daily — operators, configurators, and engineers — listening to their feedback and delivering improvements that reduce friction in their workflow.

We delivered a significant number of tasks. Three of them highlighted as immediately visible improvements:

- **WYSIWYG Quick Preview** — see the screen as the client renders it, without leaving the Editor
- **Advanced Search** — wildcard search in the Configurator for projects with hundreds of variables
- **Follow Live Values** — personal variable groups to monitor across connections in one place
Feel free to participate, give your feedback
---

<!-- slide: 19/40 — WYSIWYG -->
# WYSIWYG — Quick Preview

**See how the screen looks — without saving, without switching to the client.**

Before this feature, validating a screen design meant: save the configuration → log in to the client → navigate to the screen → review → go back and edit. Every iteration meant that full loop.

Now: click the **Quick Preview** button (eye icon) in the Editor toolbar — the runtime view opens in the same window, instantly.

- No saving required — preview works on unsaved configuration
- No client login — no credentials, no session, no navigation
- No risk of losing work — the preview is read-only, configuration is not touched
- Less temporary versions - save only when you are done with a complete module

![WYSIWYG Quick Preview button](images/q1-2026/app-wysiwyg-button2.png)

---

<!-- slide: 20/40 — WYSIWYG: Demo -->
# WYSIWYG — Quick Preview

Demo

![WYSIWYG Quick Preview — full view](images/q1-2026/app-wysiwyg.png)

---

<!-- slide: 21/40 — Advanced Search & Follow Live Values -->
#  Follow Live Values & Advanced Search


**Follow Live Values** — personal variable groups

On the Live Values page, users create named groups and add variables from any connection. The group works as a filter — one page, all the values you care about, regardless of which connection they belong to.

**Advanced Search** — wildcard search in the Configurator

Activated automatically when the search field contains quotes (`"` or `'`). Use `#STAR#` for prefix/infix/suffix search:

| Query | Matches |
|-------|---------|
| `"temperature sensor"` | Exact names including whitespace |
| `"#STAR#Sensor"` | Any variable ending with Sensor |
| `"temp#STAR#"` | Everything starting with temp |
| `"temp#STAR#Sensor"` | temperatureSensor, tempMaxSensor… |

Especially useful on projects with hundreds of variables across multiple drivers.

---

<!-- slide: 22/40 — App UX: Demo -->
# App UX — Demo

![Advanced Search Demo](images/q1-2026/app-advanced-search.png)

---

<!-- slide: 23/40 — Quality: Challenges -->
# Quality in Complex Platforms

**A SCADA platform grows fast. Quality processes don't keep up automatically.**

InView has a lot of editor components, different driver behaviours, **thousands of configurable properties**.
Every release brings new features.
Every deploy carries risk.

The challenges are well-known in any platform of this scale:

- **Documentation gaps** — new features ship, documentation doesn't follow; teams rely on tribal knowledge
- **Testing by memory** — what gets tested depends on who tests it, not on a defined process
- **No visibility after deploy** — is this release better or worse than the last one?

These aren't bugs. They're process gaps — and they compound over time.

---

<!-- slide: 24/40 — Quality: Documentation -->
# Documentation

**Every component explained. Every property defined.**

The Editor and Configurator are now fully documented — every component, every property, its accepted values, its default, and when to use it.

- **Editor** — all visual components, display logic, binding properties
- **Configurator** — drivers, connections, tags, scripts; e.g. ModbusTCP driver with all fields described

Goal: any team member or client — regardless of experience — can open the documentation and understand exactly what an option does without guessing or asking support.

**Available on SharePoint:** `INIT > Documents > Teams > QA`

> The same knowledge is now also accessible via the **InView Docs Agent** — ask a question in natural language, get an answer grounded in this documentation.

---

<!-- slide: 25/40 — Documentation: Configurator -->
# Documentation — Configurator

![Documentation — Configurator](images/q1-2026/Devices_configurator.png)

---

<!-- slide: 26/40 — Documentation: Editor -->
# Documentation — Editor

![Documentation — Editor](images/q1-2026/Control_bar.png)

---

<!-- slide: 27/40 — Quality: TestRails + Automated Tests -->
# Test Rails & Automated Tests

**Documented tests. Automated execution. Proof after every deploy.**

**TestRails — test case management**

Before: testing tracked in spreadsheets, coverage depending on who ran it and when. Now: all test cases are migrated into TestRails, organized by procedure, with milestone traceability and Jira integration. 

**Automated Tests (Cypress)**

The highest-risk procedures are now covered by automated end-to-end tests that run on every deploy:

| Procedure | What it covers |
|-----------|----------------|
| **Wells CRUD** (Boomerang) | Adding, renaming, retiring, deleting Wells |
| **Advanced Configurator** | Most commonly used Configurator components |
| **Editor / Client** | Consistency between configuration and client display |

After each run: a structured **PDF report** is generated and delivered automatically to defined addresses — with pass/fail per test case and history over time.

**The loop is closed:** documented in TestRails → executed automatically → report proves the result.

---

<!-- slide: 28/40 — Automated Tests: Demo 1 -->
# Automated Tests

![Automated Tests — Editor GUI](images/q1-2026/editorGUI1.png)

---

<!-- slide: 29/40 — Automated Tests: Demo 2 -->
# Automated Tests

![Automated Tests — Editor GUI](images/q1-2026/editorGUI2.png)

---

<!-- slide: 30/40 — Test Report -->
# Test Report

![Test Report](images/q1-2026/Challanged_report.png)

---

<!-- slide: 31/40 — Highlights from 2025 -->
# Highlights from 2025

**Missed from last year SPS Expo in Nuremberg**
- InView Forecast
- Anomaly Detection
- **Integration tools** - Power BI, Grafana, Web Hook

---

<!-- slide: 32/40 — InView Forecast -->
# InView Forecast — Future Variable Value

**The platform predicts what a variable will be — before it gets there.**

Every variable has a history. InView Forecast uses that history to **train a model** and generate a **forecast** — a predicted future value with a confidence range. The prediction updates incrementally as new data arrives.

**How it works:**

- **Model**: LSTM neural networks + Random Forest — two complementary approaches, combined for accuracy
- **Feature selection**: Pearson / Spearman / Mutual Information — the model identifies which other variables correlate with the target
- **Incremental updates**: the model improves continuously without full retraining

**What it enables:**

- Set an alarm on the *predicted* value — get notified before the threshold is breached, not after
- See the trend before it happens — operators gain reaction time
- Detect slow-moving problems that real-time monitoring misses

Easy AI tool for everyone

---

<!-- slide: 33/40 — InView Forecast: Demo -->
# InView Forecast

Demo

![Anomaly detection](images/q1-2026/ai.png)

---

<!-- slide: 34/40 — Anomaly Detection -->
# Anomaly Detection

**Stop setting alarms manually. Let the platform learn what normal looks like.**

Traditional SCADA alarm configuration is static — an engineer sets a threshold, and the alarm fires when the value crosses it. This works for known limits, but misses gradual drift, timing anomalies, and patterns that are hard to express as a single number.

**Anomaly Detection observes the variable's behavior over time and flags deviations automatically.**

Five detection algorithms are available — each targeting a different class of anomaly:

| Algorithm | What it catches |
|-----------|----------------|
| **Out-of-Range** | Values outside defined min/max (auto-learned or manual) |
| **Timeout** | Missing measurements beyond the 95th-percentile interval |
| **Rate-of-Change** | Values changing faster than historically normal |
| **IQR** | Statistical outliers using Q1/Q3 bounds |
| **Z-Score** | Deviations beyond ±3 standard deviations |
| #STAR#Ensemble | Anomaly only when all selected algorithms agree — fewer false positives |

**Configurable per variable:** choose which algorithms to apply, set auto or manual mode, combine them in ensemble.

---

<!-- slide: 35/40 — Anomaly Detection: Demo -->
# Anomaly Detection

Demo

![Anomaly detection](images/q1-2026/ad.png)

---

<!-- slide: 36/40 — Integrations -->
# Integrations — Power BI, Grafana, WebHooks

**inView data, in the tools the business already uses.**

SCADA data is operations data — but operations data is also business data. Teams that live in Power BI or Grafana shouldn't need to switch to a different interface to see plant performance.

**Power BI**
Connect inView variable history directly to Power BI. Build operational reports and executive dashboards using the same data that drives the SCADA screen — no manual export, no CSV.

**Grafana**
inView acts as a data source for Grafana. Teams already running Grafana for IT/DevOps monitoring can add OT data to the same dashboards, with the same alerting and visualization tools.

**WebHooks**
Event-driven HTTP callbacks — when a variable changes, an alarm fires, or a condition is met, inView sends a POST to any external endpoint. Connect to Slack, Teams, custom APIs, ERP systems, or any HTTP-capable service.

---

<!-- slide: 37/40 — Power BI Demo -->
# Power BI

![Power BI](images/q1-2026/power-bi.png)

---

<!-- slide: 38/40 — Grafana Demo -->
# Grafana

![Grafana](images/q1-2026/grafana-prev.png)

---

<!-- slide: 39/40 — WebHooks Demo -->
# Hooks

![Hooks](images/q1-2026/hooks.png)

---

<!-- slide: 40/40 — Q&A -->
# Q&A

**Questions?**

![INIT Logo](images/init-logo.png)

*INIT Technologies — inView Web SCADA*
