"""create projects table

Revision ID: eb7cb157afda
Revises: b0fd2d114b13
Create Date: 2023-10-23 14:09:07.425955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb7cb157afda'
down_revision = 'b0fd2d114b13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('projectId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('deadline', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('statusId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['statusId'], ['status.statusId'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('projectId')
    )
    op.create_index(op.f('ix_projects_name'), 'projects', ['name'], unique=False)
    op.alter_column('status', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_constraint(None, 'status', type_='foreignkey')
    op.alter_column('task', 'projectId',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('task', 'statusId',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.create_foreign_key(None, 'task', 'projects', ['projectId'], ['projectId'])
    op.create_foreign_key(None, 'task', 'status', ['statusId'], ['statusId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.alter_column('task', 'statusId',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('task', 'projectId',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_foreign_key(None, 'status', 'task', ['description'], ['description'])
    op.alter_column('status', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_index(op.f('ix_projects_name'), table_name='projects')
    op.drop_table('projects')
    # ### end Alembic commands ###
