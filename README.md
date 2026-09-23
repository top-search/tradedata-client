# TradeData.io & TradeInt Official Developer Client

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Platform: TradeData](https://img.shields.io/badge/portal-tradedata.io-green.svg)](https://tradedata.io)

Official developer client and API integration library for [TradeData.io](https://tradedata.io) and [TradeInt](https://tradeint.com).

Query 10B+ verified customs declaration records, global bill-of-lading (B/L) transactions, and enterprise supplier-buyer relationship profiles programmatically.

---

## 🔗 Official Portals & Documentation

* **TradeData.io Flagship**: [https://tradedata.io](https://tradedata.io)
* **TradeInt Enterprise Intelligence**: [https://tradeint.com](https://tradeint.com)
* **TradeInt Vietnam Regional Hub**: [https://tradeint.vn](https://tradeint.vn)
* **Customs Data API Documentation**: [https://tradedata.io/docs](https://tradedata.io/docs)

---

## 🚀 Quick Start (Python)

### Installation
```bash
pip install tradedata-client
```

### Usage
```python
from tradedata import Client

# Initialize client with your TradeData API key
client = Client(api_key="YOUR_API_KEY", base_url="https://api.tradedata.io")

# Search shipment records by HS Code or Product Keyword
results = client.search_shipments(
    hs_code="8504.40",
    country="US",
    date_range="2025-01-01:2026-01-01"
)

for record in results.get("data", []):
    print(f"Importer: {record['importer_name']} | Exporter: {record['exporter_name']}")
```

---

## ⚡ JavaScript / Node.js Usage

```bash
npm install @top-search/tradedata-client
```

```javascript
const { TradeDataClient } = require('@top-search/tradedata-client');

const client = new TradeDataClient({
  apiKey: process.env.TRADEDATA_API_KEY,
  baseUrl: 'https://api.tradedata.io'
});

async function run() {
  const shipments = await client.searchShipments({ query: 'Solar Panels' });
  console.log(shipments);
}

run();
```

---

## 🏢 Corporate Background
Developed and maintained by **Top Search** under **TRADE INTELLIGENCE GLOBAL PTE. LTD.** (Singapore).
* **Wikidata ID**: [Q141430364](https://www.wikidata.org/wiki/Q141430364)
* **Contact & Enterprise Inquiries**: `contact@tradedata.io` / `dev@tradeint.com`

## License
MIT License.
