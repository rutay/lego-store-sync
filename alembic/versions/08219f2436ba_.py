"""empty message

Revision ID: 08219f2436ba
Revises: 7017f4f7e5b1
Create Date: 2021-11-13 19:15:19.651855

"""
from alembic import op
import sqlalchemy as sa


revision = '08219f2436ba'
down_revision = '7017f4f7e5b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('op', sa.Column('id_parent', sa.Integer(), nullable=True))
    op.add_column('op', sa.Column('invoked_at', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'op', 'op', ['id_parent'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'op', type_='foreignkey')
    op.drop_column('op', 'invoked_at')
    op.drop_column('op', 'id_parent')
    # ### end Alembic commands ###
