#!/usr/bin/env python3
"""
Chapter 12: Parity Bits
Demonstrates even and odd parity for error detection
"""

def count_ones(binary_str):
    """Count the number of 1s in a binary string"""
    return binary_str.count('1')

def calculate_even_parity(data_bits):
    """Calculate even parity bit"""
    ones = count_ones(data_bits)
    # Even parity: total 1s (including parity) should be even
    return '0' if ones % 2 == 0 else '1'

def calculate_odd_parity(data_bits):
    """Calculate odd parity bit"""
    ones = count_ones(data_bits)
    # Odd parity: total 1s (including parity) should be odd
    return '1' if ones % 2 == 0 else '0'

def add_parity_bit(data_bits, parity_type='even', position='msb'):
    """Add parity bit to data"""
    if parity_type == 'even':
        parity_bit = calculate_even_parity(data_bits)
    else:
        parity_bit = calculate_odd_parity(data_bits)
    
    if position == 'msb':
        return parity_bit + data_bits
    else:
        return data_bits + parity_bit

def check_parity(received_bits, parity_type='even', parity_position='msb'):
    """Check if received data has correct parity"""
    total_ones = count_ones(received_bits)
    
    if parity_type == 'even':
        return total_ones % 2 == 0
    else:
        return total_ones % 2 == 1

def simulate_transmission(data, parity_type='even', introduce_error=False, error_position=3):
    """Simulate data transmission with parity checking"""
    print(f"\n--- Simulating Transmission ({parity_type} parity) ---")
    
    # Add parity bit
    transmitted = add_parity_bit(data, parity_type, 'msb')
    print(f"Original data:    {data} ({count_ones(data)} ones)")
    
    parity_bit = transmitted[0]
    print(f"Parity bit:       {parity_bit}")
    print(f"Transmitted:      {transmitted}")
    
    # Simulate transmission
    received = transmitted
    if introduce_error:
        # Flip a bit
        received_list = list(received)
        received_list[error_position] = '0' if received_list[error_position] == '1' else '1'
        received = ''.join(received_list)
        print(f"Error at bit {error_position}!  Received: {received}")
    else:
        print(f"No errors:        {received}")
    
    # Check parity
    parity_ok = check_parity(received, parity_type, 'msb')
    
    if parity_ok:
        print(f"Parity check:     ✓ PASS (data likely correct)")
    else:
        print(f"Parity check:     ✗ FAIL (error detected!)")
    
    return parity_ok

