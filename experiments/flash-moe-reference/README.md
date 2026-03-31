# Flash-MoE Reference Experiments

Este directorio contiene adaptaciones de código del proyecto [Flash-MoE](https://github.com/gorroai/flash-moe) de Martin Gorrochategui, utilizadas para experimentar con técnicas de optimización en Evo-2.

## Atribucion

Los scripts originales fueron desarrollados por:

- Martin Gorrochategui Vigoreaux (investigador independiente)
- Claude Code (Anthropic) como asistente de implementacion

Paper asociado:  
Gorrochategui, M. & Claude Code (2026). Beyond the DRAM Wall: Optimizing 397B-Parameter MoE Inference on Apple M5 Max with Analysis of ANE Co-processing Constraints.

Repositorio original: https://github.com/gorroai/flash-moe

## Adaptaciones realizadas

| Script original | Adaptacion | Proposito en Evo-2 |
|-----------------|------------|-------------------|
| repack_experts_q3.py | repack_experts_q3.py | Convertir expertos de Evo-2 a formato GGUF Q3 mixto (IQ3_XXS/IQ4_XS/Q5_K) para reducir tamano y mejorar I/O |
| prepare_ppl_tokens.py | prepare_ppl_tokens.py | Tokenizar dataset de prueba (ej. WikiText-2) para medir perplejidad y validar calidad tras cuantizacion |

## Uso

### 1. Convertir expertos a Q3

python repack_experts_q3.py \
  --model-dir /ruta/al/modelo_mlx \
  --gguf-path /ruta/al/modelo.gguf \
  --output-dir ./expertos_q3 \
  --skip-layers 27

### 2. Preparar tokens para perplejidad

python prepare_ppl_tokens.py \
  --tokenizer /ruta/al/tokenizer.json \
  --input-file wikitext-2.txt \
  --max-tokens 2000 \
  --output ppl_tokens.bin

## Estado

- [ ] Adaptar lectura real de tensores GGUF (requiere llama.cpp o gguf-python)
- [ ] Validar formato de expertos de Evo-2 vs Qwen
- [ ] Ejecutar pruebas de perplejidad con WikiText-2
- [ ] Medir speedup en I/O con los expertos Q3

## Limitaciones actuales

Este repositorio contiene codigo en etapa experimental. Actualmente no contamos con infraestructura de simulacion adecuada para validar completamente estas optimizaciones en Evo-2. Los scripts se proporcionan como punto de partida para quienes tengan acceso a hardware con suficiente VRAM (ej. RTX 3090/4090 con 24GB) y deseen experimentar, y como referencia academica de tecnicas probadas en otros modelos MoE (Qwen3.5-397B) que podrian ser aplicables a Evo-2.

Si tienes acceso a hardware y deseas contribuir con resultados reales (perplejidad, speedup, uso de VRAM), tus pruebas seran bienvenidas en la seccion de Issues o mediante Pull Requests.

Por ahora, este trabajo es teorico/metodologico hasta que podamos ejecutar simulaciones completas.

## Licencia

Los scripts originales estan bajo licencia CC BY-NC 4.0. Esta adaptacion mantiene la misma licencia.
