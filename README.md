# MeAIM — Meesho AI Marketplace (Explainer README)
*A clear, human-readable guide to the report: what it proposes, why it matters, and how to read it effectively.*

---

## 1) What this document is
The report proposes a **connected, AI-driven marketplace operating system** for Meesho. It describes four tightly-coupled layers that work end-to-end—from how shoppers discover products, to how Meesho prevents fraud/counterfeits, to how eco-friendly/local choices are surfaced, and how sellers get AI assistance. The business goal: **right-first-time purchases, higher trust, and durable unit economics**.

---

## 2) The four layers at a glance

### L1 — Intelligent Discovery
- **Problem:** Shoppers struggle to find the “right” item (fit/ETA/quality); local/eco sellers are under-exposed.  
- **Solution:**  
  - Two-stage retrieval + **multi-objective** re-ranking (conversion, return risk, ETA, margin, sustainability, fairness)  
  - **Multimodal search** (photo + natural language) with keyword fallback  
  - **Fit Passport / VTO** and a PDP **Fit Confidence** signal  
  - **Session-aware personalization** (contextual bandits)
- **Impact:** Better matches → fewer misfits/returns, higher CVR/AOV, healthier catalog exposure.

---

### L2 — Trust, Safety & Seller Quality
- **Problem:** Counterfeits, duplicate storefronts, review manipulation; siloed rules miss network-level patterns.  
- **Solution:**  
  - **Integrity Graph** across buyers, sellers, devices, addresses, payments, and images  
  - Vision checks for logo/similarity to deter counterfeits  
  - **Aspect-level sentiment** (fit, stitching, colorfastness) from reviews  
  - **Pre-publish** listing checks + continuous **risk scoring** feeding ranking/logistics  
  - **Verified Seller+** tiers (KYC++, SLA consistency, low disputes, sustainability signals)
- **Impact:** Stronger PDP credibility, lower reverse logistics, protection for good sellers.

---

### L3 — Sustainable & Local-First Growth
- **Problem:** Eco attributes stay hidden; split shipments/over-boxing raise costs; local/handmade sellers lack visibility.  
- **Solution:**  
  - **Leaf-meter** on PDP/cart and **Green Cart** nudges  
  - **Cart Optimizer** (bundling, eco alternatives with similar aesthetics/price)  
  - **Meesho Local+** curation (geo-proximity, artisan stories), themed **Mela** events
- **Impact:** Lower packaging waste/cost, reduced split shipments, stronger “shop local” equity.

---

### L4 — AI for Sellers
- **Problem:** SMBs struggle with titles/images/size charts, pricing, and SLA choices; manual ops don’t scale.  
- **Solution:**  
  - **Seller Copilot** (LLM tools for listing quality, Q&A, size-chart normalization)  
  - Demand-aware **pricing/stock hints** with margin guardrails  
  - **Smart SLA/Carrier** selection under ETA/cost/packaging constraints  
  - **Coach-before-penalize:** Copilot nudges fixes when L2 flags risks
- **Impact:** Faster time-to-first-sale, better listing quality, fewer returns, predictable SLAs.

---

## 3) Who benefits (stakeholder view)
- **Customers:** Fewer “wrong fit/color” buys, clearer PDPs, higher authenticity confidence.  
- **Genuine sellers:** Fair exposure, protection from brigading/counterfeits, faster ramp to first sales.  
- **Delivery partners:** More predictable ETAs, fewer fraud-driven reversals.  
- **Platform teams:** Lower support/returns, cleaner catalog, better unit economics.

---

## 4) Data & signals (used under the hood)
- **Events & catalog:** queries, sessions, dwell, add-to-cart; enriched attributes (materials, sizes).  
- **Reviews & disputes:** aspect-level sentiment; return outcomes.  
- **Vision & brand refs:** image similarity to catch look-alikes/counterfeits.  
- **Graph entities:** sellers, buyers, devices, addresses, payments, images for anomaly/community detection.  
- **Geo & logistics:** proximity, lane-level SLAs, packaging types, split-shipment risk.

---

## 5) How to read the report quickly (guided tour)
1. **Start with “Why Now / Rationale”** to anchor the pain points (misfits, low PDP trust, packaging/returns).  
2. **Scan the four layers** to see solution components and how they interlock.  
3. **Note the “Programs / Models / Pipelines” callouts** (risk scoring, eco-score, Fit Passport).  
4. **Finish with KPIs & Call-to-Action** to internalize success criteria and the initial pilot plan.

---

## 6) What success looks like (KPIs & guardrails)

### Discovery (L1)
- CTR/CVR/AOV ↑  
- Return-risk **decile** reductions  
- PDP engagement with Fit/Leaf-meter ↑

### Integrity (L2)
- Precision/recall on fraud labels ↑  
- Counterfeit catch rate ↑ with FP caps  
- Dispute/return rates by risk decile ↓  
- Human-auditable actions & logs

### Sustainability & Local (L3)
- Packaging weight ↓  
- Split-shipment rate ↓  
- Eco feature adoption ↑  
- Local+ share of GMV ↑

### Seller Copilot & SLA (L4)
- Time-to-first-sale ↓  
- Listing quality scores ↑  
- Return rate ↓  
- SLA adherence ↑, cost/order ↓

**Experimentation & Safety:** A/B with guardrails, canaries, auto-rollback; bias/drift monitoring; explainable policy enforcement (rules + logs).

---

## 7) Phased rollout (prioritization)

**Phase-1: Discovery + Integrity**  
- Launch ANN retrieval + multi-objective re-ranker (with return-risk & ETA) in top categories.  
- Stand up the **Risk Scoring API** (graph + vision counterfeit) feeding ranking and PDP warnings.  
- *Success = CVR ↑, returns ↓, high fraud precision/recall, auditable actions.*

**Phase-2: Fit & Sustainability**  
- **Fit Passport** + PDP **Fit Confidence**; **Leaf-meter** + Green Cart nudges; limited **Local+** curation.

**Phase-3: Seller Copilot & Smart SLA**  
- Copilot for titles/images/size charts/replies; demand-aware pricing; SLA optimizer.

---

## 8) Risks & mitigations

- **Fairness / Exposure:** Enforce seller-equity constraints in re-ranker; monitor bias drift; document remediation playbooks.  
- **False positives (Integrity):** Calibrated thresholds; manual review queues; explainable policy logs; appeals.  
- **Cold start:** Hybrid keyword + embedding retrieval; catalog enrichment; conservative boosts for new/good sellers.  
- **Privacy & PII:** Strict scoping for identity/fraud signals; least-privilege access; data minimization; auditable usage.  
- **Operational regressions:** Guardrail metrics, canaries, reversible feature flags for all launches.

---

## 9) Glossary (quick reference)
- **ANN Retrieval:** Fast vector search to fetch candidate items for ranking.  
- **Re-ranker (Multi-objective):** Optimizes several business goals at once (CVR, returns, ETA, margin, sustainability, fairness).  
- **Fit Passport / VTO:** Fit/size confidence signals and lightweight try-on proxies to reduce misfit returns.  
- **Integrity Graph:** Marketplace entities/signals graph for fraud/counterfeit and coordinated-abuse detection.  
- **Aspect-level Sentiment:** NLP that extracts aspect-specific opinions (e.g., “runs small”, “stitching poor”).  
- **Leaf-meter / Green Cart:** Eco-attributes surfaced on PDP/cart + nudges to reduce waste/splits.  
- **Seller Copilot:** LLM-powered assistant for listing quality, pricing/stock hints, and policy-aware nudges.
