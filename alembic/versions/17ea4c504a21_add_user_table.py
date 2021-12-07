"""add user table

Revision ID: 17ea4c504a21
Revises: fd7a91d624b1
Create Date: 2021-12-07 21:28:33.133168

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null


# revision identifiers, used by Alembic.
revision = '17ea4c504a21'
down_revision = 'fd7a91d624b1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()')),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
