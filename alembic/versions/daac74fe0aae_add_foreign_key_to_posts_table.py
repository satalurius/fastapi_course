"""add foreign-key to posts table

Revision ID: daac74fe0aae
Revises: 17ea4c504a21
Create Date: 2021-12-07 21:33:31.005413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'daac74fe0aae'
down_revision = '17ea4c504a21'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users",
                             local_cols=['owner_id'],
                              remote_cols=['id'],
                               ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
