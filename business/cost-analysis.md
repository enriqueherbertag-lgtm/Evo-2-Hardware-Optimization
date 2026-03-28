# Cost Analysis: H100 vs RTX 4090 for Evo-2 7B

## Hardware Costs (7B Inference Setup)

| Component | H100 Solution | RTX 4090 Solution |
|-----------|---------------|-------------------|
| GPU | 1× H100 ($30,000) | 1× RTX 4090 ($1,800) |
| Motherboard | $5,000 | $300 |
| Power supply | $2,000 | $120 |
| Cooling | $3,000 | $100 |
| RAM | $2,000 | $100 |
| Storage | $2,000 | $80 |
| **Total** | **~$44,000** | **~$2,500** |

## Operating Costs (per year)

| Item | H100 | RTX 4090 |
|------|------|----------|
| Power (kW) | 0.35 kW | 0.45 kW |
| Energy cost (0.15 USD/kWh) | $460 | $590 |
| Cooling | $500 | $100 |
| **Total annual** | **$960** | **$690** |

## TCO (Total Cost of Ownership, 5 years)

| Item | H100 | RTX 4090 |
|------|------|----------|
| Hardware | $44,000 | $2,500 |
| Operating (5 years) | $4,800 | $3,450 |
| **Total** | **$48,800** | **$5,950** |

## Performance per Dollar (7B Inference)

| Metric | H100 | RTX 4090 (est.) |
|--------|------|-----------------|
| Performance (nt/sec) | 45 | 35 |
| Cost (TCO, 5 years) | $48,800 | $5,950 |
| **nt/sec per $1,000** | **0.92** | **5.88** |

**Conclusion:** The RTX 4090 delivers **6.4× more performance per dollar** than H100 for Evo-2 7B inference.

---

## Use Cases

| Scenario | Best Solution |
|----------|---------------|
| Production 40B training | H100 |
| Research with 7B | RTX 4090 |
| Education | RTX 4090 |
| Prototyping | RTX 4090 |
| Large-scale fine-tuning (7B) | 4× RTX 4090 |

---

**Note:** This analysis is for the **7B model only**. Larger models (40B, 20B) require H100 and are not comparable.
