"""
Performance model for Evo-2 on consumer GPUs
Estimates tokens/second based on hardware configuration
"""

import numpy as np
import matplotlib.pyplot as plt

def estimate_performance(gpu_count, gpu_type, quantization, model_size):
    """
    Estimate inference speed for Evo-2 models
    
    Parameters:
    - gpu_count: number of GPUs (1-8)
    - gpu_type: 'h100' or 'rtx4090'
    - quantization: 'fp16', 'int8', '4bit'
    - model_size: '7b', '20b', '40b'
    
    Returns:
    - tokens_per_second (estimated)
    """
    
    # Base performance (single H100, FP16, 7B model)
    base_tps = {
        '7b': 400,
        '20b': 150,
        '40b': 60
    }
    
    # GPU scaling factors
    gpu_factor = {
        'h100': 1.0,
        'rtx4090': 0.33  # based on FP16 TFLOPS ratio
    }
    
    # Quantization factors (reduced memory, increased speed)
    quant_factor = {
        'fp16': 1.0,
        'int8': 1.2,
        '4bit': 1.3
    }
    
    # Scaling with multiple GPUs (tensor parallelism)
    multi_gpu_factor = {
        1: 1.0,
        2: 1.8,
        4: 3.2,
        8: 5.5
    }
    
    # Penalty for lack of NVLink (RTX series)
    nvlink_penalty = 0.8 if gpu_type == 'rtx4090' else 1.0
    
    tps = base_tps[model_size] * gpu_factor[gpu_type] * quant_factor[quantization]
    tps *= multi_gpu_factor.get(gpu_count, 1.0) * nvlink_penalty
    
    return tps

# Example calculations
configs = [
    (1, 'h100', 'fp16', '40b'),
    (4, 'rtx4090', 'fp16', '40b'),
    (4, 'rtx4090', 'int8', '40b'),
]

print("Estimated tokens/second for Evo-2 40B:\n")
for gpu_count, gpu_type, quantization, model_size in configs:
    tps = estimate_performance(gpu_count, gpu_type, quantization, model_size)
    print(f"{gpu_count}× {gpu_type.upper()} ({quantization.upper()}): {tps:.1f} t/s")

# Plot comparison
configs = ['1× H100 (FP16)', '4× RTX 4090 (FP16)', '4× RTX 4090 (INT8)']
tps_values = [
    estimate_performance(1, 'h100', 'fp16', '40b'),
    estimate_performance(4, 'rtx4090', 'fp16', '40b'),
    estimate_performance(4, 'rtx4090', 'int8', '40b')
]

plt.figure(figsize=(8, 5))
plt.bar(configs, tps_values, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.ylabel('Tokens per second (estimated)')
plt.title('Evo-2 40B Performance Comparison')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('performance_comparison.png', dpi=150)
plt.show()
