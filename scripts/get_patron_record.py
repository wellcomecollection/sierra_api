#!/usr/bin/env python3
"""
Look up the API response for a patron record using the patron number, e.g.

    python3 get_patron_record.py 1234567

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
        patron_number = sys.argv[1]
    except IndexError:
        sys.exit(f"Usage: {__file__} <PATRON_NUMBER>")

    sierra = identity_client()
    resp = sierra.client.get(
        f"/patrons/{patron_number}", params={"fields": PATRON_FIELDS}
    )
    resp.raise_for_status()
    print(json.dumps(resp.json(), indent=2, sort_keys=True))
