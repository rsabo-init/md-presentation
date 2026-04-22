# inView Web SCADA — General Platform Context
> **Purpose**: Master context document for all AI/LLM agents. Read this first. Do NOT read all project MD files — this file consolidates the essential knowledge.
> **Last updated**: 2026-03-25
> **Maintained by**: Head of R&D, INIT Technologies

---

## 1. COMPANY & PRODUCT IDENTITY

### Company
- **INDAS Group** — founded 1992, Novi Sad, Serbia. 30+ years in industrial software.
- **INIT Technologies** — software entity of INDAS Group, spun off in 2020. Leads all product development.
- Website: https://industrial-it.software/
- Product website: https://inview.software/

### Product: inView Web SCADA / inVIEW IIoT Platform
Cloud-native, no-code Industrial IoT and SCADA platform for remote supervisory control, data acquisition, visualization, and automation of industrial processes via web and mobile. Bridges OT (factory floor) with IT (cloud/AI).

**Historical milestones:**
| Year | Milestone |
|------|-----------|
| 2007 | First internal web-based SCADA prototype |
| 2011 | Commercial inVIEW WebSCADA launched |
| 2015 | Multi-tenant Cloud SCADA |
| 2017 | Evolved into inVIEW IIoT Platform |
| 2020 | INIT Technologies established; platform modernized |
| Now  | Microservices, AI/ML, Edge automation, No-code IDE |

**Key message**: NOT a startup. 15+ years of real-world industrial deployment. Fully modernized cloud-native stack.

### Product Portfolio (INDAS/INIT Group)
| Product | Description |
|---------|-------------|
| **inVIEW IIoT / inView Web SCADA** | Core cloud IIoT/SCADA platform (main product) |
| **Oilfield-Monitor** | Specialized digital oilfield monitoring |
| **inFOCUS** | Middleware SaaS — ERP to MES/automation integration |
| **Batch-ML** | ML platform for batch manufacturing |
| **inMEDIC** | Healthcare cloud platform for remote patient monitoring |

---

## 2. PLATFORM ARCHITECTURE OVERVIEW

### Two Deployment Modes

**Monolithic**: Run `WebAndSocketServerCore` project — integrates everything in a single process. Suitable for development and smaller deployments.

**Microservices**: Run individual services separately, communicating via Apache Kafka. Suitable for production and enterprise deployments.

### Key Infrastructure Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Message Broker | Apache Kafka (17 topics) | Async event streaming between microservices |
| Cache Layer 1 — Storage Redis | Redis (port 6379) | Config cache, sessions, CSRF tokens, rate limiting, resource locks |
| Cache Layer 2 — Process Image Redis | Redis (port 6380) | Real-time SCADA variable values (populated by IwsCacheSaver) |
| Primary Database | MariaDB (production), SQLite (dev/test) | Persistent data storage |
| Resilience | Polly (retry + circuit breaker) | Redis connection resilience |
| Container Orchestration | Docker + Kubernetes + Argo CD | Production deployment |
| CI/CD | GitLab CI | Automated builds and deployments |

### Tech Stack Summary
- **Backend**: .NET 8.0 / ASP.NET Core 8.0, Java (middleware), Python (ML), Node.js
- **Frontend**: Angular 15+, React.js, jQuery 3.7.1 / Bootstrap 5.3.2 / Webpack
- **Solution**: `IwsServer/Iws.sln` — 70+ C# projects

### Branch Strategy
- `master` — production
- `develop` — active development
- `master-ofm` — Oilfield variant

### Docker Registry
- Organization: `inittech` on Docker Hub

### Deployment Environments
| Environment | URL |
|-------------|-----|
| Production | https://platform.inviewscada.com |
| Staging | https://stage.inviewscada.com |
| Oilfield Test | https://ofmtest.inviewscada.com |
| Local (SQLite) | localhost:81 |
| Local (MariaDB/MS) | localhost:8081 |

---

## 3. MICROSERVICES — COMPLETE REFERENCE

### Core Processing Services

