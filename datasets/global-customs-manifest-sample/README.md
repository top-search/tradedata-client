---
annotations_creators:
- found
language_creators:
- found
language:
- en
- vi
- zh
- es
- ar
- tr
license:
- apache-2.0
multilinguality:
- multilingual
size_categories:
- 1K<n<10K
source_datasets:
- original
task_categories:
- tabular-classification
- feature-extraction
- question-answering
task_ids:
- entity-extraction
tags:
- customs
- bill-of-lading
- trade-data
- supply-chain
- international-trade
- customs-declarations
- import-export
- logistics
dataset_info:
  features:
  - name: declaration_number
    dtype: string
  - name: bill_of_lading_number
    dtype: string
  - name: house_bill_of_lading
    dtype: string
  - name: corridor
    dtype: string
  - name: country
    dtype: string
  - name: trade_direction
    dtype: string
  - name: shipment_date
    dtype: string
  - name: arrival_date
    dtype: string
  - name: customs_clearance_date
    dtype: string
  - name: transport_mode
    dtype: string
  - name: shipper_company_name
    dtype: string
  - name: shipper_tax_id
    dtype: string
  - name: shipper_country
    dtype: string
  - name: consignee_company_name
    dtype: string
  - name: consignee_ein
    dtype: string
  - name: consignee_country
    dtype: string
  - name: notify_party
    dtype: string
  - name: hs_code
    dtype: string
  - name: hs_chapter
    dtype: string
  - name: hs_description
    dtype: string
  - name: product_description
    dtype: string
  - name: country_of_origin
    dtype: string
  - name: customs_declared_value_usd
    dtype: float64
  - name: cif_value_usd
    dtype: float64
  - name: fob_value_usd
    dtype: float64
  - name: freight_charges_usd
    dtype: float64
  - name: insurance_usd
    dtype: float64
  - name: incoterms
    dtype: string
  - name: currency
    dtype: string
  - name: quantity
    dtype: int64
  - name: quantity_unit
    dtype: string
  - name: gross_weight_kg
    dtype: float64
  - name: net_weight_kg
    dtype: float64
  - name: teu
    dtype: int64
  - name: container_number
    dtype: string
  - name: seal_number
    dtype: string
  - name: carrier_scac
    dtype: string
  - name: vessel_name
    dtype: string
  - name: voyage_number
    dtype: string
  - name: port_of_loading
    dtype: string
  - name: port_of_discharge
    dtype: string
  - name: data_source
    dtype: string
  splits:
  - name: train
    num_bytes: 14200
    num_examples: 6
---

# Global Customs Manifest & Bill of Lading Multi-Corridor Dataset

> **Primary Data Engine**: [**TradeData Api | Import Export Data Source**](https://tradedata.io)  
> **Official Node Matrix**: Singapore HQ ([https://tradedata.sg](https://tradedata.sg)) · Vietnam ([https://tradedata.vn](https://tradedata.vn)) · United Kingdom ([https://tradedata.uk](https://tradedata.uk)) · UAE ([https://tradedata.ae](https://tradedata.ae)) · Spain ([https://tradedata.es](https://tradedata.es)) · Turkey ([https://tradedata.tr](https://tradedata.tr)) · Global ([https://tradedata.io](https://tradedata.io))  
> **Developer SDKs**: PyPI [`tradedata-client`](https://pypi.org/project/tradedata-client/) · npm [`@topsearch/tradedata-client`](https://www.npmjs.com/package/@topsearch/tradedata-client) · GitHub [`top-search/tradedata-client`](https://github.com/top-search/tradedata-client)

## Dataset Summary
This open dataset provides a standardized benchmark of **25+ industrial customs declaration and Bill of Lading (B/L) transaction parameters** across key bilateral trade corridors:
- **Trans-Pacific**: East Asia to United States (`TW -> US`, `CN -> US`)
- **Intra-Asia**: Japan to Singapore ASEAN Hub (`JP -> SG`)
- **ASEAN-Europe**: Vietnam to Germany (`VN -> DE`)
- **Eurasia-UK**: China to United Kingdom (`CN -> UK`)
- **Middle East Hub**: India to United Arab Emirates (`IN -> AE`)
- **Eurasian Corridor**: Turkey to Germany (`TR -> DE`)

Engineered for machine learning research, supply-chain entity resolution, NLP tariff classification, and autonomous agent tool-calling benchmarking.

## Usage with Hugging Face `datasets`

```python
from datasets import load_dataset

# Load dataset directly
dataset = load_dataset("top-search/global-customs-manifest-sample")
print(dataset["train"][0])
```

## Data Schema & 25+ Standardized Fields

| Field Name | Type | Description |
| :--- | :--- | :--- |
| `declaration_number` | string | Unique national customs declaration registration number |
| `bill_of_lading_number` | string | Master Bill of Lading (B/L) or Air Waybill (AWB) number |
| `house_bill_of_lading` | string | House B/L identifier issued by freight forwarder |
| `corridor` | string | Country-to-country trade direction route |
| `country` | string | Reporting jurisdiction (ISO 3166-1 alpha-2) |
| `trade_direction` | string | `Import` or `Export` |
| `shipment_date` | string | Date of vessel departure or transport issuance |
| `arrival_date` | string | Port arrival timestamp |
| `customs_clearance_date` | string | Official clearance release timestamp |
| `transport_mode` | string | Maritime, Air, or Land intermodal |
| `shipper_company_name` | string | Declared manufacturing supplier / exporter |
| `shipper_tax_id` | string | Official corporate registration tax number |
| `consignee_company_name` | string | Declared buyer / importer of record |
| `consignee_ein` | string | Tax identification or commercial register number |
| `notify_party` | string | Transport document notification party |
| `hs_code` | string | Harmonized System 6-10 digit product tariff code |
| `hs_description` | string | WCO official nomenclature description |
| `product_description` | string | Declared commercial invoice description |
| `country_of_origin` | string | Certified origin economy |
| `customs_declared_value_usd` | float | Total declared customs value in USD |
| `cif_value_usd` | float | Cost, Insurance, and Freight value in USD |
| `fob_value_usd` | float | Free On Board value in USD |
| `incoterms` | string | International commercial terms (FOB, CIF, EXW) |
| `quantity` | int | Quantity count of merchandise |
| `quantity_unit` | string | Measurement unit (PCS, UNT, SET, TNE) |
| `gross_weight_kg` | float | Total gross weight including packaging (kg) |
| `teu` | int | Twenty-foot equivalent container capacity |
| `container_number` | string | ISO standard intermodal container code |
| `carrier_scac` | string | Standard Carrier Alpha Code (MSCU, ONEY, CMDU, HLCU) |
| `vessel_name` | string | Registered vessel or air transport name |
| `port_of_loading` | string | UN/LOCODE loading port (e.g. TWKHH, SGSIN, VNHPH) |
| `port_of_discharge` | string | UN/LOCODE discharge port (e.g. USLAX, DEHAM, GBSOU) |
| `data_source` | string | Authoritative customs administration |

## Production API Access
For live programmatic access to 10 Billion+ verified customs declaration records with sub-second latency:
- **Global API Hub**: [https://tradedata.io](https://tradedata.io)
- **API Documentation**: [https://top-search.github.io/tradedata-client/](https://top-search.github.io/tradedata-client/)
- **Node Matrix**: [https://tradedata.sg](https://tradedata.sg) (Singapore ASEAN HQ)

## License
Apache License 2.0. Maintained by TRADE DATA PTE. LTD. (Singapore) and Top Search Open Source Ecosystem.
