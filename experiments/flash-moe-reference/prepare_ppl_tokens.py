#!/usr/bin/env python3
"""
Adaptación de prepare_ppl_tokens.py de gorroai/flash-moe
Tokeniza un archivo de texto (ej. WikiText-2) para evaluar perplejidad.

Uso:
    python prepare_ppl_tokens.py --tokenizer ./tokenizer.json --max-tokens 2000 --output ppl_tokens.bin

Créditos:
    Original: Martin Gorrochategui & Claude Code (2026)
    Repo: https://github.com/gorroai/flash-moe
"""

import argparse
import json
import struct
import sys
from pathlib import Path

def load_tokenizer(tokenizer_path):
    """Carga el tokenizer desde tokenizer.json (formato HuggingFace)"""
    import json
    with open(tokenizer_path, 'r') as f:
        data = json.load(f)
    
    # Extraer el modelo de tokenizador (asume BPE con vocab)
    vocab = data.get("model", {}).get("vocab", {})
    if not vocab:
        # Fallback: buscar en la raíz
        vocab = data.get("vocab", {})
    
    # Construir mapeo token -> id
    token_to_id = vocab
    return token_to_id

def tokenize_text(text, tokenizer):
    """
    Tokeniza un texto usando el tokenizer cargado.
    Esta es una versión simplificada; para un uso real se necesita
    el algoritmo BPE completo.
    """
    # Stub: en producción usar la lógica real del tokenizer
    # Por ahora, asume que el texto viene con espacios separando tokens
    # Esto es solo para demostración
    tokens = []
    for word in text.split():
        token_id = tokenizer.get(word)
        if token_id is not None:
            tokens.append(token_id)
    return tokens

def main():
    parser = argparse.ArgumentParser(description="Prepare tokens for perplexity evaluation")
    parser.add_argument("--tokenizer", required=True, help="Ruta a tokenizer.json")
    parser.add_argument("--input-text", help="Texto a tokenizar (alternativa a --input-file)")
    parser.add_argument("--input-file", help="Archivo de texto a tokenizar")
    parser.add_argument("--max-tokens", type=int, default=2000, help="Máximo número de tokens a generar")
    parser.add_argument("--output", required=True, help="Archivo binario de salida")
    args = parser.parse_args()
    
    # Cargar tokenizer
    print("Cargando tokenizer...")
    tokenizer = load_tokenizer(args.tokenizer)
    
    # Obtener texto
    if args.input_text:
        text = args.input_text
    elif args.input_file:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            text = f.read()
    else:
        print("Error: especificar --input-text o --input-file")
        sys.exit(1)
    
    # Tokenizar
    print("Tokenizando...")
    tokens = tokenize_text(text, tokenizer)
    
    # Limitar a max_tokens
    if len(tokens) > args.max_tokens:
        tokens = tokens[:args.max_tokens]
    
    # Guardar en formato binario (lista de int32)
    print(f"Guardando {len(tokens)} tokens en {args.output}")
    with open(args.output, 'wb') as f:
        f.write(struct.pack('i', len(tokens)))
        for token in tokens:
            f.write(struct.pack('i', token))
    
    print("Listo.")

if __name__ == "__main__":
    main()
