"""empty message

Revision ID: 4bf5848287c
Revises: f12eff482d6f
Create Date: 2016-11-30 10:59:53.134602

"""

# revision identifiers, used by Alembic.
revision = '4bf5848287c'
down_revision = 'f12eff482d6f'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('companies', sa.Column('trial_expiry_date_override', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('companies', 'trial_expiry_date_override')
    ### end Alembic commands ###