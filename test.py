import sys
print("Python path:", sys.path)

try:
    import fstrent_tools
    print("Package location:", fstrent_tools.__file__)
    print("Package version:", fstrent_tools.__version__)
except ImportError as e:
    print("Import error:", str(e))

try:
    from fstrent_tools import load_json, get_timestamp
    print("Successfully imported load_json and get_timestamp")
except ImportError as e:
    print("Failed to import specific functions:", str(e))