# revision identifiers, used by Alembic.
revision = "2dade673f10e"
down_revision = "1d8eda758ba6"

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column("flights", sa.Column("qnh", sa.Float(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("flights", "qnh")
    ### end Alembic commands ###
