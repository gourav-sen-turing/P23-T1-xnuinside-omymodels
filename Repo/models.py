import sqlalchemy as sa
from sqlalchemy import Table, Column, MetaData


metadata = MetaData()


materials = Table("materials", metadata,
        Column(sa.Integer(), primary_key=True),
        Column(sa.String(), nullable=False),
        Column(sa.String()),
        Column(sa.String()),
        Column(sa.TIMESTAMP()),
        Column(sa.TIMESTAMP()),
)


material_attachments = Table("material_attachments", metadata,
        Column(sa.Integer(), sa.ForeignKey('materials.id')),
        Column(sa.Integer(), sa.ForeignKey('attachments.id')),
        schema="schema_name")


attachments = Table("attachments", metadata,
        Column(sa.Integer(), primary_key=True),
        Column(sa.String()),
        Column(sa.String()),
        Column(sa.TIMESTAMP()),
        Column(sa.TIMESTAMP()),
)
