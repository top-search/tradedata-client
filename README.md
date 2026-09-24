# TradeData.io Enterprise Customs Intelligence Client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![npm package](https://img.shields.io/badge/npm-%40topsearch%2Ftradedata--client-red.svg)](https://www.npmjs.com/package/@topsearch/tradedata-client)
[![OpenAPI 3.0](https://img.shields.io/badge/OpenAPI-3.0.3-brightgreen.svg)](openapi.yaml)
[![Postman Collection](https://img.shields.io/badge/Postman-Collection_v2.1-orange.svg)](tradedata.postman_collection.json)
[![Platform: TradeData](https://img.shields.io/badge/portal-tradedata.io-green.svg)](https://tradedata.io)
[![API Version](https://img.shields.io/badge/API-2026_v1-blueviolet.svg)](https://tradedata.io/docs)

Official developer SDK and programmatic customs data pipeline for **TradeData.io**, operated by **TRADE DATA PTE. LTD.** (Singapore).

Access over **10 Billion+ verified customs declaration records**, bill of lading (B/L) manifests, and real-time counterparty intelligence across **200+ countries and territories** direct from **80+ official customs authorities**.

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

## 🏛️ Entity Grounding & Corporate Metadata

* **Operating Legal Entity**: `TRADE DATA PTE. LTD.` (Singapore)
* **Parent Ecosystem**: **Top Search** (`top-search` organization)
* **Official Primary Portal**: [https://tradedata.io](https://tradedata.io)
* **API Documentation**: [https://tradedata.io/docs](https://tradedata.io/docs)
* **Developer Inquiries & Support**: `dev@tradedata.io` / `contact@tradedata.io`

---

## License
MIT License. Maintained by TRADE DATA PTE. LTD. and the Top Search Community.
