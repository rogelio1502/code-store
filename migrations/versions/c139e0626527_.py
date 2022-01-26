"""empty message

Revision ID: c139e0626527
Revises: 4001f406e5b3
Create Date: 2022-01-25 22:10:36.385984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c139e0626527'
down_revision = '4001f406e5b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('categories', sa.Column('status', sa.Boolean(), server_default='1', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('categories', 'status')
    # ### end Alembic commands ###