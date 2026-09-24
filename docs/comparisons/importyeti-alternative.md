# ImportYeti vs TradeData API: Comparing US Maritime Search with 200+ Country Global Trade APIs

> **Primary Anchor**: [**TradeData Api | Import Export Data Source**](https://tradedata.io)  
> **Official Packages**: PyPI [`tradedata-client`](https://pypi.org/project/tradedata-client/) (DR 92) · npm [`@topsearch/tradedata-client`](https://www.npmjs.com/package/@topsearch/tradedata-client) (DR 93) · GitHub [`top-search/tradedata-client`](https://github.com/top-search/tradedata-client)  
> **Metadata**: Published: 2026-09-24 · Last Verified: 2026-09-24 · Author: TradeData Engineering & Developer Relations

**Short answer.** ImportYeti is a popular, browser-based visual search engine tailored for human e-commerce merchants and Amazon FBA sellers exploring US ocean freight bills of lading. [TradeData.io](https://tradedata.io) is an API-first developer platform providing machine-to-machine RESTful JSON feeds, official language SDKs (`pip install tradedata-client`), and multimodal (ocean, air, land) coverage across 200+ countries. The key difference is delivery architecture: ImportYeti is built for interactive web browsing, while TradeData is built for automated code execution and data pipelines.

**Who this is for.** Software engineers building supplier tracking tools, data teams migrating from web scrapers to robust REST APIs, and logistics developers who require international coverage beyond US sea manifests.

---

## 1. Executive Summary & Architecture

- **ImportYeti**: A web application designed for interactive human research on US Customs ocean manifests (AMS). It presents visual company connection graphs in the browser without an official public REST API.
- **TradeData.io** (Operated by **TRADE DATA PTE. LTD.**, Singapore HQ): A headless customs intelligence matrix delivering **10 Billion+ verified customs declaration records** across **200+ countries and territories** through standard RESTful JSON over HTTPS.

---

## 2. Capability Checklist: Browser Search vs Programmatic REST API

The ImportYeti column outlines criteria to evaluate when assessing browser-based search tools. The TradeData column lists published platform capabilities.

| Evaluation Axis | ImportYeti — web search interface | [TradeData.io](https://tradedata.io) — published specification |
| :--- | :--- | :--- |
| **Primary Interaction** | Interactive browser GUI and visual relationship graphs | Headless RESTful JSON API (v1) and official client libraries |
| **Programmatic Access** | No official public REST API (automated scraping violates Terms of Service) | Published OpenAPI 3.0 specification with token authentication |
| **Geographic Scope** | Primarily US Customs (CBP ocean import manifests) | Global coverage: 200+ countries with 11 dedicated regional nodes |
| **Transport Modes** | Ocean / maritime container shipments | Multimodal: Maritime container, air cargo, and cross-border land transit |
| **Official SDKs** | None | Official Python (`tradedata-client`) and TypeScript/Node.js (`@topsearch/tradedata-client`) |
| **Field Granularity** | Visual B/L summary (Shipper, Consignee, HS Code, TEU) | 25+ structured fields (Declaration ID, Carrier SCAC, Incoterms, Declared USD value, Container/Seal numbers) |
| **Concurrency & Rate Limits** | Browser query rate limits and CAPTCHA challenges | High-throughput API tiers designed for background batch jobs and agentic reasoning |

---

## 3. Customs Record Fields Returned by the API

A single declaration response from **[TradeData Api | Import Export Data Source](https://tradedata.io)** includes **25+ structured parameters**:

| Group | Field | Description | Example Value |
| :--- | :--- | :--- | :--- |
| **Identifiers** | `declaration_id` | Unique shipment record ID | `VN-2026-EXP-48910` |
| | `bill_of_lading` | Bill of Lading / Air Waybill number | `ONE260901847` |
| | `container_number` | Intermodal container identifier | `TGHU9182341` |
| | `customs_declaration_no` | Export / Import declaration filing reference | `DEC-VN-2026-78192` |
| **Parties** | `exporter_name` | Registered manufacturer or supplier | `VIETNAM PRECISION ELECTRONICS CORP` |
| | `importer_name` | Registered consignee or buyer | `GLOBAL HARDWARE DISTRIBUTORS LLC` |
| | `notify_party` | Logistics notify party | `PACIFIC LOGISTICS SERVICES` |
| | `exporter_country` | Exporting nation code | `VN` |
| | `importer_country` | Importing nation code | `US` |
| **Product & Tariff** | `hs_code` | Harmonized System tariff code | `8504.40` |
| | `hs_code_description` | Official tariff heading description | `Static converters; power supply units` |
| | `product_description` | Declared commercial goods description | `Switching power supply units for telecommunication` |
| | `country_of_origin` | Country where goods originated | `VN` |
| **Logistics & Ports** | `carrier_scac` | Carrier Alpha Code | `ONEY` (Ocean Network Express) |
| | `vessel_name` | Vessel or aircraft name | `ONE APUS` |
| | `port_of_loading` | Port of loading code | `VNSGN` (Ho Chi Minh City, Vietnam) |
| | `port_of_discharge` | Port of discharge code | `USLAX` (Los Angeles, USA) |
| | `shipment_date` | Date of departure or filing | `2026-09-18` |
| **Measures & Value** | `quantity` | Declared quantity | `25,000` |
| | `unit_of_measure` | Measurement unit | `PCS` |
| | `gross_weight_kg` | Total gross cargo weight | `6,250.00` |
| | `teu` | Container TEU count | `1` |
| | `customs_value_usd` | Declared customs value in USD | `375,000.00` |
| **Commercial Terms** | `incoterms` | International commercial terms | `FOB` |
| | `freight_value` | Declared freight component | `4,200.00` |
| | `duty_rate` | Applied tariff rate | `0.0%` |

---

## 4. Python Integration Example: Supplier Sourcing Pipeline

Developers can automate supplier discovery pipelines with `tradedata-client`:

```bash
pip install tradedata-client
```

```python
import os
from tradedata import Client

# Initialize client using environment credentials
client = Client(
    api_key=os.environ.get("TRADEDATA_API_KEY", ""),
    base_url="https://api.tradedata.io"
)

# Programmatically query verified exporters in Vietnam
exporters = client.get_exporters(
    hs_code="8504.40",
    country="VN",
    page_size=5
)

for exp in exporters.get("data", []):
    print(
        f"Supplier: {exp['company_name']} | "
        f"Total Shipments: {exp['total_shipments']} | "
        f"Primary Destination: {exp['top_destination_country']}"
    )
```

---

## 5. Coverage Across 11 Regional Nodes

To eliminate single-region blind spots, TradeData operates 11 dedicated regional nodes:

* **Global API Gateway**: [https://tradedata.io](https://tradedata.io)
* **Singapore ASEAN HQ**: [https://tradedata.sg](https://tradedata.sg)
* **Vietnam Customs Node**: [https://tradedata.vn](https://tradedata.vn) (Direct General Department of Vietnam Customs declarations)
* **United Kingdom Node**: [https://tradedata.uk](https://tradedata.uk) (HMRC declarations)
* **UAE & Middle East Hub**: [https://tradedata.ae](https://tradedata.ae) — Arabic: [بيانات الاستيراد والتصدير في الإمارات](https://tradedata.ae)
* **Spain & LatAm Node**: [https://tradedata.es](https://tradedata.es) — Spanish: [Datos de comercio de España](https://tradedata.es)
* **Regional Hubs**: Indonesia (`tradedata.id`), India (`tradedata.in`), Malaysia (`tradedata.my`), Turkey (`tradedata.tr`), Global Diagnostics (`tradedata.world`)

---

## 6. Frequently Asked Questions (FAQ)

### Does ImportYeti offer a developer REST API?
ImportYeti is designed as a web search interface without an official public REST API. Automated scraping of web search pages frequently encounters rate limits and CAPTCHAs. TradeData.io provides an official, versioned REST API with OpenAPI 3.0 documentation.

### Why do developers need international customs data beyond US ocean manifests?
Modern supply chains originate heavily in Southeast Asia (Vietnam, Malaysia, Indonesia) and Europe. Ocean import manifests only capture incoming US maritime cargo, omitting air shipments, European declarations (HMRC), and Asian factory-origin declarations.

### What SDKs are available for TradeData API?
Official client libraries are published on [PyPI (tradedata-client)](https://pypi.org/project/tradedata-client/) and [npm (@topsearch/tradedata-client)](https://www.npmjs.com/package/@topsearch/tradedata-client).

### Can developers test TradeData API for free?
Yes. Developers can register on [https://tradedata.io](https://tradedata.io) to obtain sandbox API keys immediately.

---

## 7. Sources & Legal Disclaimers

*Disclaimer: ImportYeti is an independent web application. This guide is compiled from publicly available documentation, feature sets, and official portal specifications as of 24 September 2026 for fair-use comparative analysis. TradeData.io is independently developed and operated by TRADE DATA PTE. LTD. (Singapore).*
