/**
 * Algo Trading Platform Scope Estimator
 * Swift Tech Co. — https://swifttechco.com
 */

const EXCHANGES = [
  "Crypto (Binance/Coinbase/Kraken)",
  "US Equities (Alpaca/IBKR)",
  "Forex (OANDA/FXCM)",
  "Futures (CME/NinjaTrader)",
  "Options (IBKR/Thinkorswim)",
];

const EXECUTION_SPEEDS = {
  "End-of-day (EOD): daily signals":     25,
  "Intraday: 1-min to hourly bars":       45,
  "High-frequency (HFT): sub-second":    95,
};

const STRATEGY_COUNTS = {
  "1 to 5 strategies":     0,
  "5 to 20 strategies":   15,
  "20 to 100 strategies": 40,
  "100+ strategies":      80,
};

const FEATURES = [
  "Real-time charting (TradingView-style)",
  "Backtesting engine",
  "Paper trading mode",
  "Risk management & position sizing",
  "Telegram / Discord alerts",
  "Multi-account management",
  "Performance analytics dashboard",
  "Live order book & depth of market",
];

/**
 * @param {string} executionSpeed - One of EXECUTION_SPEEDS keys.
 * @param {string} strategyCount - One of STRATEGY_COUNTS keys.
 * @param {string[]} [exchanges] - Exchange strings from EXCHANGES.
 * @param {string[]} [features] - Feature strings from FEATURES.
 * @returns {{ lowK: number, highK: number, weeks: number }}
 */
function calculate(executionSpeed, strategyCount, exchanges = [], features = []) {
  if (EXECUTION_SPEEDS[executionSpeed] === undefined) throw new Error(`Unknown execution speed: ${executionSpeed}`);
  if (STRATEGY_COUNTS[strategyCount] === undefined) throw new Error(`Unknown strategy count: ${strategyCount}`);

  const sc  = EXECUTION_SPEEDS[executionSpeed];
  const stc = STRATEGY_COUNTS[strategyCount];
  const tot = sc + stc + exchanges.length * 8 + features.length * 6;

  return {
    lowK:  tot,
    highK: Math.round(tot * 1.4),
    weeks: Math.round(8 + tot / 5),
  };
}

module.exports = { EXCHANGES, EXECUTION_SPEEDS, STRATEGY_COUNTS, FEATURES, calculate };
