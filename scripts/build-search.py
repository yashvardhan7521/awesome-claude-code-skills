#!/usr/bin/env python3
"""Build a simple search index (JSON) from data/skills.json"""
import json
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
skills_file = BASE / 'data' / 'skills.json'
index_file = BASE / 'website' / 'search-index.json'

def main():
    skills = json.load(open(skills_file))
    index = []
    for s in skills:
        index.append({'name': s.get('name'), 'category': s.get('category'), 'command': s.get('command'), 'purpose': s.get('purpose')})
    open(index_file, 'w').write(json.dumps(index, indent=2))
    print('Search index written to', index_file)

if __name__ == '__main__':
    main()
