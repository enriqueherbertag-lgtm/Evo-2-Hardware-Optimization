
---

## 2. `docs/hardware-budget-guide.md` (completo)

```markdown
# Hardware Budget Guide for Evo-2 7B

**How to run Evo-2 7B without breaking the bank.**

This guide focuses on the **7B model**, which is the only version that runs on consumer hardware. For 40B, you need H100 (not covered here).

---

## What Model Can You Run?

| Model | Hardware Required | VRAM | Cost (New) | Cost (Used) |
|-------|-------------------|------|------------|-------------|
| **7B** | RTX 3090 / 4090 | 24 GB | $1,600–1,800 | $700–900 |
| **7B** | A100 (cloud) | 40 GB | $1–2/hour | — |
| **20B** | H100 | 80 GB | $30,000 | — |
| **40B** | H100 cluster | 80 GB+ | $60,000+ | — |

**Conclusion:** The 7B model is the only viable option for budget-conscious labs.

---

## Option 1: Local Workstation (On-Premise)

### Recommended Configuration (Evo-2 7B)

| Component | Recommendation | Cost (New) | Cost (Used) |
|-----------|----------------|------------|-------------|
| **GPU** | RTX 3090 (24 GB) | $1,600 | $700–900 |
| **GPU (alternative)** | RTX 4090 (24 GB) | $1,800 | $1,400–1,600 |
| **CPU** | AMD Ryzen 7 / Intel i7 | $200–300 | $150–200 |
| **RAM** | 64 GB DDR4 | $150 | $100 |
| **Storage** | 1 TB NVMe SSD | $80 | $50 |
| **Power Supply** | 850 W | $100 | $70 |
| **Total (used RTX 3090)** | | | **$1,200–1,500** |

### Why RTX 3090 instead of 4090?

- **24 GB VRAM** (same as 4090)
- **40% cheaper** used ($700–900 vs $1,400+)
- **Sufficient** for 7B inference and fine-tuning with QLoRA

### Important Notes

- **NVMe SSD is mandatory.** HDDs cause massive bottlenecks for loading models and genomic data.
- **64 GB RAM minimum.** The system needs memory for offloading.
- **850 W power supply minimum.** RTX 3090/4090 draw 350–450 W.

---

## Option 2: Cloud GPU Rentals (No Hardware Investment)

If you don't want to buy hardware, rent by the hour:

| Provider | GPU | VRAM | Price/hour | Best for |
|----------|-----|------|------------|---------|
| **Vast.ai** | RTX 3090 | 24 GB | $0.30–0.50 | Cheapest inference |
| **RunPod** | RTX 4090 | 24 GB | $0.50–0.80 | Budget inference |
| **Lambda Labs** | A100 | 40 GB | $1.00–1.50 | 7B fine-tuning |
| **Vast.ai** | A100 | 40 GB | $1.20–1.80 | Fine-tuning |
| **AWS/GCP** | A100/H100 | 40–80 GB | $3.00–5.00 | Enterprise only |

### Cost Examples

| Scenario | Hours | Cost (RunPod) | Cost (Vast.ai) |
|----------|-------|---------------|----------------|
| Inference (7B) | 100 | $50–80 | $30–50 |
| Fine-tuning (7B, QLoRA) | 50 | $40–60 | $25–40 |
| Prototyping | 20 | $10–15 | $6–10 |

---

## Option 3: NVIDIA NIM (Free for Academic Research)

NVIDIA offers NIM microservices for Evo-2. **Free for academic research.**

```bash
# Sign up at NVIDIA NGC (free)
# Pull and run the container
docker run --gpus all -it nvcr.io/nvidia/nim/bionemo/evo2:2.1.0

Requirements:

NVIDIA NGC account (free)

Docker with GPU support

Internet connection

Option 4: Hugging Face API (No GPU Needed)
If you don't have a GPU at all, use the Hugging Face Inference API

import requests

API_URL = "https://api-inference.huggingface.co/models/arcinstitute/evo2-7b"
headers = {"Authorization": "Bearer YOUR_HF_TOKEN"}

def query(dna_sequence):
    response = requests.post(API_URL, headers=headers, json={"inputs": dna_sequence})
    return response.json()

Cost: Free tier includes limited requests.

Comparison Table
Method	Upfront Cost	Hourly Cost	VRAM	Setup Time
Used RTX 3090	$700–900	$0	24 GB	2–4 hours
New RTX 4090	$1,600–1,800	$0	24 GB	2–4 hours
RunPod / Vast.ai	$0	$0.30–0.80	24 GB	5–10 minutes
NVIDIA NIM	$0	$0	—	5 minutes
HF API	$0	$0	—	1 minute
Summary
Budget	Recommended Setup
$0	NVIDIA NIM (free research tier) or Hugging Face API
$20–50	Cloud rental (Vast.ai, RunPod) for short experiments
$100–200	Cloud rental for longer projects (200–300 hours)
$1,200–1,500	Local workstation with used RTX 3090 + NVMe SSD
$30,000+	H100 for 40B models (not covered here)
Next Steps
For cloud users: Sign up at Vast.ai or RunPod, launch an RTX 3090 instance.

For local builders: Buy a used RTX 3090, 64 GB RAM, NVMe SSD.

For researchers: Apply for NVIDIA NIM free access.

*"Evo-2 7B is accessible. You don't need a $30,000 H100 to get started."*


