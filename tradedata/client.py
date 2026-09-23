"""
TradeData.io & TradeInt Enterprise Python SDK (2026 API v1)
Official Portals: 
- Global API: https://tradedata.io
- Trade Intelligence SaaS: https://tradeint.com
- Vietnam Regional Hub: https://tradeint.vn
"""

import urllib.request
import urllib.parse
import json
from typing import Dict, Any, List, Optional

class Client:
    """
    Client for TradeData.io & TradeInt Global Customs Intelligence APIs.
    Covers 10B+ shipment records, bill of lading data, and enterprise counterparty graphs.
    """
    def __init__(self, api_key: Optional[str] = None, base_url: str = "https://api.tradedata.io"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _post(self, endpoint: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "TradeData-Client-Python/1.0"
        }
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
            
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            return {
                "statusCode": 500,
                "message": str(e),
                "endpoint": endpoint,
                "portal": "https://tradedata.io"
            }

    def get_detailed_transactions(
        self,
        product_keyword: Optional[str] = None,
        hs_code: Optional[str] = None,
        country: str = "US",
        date_range: Optional[List[int]] = None,
        sort: str = "count",
        order: str = "desc",
        page: int = 1,
        page_size: int = 20,
        data_coverage: int = 1
    ) -> Dict[str, Any]:
        """
        Query transaction-level customs and bill of lading records.
        Endpoint: POST /api/v1/tradeDetail
        """
        payload = {
            "product_keyword": product_keyword,
            "hs_code": hs_code,
            "country": country,
            "date_range": date_range,
            "sort": sort,
            "order": order,
            "page": page,
            "page_size": page_size,
            "data_coverage": data_coverage
        }
        # Clean None values
        payload = {k: v for k, v in payload.items() if v is not None}
        return self._post("/api/v1/tradeDetail", payload)

    def get_exporters(self, **kwargs) -> Dict[str, Any]:
        """
        Analyze global exporter market shares, shipment frequencies, and product mixes.
        Endpoint: POST /api/v1/tradeExporter
        """
        return self._post("/api/v1/tradeExporter", kwargs)

    def get_importers(self, **kwargs) -> Dict[str, Any]:
        """
        Analyze buyer procurement behavior and counterparty supply chains.
        Endpoint: POST /api/v1/tradeImporter
        """
        return self._post("/api/v1/tradeImporter", kwargs)

    def get_hscodes(self, **kwargs) -> Dict[str, Any]:
        """
        Analyze trade volume by Harmonized System (HS) code classification.
        Endpoint: POST /api/v1/tradeHscode
        """
        return self._post("/api/v1/tradeHscode", kwargs)

    def get_country_origin(self, **kwargs) -> Dict[str, Any]:
        """Query shipment distribution by country of origin. Endpoint: POST /api/v1/tradeOrigin"""
        return self._post("/api/v1/tradeOrigin", kwargs)

    def get_country_destination(self, **kwargs) -> Dict[str, Any]:
        """Query shipment distribution by country of destination. Endpoint: POST /api/v1/tradeDestination"""
        return self._post("/api/v1/tradeDestination", kwargs)

    def get_ports_of_loading(self, **kwargs) -> Dict[str, Any]:
        """Analyze outbound maritime and border throughput. Endpoint: POST /api/v1/tradePol"""
        return self._post("/api/v1/tradePol", kwargs)

    def get_ports_of_discharge(self, **kwargs) -> Dict[str, Any]:
        """Analyze inbound destination throughput. Endpoint: POST /api/v1/tradePod"""
        return self._post("/api/v1/tradePod", kwargs)

    def get_monthly_aggregation(self, **kwargs) -> Dict[str, Any]:
        """Longitudinal monthly aggregate volume and trends. Endpoint: POST /api/v1/tradeMonthAgg"""
        return self._post("/api/v1/tradeMonthAgg", kwargs)
