"""update membership type.

Revision ID: 93ba1db65ed3
Revises: 70d2fe46051f
Create Date: 2019-12-04 10:08:40.118775

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ba1db65ed3'
down_revision = '70d2fe46051f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('membership_type', sa.Column('icon', sa.String(length=100), nullable=True))
    op.add_column('membership_type', sa.Column('label', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###

    # Update all existing user records to active
    op.execute('update "membership_type" set icon=\'mdi-account\', label=\'can add businesses, and file for a business.\' where code=\'MEMBER\'')
    op.execute('update "membership_type" set icon=\'mdi-settings\', label=\'can add/remove team members, add businesses, and file for a business.\' where code=\'ADMIN\'')
    op.execute('update "membership_type" set icon=\'mdi-shield-key\', label=\'can add/remove team members and businesses, and file for a business.\' where code=\'OWNER\'')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('membership_type', 'label')
    op.drop_column('membership_type', 'icon')
    # ### end Alembic commands ###
