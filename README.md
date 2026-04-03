# Evo-2 7B en tu GPU: IA genómica por menos de USD 1,000

[![License](https://img.shields.io/badge/License-Proprietary-red.svg)](LICENSE)
[![EN](https://img.shields.io/badge/English-version-blue.svg)](./README.en.md)

**¿Por qué gastar USD 30,000 en una H100 si puedes correr Evo-2 7B en una RTX 3090 usada por USD 700–900?**

Este repositorio es un análisis técnico basado en benchmarks oficiales de NVIDIA y reportes de la comunidad. No incluye benchmarks propios ni código ejecutable todavía.

## ¿Qué problema resuelve?

Evo-2 es un modelo de IA genómica revolucionario. La versión 40B requiere GPUs empresariales H100 (USD 30,000+). Pero la versión **7B corre en hardware de consumo**.

**Este proyecto demuestra que no necesitas una H100 para investigar con IA genómica.**

## ¿Qué GPU necesito?

| GPU | VRAM | Corre Evo-2 7B? | Costo (usado) |
|-----|------|----------------|---------------|
| RTX 3090 | 24 GB | ✅ Sí | USD 700–900 |
| RTX 4090 | 24 GB | ✅ Sí | USD 1,200–1,500 |
| H100 | 80 GB | ✅ 40B, 20B, 7B | USD 30,000+ |

## ¿Qué velocidad esperar?

| Hardware | Velocidad (nt/sec) | Confianza |
|----------|-------------------|-----------|
| H100 | 45 | ✅ Verificado (NVIDIA) |
| RTX 4090 | 30–40 | 🔲 Reportes comunitarios |
| RTX 3090 | 25–35 | 🔲 Estimado |

## ¿Cuánto cuesta un equipo local?

| Componente | Precio (usado) |
|------------|----------------|
| RTX 3090 (24 GB) | USD 700–900 |
| 64 GB RAM | USD 100 |
| 1 TB NVMe SSD | USD 50 |
| **Total** | **USD 850–1,050** |

## ¿Qué NO corre en RTX 3090/4090?

- ❌ Evo-2 40B, 20B, 1B (requieren FP8, H100/H200)
- ❌ Fine-tuning a escala de producción
- ❌ Aplicaciones de baja latencia

## ¿Para quién es?

- Laboratorios con poco presupuesto.
- Universidades y centros de investigación.
- Estudiantes que quieren experimentar con IA genómica.
- Cualquier persona que quiera correr Evo-2 sin gastar USD 30,000.

## Próximos pasos

1. Portar Evo-2 7B a sistemas ARM (como CORPUS).
2. Optimizar consumo energético para operación autónoma.
3. Integrar con sensores y actuadores para IA embebida.

Ver [CORPUS](https://github.com/enriqueherbertag-lgtm/Corpus) para arquitectura y especificaciones.

## Experimentos

En la carpeta `experiments/` se encuentran adaptaciones de código de terceros y pruebas de concepto. Ver `experiments/flash-moe-reference/README.md` para detalles.

## Licencia

Copyright © 2026 Enrique Aguayo. Todos los derechos reservados.

## Autor

Enrique Aguayo H. – Mackiber Labs
