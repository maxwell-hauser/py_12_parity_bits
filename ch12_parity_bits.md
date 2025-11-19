# Chapter 12: Parity Bits

_Originally created 12 March 2021, by Maxwell Hauser — Updated 8 October 2025._

_Builds upon material from Chapter 7: Unsigned, Signed Magnitude and Signed Two's Complement Binary Numbers and Chapter 8: Binary Addition._

---

## Overview

A **parity bit** is a bit that is added to a string of binary code. It is used to check whether the data has been transmitted correctly.

A parity bit is used for error detection of information. Since a bit or bits may be changed during the transmission of information from source to destination, a parity bit is an extra bit appended to the information. It represents whether the number of ones (or zeros) is either even or odd in the original transmission and can alert the destination to a loss of information.
 
---

## Definitions

**Parity Bit:**

A parity bit is a bit that is added to a string of binary code. It is used to check whether the data has been transmitted correctly.

**Types:**
- **Even Parity:** The extra bit (0 or 1) is chosen such that the total number of ones becomes even.
- **Odd Parity:** The extra bit (0 or 1) is chosen such that the total number of ones becomes odd.

---

## Examples

**Example 1:** Our message is $(00111)_2$.

- **Even Parity:** By appending a one to the left side of the message, we create $(100111)_2$. Our even parity bit has made the total number of ones even (from 3 to 4 ones).
- **Odd Parity:** By appending a zero to the left side of the message, we create $(000111)_2$. Our odd parity bit has left the total number of ones odd (3 ones).

**Example 2:** Our message is $(10111)_2$.

- **Even Parity:** By appending a zero to the left side of the message, we create $(010111)_2$. Our even parity bit has left the total number of ones even (4 ones).
- **Odd Parity:** By appending a one to the left side of the message, we create $(110111)_2$. Our odd parity bit has made the total number of ones odd (from 4 to 5 ones).).

---

## Applications of Parity Bits

1. **Error Detection:** Parity bits are commonly used in communication systems to detect errors in data transmission. If the number of ones in the received data does not match the expected parity, an error is detected.
2. Memory Systems: Parity bits are used in computer memory systems to detect errors in stored data. Each byte of data is typically stored with an additional parity bit to ensure data integrity.
3. Data Storage: Parity bits are used in data storage systems, such as RAID (Redundant Array of Independent Disks), to provide error detection and correction capabilities.
4. Networking: Parity bits are used in networking protocols to ensure data integrity during transmission over networks.
5. Serial Communication: Parity bits are often used in serial communication protocols, such as UART (Universal Asynchronous Receiver-Transmitter), to detect errors in transmitted data.
6. **Telecommunications:** Parity bits are used in telecommunications systems to ensure the accuracy of transmitted data over long distances.
7. **Digital Systems:** Parity bits are used in various digital systems, including microcontrollers and embedded systems, to ensure data integrity during processing and communication.
8. **Cryptography:** Parity bits can be used in cryptographic systems to ensure the integrity of encrypted data during transmission and storage.

---

## Limitations of Parity Bits

1. **Limited Error Detection:** Parity bits can only detect an odd number of bit errors. If an even number of bits are altered, the parity check will not detect the error, leading to undetected data corruption.
2. **No Error Correction:** Parity bits can only detect errors; they cannot correct them. More advanced error detection and correction techniques, such as checksums and cyclic redundancy checks (CRC), are needed for error correction.
3. **Overhead:** Adding parity bits increases the amount of data that needs to be transmitted or stored, which can lead to increased overhead and reduced efficiency.
4. **Vulnerability to Burst Errors:** Parity bits are not foolproof and can be bypassed by certain types of errors, such as burst errors, where multiple bits are affected in a short span of data.
5. **Compatibility Issues:** Different systems may use different parity schemes (even vs. odd), leading to compatibility issues when transmitting data between systems.
6. **Limited Use in Modern Systems:** With the advent of more advanced error detection and correction techniques, such as CRC and ECC (Error-Correcting Code), the use of parity bits has become less common in modern systems, especially in applications requiring high levels of data integrity and reliability.

---

## Summary

1. A parity bit is an extra bit added to binary code to check data transmission accuracy.
2. **Even parity** ensures the total number of ones is even; **odd parity** ensures it is odd.
3. Parity bits are used in communication systems, memory, data storage, networking, and digital systems.
4. **Limitations:** Can only detect odd numbers of bit errors, cannot correct errors, and add overhead.
5. Modern systems often use more advanced techniques like CRC and ECC.

---

## Exercises

**Exercise 1:** Given the binary message $(1101001)_2$, calculate the even and odd parity bits and append them to the message.

**Solution:**
- **Even Parity:** The number of ones in the message is 4 (which is already even). Therefore, the even parity bit is 0. The message with the even parity bit appended is $(01101001)_2$.
- **Odd Parity:** The number of ones in the message is 4 (which is even). Therefore, the odd parity bit is 1. The message with the odd parity bit appended is $(11101001)_2$.

**Exercise 2:** A binary message $(1010110)_2$ is transmitted with an even parity bit. If the received message is $(11010110)_2$, determine if there was an error in transmission.

**Solution:**
- The received message has 5 ones (which is odd). Since the message was transmitted with an even parity bit, there is an error in transmission.
- The received message has 5 ones (which is odd). Since the message was transmitted with an even parity bit, there is an error in transmission.

**Exercise 3:** A binary message $(1001101)_2$ is transmitted with an odd parity bit. If the received message is $(11001101)_2$, determine if there was an error in transmission.

**Solution:**
- The received message has 5 ones (which is odd). Since the message was transmitted with an odd parity bit, there is no error detected in transmission.

3. A binary message $(1001101)_2$ is transmitted with an odd parity bit. If the received message is $(11001101)_2$, determine if there was an error in transmission.
    - The received message has 5 ones (which is odd). Since the message was transmitted with an odd parity bit, there is no error in transmission.