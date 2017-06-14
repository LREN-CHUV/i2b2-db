"""use sequences for encounter and patient IDs

Revision ID: 0bde60e6657f
Revises: 1bf70b8d9122
Create Date: 2017-06-14 16:43:26.102471

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bde60e6657f'
down_revision = '1bf70b8d9122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('encounter_mapping', 'encounter_num',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_index('em_idx_encpath', table_name='encounter_mapping')
    op.drop_index('ix_encounter_mapping_encounter_num', table_name='encounter_mapping')
    op.drop_constraint('patient_mapping_patient_num_key', 'patient_mapping', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('patient_mapping_patient_num_key', 'patient_mapping', ['patient_num'])
    op.create_index('ix_encounter_mapping_encounter_num', 'encounter_mapping', ['encounter_num'], unique=False)
    op.create_index('em_idx_encpath', 'encounter_mapping', ['encounter_ide', 'encounter_ide_source', 'patient_ide', 'patient_ide_source', 'encounter_num'], unique=False)
    op.alter_column('encounter_mapping', 'encounter_num',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###