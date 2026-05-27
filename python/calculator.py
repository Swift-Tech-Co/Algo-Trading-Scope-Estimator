"""
Algo Trading Platform Scope Estimator
Swift Tech Co. — https://swifttechco.com

Estimates build cost and timeline for algorithmic trading platforms based on
exchange integrations, execution speed, strategy count, and platform features.
"""

EXCHANGES = [
    "Crypto (Binance/Coinbase/Kraken)",
    "US Equities (Alpaca/IBKR)",
    "Forex (OANDA/FXCM)",
    "Futures (CME/NinjaTrader)",
    "Options (IBKR/Thinkorswim)",
]

EXECUTION_SPEEDS = {
    "End-of-day (EOD): daily signals":      25,
    "Intraday: 1-min to hourly bars":        45,
    "High-frequency (HFT): sub-second":     95,
}

STRATEGY_COUNTS = {
    "1 to 5 strategies":     0,
    "5 to 20 strategies":   15,
    "20 to 100 strategies": 40,
    "100+ strategies":      80,
}

FEATURES = [
    "Real-time charting (TradingView-style)",
    "Backtesting engine",
    "Paper trading mode",
    "Risk management & position sizing",
    "Telegram / Discord alerts",
    "Multi-account management",
    "Performance analytics dashboard",
    "Live order book & depth of market",
]


def calculate(
    execution_speed: str,
    strategy_count: str,
    exchanges: list = None,
    features: list = None,
) -> dict:
    """
    Returns estimated build cost range (USD thousands) and timeline (weeks).

    Args:
        execution_speed: One of the EXECUTION_SPEEDS keys.
        strategy_count: One of the STRATEGY_COUNTS keys.
        exchanges: List of exchange strings from EXCHANGES.
        features: List of feature strings from FEATURES.

    Returns:
        dict with keys: low_k, high_k, weeks
    """
    if execution_speed not in EXECUTION_SPEEDS:
        raise ValueError(f"Unknown execution speed: {execution_speed}")
    if strategy_count not in STRATEGY_COUNTS:
        raise ValueError(f"Unknown strategy count: {strategy_count}")

    exchanges = exchanges or []
    features  = features  or []

    sc  = EXECUTION_SPEEDS[execution_speed]
    stc = STRATEGY_COUNTS[strategy_count]
    tot = sc + stc + len(exchanges) * 8 + len(features) * 6

    return {
        "low_k":  tot,
        "high_k": round(tot * 1.4),
        "weeks":  round(8 + tot / 5),
    }
