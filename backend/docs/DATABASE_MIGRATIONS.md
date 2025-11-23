# Database Migrations Guide

## Overview

Job-o-matic uses [Alembic](https://alembic.sqlalchemy.org/) for database schema migrations. Alembic provides automatic migration generation, version control, and safe schema evolution for PostgreSQL databases.

## Current Status

**Latest Migration:** `3fab9ff6e7ab` - initial schema
**Database:** PostgreSQL 16
**Tables:** 8 (users, companies, jobs, applications, application_status_history, cover_letters, search_queries, activity_logs)

---

## Quick Reference

### Check Current Migration Version
```bash
cd backend
uv run alembic current
```

### Apply All Pending Migrations
```bash
uv run alembic upgrade head
```

### Rollback One Migration
```bash
uv run alembic downgrade -1
```

### Generate New Migration (Auto-detect Changes)
```bash
uv run alembic revision --autogenerate -m "description of changes"
```

### View Migration History
```bash
uv run alembic history
```

---

## Configuration

### Database URL

Alembic uses the database URL from environment variables or `alembic.ini`:

**Environment Variable (Recommended):**
```bash
export DB_DATABASE_URL="postgresql+asyncpg://jobuser:password@localhost:5432/jobmanager"
```

**Default from alembic.ini:**
```
sqlalchemy.url = postgresql+asyncpg://jobuser:password@localhost:5432/jobmanager
```

### Migration File Naming

Configured in `alembic.ini`:
```
file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
```

Example: `2025_11_23_1240-3fab9ff6e7ab_initial_schema.py`

---

## Common Workflows

### 1. Creating a New Migration

#### Option A: Auto-generate from Model Changes (Recommended)

1. **Modify your SQLAlchemy models** in `src/models/database.py`

2. **Generate migration:**
   ```bash
   uv run alembic revision --autogenerate -m "add user preferences field"
   ```

3. **Review the generated migration file** in `alembic/versions/`
   - Check that changes are correct
   - Alembic may miss some changes (indexes, constraints)
   - Manually add any missing operations

4. **Test the migration:**
   ```bash
   # Apply migration
   uv run alembic upgrade head

   # Verify schema
   psql -U jobuser -d jobmanager -c "\d users"

   # Test rollback
   uv run alembic downgrade -1
   uv run alembic upgrade head
   ```

#### Option B: Manual Migration

For complex changes (data migrations, custom SQL):

```bash
uv run alembic revision -m "migrate application statuses"
```

Edit the generated file:
```python
def upgrade() -> None:
    # Add your SQL or SQLAlchemy operations
    op.execute("""
        UPDATE applications
        SET status = 'submitted'
        WHERE status = 'applied'
    """)

def downgrade() -> None:
    # Reverse the operation
    op.execute("""
        UPDATE applications
        SET status = 'applied'
        WHERE status = 'submitted'
    """)
```

### 2. Applying Migrations

#### Development
```bash
# Apply all pending migrations
uv run alembic upgrade head

# Apply one migration forward
uv run alembic upgrade +1

# Upgrade to specific revision
uv run alembic upgrade 3fab9ff6e7ab
```

#### Production

**IMPORTANT:** Always backup before running migrations in production!

```bash
# 1. Backup database
pg_dump -U jobuser jobmanager > backup_$(date +%Y%m%d_%H%M%S).sql

# 2. Test migration in staging environment first

# 3. Apply migration with downtime window
uv run alembic upgrade head

# 4. Verify application functionality

# 5. If issues occur, rollback:
uv run alembic downgrade -1
```

### 3. Rolling Back Migrations

```bash
# Rollback one migration
uv run alembic downgrade -1

# Rollback to specific revision
uv run alembic downgrade 3fab9ff6e7ab

# Rollback all migrations (dangerous!)
uv run alembic downgrade base
```

---

## Best Practices

### ✅ DO

1. **Always review auto-generated migrations**
   - Alembic can't detect all changes
   - May generate incorrect operations
   - Verify column types, constraints, indexes

2. **Test migrations thoroughly**
   ```bash
   # Test upgrade
   uv run alembic upgrade head

   # Test downgrade
   uv run alembic downgrade -1

   # Test upgrade again
   uv run alembic upgrade head
   ```

3. **Write reversible migrations**
   - Every `upgrade()` should have a corresponding `downgrade()`
   - Document any irreversible operations

4. **Use transactions for data migrations**
   ```python
   def upgrade() -> None:
       connection = op.get_bind()
       # Operations are automatically in a transaction
       connection.execute("""...""")
   ```

5. **Version control migrations**
   - Commit migration files to git
   - Never modify applied migrations
   - Create new migration instead

6. **Document complex migrations**
   ```python
   """add user preferences

   This migration adds a JSONB preferences column to store user settings:
   - theme (light/dark)
   - email_notifications (bool)
   - job_alerts_frequency (daily/weekly)
   """
   ```

### ❌ DON'T

1. **Don't edit applied migrations**
   - Create new migration to fix issues
   - Old migrations may already be applied in production

2. **Don't skip migrations**
   - Apply migrations in order
   - Don't cherry-pick specific migrations

3. **Don't use DROP TABLE without backup**
   ```python
   # Bad
   op.drop_table('old_table')

   # Better
   op.rename_table('old_table', 'old_table_backup')
   ```

4. **Don't mix DDL and DML without testing**
   - Schema changes (DDL) and data changes (DML) can cause issues
   - Test on realistic dataset

5. **Don't forget indexes**
   ```python
   # Alembic may not detect index changes
   # Manually add them:
   op.create_index('idx_user_email', 'users', ['email'])
   ```

---

## Migration File Structure

```python
"""descriptive message

Revision ID: 3fab9ff6e7ab
Revises: previous_revision_id
Create Date: 2025-11-23 12:40:14.444108
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# Revision identifiers
revision: str = "3fab9ff6e7ab"
down_revision: Union[str, None] = None  # Previous migration
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Apply migration changes."""
    # Create tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), nullable=False),
    )

    # Add columns
    op.add_column('users', sa.Column('verified', sa.Boolean()))

    # Modify columns
    op.alter_column('users', 'email', nullable=False)

    # Create indexes
    op.create_index('idx_user_email', 'users', ['email'])


def downgrade() -> None:
    """Reverse migration changes."""
    op.drop_index('idx_user_email', 'users')
    op.drop_column('users', 'verified')
    op.drop_table('users')
```

---

## Troubleshooting

### Migration Failed

```bash
# Check error message
uv run alembic upgrade head

# Common issues:
# 1. Database connection error
psql -U jobuser -d jobmanager -c "SELECT 1"

# 2. Conflicting changes
uv run alembic current
uv run alembic history

# 3. Manual intervention needed
psql -U jobuser -d jobmanager
# Fix schema manually
# Update alembic_version table if needed
```

### Alembic Version Table Out of Sync

```sql
-- Check current version in database
SELECT * FROM alembic_version;

-- Manually set version (use with caution!)
UPDATE alembic_version SET version_num = '3fab9ff6e7ab';
```

### Reset Alembic (Development Only)

```bash
# WARNING: This destroys all data!

# 1. Drop all tables
psql -U jobuser -d jobmanager -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

# 2. Reapply migrations
uv run alembic upgrade head
```

---

## Advanced Topics

### Data Migrations

For complex data transformations:

```python
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

def upgrade() -> None:
    # Create temporary table representation
    applications = table(
        'applications',
        column('id', sa.Integer),
        column('old_status', sa.String),
        column('new_status', sa.String),
    )

    # Update data
    connection = op.get_bind()
    connection.execute(
        applications.update()
        .where(applications.c.old_status == 'applied')
        .values(new_status='submitted')
    )
```

### Enum Type Changes

PostgreSQL enums require special handling:

```python
def upgrade() -> None:
    # Option 1: Using ALTER TYPE (PostgreSQL 9.1+)
    op.execute("ALTER TYPE applicationstatus ADD VALUE 'technical'")

    # Option 2: Recreate enum (for removing values)
    op.execute("ALTER TYPE applicationstatus RENAME TO applicationstatus_old")
    op.execute("""
        CREATE TYPE applicationstatus AS ENUM (
            'draft', 'submitted', 'screening',
            'interview', 'technical', 'offer',
            'accepted', 'rejected', 'withdrawn'
        )
    """)
    op.execute("""
        ALTER TABLE applications
        ALTER COLUMN status TYPE applicationstatus
        USING status::text::applicationstatus
    """)
    op.execute("DROP TYPE applicationstatus_old")
```

### Branching and Merging

For multiple developers:

```bash
# Create branch migration
uv run alembic revision -m "feature branch" --branch-label feature_a

# Merge branches
uv run alembic merge -m "merge features" heads
```

---

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Run Migrations
on:
  push:
    branches: [main]
    paths: ['backend/alembic/versions/**']

jobs:
  migrate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Apply migrations
        env:
          DB_DATABASE_URL: ${{ secrets.DATABASE_URL }}
        run: |
          cd backend
          uv run alembic upgrade head
```

### Pre-deployment Check

```bash
#!/bin/bash
# scripts/check-migrations.sh

# Check for pending migrations
CURRENT=$(uv run alembic current | grep -oP '[\w]+')
HEAD=$(uv run alembic heads | grep -oP '[\w]+')

if [ "$CURRENT" != "$HEAD" ]; then
  echo "⚠️  Pending migrations detected!"
  echo "Current: $CURRENT"
  echo "Head: $HEAD"
  uv run alembic upgrade head
else
  echo "✅ Database is up to date"
fi
```

---

## References

- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [SQLAlchemy 2.0 Migration Guide](https://docs.sqlalchemy.org/en/20/changelog/migration_20.html)
- [PostgreSQL ALTER TYPE](https://www.postgresql.org/docs/current/sql-altertype.html)

---

## Migration History

| Version | Date | Description | Author |
|---------|------|-------------|--------|
| 3fab9ff6e7ab | 2025-11-23 | Initial schema with all 8 tables | Claude (Sonnet 4.5) |

---

**Last Updated:** 2025-11-23
**Maintained by:** Job-o-matic Development Team
