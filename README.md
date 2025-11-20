# Chapter 12: Parity Bits (Error Detection)

## Overview

This chapter covers parity bits—a simple but effective method for detecting errors in digital data transmission and storage. Parity is one of the most fundamental error detection techniques used in computer systems and communication.

## Key Concepts

### What is a Parity Bit?

**Definition:** An extra bit added to binary data to make the total number of 1's either even (even parity) or odd (odd parity).

**Purpose:** Detect single-bit errors in data transmission or storage

### How Parity Works

```
Original Data: 1011010  (4 ones)

Even Parity: Add bit to make total 1's even
  1011010 + 0 = 10110100 (still 4 ones, even ✓)

Odd Parity: Add bit to make total 1's odd
  1011010 + 1 = 10110101 (5 ones, odd ✓)
```

## Even Parity

### Definition
The parity bit is set so that the **total number of 1-bits (including parity) is even**.

### Calculation
```
Count the 1's in data bits:
  If count is even → parity bit = 0
  If count is odd  → parity bit = 1
```

### Examples

#### Example 1: Data = 1010101
```
Count 1's: 1+0+1+0+1+0+1 = 4 (even)
Parity bit = 0 (to keep total even)
Result: 10101010
```

#### Example 2: Data = 1111000
```
Count 1's: 1+1+1+1+0+0+0 = 4 (even)
Parity bit = 0
Result: 11110000
```

#### Example 3: Data = 1010011
```
Count 1's: 1+0+1+0+0+1+1 = 4 (even)
Parity bit = 0
Result: 10100110
```

#### Example 4: Data = 1111111
```
Count 1's: 7 (odd)
Parity bit = 1 (to make total even)
Result: 11111111
```

## Odd Parity

### Definition
The parity bit is set so that the **total number of 1-bits (including parity) is odd**.

### Calculation
```
Count the 1's in data bits:
  If count is even → parity bit = 1
  If count is odd  → parity bit = 0
```

### Examples

#### Example 1: Data = 1010101
```
Count 1's: 4 (even)
Parity bit = 1 (to make total odd)
Result: 10101011
```

#### Example 2: Data = 1111000
```
Count 1's: 4 (even)
Parity bit = 1
Result: 11110001
```

#### Example 3: Data = 1010011
```
Count 1's: 4 (even)
Parity bit = 1
Result: 10100111
```

#### Example 4: Data = 1111111
```
Count 1's: 7 (odd)
Parity bit = 0 (to keep total odd)
Result: 11111110
```

## Error Detection

### Single-Bit Error Detection

**How it works:**
1. Sender calculates parity and transmits data + parity bit
2. Receiver recalculates parity from received data
3. If calculated parity ≠ received parity → **error detected**

### Example: Error Detection

#### Successful Transmission (No Error)
```
Sender (even parity):
  Data:          1011010
  Count 1's:     4 (even)
  Parity bit:    0
  Transmitted:   10110100

Receiver:
  Received:      10110100
  Count 1's:     4 (even)
  Parity check:  ✓ OK (even parity maintained)
```

#### Transmission with Error
```
Sender (even parity):
  Data:          1011010
  Parity bit:    0
  Transmitted:   10110100

During transmission, bit 4 flips: 10110100 → 10100100

Receiver:
  Received:      10100100
  Count 1's:     3 (odd!)
  Parity check:  ✗ ERROR (expected even, got odd)
```

## Parity Bit Placement

### Append to End (Most Common)
```
Data: D₇ D₆ D₅ D₄ D₃ D₂ D₁ D₀
With parity: D₇ D₆ D₅ D₄ D₃ D₂ D₁ D₀ P
```

### Prepend to Start
```
With parity: P D₇ D₆ D₅ D₄ D₃ D₂ D₁ D₀
```

### Insert at Specific Position
```
Example: After every 7 bits
D₆ D₅ D₄ D₃ D₂ D₁ D₀ P
```

## Limitations of Parity

### What Parity CAN Detect ✓
- **Single-bit errors:** Any one bit flip is detected
- **Odd number of bit errors:** 1, 3, 5, 7, ... bit errors

