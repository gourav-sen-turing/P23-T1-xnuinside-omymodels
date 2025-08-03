import sqlalchemy as sa
from sqlalchemy import Table, Column, MetaData
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import UniqueConstraint
from sqlalchemy import Index


metadata = MetaData()


table = Table("table", metadata,
        Column(UUID, primary_key=True),
        Column(sa.Integer()),
        UniqueConstraint('one_more_id', name='table_pk'),
        schema="prefix--schema-name")

Index('table_ix2', table.c._id)