#### IwsCore — Central SCADA Engine
- **Entry**: `IwsCore.IwsCoreMSRunner`
- **Role**: Central data acquisition, variable processing, real-time control, protocol driver management
- **Kafka**: PRODUCES to `LIVE_VALUES_TOPIC` (live values) and `CONFIGURATION_EVENT_TOPIC`; CONSUMES from `VALUE_WRITE_TOPIC` (write commands) and `MS_REGISTER_TOPIC` (registration with Manager)
- **Enabled in MS mode when**: `AppConfig.MICROSERVICE_CONFIGURATION = true`
- **Docs**: `IwsServer/IwsCore/README.md`

#### IwsManager — System Orchestration
- **Entry**: `IwsManager.IwsManagerMSRunner`
- **Role**: Microservice lifecycle, health monitoring, GUID assignment, connection distribution, heartbeat tracking, auto-recovery
- **LiveDrivers managed**: CoreLiveDriver, ScriptLiveDriver, HistoryLiveDriver
- **Restart policies**: Always, On-Failure, Never, Delayed (with escalation)
- **Kafka**: BIDIRECTIONAL on `MS_REGISTER_TOPIC`, `MS_REGISTER_TOPIC_HISTORY`, `MS_REGISTER_TOPIC_SCRIPT`, `CONFIGURATION_EVENT_TOPIC`
- **Docs**: `IwsServer/IwsManager/README.md`

#### IwsWebApi — Legacy REST API
- **Role**: HTTP/REST endpoints, WebSocket communication, client data delivery, backward compatibility
- **Kafka**: PRODUCES to `VALUE_WRITE_TOPIC`, `CONFIGURATION_EVENT_TOPIC`, `REPORT_MS_TOPIC`; CONSUMES from `LIVE_VALUES_TOPIC`, `AE_STREAM_TO_DB`, `HOOK_STATE_TOPIC`, `SEND_TO_CLIENT_TOPIC`
- **Docs**: `IwsServer/IwsWebApi/README.md`

#### IwsAspNetCoreWebApi — Modern Web API
- **Role**: Modern ASP.NET Core 8.0 REST API; replaces/augments legacy IwsWebApi; Swagger integration; enhanced security
- **Status**: Active migration target from IwsWebApi
- **Docs**: `IwsServer/IwsAspNetCoreWebApi/README.md`

### Data & Cache Services

#### IwsCacheSaver — Redis Cache Populator
- **Role**: Consumes `LIVE_VALUES_TOPIC` from Kafka; writes to Process Image Redis with buffered batch writes; chronological validation; emergency notifications (Twilio, PagerDuty, email)
- **Redis key pattern**: `ProcessImage_{varId}`
- **Consumer group**: `cache_stream`
- **Kafka**: CONSUMES from `LIVE_VALUES_TOPIC` only
- **Docs**: `IwsServer/IwsCacheSaver/README.md`

#### IwsRedisCache — Caching Infrastructure Library
- **Role**: Dual-Redis architecture library; Polly resilience wrappers; used by all services
- **Docs**: `IwsServer/IwsRedisCache/README.md`

#### IwsHistory — Historical Data
- **Role**: Historical data storage and retrieval; database write for time-series variable values
- **Kafka**: Registers via `MS_REGISTER_TOPIC_HISTORY`

#### IwsLogging — Centralized Logging
- **Role**: System-wide structured logging via Log4net; multiple outputs (file, database, remote)
- **Docs**: `IwsServer/IwsLogging/README.md`

### Automation & Scripting

#### IwsScriptProcessing — Script Execution Engine
- **Entry**: `IwsScriptProcessing.IwsScriptProcessingMSRunner`
- **Role**: Dynamic C# script compilation (System.CodeDom), Quartz.NET scheduling; value-change, scheduled, event-driven, and on-demand scripts
- **Script types**: Default, Important, Scheduling, History
- **Kafka**: CONSUMES from `SCRIPTING_MESSAGES_TOPIC` (commands) + `LIVE_VALUES_TOPIC` (triggers); PRODUCES to `VALUE_WRITE_TOPIC`
- **Docs**: `IwsServer/IwsScriptProcessing/README.md`

#### IwsHook — Event Hooks
- **Role**: Webhook execution and event-driven automation triggers
- **Kafka**: `HOOK_STATE_TOPIC`

