# Sales Manager Context — inView Web SCADA
> Role: Sales Manager with Industrial Automation & SCADA background
> Purpose: Reference document for marketing conversations. Contains everything learned about the company, product, technology, and market positioning.
> Last updated: 2026-03-12

---

## 1. THE COMPANY

### INDAS Group (Parent)
- Founded: **1992** — over 30 years in industrial software
- Headquarters: Heroja Pinkija 95, Novi Sad, Serbia
- A well-established industrial IT company with deep domain roots

### INIT Technologies (Software Entity)
- Spun off from INDAS R&D in **2020** as an independent, innovation-focused software company
- Responsible for all software product development and commercialization
- Operates under the INDAS Group umbrella

### Product Portfolio (INDAS/INIT Group)
| Product | Description |
|---|---|
| **inVIEW IIoT / inView Web SCADA** | Core cloud IIoT/SCADA platform (main product) |
| **Oilfield-Monitor** | Specialized digital oilfield monitoring service |
| **inFOCUS** | Middleware SaaS — ERP to MES/automation integration |
| **Batch-ML** | ML platform for batch manufacturing processes |
| **inMEDIC** | Healthcare cloud platform for remote patient monitoring |

### Company Strengths & Credibility Points
- 30+ years of industrial domain experience (through INDAS)
- Real, deployed products in multiple verticals (not just a startup pitch)
- In-house R&D team driving continuous innovation
- Full-stack capability: hardware protocols → cloud → AI/ML → mobile
- European (Serbian) company — relevant for EU market positioning and GDPR compliance

---

## 2. THE PRODUCT — inView Web SCADA / inVIEW IIoT Platform

### Product Website
- **https://inview.software/**

### Company Website
- **https://industrial-it.software/**

### Core Identity
inView Web SCADA is a **cloud-native, no-code Industrial IoT and SCADA platform** that enables businesses to monitor, control, and automate industrial processes from anywhere using a web or mobile interface. It bridges the gap between the factory floor (OT/devices) and enterprise systems (IT/cloud/AI).

### Historical Evolution — This Is a Mature Product
| Year | Milestone |
|---|---|
| 1992 | INDAS Group founded |
| 2007 | First internal web-based SCADA prototype |
| 2011 | Commercial **inVIEW WebSCADA** launched |
| 2015 | Transformed to **multi-tenant Cloud SCADA** |
| 2017 | Evolved into **inVIEW IIoT Platform** |
| 2020 | INIT Technologies established; platform modernized |
| Present | Microservices, AI/ML, Edge automation, No-code IDE |

> **Sales Note:** This is NOT a startup product. It has 15+ years of real-world industrial deployment behind it. That is a powerful trust signal.

### The 6 Core Platform Modules
1. **EDGE** — Edge automation for distributed, local processing
2. **AI/ML** — Built-in machine learning and artificial intelligence
3. **DEVICES** — Multi-protocol device connectivity layer
4. **CORE ENGINE** — Central real-time SCADA processing and control
5. **ENDPOINTS** — Multi-protocol connection points (REST, WebSocket, MQTT, etc.)
6. **NO-CODE IDE** — Visual drag-and-drop application builder

---

## 3. TECHNOLOGY DEEP DIVE

### Architecture Philosophy
- **Microservices-first** with optional monolithic fallback for simplicity
- **Event-driven** via Apache Kafka for loose coupling and scalability
- **Cloud-native** — containerized with Docker, orchestrated with Kubernetes
- **AI-augmented** — ML modules embedded directly into the platform, not bolted on

### Tech Stack
**Frontend:**
- Angular 15+
- React.js
- Responsive web design (works on desktop, tablet, mobile)

**Backend:**
- .NET 8.0 (core engine, APIs)
- ASP.NET Core 8.0 (modern REST API)
- Java (middleware and integration services)
- Python (ML/analytics modules)
- Node.js

**Infrastructure & Messaging:**
- Apache Kafka — event streaming backbone (17 system-wide topics)
- Redis — high-performance caching (sub-millisecond data access)
- MariaDB — primary production database
- SQLite — lightweight option for dev/testing
- Kubernetes — container orchestration
- Docker — containerization

### Protocol Support (Industrial Connectivity)
This is a critical differentiator — broad protocol coverage out of the box:

| Protocol | Standard |
|---|---|
| OPC UA / OPC DA | Industrial interoperability standard |
| Modbus TCP | Most common industrial protocol |
| IEC 60870-5-104 | Telecontrol / power grid systems |
| DNP3 | Utility and infrastructure SCADA |
| Siemens S7 | Siemens PLC direct connection |
| MQTT | IoT messaging standard |
| LoRaWAN | Long-range low-power IoT |
| i3x | Custom InView proprietary protocol |
| Custom IPP driver | Extensible driver architecture |

> **Sales Note:** Supporting IEC 60870-5-104 and DNP3 alongside OPC UA means the platform is suitable for **critical infrastructure** (energy, water, utilities) — a very specific and lucrative market segment.

### Microservices Architecture (26 Services)
Key services by category:

