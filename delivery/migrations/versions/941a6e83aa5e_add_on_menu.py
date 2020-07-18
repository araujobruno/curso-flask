"""add on_menu

Revision ID: 941a6e83aa5e
Revises: 
Create Date: 2020-07-17 17:58:13.514142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '941a6e83aa5e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('on_menu', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'on_menu')
    # ### end Alembic commands ###