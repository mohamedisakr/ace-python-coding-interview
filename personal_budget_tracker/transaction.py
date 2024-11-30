from datetime import datetime


class Transaction:
    def __init__(self, date, category, amount, description):
        # Validate the date
        try:
            datetime.strptime(
                date, "%Y-%m-%d") or datetime.strptime(date, "%Y/%m/%d")
        except ValueError:
            raise ValueError(f"Invalid date format: {date}")
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description

# except Exception as error:
#     raise GetPipelinesError(json.dumps(       {"httpStatus": 400, "message": "Unable to fetch Pipelines"})) from error
