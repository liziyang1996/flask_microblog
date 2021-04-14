"""new field in user modle

Revision ID: 716542a62ff0
Revises: 55ba2eb44bd9
Create Date: 2021-04-13 21:34:45.881737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '716542a62ff0'
down_revision = '55ba2eb44bd9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
