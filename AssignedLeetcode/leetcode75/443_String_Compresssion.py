from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # Where to write compressed characters
        count = 1  # Track occurrences
        
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1  # Count consecutive characters
            else:
                # Store the character
                chars[write_index] = chars[i - 1]
                write_index += 1
                
                # Store the frequency (only if greater than 1)
                if count > 1:
                    for digit in str(count):
                        chars[write_index] = digit
                        write_index += 1
                        
                count = 1  # Reset count for next character sequence

        return write_index  # Return the compressed length
