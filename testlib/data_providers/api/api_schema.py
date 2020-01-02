APPLICATION_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "customId": {
            "type": "string"
        },
        "name": {
            "type": "string"
        },
        "description": {
            "type": "string"
        },
        "version": {
            "type": "string"
        },
        "ownerId": {
            "type": "null"
        },
        "availability": {
            "type": "string"
        },
        "connectivityMethod": {
            "type": "null"
        },
        "timeouts": {
            "type": "null"
        }
    },
    "required": [
        "id",
        "customId",
        "name",
        "description",
        "version",
        "ownerId",
        "availability",
        "connectivityMethod",
        "timeouts"
    ]
}

CURRENT_APPLICATIONS_SCHEMA = {
    "type": "object",
    "properties": {
        "paging": {
            "type": "object",
            "properties": {
                "totalItemsCount": {
                    "type": "integer"
                },
                "page": {
                    "type": "integer"
                },
                "take": {
                    "type": "integer"
                }
            },
            "required": [
                "totalItemsCount",
                "page",
                "take"
            ]
        },
        "sort": {
            "type": "object",
            "properties": {
                "sortByField": {
                    "type": "string"
                },
                "column": {
                    "type": "string"
                },
                "sort": {
                    "type": "integer"
                }
            },
            "required": [
                "sortByField",
                "column",
                "sort"
            ]
        },
        "items": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "id": {
                            "type": "integer"
                        },
                        "customId": {
                            "type": "string"
                        },
                        "description": {
                            "type": "string"
                        },
                        "version": {
                            "type": "string"
                        },
                        "owner": {
                            "type": "null"
                        },
                        "availability": {
                            "type": "string"
                        },
                        "connectivityMethod": {
                            "type": "null"
                        },
                        "timeouts": {
                            "type": "string"
                        },
                        "deleted": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "name",
                        "id",
                        "customId",
                        "description",
                        "version",
                        "owner",
                        "availability",
                        "connectivityMethod",
                        "timeouts",
                        "deleted"
                    ]
                }
            ]
        }

    },
    "required": [
        "paging",
        "sort",
        "items"
    ]
}
