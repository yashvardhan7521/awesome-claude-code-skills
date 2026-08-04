#!/usr/bin/env python3
"""Compute rankings using weights in data/rankings.json and fields in data/skills.json"""
import json
from pathlib import Path
BASE = Path(__file__).resolve().parent.parent
skills_file = BASE / 'data' / 'skills.json'
rankings_file = BASE / 'data' / 'rankings.json'

def main():
    skills = json.load(open(skills_file))
    rankings = json.load(open(rankings_file))
    weights = rankings.get('ranking_formula', {})
    out_list = []
    for s in skills:
        score = 0
        # numeric fields expected: time_saved, frequency, automation, difficulty_reduction, overall_usefulness
        for key, w in weights.items():
            val = s.get(key, 0)
            score += (val * w)
        # normalize by sum of weights
        total_w = sum(weights.values()) or 1
        final = round(score / total_w, 2)
        out_list.append({'name': s.get('name'), 'score': final})
    # sort desc
    out_list.sort(key=lambda x: x['score'], reverse=True)
    rankings['rankings'] = out_list
    open(rankings_file, 'w').write(json.dumps(rankings, indent=2))
    print('Rankings computed and saved to', rankings_file)

if __name__ == '__main__':
    main()
