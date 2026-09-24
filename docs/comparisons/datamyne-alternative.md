# Descartes Datamyne vs TradeData API: Developer Integration & REST Architecture Comparison

> **Primary Anchor**: [**TradeData Api | Import Export Data Source**](https://tradedata.io)
> *Service: [https://tradedata.io](https://tradedata.io) · SDKs: [`@topsearch/tradedata-client`](https://www.npmjs.com/package/@topsearch/tradedata-client) (npm) · [`tradedata-client`](https://pypi.org/project/tradedata-client/) (PyPI)*

**Short answer.** Descartes Datamyne is an enterprise-procurement global trade database sold into logistics and compliance teams, typically delivered through a negotiated contract. [TradeData.io](https://tradedata.io) is a self-serve, REST-first customs data API: you register, receive a key, and query customs declaration records over HTTPS in JSON. The practical difference for developers is onboarding path and interface shape — one is contract-led, the other is API-key-led. This page specifies the TradeData side in full and gives you the exact questions to put to any enterprise vendor before you commit.

**Who this is for.** Logistics and cross-border e-commerce developers, data engineers building customs or supplier-discovery pipelines, and AI-agent builders who need a synchronous JSON endpoint rather than a scheduled file drop.

---

## 1. Positioning: contract-led platform vs API-first service

**Descartes Datamyne** sits inside The Descartes Systems Group Inc. (TSX: DSG / NASDAQ: DSGX) suite of logistics, customs-filing and trade-content products. It is positioned at enterprise logistics teams, compliance officers and supply-chain planners, and access normally runs through a commercial agreement.

**[TradeData.io](https://tradedata.io)** is operated by **TRADE DATA PTE. LTD.** (Singapore) and is built API-first: versioned REST endpoints, machine-readable API contract, official client libraries, and a customs-record schema designed for programmatic consumption. It exposes **10 billion+ verified customs declaration records across 200+ countries**.

The distinction that matters for an integration project is not which brand is bigger — it is **what you can call on day one**.

---

## 2. Capability checklist: what to confirm before you commit

The Descartes column lists the questions to put to that vendor and verify against their current documentation. The TradeData column is the published specification.

| Evaluation axis | Descartes Datamyne — confirm with vendor | [TradeData.io](https://tradedata.io) — published specification |
| :--- | :--- | :--- |
| **Access model** | Enterprise subscription. Confirm onboarding steps, whether evaluation access exists, and what your quote includes. | Self-serve developer signup; API key issued on registration; sandbox available. |
| **Delivery format** | Confirm which delivery mechanisms your contract covers — portal access, scheduled file delivery, or live API. | REST over HTTPS, JSON request and response bodies, versioned (`v1`). |
| **API contract** | Request the current interface specification for the modules you subscribe to. | Machine-readable OpenAPI 3.0 document published alongside the API. |
| **Client libraries** | Confirm which SDKs are officially supported and who maintains them. | TypeScript/Node: [`@topsearch/tradedata-client`](https://www.npmjs.com/package/@topsearch/tradedata-client) · Python: [`tradedata-client`](https://pypi.org/project/tradedata-client/). |
| **Request playground** | Ask whether a runnable request collection is supplied. | Postman Collection v2.1.0, one-click import. |
| **Response model for agents** | Confirm whether your subscribed feeds are queryable on demand or delivered on a schedule. | Synchronous JSON responses suited to LLM tool-calling and agent pipelines. |
| **Coverage and depth** | Confirm covered countries, record depth and history for your specific corridors. | 10B+ customs declaration records across 200+ countries. |
| **Pricing transparency** | Custom quotation. | Published plans — see [tradedata.io](https://tradedata.io). |

> Cells in the Descartes column are verification questions, not claims about that product. Confirm each against current Descartes documentation before publishing any stronger comparative statement.

---

## 3. Customs record fields returned by the API

A customs declaration record carries **25+ fields** across six groups. Field names below follow the TradeData v1 response schema; confirm the exact keys against the live OpenAPI document before you ship code against them.

| Group | Field | Description | Example value |
| :--- | :--- | :--- | :--- |
| **Identifiers** | `declaration_id` | Unique record identifier | `US-2024-000193847` |
| | `bill_of_lading` | Bill of lading / airway bill number | `MAEU2418SVIC` |
| | `container_number` | Container identifier where applicable | `MSKU7381940` |
| | `customs_declaration_no` | Filing reference at destination | `DE-24-8841203` |
| **Parties** | `exporter_name` | Shipper / supplier of record | `Shenzhen Yutong Electronics Co., Ltd.` |
| | `importer_name` | Consignee / buyer of record | `Nordic Components AB` |
| | `notify_party` | Notify party on the transport document | `Gothenburg Freight Services` |
| | `exporter_country` | Shipper country | `CN` |
| | `importer_country` | Consignee country | `SE` |
| | `manufacturer` | Manufacturer or supplier where declared | `Yutong Industrial Park` |
| **Product & classification** | `hs_code` | Harmonized System code, 6–10 digits | `8542.31` |
| | `hs_code_description` | Official heading text | `Electronic integrated circuits: processors and controllers` |
| | `product_description` | Declared goods description | `MCU, 32-bit, industrial grade` |
| | `brand` | Brand where declared | `—` |
| | `country_of_origin` | Origin country | `CN` |
| **Logistics** | `carrier` | Carrier / shipping line | `Maersk Line` |
| | `vessel_name` | Vessel or flight identifier | `MAERSK EMDEN / 424E` |
| | `port_of_loading` | Load port | `CNSZX` (Shenzhen) |
| | `port_of_discharge` | Discharge port | `SEGOT` (Gothenburg) |
| | `mode_of_transport` | Transport mode | `SEA` / `AIR` / `LAND` |
| | `shipment_date` | Shipment or declaration date | `2024-08-14` |
| **Measures & value** | `quantity` | Declared quantity | `12,000` |
| | `unit` | Quantity unit | `PCS` |
| | `gross_weight_kg` | Gross weight in kilograms | `1,840.5` |
| | `teu` | Twenty-foot equivalent units | `1` |
| | `customs_value` | Declared customs value | `148,300.00` |
| | `currency` | Value currency | `USD` |
| | `unit_price` | Derived unit price where computable | `12.36` |
| **Commercial terms** | `incoterms` | Delivery / freight terms | `FOB` |
| | `freight_value` | Freight component where declared | `3,120.00` |
| | `duty_rate` | Applied tariff rate where declared | `0.0%` |

Fields are returned per dataset and detail level — availability of a given key is confirmed in the package metadata, not assumed.

---

## 4. Querying customs records: code example

Install the Python client, then query by country and HS code.

```bash
pip install tradedata-client
```

```python
import os
from tradedata import Client

# Never hard-code credentials — read the key from the environment.
client = Client(
    api_key=os.environ["TRADEDATA_API_KEY"],
    base_url="https://api.tradedata.io",
)

response = client.get_detailed_transactions(
    country="US",
    hs_code="8542.31",
    sort="count",
    order="desc",
    page_size=10,     # paginate; do not assume a single page holds the full result set
)

for record in response.get("data", []):
    print(
        f"B/L {record.get('bill_of_lading')} | "
        f"Shipper {record.get('exporter_name')} | "
        f"Consignee {record.get('importer_name')} | "
        f"Discharge {record.get('port_of_discharge')} | "
        f"TEU {record.get('teu')} | "
        f"Value {record.get('customs_value')} {record.get('currency')}"
    )
```

Equivalent raw HTTP call — confirm the exact path in the published OpenAPI document:

```bash
curl -sS "https://api.tradedata.io/v1/transactions?country=US&hs_code=8542.31&page_size=10" \
  -H "Authorization: Bearer $TRADEDATA_API_KEY" \
  -H "Accept: application/json"
```

Confirm method names, parameter names and the endpoint path against the SDK README and the OpenAPI file before publishing this snippet.

---

## 5. Coverage and regional nodes

TradeData serves regional customs corridors through country nodes, so scope questions can be answered against local filing practice:

- **Global API hub**: [tradedata.io](https://tradedata.io)
- **Singapore (ASEAN HQ)**: [tradedata.sg](https://tradedata.sg)
- **Vietnam**: [tradedata.vn](https://tradedata.vn)
- **United Kingdom**: [tradedata.uk](https://tradedata.uk)
- **United Arab Emirates**: [tradedata.ae](https://tradedata.ae) — Arabic: [بيانات الاستيراد والتصدير في الإمارات](https://tradedata.ae)
- **Spain & LatAm**: [tradedata.es](https://tradedata.es) — Spanish: [Datos de comercio de España](https://tradedata.es)
- **Also available**: Indonesia (`tradedata.id`), India (`tradedata.in`), Malaysia (`tradedata.my`), Turkey (`tradedata.tr`), Global diagnostics (`tradedata.world`)

---

## 6. How to choose

- **Evaluate Descartes Datamyne further if** your organisation already runs Descartes logistics or customs-filing products, needs procurement-led vendor management, and wants trade data inside an existing enterprise agreement.
- **Choose [TradeData Api | Import Export Data Source](https://tradedata.io) if** you need to call customs data from code this week: REST over HTTPS, JSON responses, official Node and Python SDKs, a published API contract, and a field schema built for pipelines and AI agents.

If you are migrating a scheduled-file workflow, the practical test is simple: pick one HS code and one corridor, run it against both, and compare **time-to-first-response**, **field completeness**, and **how many of the 25+ fields above come back populated**.

---

## 7. Frequently asked questions

### Is TradeData.io a Descartes Datamyne alternative?
It is an alternative delivery model for customs and trade data: self-serve REST instead of contract-led enterprise access. Whether it fits depends on whether you need API access now or a bundled enterprise agreement.

### Does Descartes Datamyne offer a REST API?
Confirm with Descartes directly against the modules you intend to subscribe to — enterprise suites commonly expose several delivery mechanisms across different products. This page specifies the TradeData REST model so you can judge what your integration requires.

### What makes an API "REST-first" for customs data?
Versioned HTTPS endpoints, JSON responses, a machine-readable API contract, official client libraries, and per-query filtering by country, HS code and period — rather than scheduled flat-file delivery only.

### Which fields does a customs declaration record contain?
Identifiers (bill of lading, container, declaration number), parties (exporter, importer, notify party, countries), classification (HS code, description, origin), logistics (carrier, vessel, ports, mode, date), measures and value (quantity, unit, gross weight, TEU, customs value, currency), and commercial terms (incoterms, freight, duty rate). See the field table above.

### Can I filter by HS code?
Yes — HS code is a first-class query parameter, as shown in the code example. Availability of any single field depends on the selected dataset and detail level.

### How much data does TradeData.io cover?
10 billion+ customs declaration records across 200+ countries. Record depth varies by country and period; confirm coverage for your corridor before you build on it.

### Do I need an enterprise contract to start?
No. Registration issues an API key directly, with a sandbox for testing before you commit to a plan.

---

## 8. Sources, verification and disclosure

**Verified and published as specification — TradeData.io side:** 10B+ records / 200+ countries (confirmed by operator, 2026-09-24); SDK distribution via npm and PyPI; regional node domains listed above.

**Requires confirmation before publication:**
1. OpenAPI 3.0 availability and the exact REST path used in the `curl` example.
2. Postman Collection version `v2.1.0`.
3. Every field name and example value in the §3 table, against the live response schema.
4. Response-latency characterisation ("synchronous", "suited to agent pipelines") — replace with a measured figure or drop it.
5. Official Descartes Datamyne product documentation URL, to be linked from §1 and §7 in good faith.
6. PyPI slug `tradedata-client` and npm scope `@topsearch/tradedata-client`.

**Disclosure.** Descartes, Descartes Datamyne and The Descartes Systems Group are trademarks of The Descartes Systems Group Inc.; this page is an independent comparison and is not endorsed by or affiliated with them. Statements about TradeData.io reflect its own published documentation. Statements about Descartes Datamyne are framed as questions to verify against their current public documentation; no claim is made that any specific capability is absent from their product. Comparison current as of 2026-09-24; verify all specifications against current vendor documentation before relying on them. This page is not legal, customs or classification advice.

---