**Core Processing:**
- `IwsCore` — Central SCADA engine
- `IwsWebApi` — Legacy REST API
- `IwsAspNetCoreWebApi` — Modern ASP.NET Core API
- `IwsManager` — Service orchestration and lifecycle

**Data & Analytics:**
- `IwsLogging` — Centralized structured logging
- `IwsHistory` — Historical data storage and retrieval
- `IwsAnomalyDetection` — ML-based anomaly detection
- `IwsAI` — AI feature consolidation service
- `IwsCacheSaver` — Redis caching layer

**Alarms & Events:**
- `IwsEventsAndAlarms` — Alarm/event detection engine
- `IwsAEStream` — Real-time alarm/event streaming
- `IwsAEDBWritter` — Dedicated alarm/event database persistence

**Automation & Integration:**
- `IwsScripting` — JavaScript-based script execution
- `IwsHook` — Event hooks and automation triggers
- `IwsValue2Rest` — Push values to external REST endpoints
- `IwsPluginRunner` — Plugin extension system

**Infrastructure:**
- `IwsWss` — WebSocket server (monolith variant)
- `IwsMqttStats` — MQTT statistics and monitoring
- `IwsPing` — Network availability monitoring
- `IwsReport` — Report generation
- `IwsInterwithpurposemanager` — i3x protocol integration

### Data Flow (Simplified)
```
Field Devices / PLCs / Sensors
        ↓ (OPC UA, Modbus, MQTT, etc.)
IwsCore (SCADA Engine)
        ↓ publishes to Kafka topics
Parallel consumers:
  → IwsLogging (persist raw data)
  → IwsEventsAndAlarms (detect alarms)
  → IwsCacheSaver (Redis cache)
  → IwsScripting (trigger automation)
  → IwsAnomalyDetection (ML analysis)
        ↓
Redis Cache / MariaDB / WebSocket broadcast
        ↓
Web Clients / Mobile Apps / Third-party Systems (REST, MQTT)
```

### Deployment Models
| Model | Description |
|---|---|
| **On-Premise** | Self-hosted on customer infrastructure |
| **Cloud** | Managed cloud (SaaS model) |
| **Hybrid** | Mix of on-premise and cloud |
| **Edge + Cloud** | Local edge processing + cloud synchronization |

### Deployment Variants (Technical)
| Variant | Database | Caching | Messaging | Best For |
|---|---|---|---|---|
| SQLite | SQLite (file) | In-memory | None | Dev/Testing |
| MariaDB | MariaDB | Optional Redis | Optional Kafka | Small Production |
| Full Stack | MariaDB | Redis | Kafka + Zookeeper | Full Production |
| Microservices | MariaDB | Redis | Kafka | Enterprise/Scalable |

---

## 4. KEY FEATURES & CAPABILITIES

### Real-Time Monitoring & Control
- Live variable streaming via WebSockets
- Multi-source data aggregation from heterogeneous devices
- Custom dashboards and KPI visualization
- Remote control of field devices from anywhere in the world

### Alarm & Event Management
- Configurable alarm thresholds (High/Low) with deadband support
- False alarm prevention via double-check validation (AlarmsDoubleChecker)
- Multi-channel notifications: SMS, Email, Push notifications
- Complete alarm/event history and audit trail
- Parallel processing for high-volume alarm environments

### No-Code IDE / Visual Builder
- Drag-and-drop SCADA screen builder
- Flow-based automation editor (no programming required)
- Configurator v2 and v3 (active development)
- Enables rapid deployment without software developers

### AI & Machine Learning (Built-In)
- **Self-Prediction module**: Time-series forecasting using LSTM neural networks and Random Forest models
- **Anomaly Detection**: Multiple algorithms — Z-Score, IQR, Out-of-Range, Rate-of-Change, Timeout
- Feature selection using Pearson, Spearman, Mutual Information statistical methods
- Ensemble detection combining multiple algorithms for improved accuracy
- Model versioning and incremental updates (no full retraining required)
- MLflow integration for ML lifecycle management
- Auto and manual threshold configuration modes

### Automation & Scripting
- No-code visual workflow editor
- JavaScript-based scripting engine
- Soft PLC (Programmable Logic Controller) capabilities
- Conditional logic, event-driven triggers, scheduled tasks
- Hook system for event-driven automation

### Historical Data & Reporting
- Full historical data storage and retrieval
- Configurable data retention policies
- Report generation module
- Export capabilities for external analytics tools

### Multi-Tenancy
- Full multi-tenant cloud architecture
- Supports multiple enterprise customers on shared infrastructure
- Role-based access control
- Tenant isolation and security

### Security & Compliance
- Modern authentication mechanisms
- European company — GDPR-aware architecture
- Role-based permissions
- Audit trails for critical operations

---

## 5. TARGET MARKETS & CUSTOMER SEGMENTS

### Primary Industry Verticals

**1. Industrial Manufacturing & Automation**
- SCADA systems for production lines
- DCS (Distributed Control Systems)
- Machine monitoring and OEE tracking
- Predictive maintenance via AI/ML

