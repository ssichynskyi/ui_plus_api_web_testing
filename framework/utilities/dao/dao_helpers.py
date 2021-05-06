from typing import Iterable, List, Tuple, Optional, Dict, Union
from framework.utilities.dao.exceptions import ObjectSerializationError
from framework.utilities.db_connector import db


def serialize(obj, attributes: Iterable[str]) -> None:
    """Forced initialization of object properties listed in "attributes" arg

    Args:
        obj: object to try serialization on
        attributes: list of attribute names to serialize

    Returns:
        None

    Raises:
        ObjectSerializationError

    """
    for attribute in attributes:
        if not attribute.startswith('_'):
            try:
                getattr(obj, attribute)
            except (KeyError, AttributeError) as e:
                msg = f'Unable to serialize attribute: "{attribute}" in object type: "{type(obj)}'
                raise ObjectSerializationError(msg) from e


def generate_objs_from_sql_query(query: str, serialize_to: type) -> Union[List[object], None]:
    """Get data from DB using query and serialize

    Args:
        query: query string to execute on DB
        serialize_to: type of the object that shall serialize the query result

    Returns:
        List of serialized objects
    """
    data = db.execute_sql(query)
    results = list(map(serialize_to, data))
    for result in results:
        serialize(result, dir(result))
    return results


def build_sql_query(
        table: str,
        columns: Tuple[str] = '*',
        filter_criteria: Optional[Dict] = None,
        order_by: Tuple[str] = ('id', 'ASC')
) -> str:
    """Builds simplified SQL query based on params

    Args:
        table: name of the table
        columns: name of the columns to return
        filter_criteria: WHERE '=' criteria joined by 'AND'
        order_by: ORDER BY tuple. Must end with either 'ASC' or 'DESC'

    Limitations:
        supports only SELECT, FROM, WHERE, ORDER BY
        for WHERE criteria provides only '=' criterion and 'AND' joiner

    Returns:
        SQL query string

    """
    if order_by[-1] not in ('ASC', 'DESC'):
        order_by = list(order_by).append('ASC')
    query = f'SELECT {", ".join(columns)} FROM {table} %s ORDER BY {", ".join(order_by[:-1])} {order_by[-1]};'
    if filter_criteria:
        params = [f'{k}=\'{str(v)}\'' for k, v in filter_criteria.items()]
        where_params = f'WHERE {" AND ".join(params)}'
    else:
        where_params = ''
    return query.replace('%s', where_params)


def generate_dao_objects(
        serialize_to: type,
        table: str,
        columns: Optional[Tuple[str]] = '*',
        filter_criteria: Optional[Dict] = None,
        order_by: Tuple = ('id', 'ASC')
) -> List:
    """Combines functions build_sql_query() and generate_objs_from_sql_query()"""
    sql_query = build_sql_query(table, columns, filter_criteria, order_by)
    return generate_objs_from_sql_query(sql_query, serialize_to)
