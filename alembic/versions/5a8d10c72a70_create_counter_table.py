"""Create counter table

Revision ID: 5a8d10c72a70
Revises: 
Create Date: 2023-04-19 15:29:57.286206

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a8d10c72a70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table("web_page_counter",
                    sa.Column("id", sa.Integer, primary_key=True,
                              autoincrement=True, unique=True),
                    sa.Column("new_value", sa.Integer),
                    sa.Column("updated_at", sa.DateTime),
                    sa.Column("last_value", sa.Integer)
                    )


def downgrade() -> None:
    op.drop_table('web_page_counter')
