# 👻 GhostText — Zero-Width Text Mutator

**GhostText** is a powerful yet lightweight Python tool that invisibly alters text by inserting **zero-width characters**.  
This allows you to create strings that *look identical* to humans—but differ at the byte level—making it useful for **bypassing duplicate-text detectors**, watermarking, fingerprinting, and subtle text mutation.

---

## 🌟 Features

- ✅ Add invisible **zero-width Unicode characters**  
- ✅ Remove zero-width characters and clean your text  
- ✅ CLI with subcommands: 'add' and 'remove'  
- ✅ Supports text input or file input  
- ✅ Adjustable randomness: probability, run length, seeding  
- ✅ '--fast' mode for simpler, quicker mutation  
- ✅ '--no-whitespace-skip' to allow insertion everywhere  
- ✅ Fully cross-platform (Windows, macOS, Linux)

---

## 📦 Installation

Clone the repo:

```
git clone https://github.com/Sententional/GhostText.git
cd GhostText
```

Run directly with Python:

```
python3 ghosttext.py add "Hello world"
```

---

## 🧩 Usage

GhostText has **two commands**:

### ➕ Add zero-width characters

```
python3 ghosttext.py add "hello world"
```

With file input:

```
python3 ghosttext.py add --input input.txt --output output.txt
```

Advanced options:

```
python3 ghosttext.py add \
  --input text.txt \
  --output mutated.txt \
  --min-prob 0.2 \
  --max-prob 0.6 \
  --max-run 4 \
  --fast \
  --seed 1337
```

### ➖ Remove zero-width characters

```
python3 ghosttext.py remove "text"
```

With file input/output:

```
python3 ghosttext.py remove --input encoded.txt --output clean.txt
```

---

## ⚙️ Options Overview

| Option                      | Description                      |
|-----------------------------|----------------------------------|
| '--input <file>'            | Read text from a file            |
| '--output <file>'           | Save result to a file            |
| '--seed <n>'                | Reproducible randomness          |
| '--min-prob' / '--max-prob' | Control insertion chance         |
| '--max-run'                 | Maximum characters per insertion |
| '--fast'                    | Faster mode (single-char runs)   |
| '--no-whitespace-skip'      | Allow insertion after whitespace |

---

## 🧪 Example Flow

1. You pass a string or a file into GhostText.  
2. The tool inserts tiny, invisible Unicode characters at random positions.  
3. The text appears **100% identical** to humans.  
4. Duplicate-text scanners and matching systems see the content as **different**.  
5. 'remove' can fully restore the original text by stripping all hidden characters.

---

## 🔒 Safety & Policy Notes

GhostText is provided **for educational, research, and watermarking purposes only**.  
If you intend to bypass content-matching systems, ensure you comply with relevant **terms of service** and **legal requirements**.

Use responsibly.

---

## 🪪 License

This project is licensed under the **MIT License**, permitting personal and commercial use.  
See **[LICENSE](LICENSE)** for details.

---
