"""Add column backup_url

Revision ID: 724592c26e5f
Revises: f3d96845189a
Create Date: 2023-06-04 15:08:24.302049

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '724592c26e5f'
down_revision = 'f3d96845189a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('courses', sa.Column('backup_url', sa.String(length=255), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('courses', 'backup_url')
    # ### end Alembic commands ###