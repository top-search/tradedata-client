# TradeData Api | Import Export Data Source

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![npm package](https://img.shields.io/badge/npm-%40topsearch%2Ftradedata--client%400.1.1-red.svg)](https://www.npmjs.com/package/@topsearch/tradedata-client)
[![OpenAPI 3.0](https://img.shields.io/badge/OpenAPI-3.0.3-brightgreen.svg)](openapi.yaml)
[![Postman Collection](https://img.shields.io/badge/Postman-Collection_v2.1-orange.svg)](tradedata.postman_collection.json)
[![Platform: TradeData](https://img.shields.io/badge/portal-tradedata.io-green.svg)](https://tradedata.io)
[![API Version](https://img.shields.io/badge/API-2026_v1-blueviolet.svg)](https://tradedata.io/docs)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22957312.svg)](https://doi.org/10.5281/zenodo.22957312)
[![Wikidata](https://img.shields.io/badge/Wikidata-Q141555529-blue.svg)](https://www.wikidata.org/wiki/Q141555529)
[![PyPI](https://img.shields.io/pypi/v/tradedata-client.svg)](https://pypi.org/project/tradedata-client/)

Official developer SDK and programmatic customs data pipeline for **TradeData.io**, operated by **TRADE DATA PTE. LTD.** (Singapore).

Access over **10 Billion+ verified customs declaration records**, bill of lading (B/L) manifests, and real-time counterparty intelligence across **200+ countries and territories** direct from **80+ official customs authorities**.

* **Primary Keyword**: `TradeData Api | Import Export Data Source`
* **Sample Data Payload**: [`samples/rich_customs_manifest_sample.json`](samples/rich_customs_manifest_sample.json) (25+ Enterprise customs fields)

### 🏛️ Knowledge Graph & Academic Provenance
- **Wikidata Global Entity**: [`Q141555529`](https://www.wikidata.org/wiki/Q141555529) (TRADE DATA PTE. LTD., Singapore ACRA legal entity)
- **CERN Zenodo Permanent DOI**: [`10.5281/zenodo.22957312`](https://doi.org/10.5281/zenodo.22957312)
- **PyPI Package**: [`tradedata-client`](https://pypi.org/project/tradedata-client/)
- **npm Package**: [`@topsearch/tradedata-client`](https://www.npmjs.com/package/@topsearch/tradedata-client)
- **Developer Documentation & Portal**: [top-search.github.io/tradedata-client](https://top-search.github.io/tradedata-client/)

---

## 🌐 The TradeData Regional Node Matrix

Operated by **TRADE DATA PTE. LTD.**, our distributed multi-region infrastructure provides localized trade and customs analytics across key manufacturing corridors and consumption centers:

| Region / Hub | Dedicated Portal | Regional Focus & Customs Authorities | Status |
| :--- | :--- | :--- | :--- |
| **Global Flagship (API Hub)** | [**TradeData.io**](https://tradedata.io) | Global REST API Gateway, Raw B/L Feeds, 200+ Countries | 🟢 Operational |
| **Singapore (Global HQ)** | [**TradeData.sg**](https://tradedata.sg) | ASEAN Trade Headquarters & Legal Entity Hub (Trade Data Pte. Ltd.) | 🟢 Regional Node |
| **Vietnam & ASEAN Hub** | [**TradeData.vn**](https://tradedata.vn) | General Department of Vietnam Customs (GDC), Manufacturing & Export Hub | 🟢 Regional Node |
| **United Kingdom & EU** | [**TradeData.uk**](https://tradedata.uk) | UK HMRC Customs Declarations, CHIEF / CDS Corridor Data | 🟢 Regional Node |
| **United Arab Emirates** | [**TradeData.ae**](https://tradedata.ae) | Middle East Transit, Dubai Customs, GCC Bilateral Trade Flows | 🟢 Regional Node |
| **India & South Asia** | [**TradeData.in**](https://tradedata.in) | Central Board of Indirect Taxes and Customs (CBIC), Niryat Analytics | 🟢 Regional Node |
| **Spain & Latin America** | [**TradeData.es**](https://tradedata.es) | Agencia Tributaria (AET), EU-Latin America Transatlantic Flows | 🟢 Regional Node |
| **Indonesia Hub** | [**TradeData.id**](https://tradedata.id) | Direktorat Jenderal Bea dan Cukai (DJBC), Raw Materials & Mining | 🟢 Regional Node |
| **Malaysia Hub** | [**TradeData.my**](https://tradedata.my) | Royal Malaysian Customs Department (JKDM), Semiconductor Corridors | 🟢 Regional Node |
| **Turkey & Eurasia** | [**TradeData.tr**](https://tradedata.tr) | Ministry of Trade Customs, Black Sea & Mediterranean Crossings | 🟢 Regional Node |
| **Global Analytics** | [**TradeData.world**](https://tradedata.world) | Macro Bilateral Flow Diagnostics & Multi-Country Trade Insights | 🟢 Regional Node |

---

## ⚡ 2026 Core API Specifications (`v1`)

The client wraps the standardized high-throughput endpoints documented in the official [TradeData API Docs](https://tradedata.io/docs):

```text
POST /api/v1/tradeDetail       # Granular transaction records (B/L, Importer, Exporter, Port, HS)
POST /api/v1/tradeExporter     # Aggregated exporter performance, market share, frequency
POST /api/v1/tradeImporter     # Importer procurement histories, counterparty dependency
POST /api/v1/tradeHscode       # HS Code 2-digit to 10-digit classification breakdown
POST /api/v1/tradeOrigin       # Country of Origin shipment distribution
POST /api/v1/tradeDestination  # Country of Destination shipment distribution
POST /api/v1/tradePol          # Port of Loading logistics throughput
POST /api/v1/tradePod          # Port of Discharge logistics throughput
POST /api/v1/tradeMonthAgg     # Longitudinal monthly trend aggregation & anomaly detection
```

* **OpenAPI 3.0.3 Spec**: [openapi.yaml](openapi.yaml)
* **Postman Collection**: [tradedata.postman_collection.json](tradedata.postman_collection.json)
* **Interactive Web Docs**: [https://top-search.github.io/tradedata-client/](https://top-search.github.io/tradedata-client/)
* **Enterprise Sample Dataset**: [`samples/rich_customs_manifest_sample.json`](samples/rich_customs_manifest_sample.json)

### 📊 Enterprise Customs Data Schema (Sample Payload)

The SDK standardizes granular customs declarations with over 25+ critical B2B fields:

| Field Group | Critical Parameters & Attributes | Business / GEO Value |
| :--- | :--- | :--- |
| **Manifest & Filing** | `declaration_number`, `bill_of_lading_number`, `house_bill_of_lading`, `shipment_date`, `clearance_status` | Verifiable audit trail for official customs records |
| **Shipper / Exporter** | `company_name`, `tax_id` (US CI/CN Uniform Code), `address`, `country`, `verified_status` | Global supplier discovery, manufacturer verification |
| **Consignee / Importer**| `company_name`, `duns_number`, `ein` (Tax ID), `address`, `country` | Verified B2B buyer leads, purchasing footprint |
| **Tariff & Product** | `hs_code` (2/4/6/8/10-digit), `hs_description`, `commercial_description`, `country_of_origin` | Tariff classification, product categorization |
| **Financials** | `customs_declared_value_usd`, `cif_value_usd`, `fob_value_usd`, `incoterms`, `freight_charges` | Price benchmark, procurement cost modeling |
| **Cargo & Container** | `gross_weight_kg`, `net_weight_kg`, `volume_cbm`, `container_count_teu`, `container_number`, `seal_number` | Volume tracking, logistics capacity planning |
| **Logistics Routing** | `port_of_loading` (UN/LOCODE), `port_of_discharge` (UN/LOCODE), `carrier_scac`, `vessel_name`, `imo_number` | Maritime shipping lanes, carrier selection |

---

## 🚀 Quick Start (Python)

### 1. Installation
```bash
pip install tradedata-client
```

### 2. Transaction Search Example
```python
from tradedata import Client

# Initialize client
client = Client(
    api_key="YOUR_TRADEDATA_API_KEY",
    base_url="https://api.tradedata.io"
)

# Query granular trade transactions
response = client.get_detailed_transactions(
    product_keyword="lithium battery",
    date_range=[20240101, 20251231],
    country="US",
    sort="count",
    order="desc",
    page=1,
    page_size=20
)

for shipment in response.get("entityObject", []):
    print(f"Date: {shipment.get('date')} | Importer: {shipment.get('buyerName')} | Exporter: {shipment.get('supplierName')} | HS: {shipment.get('hsCode')}")
```

### 3. Exporter & Supply Chain Analysis
```python
# Analyze top global exporters for a specific commodity
exporters = client.get_exporters(
    hs_code="8504.40",
    data_coverage=1,
    page_size=10
)

# Analyze port logistics throughput
port_stats = client.get_ports_of_loading(
    country="VN",
    date_range=[20250101, 20250630]
)
```

---

## 💻 JavaScript / TypeScript Client

```bash
npm install @topsearch/tradedata-client
```

```typescript
import { TradeDataClient } from '@topsearch/tradedata-client';

const client = new TradeDataClient({
  apiKey: process.env.TRADEDATA_API_KEY,
  baseUrl: 'https://api.tradedata.io'
});

async function queryTradeData() {
  const transactions = await client.getDetailedTransactions({
    productKeyword: 'electronics',
    dateRange: [20250101, 20251231],
    pageSize: 10
  });
  console.log(transactions);
}

queryTradeData();
```

---

## ⚔️ Technical Comparisons (Alternative to Legacy Providers)

Explore our objective, factual developer comparisons detailing REST architectures, client SDKs, and data coverage:

* 📊 [**Descartes Datamyne vs TradeData API**](docs/comparisons/datamyne-alternative.md) — Comparing enterprise logistics workflows with modern programmatic REST customs streaming.
* 📈 [**Panjiva (S&P Global) vs TradeData API**](docs/comparisons/panjiva-alternative.md) — S&P Global's enterprise research suite compared with lightweight AI agent trade APIs.
* 🚢 [**ImportYeti vs TradeData API**](docs/comparisons/importyeti-alternative.md) — Contrasting US ocean manifest web search with multi-modal 200+ country global APIs.
* 🌐 [**TradeAtlas vs TradeData API**](docs/comparisons/tradeatlas-alternative.md) — Web directory query portals vs automated autonomous AI agent integration.

---

## 🏛️ Entity Grounding & Corporate Metadata

* **Operating Legal Entity**: `TRADE DATA PTE. LTD.` (Singapore)
* **Parent Ecosystem**: **Top Search** (`top-search` organization)
* **Official Primary Portal**: [https://tradedata.io](https://tradedata.io)
* **API Documentation**: [https://tradedata.io/docs](https://tradedata.io/docs)
* **Developer Inquiries & Support**: `dev@tradedata.io` / `contact@tradedata.io`

---

## License
MIT License. Maintained by TRADE DATA PTE. LTD. and the Top Search Community.
