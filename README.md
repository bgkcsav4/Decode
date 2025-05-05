# Decode

A concise **Python 3** utility that converts so‑called **“XKCD Roman numerals”** back into ordinary integers and picks the *k* largest of them.
The script is a standalone, dependency‑free solution for the homework described at the top of `program01.py`.

---

## What is the XKCD format?

Randall Munroe once joked about writing Roman numerals by **concatenating the decimal value of each symbol** (comic #2637, *Roman Numerals*). For example:

```
397  →  CCCXCVII           (classic Roman)
      → 100 100 100 10 100 5 1 1  (symbol weights)
      → 10010010010100511         (XKCD format)
```

Your task (and this repo) is to take strings like `"10010010010100511"` and recover the original value—in this case `397`—while obeying the usual “subtractive” rule of Roman numerals (e.g. 4 = `IV`, 900 = `CM`).


```

### Key Functions (in `program01.py`)

| Function                                               | Purpose                                                                                           |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **`decode_XKCD_tuple(values: tuple[str, …], k: int)`** | Convert every string in `values`, sort the results in decreasing order, and return the first *k*. |
| `decode_value(xkcd: str)`                              | Orchestrates the three helpers below to turn one XKCD string into an `int`.                       |
| `xkcd_to_list_of_weights(xkcd: str)`                   | Splits the run‑together digits into `[100, 100, 10, …]`, one per Roman symbol.                    |
| `list_of_weights_to_number(weights: list[int])`        | Applies the Roman “add‑unless‑smaller‑precedes‑larger” rule to get the final value.               |


## How the Algorithm Works

1. **Tokenisation** – `xkcd_to_list_of_weights` walks the string and groups trailing zeros so that `"100"` becomes `100`, `"5"` stays `5`, etc.
2. **Roman evaluation** – `list_of_weights_to_number` iterates left→right and subtracts a weight when it precedes a larger weight, emulating classical Roman numerals (`10` before `100` → −10).
3. **Top‑k selection** – Normal Python `list.sort(reverse=True)` followed by slicing—fast and simple for typical homework‑sized inputs.

---
