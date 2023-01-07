from tinydb import TinyDB, Query
from fastapi import FastAPI
import re
from datetime import datetime

db = TinyDB("project.json")
app = FastAPI()


# Date validator func
def date_validator(date):
    """
    :param date:
    :return:
    """
    template = ''
    if '.' in date:
        template = '%d.%m.%Y'
    elif '-' in date:
        template = '%Y-%m-%d'
    try:
        return lambda d: datetime.strptime(d, template).date() <= datetime.today().date()
    except:
        return False


# Main validator func
def validator(value):
    """
    :param value: Takes on a value of field
    :return: Type of value
    """
    if not value:
        return None
    elif '+7' in value:
        regex = r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$'
        if re.fullmatch(regex, value):
            return 'phone'
    elif len(value) == 10:
        if date_validator(value):
            return 'date'
    elif '@' in value:
        regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.fullmatch(regex, value):
            return 'email'
    return 'text'


# Processing path
def processing_path(path):
    """
    :param path: Takes on a path from url
    :return: Processed dict with field name and type of value
    """
    try:
        items = path.split('&')
    except:
        return 'Error with query'
    # Dict with keys and values that processing
    processing = {}
    for item in items:
        try:
            key, value = item.split('=')
            # Field type detection
            processing[key] = validator(value)
        except:
            return 'Error with key/value'
    return processing


@app.post("/get_form/{path}")
def get_item(path):
    # Get dict with key and values to search for matches
    query_dict = processing_path(path)
    # Search for matches in db
    result = db.search(Query().fragment(query_dict))
    if result:
        return result[0]['name']
    else:
        # If no matches return just url attrs in dict form
        return query_dict
