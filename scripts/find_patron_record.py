#!/usr/bin/env python3
"""
Look up the API response for a patron record using the email address, e.g.

    python3 find_patron_record.py example@example.com

You need to have access to the Wellcome Collection Identity AWS account
for this script to work.

"""

import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import identity_client, PATRON_FIELDS


if __name__ == "__main__":
    try:
        email_address = sys.argv[1]
    except IndexError:
        sys.exit(f"Usage: {__file__} <EMAIL_ADDRESS>")

    sierra = identity_client()
    resp = sierra.client.get(
        "/patrons/find",
        params={
            "varFieldTag": "z",
            "varFieldContent": email_address.lower(),
            "fields": PATRON_FIELDS,
        },
    )
    resp.raise_for_status()
    print(json.dumps(resp.json(), indent=2, sort_keys=True))
