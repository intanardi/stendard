"""empty message

Revision ID: 91c3c6f11d03
Revises: 
Create Date: 2022-04-03 11:32:25.952681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91c3c6f11d03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('files',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('filename', sa.String(length=128), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('files')
    # ### end Alembic commands ###
