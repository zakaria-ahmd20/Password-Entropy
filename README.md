# Password-Entropy

A tool to calculate and analyze password entropy, helping users understand password strength by evaluating length and character set. This tool provides insights for creating secure passwords based on entropy calculations.

## Entropy Formula

Password entropy is calculated using the following formula:

\[
H = L \times \log_2(N)
\]

Where:
- **H** = Entropy (measured in bits)
- **L** = Length of the password
- **N** = Number of possible characters in the character set

### Character Set Example:

- For **lowercase letters (a-z)**: \( N = 26 \)
- For **lowercase and uppercase letters (a-z, A-Z)**: \( N = 52 \)
- For **lowercase, uppercase, and digits (a-z, A-Z, 0-9)**: \( N = 62 \)
- For **lowercase, uppercase, digits, and special characters** (e.g., `!@#$%^&*()`): \( N = 94 \)

## Example Password and Entropy Calculation

Consider the password: `Zakaria-is-a-nice-fella`

- **Length (L):** 23 characters
- **Character Set (N):** 26 (lowercase letters)

Entropy:

\[
H = 23 \times \log_2(26) \approx 23 \times 4.7004 = 108.11 \text{ bits}
\]

This password has an entropy of approximately **108.11 bits**, indicating a strong password.

## Why This Matters

The higher the entropy of a password, the more secure it is. Using long passwords with a wide character set helps ensure that they cannot be easily guessed or cracked. This repository provides a simple way to calculate password entropy and choose strong passwords.
