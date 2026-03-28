# Evo-2 Hardware Optimization

“Este repositorio es un análisis técnico basado en benchmarks oficiales de NVIDIA y reportes de la comunidad. No incluye benchmarks propios ni código ejecutable todavía.”

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

**Making Evo-2 7B accessible on consumer GPUs. Honest analysis, real benchmarks, and practical limitations.**

Evo-2 is a groundbreaking genomic AI from Arc Institute. While the 40B model requires enterprise GPUs (H100), the **7B model runs on consumer hardware** (RTX 4090/3090). This project analyzes what actually works, what doesn't, and where the real opportunities lie.

---

## Quick Summary

| Question | Answer |
|----------|--------|
| **Can RTX 4090 run Evo-2?** | ✅ Yes, the **7B model** runs on a single RTX 4090 (22 GB VRAM). |
| **Can RTX 3090 run Evo-2?** | ✅ Yes, the 7B model runs on RTX 3090 (24 GB VRAM). |
| **Can RTX 4090 run 40B?** | ❌ No. Requires FP8 (H100/H200 only). |
| **What's the cost difference?** | 1× RTX 3090 (used) = $700–900 vs 1× H100 = $30,000. **30× cheaper**. |
| **Performance difference?** | H100: 45 nt/sec. RTX 4090/3090: estimated 30–40 nt/sec. |

---

## Budget Guide: Running Evo-2 7B on a Budget

You don't need a $30,000 H100 to run Evo-2. Here are realistic options:

| Budget | Recommended Setup |
|--------|-------------------|
| **$0** | NVIDIA NIM (free research) or Hugging Face API |
| **$20–50** | Cloud rental (Vast.ai, RunPod) |
| **$1,200–1,500** | Local workstation with used RTX 3090 + NVMe SSD |

For detailed hardware recommendations, see the [Hardware Budget Guide](docs/hardware-budget-guide.md).

### Quick Cloud Setup (Cheapest)

