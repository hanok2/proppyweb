"""CRM clients

Revision ID: ef7d5195ae7d
Revises: e77bb317b569
Create Date: 2016-11-24 22:22:38.453970

"""

# revision identifiers, used by Alembic.
revision = 'ef7d5195ae7d'
down_revision = 'e77bb317b569'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts_integrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('source', sa.String(length=512), nullable=False),
    sa.Column('contacts', postgresql.JSONB(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_integrations_company_id'), 'contacts_integrations', ['company_id'], unique=False)
    op.create_table('insightly_integrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_key', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_insightly_integrations_company_id'), 'insightly_integrations', ['company_id'], unique=False)
    op.create_table('pipedrive_integrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('api_token', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pipedrive_integrations_company_id'), 'pipedrive_integrations', ['company_id'], unique=False)
    op.create_table('zohocrm_integrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('auth_token', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_zohocrm_integrations_company_id'), 'zohocrm_integrations', ['company_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_zohocrm_integrations_company_id'), table_name='zohocrm_integrations')
    op.drop_table('zohocrm_integrations')
    op.drop_index(op.f('ix_pipedrive_integrations_company_id'), table_name='pipedrive_integrations')
    op.drop_table('pipedrive_integrations')
    op.drop_index(op.f('ix_insightly_integrations_company_id'), table_name='insightly_integrations')
    op.drop_table('insightly_integrations')
    op.drop_index(op.f('ix_contacts_integrations_company_id'), table_name='contacts_integrations')
    op.drop_table('contacts_integrations')
    ### end Alembic commands ###