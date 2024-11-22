# Data Management Framework: Progress Notes

This document tracks my progress as I build the Data Management Framework in PostgreSQL.

---

## Project Overview
**Objective**: Build a scalable, compliant data management framework for PostgreSQL.

**Key Goals**:
1. Create a schema to manage raw, processed, and audit data.
2. Ensure compliance with GDPR (e.g., Subject Access Requests).
3. Track incidents and risks using PostgreSQL.
4. Generate reports and dashboards for insights.

---

## Daily Progress

### Day 1: Initial Setup
- Installed PostgreSQL and pgAdmin 4.
- Created a new database: `data_management_framework`. Right click and open Query Tool.
- Verified connection and ran a basic SQL query: `SELECT version();`.

- Created the `project_schema` schema:
  ```sql
  CREATE SCHEMA project_schema; -- Refresh for Schema to show up. 

  Key Tables to Define
1. Users: Manage user accounts and roles (e.g., admin, analyst).
2. Data Sources: Store information about where the data originates.
3. Raw Data: Capture unprocessed data from sources.
4. Processed Data: Store cleaned and structured data for analysis.
5. Audit Logs: Track changes to the data for compliance.
6. Metadata: Manage information about the data (lineage, quality, etc.).
7. Incident Reports: Log data issues, risks, or anomalies.
8. Analytics: Store pre-generated reports or results for reuse.

Create a table for each of these points.

-- Users
-- Data Sources Table
-- Raw Data Table
-- Processed Data Table
-- Audit Logs Table
-- Metadata Table
-- Incident Reports Table
-- Analytics Table

Relationships Between Tables (ERD Overview)
Here’s how the tables relate to each other:

Users interact with other tables via the user_id (e.g., generating analytics or making changes logged in audit_logs).
Data Sources link to raw_data via source_id.
Raw Data relates to:
processed_data (via data_id).
metadata for data lineage and quality.
incident_reports for risks/issues.
Audit Logs track actions performed on any table or object.
Analytics link to users and are based on processed_data.

ERD Example (Simplified Text View)
Here’s a simplified representation of how the tables connect:

users (user_id) ---> audit_logs (user_id)
                     analytics (user_id)

data_sources (source_id) ---> raw_data (source_id)
                               processed_data (raw_data_id)
                               metadata (data_id)
                               incident_reports (data_id)

After Creating the Tables Check to confirm the tables will appear in your visual model. 

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'project_schema';

Running Sample Query: 
INSERT INTO project_schema.users (email, password_hash, role)
VALUES ('test@example.com', 'hashedpassword', 'admin');

Functionality : 
SELECT * FROM project_schema.users;

Created an ERD DIAGRAM with the website dbdiagram.io
C:\data_management_project\ERD Diagram.png

