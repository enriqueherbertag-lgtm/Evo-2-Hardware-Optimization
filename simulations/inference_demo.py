#!/usr/bin/env python3
"""
Evo-2 7B Inference Demo on RTX 4090
Requires: torch, transformers, accelerate, bitsandbytes, flash-attn
"""

import torch
import time
import psutil
from transformers import AutoModelForCausalLM, AutoTokenizer

def format_memory(bytes):
    """Convert bytes to GB"""
    return f"{bytes / 1e9:.1f} GB"

def main():
    print("=" * 60)
    print("Evo-2 7B Inference Demo")
    print("=" * 60)
    
    # Check CUDA
    if not torch.cuda.is_available():
        print("❌ CUDA not available. This script requires an NVIDIA GPU.")
        return
    
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM total: {format_memory(torch.cuda.get_device_properties(0).total_memory)}")
    print()
    
    # Model name (adjust if official repo has different name)
    model_name = "arcinstitute/evo2-7b"
    
    print("Loading model with 4-bit quantization...")
    start = time.time()
    
    try:
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            load_in_4bit=True,
            torch_dtype=torch.float16,
            trust_remote_code=True
        )
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("Make sure you have access to the model and are logged into Hugging Face.")
        return
    
    load_time = time.time() - start
    vram_used = torch.cuda.memory_allocated()
    print(f"✅ Model loaded in {load_time:.1f}s")
    print(f"VRAM used: {format_memory(vram_used)}")
    print()
    
    # Test sequences
    sequences = [
        ("Short DNA", "ATGCATGCATGCATGCATGCATGCATGCATGC"),
        ("Medium DNA", "ATGC" * 50),
        ("Long DNA", "ATGC" * 200),
    ]
    
    print("-" * 60)
    print("Running inference...")
    print("-" * 60)
    
    for name, seq in sequences:
        print(f"\n{name} ({len(seq)} nt):")
        print(f"  Sequence: {seq[:50]}..." if len(seq) > 50 else f"  Sequence: {seq}")
        
        inputs = tokenizer(seq, return_tensors="pt").to("cuda")
        
        # Warm-up
        with torch.no_grad():
            _ = model.generate(**inputs, max_new_tokens=10)
        
        torch.cuda.synchronize()
        start = time.time()
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=100,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id
            )
        
        torch.cuda.synchronize()
        gen_time = time.time() - start
        
        generated = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)
        nt_count = len(generated)
        nt_per_sec = nt_count / gen_time
        
        print(f"  Generated {nt_count} nt in {gen_time:.2f}s")
        print(f"  Speed: {nt_per_sec:.1f} nt/sec")
        print(f"  Output: {generated[:100]}..." if len(generated) > 100 else f"  Output: {generated}")
    
    print("\n" + "=" * 60)
    print("Demo complete.")
    print(f"Peak VRAM: {format_memory(torch.cuda.max_memory_allocated())}")
    print("=" * 60)

if __name__ == "__main__":
    main()