### What Parity CANNOT Detect ✗
- **Even number of bit errors:** 2, 4, 6, ... bit errors
- **Which bit is wrong:** Only tells you there's an error, not where

### Example: Undetected Double-Bit Error
```
Original (even parity):  10110100  (4 ones, even)
Two bits flip:           10100110  (4 ones, still even!)
Receiver: No error detected! ✗
```

### Example: Detected Triple-Bit Error
```
Original (even parity):  10110100  (4 ones, even)
Three bits flip:         00100101  (3 ones, odd!)
Receiver: Error detected! ✓
```

## Parity in Practice

### ASCII with Parity (8th Bit)

**7-bit ASCII + 1 parity bit = 8 bits total**

```
'A' = 1000001 (7 bits)

Even parity: 01000001 (parity = 0, total 2 ones)
Odd parity:  11000001 (parity = 1, total 3 ones)
```

### UART Serial Communication

**Common formats:**
- **8N1:** 8 data bits, No parity, 1 stop bit
- **8E1:** 8 data bits, Even parity, 1 stop bit
- **8O1:** 8 data bits, Odd parity, 1 stop bit
- **7E1:** 7 data bits, Even parity, 1 stop bit (ASCII with parity)

### Frame Format with Parity
```
[Start bit][Data bits][Parity bit][Stop bit(s)]
     0     D₀ D₁ ... D₇     P           1
```

## Parity vs Other Error Detection

| Method | Overhead | Detects | Corrects | Usage |
|--------|----------|---------|----------|-------|
| **Parity** | 1 bit | Single errors | No | Simple, legacy |
| **Checksum** | 8-32 bits | Multiple errors | No | TCP/IP, files |
| **CRC** | 16-32 bits | Burst errors | No | Networks, storage |
| **Hamming Code** | log₂(n) bits | Multiple errors | Yes | RAM ECC |
| **Reed-Solomon** | Variable | Burst errors | Yes | CDs, DVDs, QR codes |

## Learning Objectives

By the end of this chapter, you should be able to:
- Calculate even and odd parity bits
- Detect errors using parity checking
- Understand when parity can and cannot detect errors
- Explain the limitations of parity (even-number errors)
- Apply parity in practical scenarios (UART, ASCII)
- Compare parity with other error detection methods
- Implement parity generation and checking in code

## Python Example

Run the interactive example:

```bash
python ch12_parity_bits.py
```

### What the Example Demonstrates

1. **Even Parity Calculation:** Computing parity for various data
2. **Odd Parity Calculation:** Alternative parity scheme
3. **Error Detection:** Simulating transmission errors
4. **Multiple Error Cases:** Showing detection limits
5. **ASCII with Parity:** 7-bit ASCII + parity bit
6. **UART Simulation:** Serial communication frames
7. **Parity Table:** Comprehensive examples
8. **Practical Applications:** Real-world usage

### Sample Output

```
============================================================
CHAPTER 12: Parity Bits (Error Detection)
============================================================

--- Example 1: Even Parity Calculation ---
Data:    1011010  (4 ones, even)
Parity:  0  (keep total even)
Result:  10110100

--- Example 2: Error Detection ---
Transmitted: 10110100 (even parity)
Received:    10100100 (bit error!)
Parity check: 3 ones (odd) → ERROR DETECTED ✗
...
```

## Real-World Applications

### Serial Communication
- **RS-232:** Optional parity bit for error detection
- **UART:** Common in embedded systems
- **Modems:** Error detection in dial-up connections
- **Industrial Protocols:** Modbus RTU uses parity

### Computer Memory
- **Legacy RAM:** Simple parity checking (rare now)
- **Modern RAM:** Uses ECC (Error Correcting Code) instead
- **Cache:** Some systems use parity for L1/L2 cache
- **Flash Memory:** Uses more advanced error correction

### Storage Systems
- **Tape Drives:** Early systems used parity tracks
- **RAID Parity:** RAID 3, 4, 5, 6 use parity for redundancy
- **Disk Controllers:** Some use parity for data integrity

