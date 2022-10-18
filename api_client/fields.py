ITEMS_FIELDS = ",".join(
    [
        "updatedDate",
        "createdDate",
        "deletedDate",
        "deleted",
        "suppressed",
        "bibIds",
        "location",
        "status",
        "barcode",
        "callNumber",
        "itemType",
        "transitInfo",
        "copyNo",
        "holdCount",
        "fixedFields",
        "varFields",
    ]
)

BIBS_FIELDS = ",".join(
    [
        "updatedDate",
        "createdDate",
        "deletedDate",
        "deleted",
        "suppressed",
        "available",
        "lang",
        "title",
        "author",
        "materialType",
        "bibLevel",
        "publishYear",
        "catalogDate",
        "country",
        "orders",
        "normTitle",
        "normAuthor",
        "locations",
        "fixedFields",
        "varFields",
    ]
)

HOLDINGS_FIELDS = ",".join(
    [
        "bibIds",
        "itemIds",
        "inheritLocation",
        "allocationRule",
        "accountingUnit",
        "labelCode",
        "serialCode1",
        "serialCode2",
        "claimOnDate",
        "receivingLocationCode",
        "vendorCode",
        "serialCode3",
        "serialCode4",
        "updateCount",
        "pieceCount",
        "eCheckInCode",
        "mediaTypeCode",
        "updatedDate",
        "createdDate",
        "deletedDate",
        "deleted",
        "suppressed",
        "fixedFields",
        "varFields",
    ]
)

# See https://techdocs.iii.com/sierraapi/Content/zReference/objects/orderObject.htm
ORDERS_FIELDS = ",".join(
    [
        "bibs",
        "updatedDate",
        "createdDate",
        "deletedDate",
        "deleted",
        "suppressed",
        "accountingUnit",
        "estimatedPrice",
        "vendorRecordCode",
        "orderDate",
        "chargedFunds",
        "vendorTitles",
        "fixedFields",
        "varFields",
    ]
)

PATRON_FIELDS = ",".join(
    [
        "id",
        "createdDate",
        "updatedDate",
        "deletedDate",
        "deleted",
        "suppressed",
        "names",
        "barcodes",
        "expirationDate",
        "birthDate",
        "emails",
        "patronType",
        "patronCodes",
        "homeLibraryCode",
        "message",
        "blockInfo",
        "autoBlockInfo",
        "addresses",
        "phones",
        "uniqueIds",
        "moneyOwed",
        "pMessage",
        "langPref",
        "fixedFields",
        "varFields",
    ]
)

HOLD_FIELDS = [
    "id",
    "record",
    "pickupLocation",
    "notNeededAfterDate",
    "note",
    "status",
    "placed",
]
