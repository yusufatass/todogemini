"""phone number added

Revision ID: 2a8616e9fad9
Revises: 
Create Date: 2026-02-20 18:34:38.947968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2a8616e9fad9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Varsa 'phone' kolonunu siliyoruz (hata vermemesi için batch kullanıyoruz)
    with op.batch_alter_table('users') as batch_op:
        # Eğer 'phone' daha önce eklenmişse onu uçuruyoruz
        batch_op.drop_column('phone') # Bu satırı sadece kolon veritabanında gerçekten varsa kullan

        # Sadece 'phone_number' kalsın
        batch_op.add_column(sa.Column('phone_number', sa.String(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('phone_number')
