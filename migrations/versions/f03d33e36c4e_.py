"""empty message

Revision ID: f03d33e36c4e
Revises: 
Create Date: 2022-04-06 14:53:25.865478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f03d33e36c4e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('twitter_link', sa.Text(), nullable=True),
    sa.Column('facebook_link', sa.Text(), nullable=True),
    sa.Column('instagram_link', sa.Text(), nullable=True),
    sa.Column('linkdin', sa.Text(), nullable=True),
    sa.Column('picture', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###
