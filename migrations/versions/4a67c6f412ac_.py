"""empty message

Revision ID: 4a67c6f412ac
Revises: 

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a67c6f412ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logmessages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('component', sa.String(length=128), nullable=False),
    sa.Column('level', sa.SmallInteger(), server_default=sa.text('0'), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('checker_script', sa.String(), nullable=False),
    sa.Column('checker_timeout', sa.Integer(), server_default=sa.text('30'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('submitted_flags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('submitted_by', sa.SmallInteger(), nullable=False),
    sa.Column('team_id', sa.SmallInteger(), nullable=False),
    sa.Column('service_id', sa.SmallInteger(), nullable=False),
    sa.Column('expires', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('ts', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('submitted_by', 'team_id', 'service_id', 'expires', name='submitted_flags_unique_1')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('checker_results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.SmallInteger(), nullable=False),
    sa.Column('service_id', sa.SmallInteger(), nullable=False),
    sa.Column('status', sa.String(length=12), nullable=False),
    sa.Column('message', sa.String(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('time', sa.Float(), server_default=sa.text('NULL'), nullable=True),
    sa.Column('integrity', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('stored', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('retrieved', sa.Boolean(), server_default=sa.text('FALSE'), nullable=False),
    sa.Column('celery_id', sa.String(length=40), nullable=False),
    sa.Column('output', sa.String(), server_default=sa.text('NULL'), nullable=True),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('round', 'team_id', 'service_id', name='checker_results_unique_1')
    )
    op.create_table('team_points',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.SmallInteger(), nullable=False),
    sa.Column('service_id', sa.SmallInteger(), nullable=False),
    sa.Column('flag_points', sa.Integer(), nullable=False),
    sa.Column('sla_points', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('round', 'team_id', 'service_id', name='team_points_unique_1')
    )
    op.create_table('team_rankings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('round', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.SmallInteger(), nullable=False),
    sa.Column('rank', sa.Integer(), nullable=False),
    sa.Column('points', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('round', 'team_id', name='team_rankings_unique_1')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_rankings')
    op.drop_table('team_points')
    op.drop_table('checker_results')
    op.drop_table('teams')
    op.drop_table('submitted_flags')
    op.drop_table('services')
    op.drop_table('logmessages')
    # ### end Alembic commands ###
