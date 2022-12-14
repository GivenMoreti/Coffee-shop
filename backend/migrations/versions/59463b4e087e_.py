"""empty message

Revision ID: 59463b4e087e
Revises: 
Create Date: 2022-07-16 12:18:58.673100

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59463b4e087e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer', sa.String(), nullable=False),
    sa.Column('order_quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coffee',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('coffee')
    op.drop_table('orders')
    # ### end Alembic commands ###
