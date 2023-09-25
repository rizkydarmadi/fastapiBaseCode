from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    DateTime,
    Table,
)
from sqlalchemy.orm import relationship

from database import Base


class Movie(Base):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    rating = Column(Float, index=True)
    image = Column(String, index=True)
    created_at = Column(DateTime, index=True)
    updated_at = Column(DateTime, index=True)


UserRole = Table(
    "user_role",
    Base.metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("role_id", Integer, ForeignKey("role.id"), nullable=False),
)


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column("email", String, unique=True, nullable=False, index=True)
    username = Column("username", String)
    password = Column("password", String, nullable=False)
    is_active = Column("is_active", Boolean, default=False)
    created_at = Column("created_at", DateTime(timezone=True))
    updated_at = Column("updated_at", DateTime(timezone=True))
    deleted_at = Column("deleted_at", DateTime(timezone=True))

    # Many to Many
    roles = relationship("Role", secondary=UserRole, back_populates="users")


RolePermission = Table(
    "role_permission",
    Base.metadata,
    Column("id", Integer, primary_key=True, nullable=False),
    Column("role_id", Integer, ForeignKey("role.id"), nullable=False),
    Column("permission_id", Integer, ForeignKey("permission.id"), nullable=False),
)


class Role(Base):
    __tablename__ = "role"

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String(length=80), nullable=False)

    # Many to Many
    users = relationship("User", secondary=UserRole, back_populates="roles")
    permissions = relationship(
        "Permission", secondary=RolePermission, back_populates="roles"
    )


class Permission(Base):
    __tablename__ = "permission"

    id = Column("id", Integer, primary_key=True, nullable=False)
    module_id = Column("module_id", ForeignKey("module.id"), nullable=True)
    name = Column("name", String, nullable=False)

    # Many to Many
    # users = relationship("UserPermission", back_populates="permission")
    roles = relationship("Role", secondary=RolePermission, back_populates="permissions")


class Module(Base):
    __tablename__ = "module"

    id = Column("id", Integer, primary_key=True, nullable=False)
    name = Column("name", String, nullable=False)