#### IwsValue2Rest — REST Push
- **Role**: Pushes SCADA variable values to external REST endpoints

#### IwsPluginRunner — Plugin System
- **Role**: Plugin extension architecture for custom integrations

### Alarms & Events

#### IwsEventsAndAlarms — Alarm Engine
- **Role**: Real-time alarm detection, configurable thresholds (High/Low), deadband support, false alarm prevention via AlarmsDoubleChecker, multi-channel notifications (SMS, email, push)
- **Kafka**: PRODUCES to `SEND_TO_CLIENT_TOPIC` and `AE_STREAM_TO_DB`
- **Docs**: `IwsServer/IwsEventsAndAlarms/README.md`

#### IwsAEStream — Alarm Event Streaming
- **Role**: Real-time alarm/event streaming to clients

#### IwsAEDBWritter — Alarm History Persistence
- **Role**: Dedicated alarm/event database persistence to TimescaleDB

### AI & Analytics

#### IwsAnomalyDetection — ML-based Anomaly Detection
- **Role**: Consumes live data from Kafka; evaluates configurable detection rules; persists anomaly events
- **Detection algorithms**:
  - Out-of-Range (auto/manual min/max)
  - Timeout (95th percentile of measurement intervals)
  - Rate-of-Change (95th percentile of change rate)
  - IQR (Q1/Q3 + 1.5×IQR bounds)
  - Z-Score (default ±3 threshold)
  - Ensemble (anomaly only if ALL selected algorithms agree)
- **Kafka**: CONSUMES from `kafka.live.values` (`LIVE_VALUES_TOPIC`)
- **Docs**: `IwsServer/IwsAnomalyDetection/IwsAnomalyDetection.md`

#### IwsAI — AI Feature Service
- **Role**: Consolidates AI features including self-prediction (LSTM + Random Forest), MLflow integration, model versioning
- **Kafka**: `AI_TRAINING_TOPIC`, `AI_GW_CHANGES_TOPIC`

#### ML / SelfPrediction
- **Tech**: LSTM neural networks + Random Forest; feature selection via Pearson/Spearman/Mutual Information; incremental model updates
- **Docs**: `IwsServer/ML/selfPrediction/docs/`

### Purpose-Driven Processing

#### IwsInternalWithPurposeProcessor
- **Role**: Processes variables based on assigned purpose (calculated, aggregated, forwarded, synchronized variables); strategy pattern; state management
- **Docs**: `IwsServer/IwsInternalWithPurposeProcessor/README.md`

### Infrastructure Services

#### IwsKafka — Kafka Infrastructure Library
- **Role**: Kafka producer/consumer wrappers; topic configuration; consumer group management; shared by all services
- **Docs**: `IwsServer/IwsKafka/README.md`; full topic visualizations: `IwsServer/IwsKafka/visualizations/KAFKA_TOPICS.md`

#### IwsWss — WebSocket Server
- **Role**: WebSocket server (used in monolith variant)

#### IwsMqttStats — MQTT Statistics
- **Role**: MQTT monitoring and statistics

#### IwsPing — Network Monitoring
- **Role**: Network availability monitoring

#### IwsReport — Report Generation
- **Role**: Report generation and distribution
- **Kafka**: `REPORT_MS_TOPIC`

#### IwsInterwithpurposemanager
- **Role**: i3x protocol integration management

---

## 4. KAFKA TOPICS — ALL 17

Full visualizations: `IwsServer/IwsKafka/visualizations/KAFKA_TOPICS.md`