**2. Energy & Utilities (Critical Infrastructure)**
- Electric power grid monitoring (IEC 60870-5-104, DNP3)
- Water and wastewater management
- Gas pipeline monitoring
- Renewable energy (wind, solar farm management)

**3. Smart Cities & Infrastructure**
- Transportation management systems
- Environmental monitoring networks
- Traffic control
- Public utility monitoring

**4. Oil & Gas**
- Oilfield monitoring (dedicated product: Oilfield-Monitor)
- Pipeline SCADA
- Remote well monitoring

**5. Healthcare & Medical**
- Remote patient monitoring (inMEDIC product)
- Medical equipment tracking
- Hospital building management systems
- Wearable device data aggregation

**6. Logistics & Cold Chain**
- Fleet and asset monitoring
- Temperature-controlled transport
- Warehouse automation
- Supply chain visibility

### Customer Types by Business Role

| Type | Description |
|---|---|
| **System Integrators (SI)** | Deploy and configure inView for their end clients — high-value reseller channel |
| **OEM Manufacturers** | Embed inView into their machines/products as a branded solution |
| **Managed Service Providers** | Offer distributed SCADA-as-a-service to multiple clients |
| **Enterprise End-Users** | Internal IT/OT teams managing industrial operations directly |
| **Government / Critical Infrastructure** | Public sector utilities, smart city operators |

---

## 6. COMPETITIVE POSITIONING NOTES

### What Makes inView Different (Observed, Not Yet Formally Defined as USPs)

1. **Maturity + Modernity**: 15 years of real-world deployment + fully modernized cloud-native architecture. Rare combination.
2. **True No-Code**: Not just a dashboard tool — full no-code application builder for SCADA screens AND automation workflows.
3. **Embedded AI/ML**: Native anomaly detection and prediction, not a third-party add-on.
4. **Protocol Breadth**: From legacy industrial (Modbus, Siemens S7) to modern IoT (MQTT, LoRaWAN) in one platform.
5. **Deployment Flexibility**: Same platform, same features — on-premise, cloud, hybrid, or edge. No feature tiering by deployment model.
6. **Multi-Vertical**: One platform covering manufacturing, utilities, healthcare, logistics — unusual for a SCADA vendor.
7. **European Heritage**: For EU customers, relevant for compliance, data sovereignty, and support timezone alignment.
8. **Microservices at Core**: Unlike legacy SCADA vendors with monolithic architectures, inView is built for cloud scale.

### Likely Competitors (Contextual — Not Explicitly Stated by Company)
- Ignition by Inductive Automation (dominant in US market)
- Siemens WinCC / MindSphere
- Wonderware (AVEVA)
- Schneider Electric EcoStruxure
- GE iFIX / CIMPLICITY
- Open-source alternatives: Thingsboard, Grafana + InfluxDB

> **Sales Note:** inView's strongest differentiator vs. legacy SCADA vendors is cloud-nativity + AI/ML + no-code. Vs. pure IoT platforms, it's the industrial protocol depth + alarm management + OT heritage.

---

## 7. ONGOING DEVELOPMENT & ROADMAP SIGNALS

### Active Development Areas (Observed from Repository)
- Migration from legacy WebAPI to modern ASP.NET Core 8.0 API
- Expansion of AI/ML capabilities (anomaly detection, self-prediction)
- Microservices architecture refinement (new services being split out)
- Configurator v3 development (next-gen no-code IDE)
- Enhanced security and modern authentication

### Technical Debt / Evolution in Progress
- Dual API layer (legacy + modern) — transitioning period
- Monolith-to-microservices migration path supported for existing customers
- Node 16.17.1 LTS pinned — client modernization likely upcoming

---

## 8. CI/CD & DEVELOPMENT PROCESS
- GitLab CI for automated builds
- Docker Hub (inittech organization) for image registry
- Kubernetes + Argo CD for production deployments
- Branch strategy: `master` (production), `develop` (active development), `master-ofm` (Oilfield variant)
- Automated versioning by commit SHA

---

## 9. KNOWN DEPLOYMENT ENVIRONMENTS
- `https://stage.inviewscada.com` — Staging
- `https://platform.inviewscada.com` — Production
- `https://ofmtest.inviewscada.com` — Oilfield module test
- Local: `localhost:81` (SQLite), `localhost:8081` (MariaDB/Microservices)

---

## 10. CONTEXT FOR THIS CONVERSATION

This document was created in the context of a **USP definition exercise**. The user is the **Head of R&D** at INIT Technologies. The team conducted an internal brainstorming session to define Unique Sales Points (USPs). The next step is to write a formal follow-up document based on the brainstorming output.

### What Was NOT Yet Shared (As of This Document's Creation)
- The actual raw output / notes from the USP brainstorming session
- The intended audience for the follow-up document (sales team, investors, marketing, customers)
- The desired format (one-pager, full brief, slide deck outline, etc.)
- Current sales challenges or objections from the field
- Existing marketing materials or messaging that should be aligned with

---

*Document created by: Sales Manager Agent (Claude Sonnet 4.6)*
*Source: inview.software, industrial-it.software, full inViewWebScada repository MD files*
