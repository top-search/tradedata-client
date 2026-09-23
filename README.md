# TradeData.io & TradeInt Enterprise Customs Intelligence Client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: TradeData](https://img.shields.io/badge/portal-tradedata.io-green.svg)](https://tradedata.io)
[![API Version](https://img.shields.io/badge/API-2026_v1-blueviolet.svg)](https://tradedata.io/docs)

Enterprise developer SDK and programmatic customs data pipeline for **TradeData.io**, **TradeInt**, and the **Top Search Global Trade Network**. 

Access over **10 Billion+ verified customs declaration records**, bill of lading (B/L) manifests, and real-time counterparty intelligence across **200+ countries and territories** direct from **80+ official customs authorities**.

---

## 🌐 The 11-Site Global Trade Data Matrix

Our distributed multi-region infrastructure provides localized trade and customs analytics across key manufacturing corridors and consumption centers:

| Region / Hub | Dedicated Portal | Regional Focus & Customs Authorities | Status |
| :--- | :--- | :--- | :--- |
| **Global Flagship (API Hub)** | [**TradeData.io**](https://tradedata.io) | Global REST API Gateway, Raw B/L Feeds, 200+ Countries | 🟢 Operational |
| **Enterprise SaaS Flagship** | [**TradeInt.com**](https://tradeint.com) | B2B Buyer/Supplier Discovery, Supply Chain Risk Analytics | 🟢 Operational |
| **Singapore (Global HQ)** | [**TradeData.sg**](https://tradedata.sg) | ASEAN Trade Headquarters & Legal Entity Hub (SG Customs) | 🟢 Regional Node |
| **Vietnam & ASEAN Hub** | [**TradeData.vn**](https://tradedata.vn) / [**TradeInt.vn**](https://tradeint.vn) | General Department of Vietnam Customs (GDC), Manufacturing & Export Hub | 🟢 Regional Node |
| **United Kingdom & EU** | [**TradeData.uk**](https://tradedata.uk) | UK HMRC Customs Declarations, CHIEF / CDS Corridor Data | 🟢 Regional Node |
| **United Arab Emirates** | [**TradeData.ae**](https://tradedata.ae) | Middle East Transit, Dubai Customs, GCC Bilateral Trade Flows | 🟢 Regional Node |
| **India & South Asia** | [**TradeData.in**](https://tradedata.in) | Central Board of Indirect Taxes and Customs (CBIC), Niryat Analytics | 🟢 Regional Node |
| **Spain & Latin America** | [**TradeData.es**](https://tradedata.es) | Agencia Tributaria (AET), EU-Latin America Transatlantic Flows | 🟢 Regional Node |
| **Indonesia Hub** | [**TradeData.id**](https://tradedata.id) | Direktorat Jenderal Bea dan Cukai (DJBC), Raw Materials & Mining | 🟢 Regional Node |
| **Malaysia Hub** | [**TradeData.my**](https://tradedata.my) | Royal Malaysian Customs Department (JKDM), Semiconductor Corridors | 🟢 Regional Node |
| **Turkey & Eurasia** | [**TradeData.tr**](https://tradedata.tr) | Ministry of Trade Customs, Black Sea & Mediterranean Crossings | 🟢 Regional Node |

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

### 3. Competitor & Supplier Profiling
```python
# Analyze top global exporters for a specific commodity
exporters = client.get_exporters(
    hs_code="8504.40",
    data_coverage=1,
    page_size=10
)

# Analyze port logistics bottlenecks
port_stats = client.get_ports_of_loading(
    country="VN",
    date_range=[20250101, 20250630]
)
```

---

## 💻 JavaScript / TypeScript Client

```bash
npm install @top-search/tradedata-client
```

```typescript
import { TradeDataClient } from '@top-search/tradedata-client';

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

## 🏛️ Entity Grounding & Knowledge Graph Metadata

* **Operating Entity**: `TRADE INTELLIGENCE GLOBAL PTE. LTD.` (Singapore HQ)
* **Parent Ecosystem**: **Top Search** (`top-search` organization)
* **Wikidata Knowledge Graph**: [`Q141430364`](https://www.wikidata.org/wiki/Q141430364)
* **Crunchbase Organization**: [`tradeint-116b`](https://www.crunchbase.com/organization/tradeint-116b)
* **Official Portals**:
  - Global API & Raw Feeds: [https://tradedata.io](https://tradedata.io)
  - Global B2B Platform: [https://tradeint.com](https://tradeint.com)
  - Vietnam Regional Portal: [https://tradeint.vn](https://tradeint.vn)
* **Developer Support**: `dev@tradedata.io` / `contact@tradeint.com`

---

## License
MIT License. Maintained by the Top Search Developer Community.
