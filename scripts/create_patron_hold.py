#!/usr/bin/env python3
"""
Returns the API response for creating a patron hold.

First parameter is the patron ID, second is the item ID.

    python3 get_patron_record.py p1234567 i7654321

You need to have access to the Wellcome Collection Identity AWS account
for this script to work.

"""

import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import identity_client


if __name__ == "__main__":
    try:
        patron_number = sys.argv[1]
        item_number = sys.argv[2]
    except IndexError:
        sys.exit(f"Usage: {__file__} <PATRON_NUMBER> <ITEM_NUMBER>")

    if not patron_number.startswith("p") or not item_number.startswith("i"):
        sys.exit(f"Usage: {__file__} <PATRON_NUMBER> <ITEM_NUMBER>")

    patron_number = patron_number[1:]
    item_number = item_number[1:]

    sierra = identity_client()
    resp = sierra.client.post(
        f"/patrons/{patron_number}/holds/requests",
        json={
            "recordType": "i",
            "recordNumber": int(item_number),
            "pickupLocation": "unspecified",
        },
    )
    print(resp)
    print(json.dumps(resp.json(), indent=2, sort_keys=True))
