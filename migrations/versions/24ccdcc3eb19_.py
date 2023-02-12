"""ADD User table
Revision ID: 24ccdcc3eb19
Revises:
Create Date: 2023-02-13 13:51:20.756705
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24ccdcc3eb19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'user',
        sa.Column('user_id', sa.String(length=100), nullable=False),
        sa.Column('username', sa.String(length=20), nullable=False),
        sa.Column('password', sa.String(length=120), nullable=False),
        sa.PrimaryKeyConstraint('user_id'),
        sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
