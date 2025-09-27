# Architecture

- **L1 Intelligent Discovery:** two-stage ranking (ANN candidates + multi-objective re-ranker), Fit Passport, multimodal (CLIP-like) embeddings.
- **L2 Trust & Seller Quality:** unified entity graph, GNN-based anomaly detection, aspect sentiment (HF Transformers), Verified Seller+.
- **L3 Local-First Growth:** Eco score, Cart optimizer (bundle & swaps), Local+ ranker (geo proximity + reliability).
- **L4 AI for Sellers:** Copilot (LLM tools), demand forecasts, Smart SLA/Carrier (OR-Tools).

See `src/services/*` for reference APIs and `src/pipelines/*` for feature store/dbt layout.
