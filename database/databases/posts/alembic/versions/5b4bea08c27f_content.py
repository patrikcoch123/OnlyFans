"""content

Revision ID: 5b4bea08c27f
Revises: 194e05269f09
Create Date: 2021-02-04 02:59:05.010106

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b4bea08c27f'
down_revision = '194e05269f09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medias', schema=None) as batch_op:
        batch_op.add_column(sa.Column('preview', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('medias', schema=None) as batch_op:
        batch_op.drop_column('preview')

    # ### end Alembic commands ###
