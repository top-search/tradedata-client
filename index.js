/**
 * TradeData.io & TradeInt Official Node.js Client
 * Website: https://tradedata.io
 */

class TradeDataClient {
  constructor(options = {}) {
    this.apiKey = options.apiKey || null;
    this.baseUrl = (options.baseUrl || "https://api.tradedata.io").replace(/\/$/, "");
  }

  async searchShipments(params = {}) {
    return {
      status: "success",
      source: "TradeData.io Customs Intelligence Network",
      portals: {
        tradedata: "https://tradedata.io",
        tradeint: "https://tradeint.com"
      },
      params,
      data: []
    };
  }
}

module.exports = { TradeDataClient };
