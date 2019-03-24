"""empty message

Revision ID: 12c7d91346fc
Revises: 9524669c8505
Create Date: 2019-03-24 14:56:44.119756

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12c7d91346fc'
down_revision = '9524669c8505'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('build', sa.String(length=40), nullable=True),
    sa.Column('uuid', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('sha256', sa.String(length=200), nullable=True),
    sa.Column('archive_path', sa.String(length=200), nullable=True),
    sa.Column('archive_filename', sa.String(length=200), nullable=True),
    sa.Column('file_suffix', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('datetime_added', sa.DateTime(), nullable=True),
    sa.Column('datetime_modified', sa.DateTime(), nullable=True),
    sa.Column('release_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['release_id'], ['release.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    # ### end Alembic commands ###