<div align="center">

<img src=".github/social-preview.png" alt="Viprasol Claude Code plugins: one marketplace, eight free plugins, 146 skills for trading, fintech, India Stack, voice agents and video." width="100%">

### Every free Claude Code plugin from Viprasol, in one marketplace

**Trading · options · TradingView automation · crypto bots · fintech · India Stack · voice agents · video editing**<br>
Add the marketplace once, then install only the plugins you need.

[![License: MIT](https://img.shields.io/badge/license-MIT-25342f?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-marketplace-d97757?style=for-the-badge)](https://code.claude.com/docs/en/plugins/create-marketplace)
[![Plugins](https://img.shields.io/badge/plugins-8-765820?style=for-the-badge)](#-plugins)
[![CI](https://img.shields.io/github/actions/workflow/status/Viprasol-Tech/claude-plugins/ci.yml?branch=main&style=for-the-badge&label=links)](https://github.com/Viprasol-Tech/claude-plugins/actions/workflows/ci.yml)

</div>

---

## ⚡ Install

```bash
claude plugin marketplace add Viprasol-Tech/claude-plugins
```

Then pick what you need:

```bash
claude plugin install trading-studio@viprasol
claude plugin install tradingview-automation@viprasol
claude plugin install options-desk@viprasol
claude plugin install crypto-bots@viprasol
claude plugin install fintech-studio@viprasol
claude plugin install india-stack@viprasol
claude plugin install voice-agents@viprasol
claude plugin install video-studio@viprasol
```

Skills load automatically when your request matches, or call one directly as
`/<plugin>:<skill>`. Update everything later with
`claude plugin marketplace update viprasol`.

## 📦 Plugins

| Plugin | Skills | For | Source |
| --- | ---: | --- | --- |
| 📈 **`trading-studio`** | 10 | Pine Script v6, MQL5 Expert Advisors, backtest audits with Deflated Sharpe, position sizing, bot security, trade journals, Kalshi / Polymarket | [claude-trading-skills](https://github.com/Viprasol-Tech/claude-trading-skills) |
| 🔔 **`tradingview-automation`** | 6 | TradingView alerts and webhooks, signal-to-order workers, Zerodha / Angel One / Dhan / Upstox under SEBI's 2026 algo rules, MT5 and crypto bridges, TradingView charts | [claude-tradingview-automation-skills](https://github.com/Viprasol-Tech/claude-tradingview-automation-skills) |
| 🧮 **`options-desk`** | 6 | Option pricing, Greeks and IV, exact multi-leg payoffs, chain data, spread orders on IBKR / Alpaca / Tradier / Kite, NSE & SEBI F&O rules, options backtests | [claude-options-trading-skills](https://github.com/Viprasol-Tech/claude-options-trading-skills) |
| 🪙 **`crypto-bots`** | 7 | Binance / Bybit / OKX signing, tick and lot filters, rate limits, order book sync, order lifecycle, perps liquidation maths, Hyperliquid and Solana | [claude-crypto-bot-skills](https://github.com/Viprasol-Tech/claude-crypto-bot-skills) |
| 💳 **`fintech-studio`** | 8 | Money maths, double-entry ledgers, Stripe / Razorpay / PayPal / Adyen, webhook security, subscriptions, reconciliation, PCI DSS, KYC/AML | [claude-fintech-skills](https://github.com/Viprasol-Tech/claude-fintech-skills) |
| 🇮🇳 **`india-stack`** | 7 | UPI, GST invoicing, GSTIN / PAN / Aadhaar validation, Aadhaar eKYC, Account Aggregator, RBI payment rules, DPDP | [claude-india-stack-skills](https://github.com/Viprasol-Tech/claude-india-stack-skills) |
| 🎙️ **`voice-agents`** | 7 | Voice agent architecture, telephony, voice prompting, latency, testing, calling compliance, audio formats | [claude-voice-agent-skills](https://github.com/Viprasol-Tech/claude-voice-agent-skills) |
| 🎬 **`video-studio`** | 95 | A full video editor: director, 42 genre skills, 46 style skins, finishing and delivery | [claude-video-editing-skills](https://github.com/Viprasol-Tech/claude-video-editing-skills) |

Each plugin lives in its own repository with its own tests, changelog and
issues. This repository only lists them: the marketplace installs each
plugin straight from its source repository (`git-subdir`), so you always get
the version on that repository's `main` branch.

## Why one marketplace

- One `marketplace add`, then browse every plugin with `/plugin`.
- Plugins you install from here and from the individual repositories are the
  same code; you do not need both.
- The CI here fetches every plugin's manifest from GitHub each week, so a
  moved or renamed plugin is caught before you hit it.

## Contributing

Bugs and corrections belong in the plugin's own repository (linked above).
Ideas for a new plugin: open an issue here.

## 📬 Contact — Viprasol Tech Private Limited

We build trading systems, fintech platforms and AI voice agents, and publish
the engineering checklists we use as free Claude Code plugins.

- 🌐 Website: [viprasol.com](https://viprasol.com)
- ✉️ Email: [support@viprasol.com](mailto:support@viprasol.com)
- 💬 Telegram: [t.me/viprasol_help](https://t.me/viprasol_help) · 📱 WhatsApp: +91 96336 52112
- 🐙 GitHub: [@Viprasol-Tech](https://github.com/Viprasol-Tech) · 💼 [LinkedIn](https://www.linkedin.com/in/viprasol/) · 𝕏 [@viprasol](https://twitter.com/viprasol)

## License

[MIT](LICENSE) © 2026 Viprasol Tech Private Limited. Each plugin carries its
own licence in its repository.
