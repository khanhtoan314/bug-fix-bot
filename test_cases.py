"""
test_cases.py - Test Cases for Bug-Fix Bot
==========================================
This file contains 20 common Python bugs that beginners make.
We use these to test if our bug detector works correctly.
"""

# Each test case is a dictionary with:
# - "code": The buggy code snippet
# - "expected_bug": What kind of bug it is (for us to verify)

TEST_CASES = [
    # 1. Missing colon after function definition
    {
        "code": """def greet(name)
    print(f"Hello, {name}!")""",
        "expected_bug": "missing colon"
    },
    
    # 2. Missing colon after if statement
    {
        "code": """if x > 5
    print("x is big")""",
        "expected_bug": "missing colon"
    },
    
    # 3. Missing colon after for loop
    {
        "code": """for i in range(10)
    print(i)""",
        "expected_bug": "missing colon"
    },
    
    # 4. Missing colon after while loop
    {
        "code": """while x < 10
    x += 1""",
        "expected_bug": "missing colon"
    },
    
    # 5. Incorrect indentation
    {
        "code": """def say_hello():
print("Hello!")""",
        "expected_bug": "indentation"
    },
    
    # 6. Missing closing parenthesis
    {
        "code": """print("Hello World" """,
        "expected_bug": "missing parenthesis"
    },
    
    # 7. Missing closing bracket
    {
        "code": """my_list = [1, 2, 3""",
        "expected_bug": "missing bracket"
    },
    
    # 8. Using = instead of == in comparison
    {
        "code": """if x = 5:
    print("x is five")""",
        "expected_bug": "assignment instead of comparison"
    },
    
    # 9. Undefined variable
    {
        "code": """print(message)""",
        "expected_bug": "undefined variable"
    },
    
    # 10. Missing quotes around string
    {
        "code": """print(Hello World)""",
        "expected_bug": "missing quotes"
    },
    
    # 11. Mismatched quotes
    {
        "code": """message = "Hello World'""",
        "expected_bug": "mismatched quotes"
    },
    
    # 12. Wrong function name (print misspelled)
    {
        "code": """pritn("Hello")""",
        "expected_bug": "misspelled function"
    },
    
    # 13. Missing comma in list
    {
        "code": """fruits = ["apple" "banana" "cherry"]""",
        "expected_bug": "missing comma"
    },
    
    # 14. Index out of range setup (off-by-one)
    {
        "code": """my_list = [1, 2, 3]
print(my_list[3])""",
        "expected_bug": "index out of range"
    },
    
    # 15. Using wrong operator for string concatenation
    {
        "code": """name = "John"
greeting = "Hello " - name""",
        "expected_bug": "wrong operator"
    },
    
    # 16. Missing return statement
    {
        "code": """def add(a, b):
    result = a + b

print(add(2, 3))""",
        "expected_bug": "missing return"
    },
    
    # 17. Modifying list while iterating
    {
        "code": """numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)""",
        "expected_bug": "modifying list while iterating"
    },
    
    # 18. Integer division confusion
    {
        "code": """result = 5 / 2
print(int(result))  # Expecting 2.5 but using int""",
        "expected_bug": "integer division"
    },
    
    # 19. Missing self in class method
    {
        "code": """class Dog:
    def bark():
        print("Woof!")""",
        "expected_bug": "missing self"
    },
    
    # 20. Incorrect boolean operator
    {
        "code": """if x > 0 and < 10:
    print("x is between 0 and 10")""",
        "expected_bug": "incomplete comparison"
    },
]


# Function to run all tests
def run_tests():
    """Run bug detector on all test cases and show results."""
    from bug_detection_device import bug_detector
    
    print("=" * 60)
    print("RUNNING BUG DETECTOR TESTS")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(TEST_CASES, 1):
        print(f"\n--- Test {i}: {test['expected_bug']} ---")
        print(f"Code: {test['code'][:50]}...")
        
        result = bug_detector(test['code'])
        
        print(f"🐛 BUG: {result['bug']}")
        print(f"🔧 FIX: {result['fix']}")
        
        # Simple check: did it find SOMETHING?
        if "Cannot find" not in result['bug'] and "System Error" not in result['bug']:
            print("✅ PASSED - Bug detected")
            passed += 1
        else:
            print("❌ FAILED - No bug detected")
            failed += 1
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Passed: {passed}/{len(TEST_CASES)}")
    print(f"Failed: {failed}/{len(TEST_CASES)}")
    print(f"Accuracy: {(passed/len(TEST_CASES))*100:.1f}%")
    print("=" * 60)


# Run tests if this file is executed directly
if __name__ == "__main__":
    run_tests()
