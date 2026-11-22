## Overview

Multimodal AI involves more than combining text, audio, images and video. The data behind robots, self-driving cars and world models is typically spread across systems that were never built to meet. Someone has to bring it all together. And that someone is a data engineer.

Learn that work here, by doing it. Build your portfolio with 17 working projects: one for each chapter of [*Data Engineering for Multimodal AI*](https://oreil.ly/data-engineering-multimodal) (O'Reilly, 2026), and five more to go further. Each runs on your laptop with one command and shows you what it measured.

Pick one. Run it. Make it yours.

## Start here

1. **Pick a playbook** from the list below, or follow a learning path.
2. **Open it** in a GitHub Codespace, or clone it.
3. **Run `make run`**, then follow the README's numbered "Run it" steps and "Try this" experiments.

Only have time for one? Go to [Playbook 05](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-05-multimodal-feature-engineering). You'll turn self-driving car data, motion tracks and the text that explains them, into one set of features a model can learn from.

> **Updates in progress (November 2026).** The one-command runs, Codespaces and step-by-step READMEs are in review in each repo. Until they are merged, each repo's open pull request has the new version.

## Playbooks

| Chapter | Playbook | What you'll do | Data |
|---|---|---|---|
| Starter | [00 CLIP claims](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-00-multimodal-ai-CLIP-claims-pipeline) | Search pet insurance claims by X-ray, text or photo | Image, text, tables |
| Starter | [00 Factory action plans](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-00-multimodal-end-to-end-pipeline) | Turn factory sensor and camera data into an action plan | Sensor, image, tables |
| Starter | [00 Music feature store](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-00-multimodal-feature-store-GTZAN) | Find songs that sound alike or look alike | Audio, image |
| 1 | [01 Semantic layer](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-01-multimodal-ai-semantic-layer) | Link an X-ray, a note and vitals into one clinical event | Image, text, sensor |
| 2 | [02 Feature store](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-02-multimodal-feature-store-streambuy) | Search products by photo, review and video | Image, text, video |
| 3 | [03 Context platform](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-03-multimodal-context-platform) | Find the right documents from a plain-language request | Image, documents |
| 4 | [04 Ingestion](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-04-multimodal-ingestion-pipeline) | Ingest kitchen sensors, reviews and photos in one pipeline | Sensor, text, image |
| 4 (bonus) | [04 bonus: Video similarity](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-04-bonus-multimodal-vector-similarity) | Find similar cooking videos with vector search | Video |
| 5 | [05 Feature engineering](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-05-multimodal-feature-engineering) | Turn driving data and its explanations into one set of features | Motion, text |
| 6 | [06 Graph retrieval](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-06-multimodal-graph-rag) | Retrieve past incidents with vectors, a graph and a cache | Text, image, graph |
| 7 | [07 Inference router](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-07-multimodal-inference-router) | Route drone and soil streams to real-time inference | Image, sensor |
| 8 | [08 MLOps](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-08-multimodal-mlops) | Build an MLOps pipeline that catches drift and retrains | Video, sensor |
| 9 | [09 Scaling](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-09-multimodal-scaling-benchmarks) | Scale a hospital pipeline on serverless GPUs, and measure it | Image, text, tables |
| 10 | [10 Inference service](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-10-multimodal-inference-service) | Serve a robot model with canary rollout and rollback | Image, text, audio, sensor |
| 11 | [11 Governance](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-11-multimodal-governance-pipeline) | Make a hospital robot's pipeline traceable, secure and fair | Text, image, video, sensor |
| 12 | [12 End-to-end](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-12-multimodal-streamkit-ops-pipeline) | Find the root cause of failures in a Kubernetes cluster | Metrics, logs |
| 12 (bonus) | [12 bonus: Factory root cause](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-12-bonus-multimodal-rca-pipeline) | Find defective products on a robot assembly line | Sensor |

Starter and bonus playbooks are not printed in the book.

## Learning paths

Each path is a few playbooks in order, each building on the last.

- **New to multimodal data:** [01](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-01-multimodal-ai-semantic-layer) → [02](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-02-multimodal-feature-store-streambuy) → [05](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-05-multimodal-feature-engineering) → [12](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-12-multimodal-streamkit-ops-pipeline). Align modalities, store them, turn them into features, then run every stage together.
- **Search and retrieval:** [00 CLIP](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-00-multimodal-ai-CLIP-claims-pipeline) → [02](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-02-multimodal-feature-store-streambuy) → [03](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-03-multimodal-context-platform) → [06](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-06-multimodal-graph-rag). From one shared vector space to vectors, filters and a graph together.
- **Streaming and real time:** [04](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-04-multimodal-ingestion-pipeline) → [07](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-07-multimodal-inference-router) → [12 bonus](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-12-bonus-multimodal-rca-pipeline). Data that arrives at different speeds, streams with different clocks, then a live factory line.
- **Models in production:** [08](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-08-multimodal-mlops) → [09](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-09-multimodal-scaling-benchmarks) → [10](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-10-multimodal-inference-service) → [11](https://github.com/Data-Engineering-for-Multimodal-AI/playbook-11-multimodal-governance-pipeline). Catch drift, scale, roll out safely, then govern it.

## What every playbook has

- **One command:** `make run` gives a first result. `make setup`, `make smoke` and `make clean` work the same way everywhere.
- **Codespaces:** each repo opens in a ready-to-run GitHub Codespace.
- **Tested every week:** CI runs each playbook on Python 3.12 and 3.13, and inside its Codespace container.
- **The code as printed:** each repo's `first-edition` tag holds the code as it was when the book was published.
- **Room to explore:** numbered "Run it" steps, measured "Try this" experiments, a "Use your own data" adapter and a "Before production" checklist linked to the chapters.

## Contribute

Found a bug or a broken step? Open an issue in that playbook's repo. Looking for somewhere to start? See the [good first issues](https://github.com/search?q=org%3AData-Engineering-for-Multimodal-AI+label%3A%22good+first+issue%22+state%3Aopen&type=issues).

The code is MIT licensed. Sample data keeps its own license; each repo lists it under "Data and licenses".

---

**The Playbooks** · Companion code for *Data Engineering for Multimodal AI* (O'Reilly, 2026)
