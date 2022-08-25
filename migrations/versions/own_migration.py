"""Added new field

Revision ID: 7477ff3af8f4
Revises: c9706ba50cc2
Create Date: 2022-08-24 08:58:45.718070

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '7477ff3af8f5'
down_revision = '7477ff3af8f4'
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            '''
            UPDATE films
            SET test = 100
            WHERE title like "%Deathly%"
            '''
        )
    )


def downgrade():
    conn = op.get_bind()
    conn.execute(
        text(
            '''
            UPDATE films
            SET test = NULL
            WHERE title like "%Deathly%"
            '''
        )
    )
