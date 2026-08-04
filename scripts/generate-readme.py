#!/usr/bin/env python3
"""Generate README and simple docs from data/*.json"""
import json
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
skills_file = BASE / 'data' / 'skills.json'
out = BASE / 'README.md'

def main():
    skills = json.load(open(skills_file))
    lines = ['# Skills index', '']
    for s in skills:
        lines.append(f"- **{s.get('name')}**: {s.get('purpose')} (Category: {s.get('category')})")
    out.write_text('\n'.join(lines))
    print('README regenerated')

if __name__ == '__main__':
    main()
