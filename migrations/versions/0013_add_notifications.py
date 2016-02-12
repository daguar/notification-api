"""empty message

Revision ID: 0013_add_notifications
Revises: 0012_add_status_to_job
Create Date: 2016-02-09 11:14:46.708551

"""

# revision identifiers, used by Alembic.
revision = '0013_add_notifications'
down_revision = '0012_add_status_to_job'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('to', sa.String(), nullable=False),
    sa.Column('job_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('service_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('template_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('sent', 'failed', name='notification_status_types'), nullable=False),
    sa.ForeignKeyConstraint(['job_id'], ['jobs.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['services.id'], ),
    sa.ForeignKeyConstraint(['template_id'], ['templates.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notifications_job_id'), 'notifications', ['job_id'], unique=False)
    op.create_index(op.f('ix_notifications_service_id'), 'notifications', ['service_id'], unique=False)
    op.create_index(op.f('ix_notifications_template_id'), 'notifications', ['template_id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_notifications_template_id'), table_name='notifications')
    op.drop_index(op.f('ix_notifications_service_id'), table_name='notifications')
    op.drop_index(op.f('ix_notifications_job_id'), table_name='notifications')
    op.drop_table('notifications')
    op.get_bind()
    op.execute("drop type notification_status_types")
    ### end Alembic commands ###
