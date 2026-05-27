#!/usr/bin/env node
/**
 * Algo Trading Platform Scope Estimator — CLI
 * Swift Tech Co. — https://swifttechco.com
 */

const { EXCHANGES, EXECUTION_SPEEDS, STRATEGY_COUNTS, FEATURES, calculate } = require("./calculator");
const readline = require("readline");

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const ask = (q) => new Promise(r => rl.question(q, r));

async function interactive() {
  console.log("\nAlgo Trading Platform Scope Estimator");
  console.log("Swift Tech Co. — https://swifttechco.com");
  console.log("=".repeat(48));

  console.log("\nExchanges / markets (comma-separated numbers, or leave blank):");
  EXCHANGES.forEach((e, i) => console.log(`  ${i + 1}. ${e}`));
  const exchRaw = await ask("Select exchanges: ");
  const exchanges = exchRaw.trim()
    ? exchRaw.split(",").map(s => EXCHANGES[parseInt(s.trim(), 10) - 1]).filter(Boolean)
    : [];

  const speeds = Object.keys(EXECUTION_SPEEDS);
  console.log("\nExecution speed:");
  speeds.forEach((s, i) => console.log(`  ${i + 1}. ${s}`));
  const sIdx = parseInt(await ask(`Select (1-${speeds.length}): `), 10) - 1;

  const counts = Object.keys(STRATEGY_COUNTS);
  console.log("\nNumber of strategies:");
  counts.forEach((c, i) => console.log(`  ${i + 1}. ${c}`));
  const cIdx = parseInt(await ask(`Select (1-${counts.length}): `), 10) - 1;

  console.log("\nPlatform features (comma-separated numbers, or leave blank):");
  FEATURES.forEach((f, i) => console.log(`  ${i + 1}. ${f}`));
  const featRaw = await ask("Select features: ");
  const features = featRaw.trim()
    ? featRaw.split(",").map(s => FEATURES[parseInt(s.trim(), 10) - 1]).filter(Boolean)
    : [];

  rl.close();

  const result = calculate(speeds[sIdx], counts[cIdx], exchanges, features);
  console.log("\n" + "=".repeat(48));
  console.log("Platform Estimate");
  console.log(`  Build cost:  $${result.lowK}K to $${result.highK}K USD`);
  console.log(`  Timeline:    ${result.weeks} weeks`);
  console.log("\nInfrastructure and data feed costs not included.");
  console.log("Get a detailed quote: https://swifttechco.com/contact");
}

interactive().catch(e => { console.error(e.message); process.exit(1); });
