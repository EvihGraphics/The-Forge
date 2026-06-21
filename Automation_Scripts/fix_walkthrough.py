import sys

file_path = r'C:\Users\l3d\.gemini\antigravity\brain\2d7a8410-35e6-47b7-a5c1-e3ce6a91a404\walkthrough.md'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken paths with proper file:/// URI scheme paths
content = content.replace('![Alpha Blending Baseline](/C:/Users/l3d/', '![Alpha Blending Baseline](file:///C:/Users/l3d/')
content = content.replace('![Adaptive OIT Ground Truth](/C:/Users/l3d/', '![Adaptive OIT Ground Truth](file:///C:/Users/l3d/')
content = content.replace('![AVBOIT Result](/C:/Users/l3d/', '![AVBOIT Result](file:///C:/Users/l3d/')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
