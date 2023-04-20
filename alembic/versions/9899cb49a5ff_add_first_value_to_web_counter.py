"""add first value to web_counter

Revision ID: 9899cb49a5ff
Revises: 5a8d10c72a70
Create Date: 2023-04-19 15:58:29.788964

"""
from alembic import op
from datetime import datetime 
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9899cb49a5ff'
down_revision = '5a8d10c72a70'
branch_labels = None
depends_on = None


def upgrade() -> None:
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    op.execute(f"""INSERT INTO web_page_counter(new_value,last_value, updated_at)
                                 VALUES (0, 0,'{now}')""")



def downgrade() -> None:
    pass
