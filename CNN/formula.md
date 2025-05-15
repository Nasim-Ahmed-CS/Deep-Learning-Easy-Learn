# 📚 CNN Layer Output Size Formulas with LaTeX (GitHub-Friendly)

This guide explains the formulas used in Convolutional Neural Networks (CNNs) to compute the output dimensions of **Conv2D** and **MaxPool2D** layers. All formulas are LaTeX-compatible and ready for GitHub markdown rendering.

---

## 🧠 1. Convolution Output Size

### 📌 Formula

Let:

- \( H_{in}, W_{in} \): Height and width of input  
- \( K \): Kernel size (assuming square kernel)  
- \( P \): Padding  
- \( S \): Stride

Then the output height and width are:

\[
H_{out} = \left\lfloor \frac{H_{in} + 2P - K}{S} \right\rfloor + 1
\]

\[
W_{out} = \left\lfloor \frac{W_{in} + 2P - K}{S} \right\rfloor + 1
\]

---

### ✅ Example 1: No Padding, Stride 1

- Input: \( 28 \times 28 \)
- Kernel: \( 3 \)
- Padding: \( 0 \)
- Stride: \( 1 \)

\[
H_{out} = \left\lfloor \frac{28 + 0 - 3}{1} \right\rfloor + 1 = 26
\]
\[
W_{out} = 26
\]

**Output size: \( 26 \times 26 \)**

---

### ✅ Example 2: Same Padding, Stride 1

- Input: \( 32 \times 32 \)
- Kernel: \( 3 \)
- Padding: \( 1 \)
- Stride: \( 1 \)

\[
H_{out} = \left\lfloor \frac{32 + 2(1) - 3}{1} \right\rfloor + 1 = 32
\]

**Output size: \( 32 \times 32 \)**

---

## 🔁 2. Pooling Layer (MaxPool2D or AvgPool2D)

### 📌 Formula

Same as Conv2D:

\[
H_{out} = \left\lfloor \frac{H_{in} + 2P - K}{S} \right\rfloor + 1
\]
\[
W_{out} = \left\lfloor \frac{W_{in} + 2P - K}{S} \right\rfloor + 1
\]

---

### ✅ Example 3: MaxPool2D (Kernel 2, Stride 2)

- Input: \( 26 \times 26 \)
- Kernel: \( 2 \)
- Stride: \( 2 \)
- Padding: \( 0 \)

\[
H_{out} = \left\lfloor \frac{26 - 2}{2} \right\rfloor + 1 = 13
\]
\[
W_{out} = 13
\]

**Output size: \( 13 \times 13 \)**

---

## 🔢 3. Layer-by-Layer Example (Mini CNN)

| Layer        | Parameters            | Output Size         |
|--------------|------------------------|----------------------|
| Input        | \(1 \times 28 \times 28\) | \(28 \times 28\)      |
| Conv2D(32)   | \(K=3, P=0, S=1\)        | \(26 \times 26 \times 32\) |
| MaxPool2D    | \(K=2, S=2\)             | \(13 \times 13 \times 32\) |
| Conv2D(64)   | \(K=3, P=0, S=1\)        | \(11 \times 11 \times 64\) |
| MaxPool2D    | \(K=2, S=2\)             | \(5 \times 5 \times 64\)   |
| Flatten      | -                       | \(1600\)              |

---

## 🧮 Optional: Padding for "Same" Output Size

To keep output size same as input:

\[
P = \frac{K - 1}{2}
\]

> Works when \( K \) is odd and \( S = 1 \)

E.g., for \( K = 3 \), then \( P = 1 \)

---

## ✅ Tips

- Use `floor` \( \left\lfloor \cdot \right\rfloor \) to represent integer division (rounding down).
- Convolution affects **spatial dimensions**; filters define **depth (channels)**.
- Use these formulas to compute CNN output sizes step-by-step during model design.

---
