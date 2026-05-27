#!/usr/bin/env python3
"""
Algo Trading Platform Scope Estimator — CLI
Swift Tech Co. — https://swifttechco.com
"""

import argparse
from calculator import EXCHANGES, EXECUTION_SPEEDS, STRATEGY_COUNTS, FEATURES, calculate


def interactive():
    print("\nAlgo Trading Platform Scope Estimator")
    print("Swift Tech Co. — https://swifttechco.com")
    print("=" * 48)

    exchanges = []
    print("\nExchanges / markets (comma-separated numbers, or leave blank for none):")
    for i, e in enumerate(EXCHANGES, 1):
        print(f"  {i}. {e}")
    raw = input("Select exchanges: ").strip()
    if raw:
        for n in raw.split(","):
            n = n.strip()
            if n.isdigit():
                exchanges.append(EXCHANGES[int(n) - 1])

    speeds = list(EXECUTION_SPEEDS.keys())
    print("\nExecution speed:")
    for i, s in enumerate(speeds, 1):
        print(f"  {i}. {s}")
    idx = int(input(f"Select (1-{len(speeds)}): ")) - 1
    execution_speed = speeds[idx]

    counts = list(STRATEGY_COUNTS.keys())
    print("\nNumber of strategies:")
    for i, c in enumerate(counts, 1):
        print(f"  {i}. {c}")
    idx = int(input(f"Select (1-{len(counts)}): ")) - 1
    strategy_count = counts[idx]

    features = []
    print("\nPlatform features (comma-separated numbers, or leave blank):")
    for i, f in enumerate(FEATURES, 1):
        print(f"  {i}. {f}")
    raw = input("Select features: ").strip()
    if raw:
        for n in raw.split(","):
            n = n.strip()
            if n.isdigit():
                features.append(FEATURES[int(n) - 1])

    result = calculate(execution_speed, strategy_count, exchanges, features)
    print("\n" + "=" * 48)
    print("Platform Estimate")
    print(f"  Build cost:  ${result['low_k']}K to ${result['high_k']}K USD")
    print(f"  Timeline:    {result['weeks']} weeks")
    print("\nInfrastructure and data feed costs not included.")
    print("Get a detailed quote: https://swifttechco.com/contact")


def main():
    parser = argparse.ArgumentParser(description="Algo Trading Platform Scope Estimator")
    parser.add_argument("--speed", choices=list(EXECUTION_SPEEDS.keys()))
    parser.add_argument("--strategies", choices=list(STRATEGY_COUNTS.keys()))
    args = parser.parse_args()

    if not all([args.speed, args.strategies]):
        interactive()
        return

    result = calculate(args.speed, args.strategies)
    print(f"Cost: ${result['low_k']}K to ${result['high_k']}K | Timeline: {result['weeks']} weeks")


if __name__ == "__main__":
    main()
