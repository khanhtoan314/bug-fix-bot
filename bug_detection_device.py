"""
This file is known as the bug_detection_device.py

This is where the main functions of the bug-fix bot would be defined,
so long as the functionalities of the system remained unchanged

"""

"""
This file is known as the bug_detection_device.py

This is where the main functions of the bug-fix bot would be defined,
so long as the functionalities of the system remained unchanged

"""

# Importing necessary libraries for this module
import vertexai
from vertexai.generative_models import GenerativeModel, GenerationConfig
import re

from config import (
    Gemini_Model_name, 
    temperature, 
    Output_Token,
    PROJECT_ID,
    LOCATION                                       
)

# Initialize Vertex AI with your project
vertexai.init(project=PROJECT_ID, location=LOCATION)

# Create the Gemini model (Fixed by using Vertex AI instead)
model = GenerativeModel(model_name=Gemini_Model_name)

# Create generation config
generation_config = GenerationConfig(
    temperature=temperature,
    max_output_tokens=Output_Token,
)

# Creating a prompt template for the bot to understand its purpose
prompt_template = """ Welcome! You are the a bug detection device created on Python for new players.

Your Task: To analyze the code snippets and identify any bugs or issues. 

Here's the Rulebook:
    1. For the output, only in two lines, no further than that.
    2. First Line: [BUG] and then followed by a simple explanation (In 1 sentence)
    3. Second Line: [FIX] and then followed by a corrected line of fixed codes.
    4. Keep it as beginner-friendly as possible.
    5. If no bugs are found, respond with [BUG] No bugs found and [FIX] code that confirmed to be correct.

Template for code to analyze:
``` Python
{Code}
```    

Your response (exactly two lines):
"""

# Now I can define the main function for the bug-fix bot
def bug_detector(codeSnippet: str) -> dict:
    """
    First, send the codes to Gemini and get the bug + fix in return.
    
    Input: A string of Python codes (possibly very buggy or straight up make no sense)
    Output: A dictionary that has 'bug' and 'fix' keys
    
    Example: 
        result = bug_detector("print('Hello World')")
        print(result['bug']) # Ex: "Missing the parenthesis"
        print(result['fix']) # Ex: "print('Hello World')"
    """

    # The bot needs a full prompt that would keep the user's code snippet intact
    full_prompt = prompt_template.format(Code=codeSnippet)

    # Then that full prompt can be sent to Gemini and receive its response
    try:
        sys_response = model.generate_content(full_prompt, generation_config=generation_config)
        sys_response_text = sys_response.text
    except Exception as e:
        # Happens when there is something wrong with the system or the API call
        return {"bug": f"System Error: {str(e)}", 
                "fix": "[FIX] Please check the system or API configuration.",
                "rawResponse": str(e)
        }
    
    bug_description = extract_tag(sys_response_text, "bug")
    fix_description = extract_tag(sys_response_text, "fix")

    return{
        "bug": bug_description,
        "fix": fix_description,
        "rawResponse": sys_response_text
    }

# Now, I can move on to create a helper function, where it extracts the tagged contents
def extract_tag(text: "str", tag: "str") -> "str":
        """
        Start with finding the content after a [TAG] market in the texts.

        Example:
        text = "[BUG] Missing the parenthesis\n[FIX] print('Hello World')"
        extract_tag(text, "bug") # Returns: "Missing the parenthesis"
        extract_tag(text, "fix") # Returns: "print('Hello World')"
        """
        sys_pattern = re.compile(rf"\[{tag.upper()}\]\s*(.*)")
        sys_match = sys_pattern.search(text)
        if sys_match:
             return sys_match.group(1).strip()
        else:
            return f"Cannot find the [{tag}] in the response."      

# Now I can start test run the system to see if any bug is detected
if __name__ == "__main__":
    # Test the bug detector with a sample code snippet
    print("=" * 50)
    print("Testing Bug Detector")
    print("=" * 50)
    
    # Test with a simple buggy code (missing colon)
    test_code = """
def greet(name)
    print(f"Hello, {name}!")

greet("World")
"""
    
    print("\nBuggy code:")
    print(test_code)
    print("\nAnalyzing...")
    
    result = bug_detector(test_code)
    
    print(f"\n🐛 BUG: {result['bug']}")
    print(f"🔧 FIX: {result['fix']}")
    print(f"\n📋 RAW: {result['rawResponse']}")
    print("\n" + "=" * 50)

# This is the end of the bug detection device module, gotta test to see if it works as expected.
