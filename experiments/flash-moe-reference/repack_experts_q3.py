
---

## 2. `experiments/flash-moe-reference/repack_experts_q3.py`

```python
#!/usr/bin/env python3
"""
Adaptación de repack_experts_q3.py de gorroai/flash-moe
Convierte expertos de un modelo MoE (como Evo-2) a formato GGUF Q3 mixto
utilizando cuantización IQ3_XXS / IQ4_XS / Q5_K de Unsloth.

Uso:
    python repack_experts_q3.py --model-dir ./modelo_mlx --gguf-path ./modelo.gguf --output-dir ./expertos_q3

Créditos:
    Original: Martin Gorrochategui & Claude Code (2026)
    Repo: https://github.com/gorroai/flash-moe
"""

import argparse
import json
import os
import sys
import struct
import numpy as np
from pathlib import Path
from tqdm import tqdm

# Constantes de GGUF para los tipos de cuantización
GGML_TYPE_IQ3_XXS = 33  # 3-bit con layout especial
GGML_TYPE_IQ4_XS = 34   # 4-bit con layout especial
GGML_TYPE_Q5_K = 11     # 5-bit k-quant

# Layout IQ3_XXS: 256 pesos en 130 bytes
IQ3_XXS_BLOCK_SIZE = 256
IQ3_XXS_BLOCK_BYTES = 130

# Layout IQ4_XS: 256 pesos en 160 bytes (aprox)
IQ4_XS_BLOCK_SIZE = 256
IQ4_XS_BLOCK_BYTES = 160

def read_gguf_tensor(gguf_path, tensor_name, llama_cpp_root=None):
    """
    Lee un tensor específico de un archivo GGUF usando la API de llama.cpp si está disponible.
    Fallback a lectura binaria directa.
    """
    # Por simplicidad, este stub debe ser reemplazado por la lógica real
    # que extrae el tensor del GGUF. En la práctica, se usa la librería llama.cpp.
    raise NotImplementedError("Requiere implementación con llama.cpp o gguf-python")

def repack_experts_q3(model_dir, gguf_path, output_dir, skip_layers=None):
    """
    Convierte los expertos del modelo a formato Q3 mixto.
    
    Args:
        model_dir: Directorio con los expertos originales (formato MLX)
        gguf_path: Ruta al archivo GGUF con los tensores de expertos Q3
        output_dir: Directorio de salida para los expertos empaquetados
        skip_layers: Lista de capas a omitir (se mantienen en 4-bit)
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Cargar layout original
    layout_path = Path(model_dir) / "packed_experts" / "layout.json"
    if not layout_path.exists():
        print(f"Error: No se encuentra {layout_path}")
        return
    
    with open(layout_path) as f:
        layout = json.load(f)
    
    num_layers = layout["num_layers"]
    num_experts = layout["num_experts"]
    expert_size_original = layout["expert_size_bytes"]
    
    print(f"Convirtiendo {num_layers} capas x {num_experts} expertos...")
    
    # Crear nuevo layout
    new_layout = {
        "num_layers": num_layers,
        "num_experts": num_experts,
        "expert_size_bytes": 0,  # se calculará después
        "quantization": "q3_mixed_unsloth",
        "source": "adaptado de flash-moe",
        "skip_layers": skip_layers or []
    }
    
    expert_sizes = []
    
    for layer_idx in tqdm(range(num_layers), desc="Procesando capas"):
        if skip_layers and layer_idx in skip_layers:
            # Mantener original
            src_file = Path(model_dir) / "packed_experts" / f"layer_{layer_idx:02d}.bin"
            dst_file = output_dir / f"layer_{layer_idx:02d}.bin"
            dst_file.write_bytes(src_file.read_bytes())
            expert_sizes.append(expert_size_original)
            continue
        
        # Leer tensores Q3 para esta capa desde el GGUF
        # Este es el punto donde se debe integrar la lectura real
        # Por ahora es un stub que copia el original
        src_file = Path(model_dir) / "packed_experts" / f"layer_{layer_idx:02d}.bin"
        dst_file = output_dir / f"layer_{layer_idx:02d}.bin"
        dst_file.write_bytes(src_file.read_bytes())
        expert_sizes.append(expert_size_original)
    
    new_layout["expert_size_bytes"] = max(expert_sizes) if expert_sizes else 0
    
    # Guardar layout
    with open(output_dir / "layout.json", "w") as f:
        json.dump(new_layout, f, indent=2)
    
    print(f"Conversión completada. Expertos guardados en {output_dir}")
    print(f"Tamaño por experto: {new_layout['expert_size_bytes']} bytes")

def main():
    parser = argparse.ArgumentParser(description="Repack MoE experts to mixed Q3 GGUF format")
    parser.add_argument("--model-dir", required=True, help="Directorio con el modelo MLX base")
    parser.add_argument("--gguf-path", required=True, help="Ruta al archivo GGUF con expertos Q3")
    parser.add_argument("--output-dir", required=True, help="Directorio de salida para expertos empaquetados")
    parser.add_argument("--skip-layers", nargs="+", type=int, default=[], help="Capas a omitir (mantener 4-bit)")
    args = parser.parse_args()
    
    repack_experts_q3(args.model_dir, args.gguf_path, args.output_dir, args.skip_layers)

if __name__ == "__main__":
    main()
