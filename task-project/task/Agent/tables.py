import django_tables2 as tables

data = [
    {
    "agentID": "1",
    "agentName": "Drona",
    "agentOccupation": "VP Marketing",
    "agency": "Terry Group",
    "mobile_no": "495-254-7744",
    "address": "441 Crest Line Court",
    "latitude": "-13.3023564",
    "longitude": "35.2478112"
    }
]

class NameTable(tables.Table):
    name = tables.Column()

table = NameTable(data)