"""empty message

Revision ID: 33d6100c4313
Revises: 85dd7574d1ad
Create Date: 2022-01-22 21:42:16.033172

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '33d6100c4313'
down_revision = '85dd7574d1ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'status',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'status',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    # ### end Alembic commands ###
