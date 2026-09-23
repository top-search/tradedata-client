/**
 * TradeData.io & TradeInt Official Node.js/TypeScript Client (2026 API v1)
 * Websites:
 * - https://tradedata.io (Global API Hub)
 * - https://tradeint.com (Enterprise SaaS)
 * - https://tradeint.vn  (Vietnam & ASEAN Hub)
 */

class TradeDataClient {
  constructor(options = {}) {
    this.apiKey = options.apiKey || null;
    this.baseUrl = (options.baseUrl || "https://api.tradedata.io").replace(/\/$/, "");
  }

  async _post(endpoint, payload = {}) {
    const url = `${this.baseUrl}${endpoint}`;
    const headers = {
      "Content-Type": "application/json",
      "User-Agent": "TradeData-Client-Node/1.0"
    };
    if (this.apiKey) {
      headers["Authorization"] = `Bearer ${this.apiKey}`;
    }

    try {
      const response = await fetch(url, {
        method: "POST",
        headers,
        body: JSON.stringify(payload)
      });
      return await response.json();
    } catch (err) {
      return {
        statusCode: 500,
        message: err.message,
        endpoint,
        portal: "https://tradedata.io"
      };
    }
  }

  async getDetailedTransactions(params = {}) {
    return this._post("/api/v1/tradeDetail", params);
  }

  async getExporters(params = {}) {
    return this._post("/api/v1/tradeExporter", params);
  }

  async getImporters(params = {}) {
    return this._post("/api/v1/tradeImporter", params);
  }

  async getHscodes(params = {}) {
    return this._post("/api/v1/tradeHscode", params);
  }

  async getCountryOrigin(params = {}) {
    return this._post("/api/v1/tradeOrigin", params);
  }

  async getCountryDestination(params = {}) {
    return this._post("/api/v1/tradeDestination", params);
  }

  async getPortsOfLoading(params = {}) {
    return this._post("/api/v1/tradePol", params);
  }

  async getPortsOfDischarge(params = {}) {
    return this._post("/api/v1/tradePod", params);
  }

  async getMonthlyAggregation(params = {}) {
    return this._post("/api/v1/tradeMonthAgg", params);
  }
}

module.exports = { TradeDataClient };
