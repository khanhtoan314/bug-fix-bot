"""
config.py - Configuration file for the bug-fix bot

Function: It stores every settings and functions for the bug-fix bot to function

In essence... this is the 'setting menu' of the bug-fix bot

"""

# Declaring my Google API key
Google_API_key = "google_api_key_here"

"""
This latter section is where the settings of the bot would be defined
"""
# Setting the Gemini Model name
Gemini_Model_name = "gemini-2.5-flash"

# Setting the temperature (paramater of the AI's smart workflow) - Usually between 0 and 1
temperature = 0.1

# Setting the tokens needed to solve a coding bug - Usually a token = a word
# Defined 200 Tokens for the bot to solve a coding bug (First fix: 300, Second fix: 2000)
Output_Token = 2000

# Settings for the Vertex AI (Currently being used in bug_detection_device.py)
PROJECT_ID = "project_id_here"
LOCATION = "location_here"
