"""empty message

Revision ID: a7bef2284b0b
Revises: 
Create Date: 2023-11-23 14:44:47.950762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7bef2284b0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('creation_date', sa.DateTime(), nullable=False),
    sa.Column('done', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_Task_title'), ['title'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Task', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_Task_title'))

    op.drop_table('Task')
    # ### end Alembic commands ###
