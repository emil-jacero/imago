"""empty message

Revision ID: 9524669c8505
Revises: 
Create Date: 2019-03-24 13:48:51.590823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9524669c8505'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('release',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('distro', sa.String(length=100), nullable=False),
    sa.Column('release', sa.String(length=100), nullable=False),
    sa.Column('company', sa.String(length=60), nullable=False),
    sa.Column('datetime_added', sa.DateTime(), nullable=True),
    sa.Column('datetime_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('release')
    # ### end Alembic commands ###
