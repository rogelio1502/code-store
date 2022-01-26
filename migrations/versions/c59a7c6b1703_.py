"""empty message

Revision ID: c59a7c6b1703
Revises: 8d077d83ca5c
Create Date: 2022-01-25 21:58:19.113525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c59a7c6b1703'
down_revision = '8d077d83ca5c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('added_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'categories', 'user', ['added_by'], ['id'])
    op.add_column('user', sa.Column('phone_number', sa.String(length=10), nullable=True))
    op.alter_column('user', 'last_name',
               existing_type=mysql.VARCHAR(length=75),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=70),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=150),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=150),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=70),
               nullable=True)
    op.alter_column('user', 'last_name',
               existing_type=mysql.VARCHAR(length=75),
               nullable=True)
    op.drop_column('user', 'phone_number')
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'added_by')
    # ### end Alembic commands ###