import time

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Analyzes and determines if a string is a palindrome using a verbose
        two-pointer approach to illustrate the decision process.
        """
        left, right = 0, len(s) - 1
        
        print("--- START OF ANALYSIS ---")
        print(f"Input string: '{s}'")
        print(f"Initial state: left = {left}, right = {right}\n")
        time.sleep(1)

        # The MAIN LOOP's condition defines the valid search space.
        while left < right:
            print(f"--- Main Loop Iteration (Check: {left} < {right} -> {left < right}) ---")
            print(f"Current Pointers: left = {left} ('{s[left]}'), right = {right} ('{s[right]}')")
            time.sleep(1.5)

            # --- Left Pointer Seeking Logic ---
            print("\n  -> Seeking for valid character with LEFT pointer...")
            # The inner loop must RESPECT the main loop's boundary.
            # `left < right` is the GUARD condition to prevent out-of-bounds access.
            while left < right and not s[left].isalnum():
                print(f"     left at {left} ('{s[left]}') is not alphanumeric. Skipping.")
                left += 1
                print(f"     New left position: {left}")
                time.sleep(1)
            
            # This check handles cases where all remaining characters are non-alphanumeric
            if left >= right:
                print("\n  -> Pointers met or crossed while seeking. All remaining chars were non-alphanumeric.")
                break

            print(f"  -> Found valid LEFT character at {left}: '{s[left]}'")
            time.sleep(1)

            # --- Right Pointer Seeking Logic ---
            print("\n  -> Seeking for valid character with RIGHT pointer...")
            # The `left < right` GUARD is equally critical here.
            while left < right and not s[right].isalnum():
                print(f"     right at {right} ('{s[right]}') is not alphanumeric. Skipping.")
                right -= 1
                print(f"     New right position: {right}")
                time.sleep(1)
            
            print(f"  -> Found valid RIGHT character at {right}: '{s[right]}'")
            time.sleep(1)

            # --- Comparison Logic ---
            print(f"\n  => COMPARING: '{s[left].lower()}' (from left) vs '{s[right].lower()}' (from right)")
            if s[left].lower() != s[right].lower():
                print("  => MISMATCH! The string is not a palindrome.")
                print("--- END OF ANALYSIS ---\n")
                return False
            else:
                print("  => Match. Moving pointers inward.")

            left += 1
            right -= 1
            print(f"     New state: left = {left}, right = {right}\n")
            time.sleep(1.5)
        
        print(f"\n--- Main Loop Condition False (Check: {left} < {right} -> {left < right}) ---")
        print("Loop terminated because pointers met or crossed. No mismatches found.")
        print("The string is a palindrome.")
        print("--- END OF ANALYSIS ---\n")
        return True

def run_test_case(solver, test_str):
    """Helper function to run and display a single test case."""
    print("="*40)
    print(f"TESTING: '{test_str}'")
    print("="*40)
    result = solver.isPalindrome(test_str)
    print(f"FINAL RESULT for '{test_str}': {result}\n\n")

if __name__ == "__main__":
    solver = Solution()

    # Test case 1: A standard palindrome that shows all logic
    run_test_case(solver, "A man, a plan, a canal: Panama")

    # Test case 2: The critical failure case for an unguarded seek
    # This demonstrates WHY `left < right` is necessary in the inner loops.
    run_test_case(solver, ",. , .," )

    # Test case 3: A standard non-palindrome to show early exit
    run_test_case(solver, "race a car")
