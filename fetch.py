# fetch.py
import os
import json
from airtable import Airtable

# Read credentials from environment
base_id = os.getenv('AIRTABLE_BASE_ID')
api_key = os.getenv('AIRTABLE_API_KEY')

at = Airtable(base_id, 'Table 1', api_key=api_key)
rows = at.get_all(view='Grid view')

bugs = []
for r in rows:
    f = r.get('fields', {})
    bugs.append({
        'name': f.get('Name', ''),
        'email': f.get('Email', ''),
        'description': f.get('Description', ''),
        'priority': f.get('Priority', ''),
        'screenshot': (f.get('Screenshot',[{}])[0].get('url','') if f.get('Screenshot') else ''),
        'created_at': r.get('createdTime','')
    })

with open('bugs.json', 'w') as fp:
    json.dump(bugs, fp, indent=2)
