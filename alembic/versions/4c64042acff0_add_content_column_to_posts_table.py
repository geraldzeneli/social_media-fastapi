"""add content column to posts table

Revision ID: 4c64042acff0
Revises: ff0571eca049
Create Date: 2023-02-28 20:35:29.068078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c64042acff0'
down_revision = 'ff0571eca049'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
