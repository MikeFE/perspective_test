#!/usr/bin/env python3

from apikey import API_KEY

import sys
import requests
import json

PERSPECTIVE_URL = 'https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze?key={}'.format(API_KEY)

def get_toxicity(text):
        data = {
            'comment': {'text': text},
            'languages': ['en'],
            'requestedAttributes': {'TOXICITY': {}}
        }

        r = requests.post(PERSPECTIVE_URL, json=data)
        return r.json()['attributeScores']['TOXICITY']['summaryScore']['value']


def main():
    try:
        while 1:
            text = input('Enter text: ')
            print('Toxicity score: {}'.format(get_toxicity(text)))
    except KeyboardInterrupt:
        print()
        return

if __name__ == '__main__':
    sys.exit(main())
