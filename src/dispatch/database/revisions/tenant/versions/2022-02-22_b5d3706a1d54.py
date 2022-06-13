"""Adds models to support first class support for data sources and queries.

Revision ID: b5d3706a1d54
Revises: ce5c4ac967d8
Create Date: 2022-02-22 10:03:21.866998

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = "b5d3706a1d54"
down_revision = "ce5c4ac967d8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "source_data_format",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_data_format_search_vector_idx",
        "source_data_format",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "source_environment",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_environment_search_vector_idx",
        "source_environment",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "source_status",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_status_search_vector_idx",
        "source_status",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "source_transport",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_transport_search_vector_idx",
        "source_transport",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "source_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_type_search_vector_idx",
        "source_type",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "source",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("cost", sa.Integer(), nullable=True),
        sa.Column("data_last_loaded_at", sa.DateTime(), nullable=True),
        sa.Column("daily_volume", sa.Integer(), nullable=True),
        sa.Column("aggregated", sa.Boolean(), nullable=True),
        sa.Column("retention", sa.Integer(), nullable=True),
        sa.Column("size", sa.BigInteger(), nullable=True),
        sa.Column("delay", sa.Integer(), nullable=True),
        sa.Column("environment", sa.String(), nullable=True),
        sa.Column("external_id", sa.String(), nullable=True),
        sa.Column("documentation", sa.Text(), nullable=True),
        sa.Column("sampling_rate", sa.Integer(), nullable=True),
        sa.Column("source_schema", sa.Text(), nullable=True),
        sa.Column("links", sa.JSON(), nullable=True),
        sa.Column("source_type_id", sa.Integer(), nullable=True),
        sa.Column("source_status_id", sa.Integer(), nullable=True),
        sa.Column("source_environment_id", sa.Integer(), nullable=True),
        sa.Column("source_data_format_id", sa.Integer(), nullable=True),
        sa.Column("source_transport_id", sa.Integer(), nullable=True),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["service.id"],
        ),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["source_data_format_id"],
            ["source_data_format.id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_environment_id"],
            ["source_environment.id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_status_id"],
            ["source_status.id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_transport_id"],
            ["source_transport.id"],
        ),
        sa.ForeignKeyConstraint(
            ["source_type_id"],
            ["source_type.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "project_id"),
    )
    op.create_index(
        "source_search_vector_idx",
        "source",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.create_table(
        "alert",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("orginator", sa.String(), nullable=True),
        sa.Column("external_link", sa.String(), nullable=True),
        sa.Column("source_id", sa.Integer(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["source.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "alert_search_vector_idx", "alert", ["search_vector"], unique=False, postgresql_using="gin"
    )
    op.create_table(
        "assoc_source_tags",
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["source_id"], ["source.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["tag_id"], ["tag.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("source_id", "tag_id"),
    )
    op.create_table(
        "query",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("text", sa.String(), nullable=True),
        sa.Column("language", sa.String(), nullable=True),
        sa.Column("source_id", sa.Integer(), nullable=True),
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["source.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "query_search_vector_idx", "query", ["search_vector"], unique=False, postgresql_using="gin"
    )
    op.create_table(
        "assoc_query_tags",
        sa.Column("query_id", sa.Integer(), nullable=False),
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["query_id"], ["query.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["tag_id"], ["tag.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("query_id", "tag_id"),
    )
    op.create_table(
        "assoc_query_incidents",
        sa.Column("query_id", sa.Integer(), nullable=False),
        sa.Column("incident_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["incident_id"], ["incident.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["query_id"], ["query.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("query_id", "incident_id"),
    )
    op.create_table(
        "assoc_source_incidents",
        sa.Column("source_id", sa.Integer(), nullable=False),
        sa.Column("incident_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["incident_id"], ["incident.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["source_id"], ["source.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("source_id", "incident_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("assoc_source_incidents")
    op.drop_table("assoc_query_incidents")
    op.drop_table("assoc_query_tags")
    op.drop_index("query_search_vector_idx", table_name="query", postgresql_using="gin")
    op.drop_table("query")
    op.drop_table("assoc_source_tags")
    op.drop_index("alert_search_vector_idx", table_name="alert", postgresql_using="gin")
    op.drop_table("alert")
    op.drop_index("source_search_vector_idx", table_name="source", postgresql_using="gin")
    op.drop_table("source")
    op.drop_index("source_type_search_vector_idx", table_name="source_type", postgresql_using="gin")
    op.drop_table("source_type")
    op.drop_index(
        "source_transport_search_vector_idx", table_name="source_transport", postgresql_using="gin"
    )
    op.drop_table("source_transport")
    op.drop_index(
        "source_status_search_vector_idx", table_name="source_status", postgresql_using="gin"
    )
    op.drop_table("source_status")
    op.drop_index(
        "source_environment_search_vector_idx",
        table_name="source_environment",
        postgresql_using="gin",
    )
    op.drop_table("source_environment")
    op.drop_index(
        "source_data_format_search_vector_idx",
        table_name="source_data_format",
        postgresql_using="gin",
    )
    op.drop_table("source_data_format")
    # ### end Alembic commands ###
