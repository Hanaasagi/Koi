from koi.querybuilder.query import Query
from koi.querybuilder.builder import Table


def test_select():
    students = Table('students')
    q = Query.from_(students).select(students.id, students.name)
    assert q.to_sql() == 'SELECT id,name FROM students'