def main():
    print("=" * 60)
    print("CHAPTER 12: Parity Bits for Error Detection")
    print("=" * 60)
    
    # Example 1: Even Parity
    print("\n--- Example 1: Even Parity ---")
    data_bits = "1011001"
    ones = count_ones(data_bits)
    parity = calculate_even_parity(data_bits)
    
    print(f"Data bits:        {data_bits}")
    print(f"Number of 1s:     {ones}")
    print(f"Even parity bit:  {parity}")
    print(f"With parity:      {parity + data_bits}")
    print(f"Total 1s:         {count_ones(parity + data_bits)} (even)")
    
    # Example 2: Odd Parity
    print("\n--- Example 2: Odd Parity ---")
    data_bits = "1011001"
    ones = count_ones(data_bits)
    parity = calculate_odd_parity(data_bits)
    
    print(f"Data bits:        {data_bits}")
    print(f"Number of 1s:     {ones}")
    print(f"Odd parity bit:   {parity}")
    print(f"With parity:      {parity + data_bits}")
    print(f"Total 1s:         {count_ones(parity + data_bits)} (odd)")
    
    # Example 3: Parity Bit Table
    print("\n--- Example 3: Even Parity Examples ---")
    print("Data      | 1s | Parity | With Parity | Total 1s")
    print("----------|-------|--------|-------------|----------")
    
    test_data = ["0000", "0001", "0011", "0111", "1111", "1010", "1100"]
    for data in test_data:
        ones = count_ones(data)
        parity = calculate_even_parity(data)
        with_parity = parity + data
        total = count_ones(with_parity)
        print(f"{data}     |   {ones}   |    {parity}   | {with_parity}    |    {total} (even)")
    
    # Example 4: Error Detection (No Error)
    print("\n--- Example 4: Error Detection (No Error) ---")
    data = "1001101"
    simulate_transmission(data, 'odd', introduce_error=False)
    
    # Example 5: Error Detection (With Error)
    print("\n--- Example 5: Error Detection (With Error) ---")
    data = "1001101"
    simulate_transmission(data, 'odd', introduce_error=True, error_position=3)
    
    # Example 6: Limitation - Two Errors
    print("\n--- Example 6: Limitation - Multiple Errors ---")
    data = "1010101"
    transmitted = add_parity_bit(data, 'even', 'msb')
    
    print(f"Original:         {transmitted}")
    print(f"Total 1s:         {count_ones(transmitted)} (even parity)")
    
    # Introduce two errors
    received = list(transmitted)
    received[1] = '0' if received[1] == '1' else '1'  # Flip bit 1
    received[3] = '0' if received[3] == '1' else '1'  # Flip bit 3
    received = ''.join(received)
    
    print(f"\nTwo errors:       {received}")
    print(f"Total 1s:         {count_ones(received)}")
    
    parity_ok = check_parity(received, 'even')
    print(f"Parity check:     {'✓ PASS' if parity_ok else '✗ FAIL'}")
    print("⚠ Warning: Two errors cancel out - not detected!")
    
    # Example 7: ASCII with Parity
    print("\n--- Example 7: ASCII with Even Parity ---")
    word = "HELLO"
    print(f"Word: {word}\n")
    print("Char | ASCII (7-bit) | Parity | 8-bit with Parity")
    print("-----|---------------|--------|-------------------")
    
    for char in word:
        ascii_7bit = format(ord(char), '07b')
        parity = calculate_even_parity(ascii_7bit)
        with_parity = parity + ascii_7bit
        print(f"  {char}  |   {ascii_7bit}   |   {parity}    |     {with_parity}")
    
    # Example 8: Applications and Limitations
    print("\n--- Example 8: Parity Bit Summary ---")
    
    print("\nApplications:")
    print("  • Serial communication (UART)")
    print("  • Memory systems (DRAM)")
    print("  • Storage devices")
    print("  • Network protocols")
    
    print("\nAdvantages:")
    print("  ✓ Simple to implement")
    print("  ✓ Low overhead (1 bit per data word)")
    print("  ✓ Fast computation")
    print("  ✓ Detects single-bit errors reliably")
    
    print("\nLimitations:")
    print("  ✗ Cannot detect even number of errors")
    print("  ✗ Cannot correct errors (only detect)")
    print("  ✗ Cannot identify which bit is wrong")
    print("  ✗ No burst error detection")
    
    # Example 9: Comparison
    print("\n--- Example 9: Even vs Odd Parity ---")
    test_data = "10110"
    
    even_parity = calculate_even_parity(test_data)
    odd_parity = calculate_odd_parity(test_data)
    
    print(f"Data:             {test_data}")
    print(f"Number of 1s:     {count_ones(test_data)}")
    print()
    print(f"Even parity bit:  {even_parity}")
    print(f"With even parity: {even_parity + test_data} (total 1s: {count_ones(even_parity + test_data)} - even)")
    print()
    print(f"Odd parity bit:   {odd_parity}")
    print(f"With odd parity:  {odd_parity + test_data} (total 1s: {count_ones(odd_parity + test_data)} - odd)")
    
    print("\n" + "=" * 60)
    print("Key Concepts:")
    print("- Parity bit: Extra bit for error detection")
    print("- Even parity: Total 1s should be even")
    print("- Odd parity: Total 1s should be odd")
    print("- Detects single-bit errors")
    print("- Cannot correct errors")
    print("- Fails with even number of errors")
    print("=" * 60)

if __name__ == "__main__":
    main()
