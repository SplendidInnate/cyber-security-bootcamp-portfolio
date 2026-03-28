# Auto-Graded Task:

# Function to print dictionary values given the keys

def print_values_of(dictionary, *keys): # Added (*) before keys to allow the passing of multiple separate arguaments
    for key in keys:
        print(dictionary[key]) # Fixed the name error by changing 'k' to 'key' to match the for-loop variable

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 
                         "homer": "d'oh!", # Fixed the error by adding (" ")
                         "maggie": "(Pacifier Suck)"
                        }

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''