| Topic | Direction | Purpose |
|-------|-----------|---------|
| `LIVE_VALUES_TOPIC` | IwsCore → [all consumers] | Real-time SCADA variable values |
| `VALUE_WRITE_TOPIC` | [WebApi/Scripts] → IwsCore | Variable write commands to devices |
| `SEND_TO_CLIENT_TOPIC` | Services → IwsWebApi → Clients | WebSocket data distribution to browsers |
| `CONFIGURATION_EVENT_TOPIC` | Bidirectional | Config sync: variable add/update/delete, connection assignment |
| `MS_REGISTER_TOPIC` | IwsCore ↔ IwsManager | IwsCore microservice registration & heartbeat |
| `MS_REGISTER_TOPIC_HISTORY` | IwsHistory ↔ IwsManager | History service registration |
| `MS_REGISTER_TOPIC_SCRIPT` | IwsScriptProcessing ↔ IwsManager | Script service registration |
| `AE_STREAM_TO_DB` | IwsEventsAndAlarms → IwsAEDBWritter | Alarm/event persistence to TimescaleDB |
| `SCRIPTING_MESSAGES_TOPIC` | IwsWebApi → IwsScriptProcessing | Script add/update/execute commands |
| `ACTION_REQUEST_TOPIC` | Services → Handlers | General action request processing |
| `HOOK_STATE_TOPIC` | Services → IwsHook | Webhook execution state |
| `REPORT_MS_TOPIC` | IwsWebApi → IwsReport | Report generation requests |
| `IPP_MONITORING_TOPIC` | IPP devices → Monitoring | IPP device communication monitoring |
| `AI_TRAINING_TOPIC` | Services ↔ IwsAI | AI model training/forecasting |
| `AI_GW_CHANGES_TOPIC` | Services → IwsAI | AI Gateway configuration changes |
| `MESSAGING_SERVICE_CHANGES_TOPIC` | Services → Messaging | Notification rule changes |
| `VALUE_TO_MQTT_SERVER_CONFIG_TOPIC` | Config → MQTT | MQTT republishing configuration |

### Key Kafka Patterns
- **IwsCore consumer groups**: Use unique GUIDs for broadcast reception
- **IwsManager**: Uses fixed key `THE_MANAGER_I_AM` for topic filtering
- **Script processors**: Have subtypes (Default, Important, Scheduling, History)
- **CacheSaver**: Consumer group `cache_stream` for exclusive consumption

---

## 5. COMPLETE DATA FLOW

### Read Path (Device → Client)
```
Field Device/PLC/Sensor
  ↓ (OPC UA, Modbus, MQTT, IEC 60870, DNP3, Siemens S7, LoRaWAN, i3x)
IwsCore (SCADA Engine)
  ↓ publishes to LIVE_VALUES_TOPIC
  ├─→ IwsCacheSaver → Process Image Redis (fast client reads)
  ├─→ IwsHistory → MariaDB (historical storage)
  ├─→ IwsEventsAndAlarms → alarm detection → SEND_TO_CLIENT_TOPIC
  ├─→ IwsScriptProcessing → execute value-change scripts
  ├─→ IwsAnomalyDetection → ML anomaly evaluation
  └─→ IwsLogging → log to file/DB
  ↓ (via IwsWebApi + WebSocket)
Web Clients / Mobile Apps
```

### Write Path (Client → Device)
```
Web Client → IwsWebApi → VALUE_WRITE_TOPIC → IwsCore → Protocol Driver → Device
```

### Registration Flow (Microservice Startup)
```
Microservice starts → publishes Init to MS_REGISTER_TOPIC[_type]
  → IwsManager assigns GUID or sets WAITING
  → Microservice receives GUID → begins operation
  → Microservice sends periodic HB → Manager monitors health
  → Missed HBs → auto-restart / promote waiting instance
```

---

## 6. PROTOCOL SUPPORT (Industrial Connectivity)

| Protocol | Standard / Use Case |
|----------|---------------------|
| OPC UA | Modern industrial interoperability standard |
| OPC DA | Legacy OPC connectivity |
| Modbus TCP | Most common industrial protocol |
| IEC 60870-5-104 | Telecontrol / power grid systems (via lib60870) |
| DNP3 | Utility and infrastructure SCADA (via opendnp3) |
| Siemens S7 | Siemens PLC direct connection (via S7netplus) |
| MQTT | IoT messaging standard |
| LoRaWAN | Long-range low-power IoT |
| i3x | InView proprietary protocol for i3x Edge Devices |
| IPP | Custom extensible driver architecture |

> IEC 60870-5-104 + DNP3 support makes the platform suitable for critical infrastructure (energy, water, utilities).

---

