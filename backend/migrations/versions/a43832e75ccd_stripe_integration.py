"""Stripe integration

Revision ID: a43832e75ccd
Revises: 656ea2856531
Create Date: 2017-02-10 20:14:40.253879

"""

# revision identifiers, used by Alembic.
revision = 'a43832e75ccd'
down_revision = '656ea2856531'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stripe_integrations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=512), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('company_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_stripe_integrations_company_id'), 'stripe_integrations', ['company_id'], unique=False)
    op.execute('COMMIT')  # See https://bitbucket.org/zzzeek/alembic/issue/123
    op.execute("ALTER TYPE \"BlockTypeEnum\" ADD value 'payment' after 'h3'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stripe_integrations_company_id'), table_name='stripe_integrations')
    op.drop_table('stripe_integrations')
    # ### end Alembic commands ###