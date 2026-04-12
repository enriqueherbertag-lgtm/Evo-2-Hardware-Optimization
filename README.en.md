# Evo-2 7B on your GPU: Genomic AI for under USD 1,000

[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![ES](https://img.shields.io/badge/Spanish-version-green.svg)](./README.md)

**Why spend USD 30,000 on an H100 when you can run Evo-2 7B on a used RTX 3090 for USD 700–900?**

This repository is a technical analysis based on official NVIDIA benchmarks and community reports. It does not include proprietary benchmarks or executable code yet.

## What problem does it solve?

Evo-2 is a revolutionary genomic AI model. The 40B version requires enterprise H100 GPUs (USD 30,000+). But the **7B version runs on consumer hardware**.

**This project demonstrates that you don't need an H100 to research genomic AI.**

## Which GPU do I need?

| GPU | VRAM | Runs Evo-2 7B? | Cost (used) |
|-----|------|----------------|---------------|
| RTX 3090 | 24 GB | ✅ Yes | USD 700–900 |
| RTX 4090 | 24 GB | ✅ Yes | USD 1,200–1,500 |
| H100 | 80 GB | ✅ 40B, 20B, 7B | USD 30,000+ |

## What speed can I expect?

| Hardware | Speed (nt/sec) | Confidence |
|----------|-------------------|-----------|
| H100 | 45 | ✅ Verified (NVIDIA) |
| RTX 4090 | 30–40 | 🔲 Community reports |
| RTX 3090 | 25–35 | 🔲 Estimated |

## How much does a local setup cost?

| Component | Price (used) |
|------------|----------------|
| RTX 3090 (24 GB) | USD 700–900 |
| 64 GB RAM | USD 100 |
| 1 TB NVMe SSD | USD 50 |
| **Total** | **USD 850–1,050** |

## What does NOT run on RTX 3090/4090?

- ❌ Evo-2 40B, 20B, 1B (require FP8, H100/H200)
- ❌ Production-scale fine-tuning
- ❌ Low-latency applications

## Who is it for?

- Budget-constrained labs.
- Universities and research centers.
- Students wanting to experiment with genomic AI.
- Anyone who wants to run Evo-2 without spending USD 30,000.

## Next steps

1. Port Evo-2 7B to ARM systems (like CORPUS).
2. Optimize power consumption for autonomous operation.
3. Integrate with sensors and actuators for embedded AI.

See [CORPUS](https://github.com/enriqueherbertag-lgtm/Corpus) for hardware architecture and specs.

## Experiments

The `experiments/` folder contains third-party code adaptations and proof-of-concept tests. See `experiments/flash-moe-reference/README.md` for details.

## License

Copyright © 2026 Enrique Aguayo. All rights reserved.

This project is protected by copyright.

**PERMITTED:**
- Non-commercial use for educational or research purposes.
- Distribution without modification, as long as this license is maintained and credit is given to the author.

**PROHIBITED without express written authorization:**
- Commercial use (including offering it as a service, SaaS, subscription, or any use that generates economic benefit).
- Modification for production environments.
- Distribution of modified versions without authorization.

For commercial licenses or inquiries, contact: **eaguayo@migst.cl**

## Author

**Enrique Aguayo H.** – Mackiber Labs