```bash
# 1. Sign up at Vast.ai (no upfront cost)
# 2. Rent an RTX 3090 instance (~$0.40/hour)
# 3. Run the model with vLLM
pip install vllm
python -m vllm.entrypoints.openai.api_server --model arcinstitute/evo2-7b


### Quick Local Setup (Used RTX 3090)

| Component | Used Price |
|-----------|------------|
| RTX 3090 (24 GB) | $700–900 |
| 64 GB RAM | $100 |
| 1 TB NVMe SSD | $50 |
| **Total** | **$850–1,050** |


## Why This Matters

| Hardware | Cost | Model Support | Who Can Use It |
|----------|------|---------------|----------------|
| H100 | $30,000+ | 40B, 20B, 7B | Well-funded labs, industry |
| RTX 4090 | $1,800 | **7B only** | Universities, researchers, students |
| RTX 3090 (used) | $700–900 | **7B only** | Budget-conscious labs, students |

**Goal:** Democratize genomic AI by identifying what actually works on accessible hardware.

---

## Official Benchmarks (NVIDIA NIM)

Real-world performance data from NVIDIA:

| Model | GPU | Configuration | Throughput (nt/sec) |
|-------|-----|---------------|---------------------|
| 40B | H200 (141 GB) | 1 GPU, 4096 nt | 33 |
| 40B | H100 (80 GB) | 2 GPUs, 512 nt | 26 |
| 7B | H200 (141 GB) | 1 GPU, 8192 nt | 52 |
| 7B | H100 (80 GB) | 1 GPU, 8192 nt | 45 |

**Source:** [NVIDIA NIM Documentation](https://docs.nvidia.com/nim/bionemo/evo2/2.1.0/benchmarking.html)

---

## RTX 3090/4090 Real-World Performance

Community testing confirms:

- **Evo-2 7B runs on a single RTX 3090/4090** (24 GB VRAM) using ~22 GB
- **No FP8 required** for the 7B model
- **Multi-GPU scaling** is possible with proper software

**Source:** [GitCode Community Testing](https://blog.gitcode.com/7a533d8a2818670ad0736ff4b675253b.html)

---

## Memory Requirements (Real Data)

| Model | FP8 Required | VRAM (FP8) | VRAM (FP16) | Runs on RTX 3090/4090? |
|-------|--------------|------------|-------------|----------------------|
| 7B | ❌ No | — | 22 GB | ✅ Yes |
| 20B | ✅ Yes | ~20 GB | 40 GB | ❌ No |
| 40B | ✅ Yes | ~40 GB | 80 GB | ❌ No |

**Key insight:** The 7B model is the sweet spot for consumer hardware. Larger models require enterprise GPUs with FP8 support.

---

## Performance Estimates (7B Model Only)

| Hardware | Speed | Confidence |
|----------|-------|------------|
| 1× H100 | 45 nt/sec | ✅ Verified (NVIDIA) |
| 1× RTX 4090 | 30–40 nt/sec | 🔲 Community reports |
| 1× RTX 3090 | 25–35 nt/sec | 🔲 Estimated |

**Note:** RTX 3090/4090 lack NVLink, which affects multi-GPU scaling. Estimates assume proper software optimization.

---

## Hardware Guide (For 7B Inference)

| Component | Recommendation (New) | Recommendation (Used) |
|-----------|---------------------|---------------------|
| **GPU** | RTX 4090 (24 GB) | RTX 3090 (24 GB) |
| **CPU** | Any modern processor | Any modern processor |
| **RAM** | 64 GB DDR5 | 64 GB DDR4 |
| **Storage** | 1 TB NVMe SSD | 1 TB NVMe SSD |
| **Power Supply** | 850 W | 850 W |
| **Total Cost** | $2,300–2,500 | $1,200–1,500 |


## What Works, What Doesn't

### ✅ Works on RTX 3090/4090

- **Evo-2 7B inference** (single GPU, ~22 GB VRAM)
- **Fine-tuning with QLoRA** (4-bit quantization)
- **Prototyping and research** for most genomic AI tasks
- **Educational use** (students, labs with limited budgets)

### ❌ Does NOT Work on RTX 3090/4090

- **Evo-2 40B, 20B, or 1B** (require FP8, H100/H200)
- **Production-scale fine-tuning** for large models
- **Low-latency applications** (H100 has better latency)
- **Any model requiring FP8** (RTX lacks hardware support)

---

## Conclusion

### Key Findings

1. **Evo-2 7B runs on consumer hardware**  
   - Single RTX 3090/4090 (24 GB) is sufficient
   - Estimated 30–40 nt/sec (vs 45 nt/sec on H100)
   - 30× cheaper with used RTX 3090 ($700–900 vs $30,000)

2. **Larger models (40B, 20B) are not accessible**  
   - Require FP8 hardware (H100/H200 only)
   - No consumer GPU alternative exists

3. **Cost-performance ratio favors RTX 3090 for 7B**  
   - $700–900 (used) vs $30,000 for H100
   - 70% of performance at 2–3% of the cost

4. **Not a replacement for enterprise**  
   - RTX 3090/4090 is ideal for research, education, and prototyping
   - H100 remains necessary for production and large models

### Call to Action

This analysis is based on:
- Official NVIDIA benchmarks
- Community testing
- Open-source software

We invite the community to:

- **Validate** these estimates with real-world tests
- **Share** benchmarks on consumer hardware
- **Contribute** installation guides and Docker images

---

## Next Steps: From Analysis to Edge AI

This analysis is the first step toward running genomic AI on **edge hardware**. The next phase involves:

1. **Porting Evo-2 7B to ARM-based systems** (like CORPUS)
2. **Optimizing power consumption** for autonomous operation
3. **Integrating with sensors and actuators** for embodied AI

See [CORPUS](https://github.com/enriqueherbertag-lgtm/Corpus) for hardware architecture and specs.

---

## Limitations

For a detailed discussion of limitations, see [docs/limitations.md](docs/limitations.md).

**Key limitations:**
- 40B models cannot run on RTX 3090/4090
- No NVLink affects multi-GPU scaling
- Power and cooling requirements are substantial
- Software setup requires technical expertise
- Performance estimates need real-world validation

---

## License

CC BY-NC 4.0 (Attribution-NonCommercial 4.0 International)

This project is for non‑commercial use. Commercial use requires a separate agreement.

---

## Author

**Enrique Aguayo H.**  
Mackiber Labs  
Contact: eaguayo@migst.cl  
ORCID: 0009-0004-4615-6825  
GitHub: [@enriqueherbertag-lgtm](https://github.com/enriqueherbertag-lgtm)

---

*"Evo-2 7B is accessible. You don't need a $30,000 H100 to get started."*