## 7. FRONTEND COMPONENTS

### Submodule Chain
```
InViewWebScada (root)
  └─ Client/ — End-user SCADA visualization (jQuery, Bootstrap, Webpack)
        └─ editor/ — No-code screen designer (drag-and-drop, visual data binding)
               └─ configurator-v2/ — System configuration (protocols, users, scripts)
               └─ configurator-v3/ — Next-gen configurator (active development)
```

### Client Tech Stack
- jQuery 3.7.1, Bootstrap 5.3.2, Webpack
- Real-time process visualization via WebSocket
- Responsive — desktop, tablet, mobile

### Additional Frontends
- `Client/chat-app/` — React-based chat/chat integration
- `Client/registration/` — User registration flow
- `Client/editor-v2/` — Next-gen editor

---

## 8. KEY FEATURES

### Real-Time Monitoring & Control
- Live variable streaming via WebSockets
- Multi-source data aggregation from heterogeneous devices
- Custom dashboards and KPI visualization
- Remote device control from anywhere

### Alarm & Event Management
- Configurable thresholds (High/Low) with deadband
- AlarmsDoubleChecker for false alarm prevention
- Multi-channel notifications: SMS, email, push
- Full alarm history and audit trail

### No-Code IDE / Visual Builder
- Drag-and-drop SCADA screen builder
- Flow-based automation editor (Configurator v2 / v3)
- Enables rapid deployment without programmers

### Scripting Engine
- Dynamic C# script compilation without recompilation
- Triggers: value change, scheduled (cron), event-driven, on-demand
- Access to: SCADA values (R/W), historical data, database, external APIs

### Historical Data & Reporting
- Full historical time-series storage
- Configurable retention policies
- Report generation module
- Export capabilities

### Multi-Tenancy
- Full multi-tenant cloud architecture
- Role-based access control
- Tenant isolation and security

### Edge Computing
- i3x Edge Devices for local processing
- Edge + Cloud hybrid topology

---

## 9. DEPLOYMENT VARIANTS

| Variant | Database | Caching | Messaging | Best For |
|---------|----------|---------|-----------|----------|
| SQLite | SQLite (file) | In-memory | None | Dev/Testing |
| MariaDB | MariaDB | Optional Redis | Optional Kafka | Small Production |
| Full Stack | MariaDB | Redis | Kafka + Zookeeper | Full Production |
| Microservices | MariaDB | Redis | Kafka | Enterprise/Scalable |

### Production Infrastructure
- **Cloud**: Oracle Cloud Infrastructure (OCI), Phoenix Region
  - Kubernetes (OKE): 20 nodes (6 high-memory, 14 standard)
  - Network Load Balancers L4/L7 for HTTP/HTTPS and MQTT
- **Database HA**: MariaDB Galera Cluster — main + backup (BC), HAProxy + virtual IPs, multi-master replication
- **Docs**: `Documentation/Infrastructure/oracle-cloud-phoenix-region.md`, `Documentation/Infrastructure/galera-cluster-detailed.md`

---

## 10. COMPETITIVE POSITIONING

**Key differentiators:**
1. Maturity + Modernity: 15 years real-world deployment + cloud-native architecture
2. True No-Code: Full application builder, not just dashboards
3. Embedded AI/ML: Native anomaly detection + prediction (not a third-party add-on)
4. Protocol Breadth: Legacy industrial (Modbus, S7) + modern IoT (MQTT, LoRaWAN) in one platform
5. Deployment Flexibility: On-premise, cloud, hybrid, edge — same features, no tiering
6. Multi-Vertical: Manufacturing, utilities, healthcare, logistics, oil & gas
7. European Heritage: GDPR-aware, EU compliance, CET timezone support
8. Microservices at Core: Built for cloud scale, not retrofitted

**Competitive landscape**: Ignition (Inductive Automation), Siemens WinCC/MindSphere, Wonderware (AVEVA), Schneider EcoStruxure, GE iFIX, Thingsboard, Grafana+InfluxDB

---

## 11. TARGET MARKETS

