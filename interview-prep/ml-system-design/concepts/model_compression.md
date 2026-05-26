# Model Compression

Techniques to make ML models smaller, faster, and cheaper to serve — without drastically sacrificing accuracy.

---

## Why It Matters

A model trained for accuracy is often too large/slow for production:
- A 70B parameter LLM can't serve 1000 QPS on a single GPU.
- A ResNet-50 might be overkill for a mobile app.
- 200ms inference latency breaks the user experience.

Compression bridges the gap between research-quality models and production constraints.

---

## Techniques

### Quantization
Reduce the numeric precision of weights and activations.

| Precision | Bits | Memory vs FP32 | Speed |
|---|---|---|---|
| FP32 | 32 | 1x (baseline) | Baseline |
| FP16 / BF16 | 16 | 0.5x | ~2x faster |
| INT8 | 8 | 0.25x | ~3–4x faster |
| INT4 | 4 | 0.125x | ~6–8x faster |

- **Post-training quantization (PTQ)**: quantize after training, no retraining needed. Fast to apply, small accuracy loss.
- **Quantization-aware training (QAT)**: simulate quantization during training. Better accuracy, requires retraining.

Most commonly used technique in production. LLMs routinely run at 4-bit or 8-bit.

### Pruning
Remove weights (or entire neurons/attention heads) that contribute little to the output.

- **Unstructured pruning**: zero out individual weights. Creates sparse matrices — hard to speed up on standard hardware.
- **Structured pruning**: remove entire filters, layers, or attention heads. More hardware-friendly.

Typically requires fine-tuning after pruning to recover accuracy.

### Knowledge Distillation
Train a smaller **student** model to mimic the outputs of a larger **teacher** model.

```
Teacher (large, accurate) → generates soft labels
Student (small, fast) → trained on teacher's soft labels
```

Student learns to approximate the teacher's behavior, not just the hard ground-truth labels.
Used to create: DistilBERT (40% smaller than BERT), TinyBERT, smaller recommendation models.

### Layer Sharing / Weight Tying
Reuse the same weights across multiple layers (e.g., ALBERT ties weights across transformer layers).
Reduces parameter count without reducing depth.

### Low-Rank Factorization (LoRA, SVD)
Approximate a large weight matrix as the product of two smaller matrices.
- **LoRA** (Low-Rank Adaptation): popular for fine-tuning LLMs efficiently.
- Reduces trainable parameters during fine-tuning; original weights unchanged.

---

## Serving Optimizations (Not Compression, but Related)

| Technique | What It Does |
|---|---|
| **ONNX / TensorRT** | Compile model to optimized hardware-specific format |
| **Batching** | Process multiple requests together; higher GPU utilization |
| **Model caching** | Keep model loaded in GPU memory between requests |
| **Speculative decoding** | Use a small draft model + large model for faster LLM inference |

---

## Choosing a Technique

| Constraint | Start With |
|---|---|
| Latency too high | Quantization (INT8), TensorRT |
| Memory too large | Quantization (INT4/INT8), pruning |
| Need a smaller deployable model | Distillation |
| Fine-tuning a large model cheaply | LoRA |

---

## Trade-offs

| Quantization | Easy to apply, big gains | Small accuracy loss at aggressive levels |
| Pruning | Can be very effective | Requires careful tuning; unstructured pruning is hard to accelerate |
| Distillation | Strong accuracy retention | Requires training the student model |
| LoRA | Cheap fine-tuning | Only addresses fine-tuning cost, not base model serving cost |
