#!/usr/bin/env python3

from apikey import API_KEY

import sys
import requests
import json

PERSPECTIVE_URL = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={}'.format(API_KEY)

enum_to_str_stats = {
    'TOXICITY': 'Toxicity',
    'ATTACK_ON_AUTHOR': 'Attack on author',
    'ATTACK_ON_COMMENTER': 'Attack on commenter',
    'INCOHERENT': 'Incorrehence',
    'INFLAMMATORY': 'Inflammatory',
    'LIKELY_TO_REJECT': 'Likely to be rejected by mod',
    'OBSCENE': 'Obscenity',
    'SEVERE_TOXICITY': 'Severe toxicity',
    'SPAM': 'Potential spam',
    'UNSUBSTANTIAL': 'Ubsubstantial comments'
}

def get_toxicity(text):
    data = {
        'comment': {'text': text},
        'languages': ['en'],
        'requestedAttributes': {
            'TOXICITY': {},
            'ATTACK_ON_AUTHOR': {},
            'ATTACK_ON_COMMENTER': {},
            'INCOHERENT': {},
            'INFLAMMATORY': {},
            'LIKELY_TO_REJECT': {},
            'OBSCENE': {},
            'SEVERE_TOXICITY': {},
            'SPAM': {},
            'UNSUBSTANTIAL': {}
        }
    }

    r = requests.post(PERSPECTIVE_URL, json=data)
    try:
        stats = {}
        for attrib in r.json()['attributeScores'].keys():
            stats[attrib] = r.json()['attributeScores'][attrib]['summaryScore']['value']
    except KeyError:
        print(r.text)
        return {}

    return stats


def main():
    try:
        while 1:
            text = input('Enter text: ')
            if not text:
                continue

            for k, v in get_toxicity(text).items():
                print('\t{} estimate: {:.1%}'.format(enum_to_str_stats[k], v))

    except KeyboardInterrupt:
        print()
        return

if __name__ == '__main__':
    sys.exit(main())
