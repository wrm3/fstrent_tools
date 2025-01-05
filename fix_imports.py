import os
import re

def fix_imports(directory):
    """Fix imports in all Python files in the given directory."""
    tools_pattern = re.compile(r'from tools_(\w+) import')
    
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace 'from tools_xxx import' with 'from .tools_xxx import'
            modified = tools_pattern.sub(r'from .tools_\1 import', content)
            
            if modified != content:
                print(f"Fixing imports in {filename}")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(modified)

if __name__ == '__main__':
    src_dir = os.path.join(os.path.dirname(__file__), 'src')
    fix_imports(src_dir) 