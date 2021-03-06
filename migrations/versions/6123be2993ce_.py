"""empty message

Revision ID: 6123be2993ce
Revises: 9e58d6057004
Create Date: 2022-01-25 22:01:21.563797

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6123be2993ce'
down_revision = '9e58d6057004'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'added_by',
               existing_type=mysql.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'added_by',
               existing_type=mysql.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
