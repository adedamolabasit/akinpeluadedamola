"""empty message

Revision ID: ea7928430607
Revises: 82a72151075c
Create Date: 2022-04-10 17:21:48.470346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea7928430607'
down_revision = '82a72151075c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=32), nullable=True),
    sa.Column('note', sa.String(length=152), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('image_link', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    # ### end Alembic commands ###
