# MeAIM — Meesho AI Marketplace (Ctrl+Alt+Elite, IIT Kharagpur)

This repository contains the **report**, **architecture**, and **reference implementation skeletons** for the MeAIM proposal — an AI-first marketplace OS focused on **Intelligent Discovery**, **Trust & Seller Quality**, **Local-First Growth**, and **AI for Sellers**.

## What's inside
- 📄 `REPORT/` — final PDF and a one-page summary
- 🧱 `docs/` — architecture, metrics, governance, roadmap
- 🧪 `src/` — reference service stubs (APIs), pipelines, and feature store layout
- 🛠️ `infra/` — Docker/K8s/Makefile to run locally
- 📊 `ops/` — monitoring/observability templates
- 🧰 `.github/` — CI, issue and PR templates
- 🗃️ `data/` — empty by default; instructions for using Git LFS
- 📚 `LICENSE`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`

> Note: This is a **shareable skeleton**. Swap stubs with your internal code as needed.

## Quick start
```bash
# 1) Build and run the Risk Scoring API locally
make up

# 2) Open http://localhost:8080/docs for Swagger UI
# 3) Run unit tests
make test
```

## Layers covered
- L1: Intelligent Discovery (multimodal search, multi-objective ranking)
- L2: Trust & Seller Quality (Fraud & Quality Graph, Aspect Sentiment, Verified Seller+)
- L3: Local-First Growth (Eco score, Cart optimizer, Local+ ranker)
- L4: AI for Sellers (Seller Copilot, Smart SLA & Routing)

---

© 2025-09-27 Ctrl+Alt+Elite — IIT Kharagpur • Meesho DICE Challenge 2.0 (Tech Track)
