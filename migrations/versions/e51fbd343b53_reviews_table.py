"""reviews table

Revision ID: e51fbd343b53
Revises: 
Create Date: 2019-07-29 10:24:35.440217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e51fbd343b53'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('roomnumber', sa.String(), nullable=True),
    sa.Column('admissionnumber', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(length=13), nullable=True),
    sa.Column('review', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_review_admissionnumber'), 'review', ['admissionnumber'], unique=False)
    op.create_index(op.f('ix_review_mobile'), 'review', ['mobile'], unique=False)
    op.create_index(op.f('ix_review_name'), 'review', ['name'], unique=False)
    op.create_index(op.f('ix_review_review'), 'review', ['review'], unique=False)
    op.create_index(op.f('ix_review_roomnumber'), 'review', ['roomnumber'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_review_roomnumber'), table_name='review')
    op.drop_index(op.f('ix_review_review'), table_name='review')
    op.drop_index(op.f('ix_review_name'), table_name='review')
    op.drop_index(op.f('ix_review_mobile'), table_name='review')
    op.drop_index(op.f('ix_review_admissionnumber'), table_name='review')
    op.drop_table('review')
    # ### end Alembic commands ###