| Vertical | Key Protocols / Features Used |
|----------|-------------------------------|
| Industrial Manufacturing | OPC UA, Modbus, scripting, predictive maintenance |
| Energy & Utilities (Critical Infra) | IEC 60870-5-104, DNP3, alarm management |
| Smart Cities & Infrastructure | MQTT, LoRaWAN, multi-source aggregation |
| Oil & Gas | Oilfield-Monitor product, pipeline SCADA |
| Healthcare | inMEDIC product, wearable device integration |
| Logistics & Cold Chain | Fleet/asset monitoring, temperature tracking |

**Customer types**: System Integrators, OEM Manufacturers, Managed Service Providers, Enterprise End-Users, Government/Critical Infrastructure

---

## 12. PROJECT FILE STRUCTURE

```
InViewWebScada/
├── IwsServer/              # All C# backend (Iws.sln — 70+ projects)
│   ├── WebAndSocketServerCore/  # Monolith entry point
│   ├── IwsCore/            # SCADA engine
│   ├── IwsManager/         # Orchestration
│   ├── IwsWebApi/          # Legacy REST API
│   ├── IwsAspNetCoreWebApi/ # Modern REST API
│   ├── IwsKafka/           # Kafka infrastructure
│   ├── IwsRedisCache/      # Redis infrastructure
│   ├── IwsScriptProcessing/ # Script engine
│   ├── IwsCacheSaver/      # Redis cache populator
│   ├── IwsEventsAndAlarms/ # Alarm engine
│   ├── IwsAnomalyDetection/ # ML anomaly detection
│   ├── IwsHistory/         # Historical data
│   ├── IwsLogging/         # Logging
│   ├── IwsManager/         # Orchestration
│   ├── ML/selfPrediction/  # LSTM/RF prediction models
│   └── Agents context/     # AI agent context docs (this file is here)
├── Client/                 # Frontend (submodule chain)
├── Docker/                 # Docker configs + installation/usage guides
├── DB/                     # Database schemas and migrations
├── Documentation/          # Infrastructure architecture docs
│   └── Infrastructure/     # Oracle Cloud, Galera cluster diagrams
├── kubernetes/             # Kubernetes deployment configs
├── k8s_stage/              # Staging K8s configs
├── InViewReports/          # Reporting components
└── Libs/                   # External libraries (OPC, IEC, Excel, etc.)
```

---

## 13. DETAILED DOCUMENTATION POINTERS

For agents requiring deeper information on specific topics, refer to:

| Topic | File |
|-------|------|
| All Kafka topics (17) with Mermaid diagrams | `IwsServer/IwsKafka/visualizations/KAFKA_TOPICS.md` |
| Redis dual-architecture details | `IwsServer/IwsRedisCache/README.md` |
| Redis usage patterns per service | `IwsServer/IwsRedisCache/visualizations/REDIS_USAGE.md` |
| IwsCore protocol drivers + Kafka | `IwsServer/IwsCore/README.md` |
| IwsWebApi REST API + Kafka | `IwsServer/IwsWebApi/README.md` |
| IwsManager orchestration flow | `IwsServer/IwsManager/README.md` |
| Script engine execution modes | `IwsServer/IwsScriptProcessing/README.md` |
| Anomaly detection algorithms | `IwsServer/IwsAnomalyDetection/IwsAnomalyDetection.md` |
| Docker installation guide | `Docker/INSTALLATION-GUIDE.md` |
| Docker usage / deployment variants | `Docker/USAGE-GUIDE.md` |
| Oracle Cloud production infra | `Documentation/Infrastructure/oracle-cloud-phoenix-region.md` |
| Galera cluster HA setup | `Documentation/Infrastructure/galera-cluster-detailed.md` |
| Sales/marketing context (detailed) | `IwsServer/Agents context/Sales_Manager_Context.md` |
| USP brainstorming materials | `IwsServer/Agents context/USP brainstorming/` |
| ML self-prediction docs | `IwsServer/ML/selfPrediction/docs/index.md` |
| Client frontend overview | `Client/README.md` |

---

*Generated by: Claude Sonnet 4.6 (claude-sonnet-4-6)*
*Source: Full scan of all project MD files — IwsServer, Client, Docker, Documentation, Agents context*
