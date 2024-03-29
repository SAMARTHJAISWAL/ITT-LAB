import os

def display_env_vars():
    for key, value in os.environ.items():
        print(f"{key}: {value}")

# Call the function to display all environment variables
display_env_vars()
