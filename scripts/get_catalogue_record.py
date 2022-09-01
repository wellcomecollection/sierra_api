#!/usr/bin/env python3
"""
Look up the API response for a patron record using the patron number, e.g.

    python3 get_catalogue_record.py c11155280

You need to have access to the Wellcome Collection Platform AWS account
for this script to work.

"""

import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api_client import catalogue_client, HOLDINGS_FIELDS


if __name__ == "__main__":
    try:
        record_number = sys.argv[1]
    except IndexError:
        sys.exit(f"Usage: {__file__} <RECORD_NUMBER>")

    if record_number.startswith("c"):
        holdings_number = record_number[1:8]

        sierra = catalogue_client()
        resp = sierra.client.get(
            "/holdings", params={"id": holdings_number, "fields": HOLDINGS_FIELDS}
        )
        resp.raise_for_status()
        print(json.dumps(resp.json(), indent=2, sort_keys=True))

    else:
        sys.exit(f"Unrecognised record number type: {record_number}")