### Networking
- **Legacy Protocols:** Early networks used parity
- **Modern:** Replaced by CRC, checksums, and stronger codes
- **Still Used:** Simple point-to-point links

## Common Questions

**Q: Why use even parity instead of odd parity (or vice versa)?**  
A: Personal/system preference. Both detect the same errors. Even parity is slightly more common. What matters is that sender and receiver agree!

**Q: Can parity detect if two bits are flipped?**  
A: No. If two bits flip, the parity remains the same (even/odd count unchanged), so the error is undetected.

**Q: Can parity correct errors?**  
A: No. Parity only detects errors; it cannot determine which bit is wrong. Use Hamming codes or ECC for error correction.

**Q: Is parity still used today?**  
A: Mostly in legacy systems and simple serial communication. Modern systems use stronger error detection (CRC, checksums) and correction (ECC, Reed-Solomon).

**Q: What's the difference between parity and a checksum?**  
A: Parity is a single bit. A checksum is usually 8-32 bits and provides much stronger error detection.

## Implementing Parity

### Python
```python
def calculate_even_parity(data):
    """Calculate even parity bit for data."""
    count = bin(data).count('1')
    return 0 if count % 2 == 0 else 1

def calculate_odd_parity(data):
    """Calculate odd parity bit for data."""
    count = bin(data).count('1')
    return 1 if count % 2 == 0 else 0

def check_parity(data_with_parity, even=True):
    """Check if parity is correct."""
    count = bin(data_with_parity).count('1')
    expected = 0 if even else 1
    return (count % 2) == expected
```

### C/C++
```c
// Calculate even parity bit
uint8_t even_parity(uint8_t data) {
    uint8_t count = 0;
    while (data) {
        count += data & 1;
        data >>= 1;
    }
    return count & 1;  // Return LSB of count
}

// OR use XOR (elegant solution!)
uint8_t even_parity_xor(uint8_t data) {
    data ^= data >> 4;
    data ^= data >> 2;
    data ^= data >> 1;
    return data & 1;
}
```

### Hardware (XOR Gates)
```
Even parity = D₀ ⊕ D₁ ⊕ D₂ ⊕ D₃ ⊕ D₄ ⊕ D₅ ⊕ D₆ ⊕ D₇

Chain of XOR gates:
D₀ ─┐
    XOR─┐
D₁ ─┘   │
        XOR─┐
D₂ ─────┘   │
            XOR── Parity Bit
D₃ ─────────┘
```

## Key Takeaways

- ✓ Parity adds one bit to detect errors
- Even parity: Total 1's = even; Odd parity: Total 1's = odd
- Detects single-bit errors and odd-number errors
- ❌ Cannot detect even-number errors (2, 4, 6, ... bits)
- 🚫 Cannot correct errors (only detect)
- Simple and low overhead (1 bit per data word)
- Common in serial communication (UART)
- Modern systems use stronger methods (CRC, ECC)

## Practice Exercises

1. Calculate even parity for: 1011010
2. Calculate odd parity for: 11110000
3. Data with even parity: 10110101. Is there an error?
4. Add even parity to ASCII 'M' (1001101)
5. Received: 11010110 (odd parity). Count 1's. Error?
6. Why can't parity detect 2-bit errors? Give an example.
7. If transmitted data is 10110100 (even parity) but received as 10110000, will the error be detected?
8. How many parity bits are needed for 64 bits of data?
9. Compare: Which is better, even or odd parity?
10. Design a simple error detection system for 4-bit data using parity

## Further Study

- Learn about Hamming codes (error correction)
- Study CRC (Cyclic Redundancy Check)
- Explore checksums (Internet Checksum, Fletcher)
- Investigate ECC RAM (Error Correcting Code)
- Learn about Reed-Solomon codes (CDs, DVDs, QR codes)

---

**Course Navigation:**  
← Previous: [Chapter 11 - Coding Schemas](../ch11_coding_schemas/) | Next: [Chapter 13 - Clock Signals](../ch13_clock_signals/) →

---

## Authorship
Authored by Maxwell Hauser on November 19, 2025

## License
MIT License
