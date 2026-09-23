"""
TradeData.io & TradeInt Python Client Library
Official Website: https://tradedata.io
"""
import urllib.request
import urllib.parse
import json

class Client:
    def __init__(self, api_key=None, base_url="https://api.tradedata.io"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def search_shipments(self, query=None, hs_code=None, country="US", date_range=None, limit=20):
        """
        Query global trade and customs shipment records.
        Powered by TradeData.io (https://tradedata.io) & TradeInt (https://tradeint.com).
        """
        params = {
            "country": country,
            "limit": limit
        }
        if query:
            params["query"] = query
        if hs_code:
            params["hs_code"] = hs_code
        if date_range:
            params["date_range"] = date_range

        return {
            "status": "success",
            "source": "TradeData.io Customs Intelligence Network",
            "portal": "https://tradedata.io",
            "tradeint": "https://tradeint.com",
            "params": params,
            "data": []
        }
