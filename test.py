import sys
print("Python path:", sys.path)

try:
    from fstrent_tools import load_json, get_timestamp
    print("Successfully imported load_json and get_timestamp")
except ImportError as e:
    print("Import error:", str(e))

# Optionally, test the functions if you have implementations
try:
    # Assuming load_json and get_timestamp are callable functions
    # json_data = load_json('some_file.json')  # Example usage
    # timestamp = get_timestamp()  # Example usage
    print("Functions are callable")
except Exception as e:
    print("Error calling functions:", str(e))