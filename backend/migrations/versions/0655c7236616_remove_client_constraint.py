"""remove client constraint

Revision ID: 0655c7236616
Revises: df334b758549
Create Date: 2016-11-26 16:19:51.943335

"""

# revision identifiers, used by Alembic.
revision = '0655c7236616'
down_revision = 'df334b758549'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('clients_name_company_id_key', 'clients', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('clients_name_company_id_key', 'clients', ['name', 'company_id'])
    ### end Alembic commands ###
