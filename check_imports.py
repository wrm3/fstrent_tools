import os
import re

def check_imports(directory):
    """Check for any remaining absolute imports in Python files."""
    tools_pattern = re.compile(r'from tools_(\w+) import|import tools_(\w+)')
    
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all matches
            matches = tools_pattern.findall(content)
            if matches:
                print(f"\nIn {filename}:")
                for match in matches:
                    # match could be from either group in the regex
                    module = match[0] or match[1]
                    print(f"  Found: from tools_{module} import ...")

if __name__ == '__main__':
    src_dir = os.path.join(os.path.dirname(__file__), 'src')
    check_imports(src_dir) 