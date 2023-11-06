from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()


task = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("text", String, nullable=False),
    Column("user", String, nullable=False, default='Val'),
    Column("done_type", String, nullable=False, default='not_started'),
)
