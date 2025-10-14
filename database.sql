-- Multi-Language Sample Project - Database Schema
-- This SQL file contains the database schema, sample data, and common queries
-- for the sample project. It demonstrates relational database design principles.

-- Create database (uncomment if needed)
-- CREATE DATABASE sample_db;
-- USE sample_db;

-- Enable foreign key constraints (for SQLite)
PRAGMA foreign_keys = ON;

-- =====================================================
-- TABLES
-- =====================================================

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP NULL
);

-- Departments table
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    manager_id INTEGER,
    budget DECIMAL(12, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (manager_id) REFERENCES users(id)
);

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    department_id INTEGER NOT NULL,
    project_manager_id INTEGER,
    status VARCHAR(20) DEFAULT 'planning',
    priority VARCHAR(10) DEFAULT 'medium',
    start_date DATE,
    end_date DATE,
    budget DECIMAL(12, 2) DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (department_id) REFERENCES departments(id),
    FOREIGN KEY (project_manager_id) REFERENCES users(id),
    CHECK (status IN ('planning', 'active', 'completed', 'cancelled', 'on_hold')),
    CHECK (priority IN ('low', 'medium', 'high', 'critical'))
);

-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    project_id INTEGER NOT NULL,
    assigned_to INTEGER,
    status VARCHAR(20) DEFAULT 'todo',
    priority VARCHAR(10) DEFAULT 'medium',
    estimated_hours DECIMAL(5, 2) DEFAULT 0.00,
    actual_hours DECIMAL(5, 2) DEFAULT 0.00,
    due_date TIMESTAMP,
    completed_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(id),
    FOREIGN KEY (assigned_to) REFERENCES users(id),
    CHECK (status IN ('todo', 'in_progress', 'review', 'completed', 'cancelled')),
    CHECK (priority IN ('low', 'medium', 'high', 'critical'))
);

-- User roles and permissions
CREATE TABLE IF NOT EXISTS roles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User-Role mapping (many-to-many)
CREATE TABLE IF NOT EXISTS user_roles (
    user_id INTEGER NOT NULL,
    role_id INTEGER NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    assigned_by INTEGER,
    PRIMARY KEY (user_id, role_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (role_id) REFERENCES roles(id) ON DELETE CASCADE,
    FOREIGN KEY (assigned_by) REFERENCES users(id)
);

-- Activity log table
CREATE TABLE IF NOT EXISTS activity_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50),
    entity_id INTEGER,
    details TEXT,
    ip_address VARCHAR(45),
    user_agent TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================================================
-- INDEXES for better performance
-- =====================================================

CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_projects_department ON projects(department_id);
CREATE INDEX IF NOT EXISTS idx_projects_status ON projects(status);
CREATE INDEX IF NOT EXISTS idx_tasks_project ON tasks(project_id);
CREATE INDEX IF NOT EXISTS idx_tasks_assigned_to ON tasks(assigned_to);
CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status);
CREATE INDEX IF NOT EXISTS idx_activity_log_user ON activity_log(user_id);
CREATE INDEX IF NOT EXISTS idx_activity_log_created_at ON activity_log(created_at);

-- =====================================================
-- SAMPLE DATA
-- =====================================================

-- Insert sample roles
INSERT OR IGNORE INTO roles (name, description) VALUES
('admin', 'System Administrator with full access'),
('project_manager', 'Project Manager with project-level access'),
('developer', 'Developer with task-level access'),
('viewer', 'Read-only access to projects and tasks');

-- Insert sample users
INSERT OR IGNORE INTO users (username, email, first_name, last_name, password_hash, is_admin) VALUES
('admin', 'admin@example.com', 'System', 'Administrator', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj75h5i3E4H2', TRUE),
('jsmith', 'john.smith@example.com', 'John', 'Smith', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj75h5i3E4H2', FALSE),
('ajohnson', 'alice.johnson@example.com', 'Alice', 'Johnson', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj75h5i3E4H2', FALSE),
('bwilson', 'bob.wilson@example.com', 'Bob', 'Wilson', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj75h5i3E4H2', FALSE),
('cdavis', 'carol.davis@example.com', 'Carol', 'Davis', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj75h5i3E4H2', FALSE);

-- Insert sample departments
INSERT OR IGNORE INTO departments (name, description, manager_id, budget) VALUES
('Engineering', 'Software development and technical operations', 2, 500000.00),
('Marketing', 'Marketing and customer outreach', 3, 200000.00),
('Sales', 'Sales and business development', 4, 300000.00),
('Human Resources', 'HR and employee relations', 5, 150000.00);

-- Insert sample projects
INSERT OR IGNORE INTO projects (name, description, department_id, project_manager_id, status, priority, start_date, end_date, budget) VALUES
('Website Redesign', 'Complete redesign of company website with modern UI/UX', 1, 2, 'active', 'high', '2024-01-15', '2024-06-30', 75000.00),
('Mobile App Development', 'Native mobile application for iOS and Android', 1, 2, 'planning', 'high', '2024-03-01', '2024-12-31', 120000.00),
('Customer Retention Campaign', 'Email marketing campaign to improve customer retention', 2, 3, 'active', 'medium', '2024-02-01', '2024-05-31', 25000.00),
('Sales Process Automation', 'Implement CRM system and automate sales workflows', 3, 4, 'completed', 'medium', '2023-09-01', '2024-01-31', 50000.00);

-- Insert sample tasks
INSERT OR IGNORE INTO tasks (title, description, project_id, assigned_to, status, priority, estimated_hours, due_date) VALUES
('Design wireframes', 'Create wireframes for all main pages', 1, 3, 'completed', 'high', 40.0, '2024-02-15'),
('Frontend development', 'Implement responsive frontend components', 1, 2, 'in_progress', 'high', 80.0, '2024-04-30'),
('Backend API development', 'Create RESTful APIs for data management', 1, 2, 'todo', 'high', 60.0, '2024-05-15'),
('User testing', 'Conduct user testing sessions and gather feedback', 1, 3, 'todo', 'medium', 20.0, '2024-06-15'),
('iOS app setup', 'Initialize iOS project and setup development environment', 2, 2, 'todo', 'high', 16.0, '2024-03-15'),
('Android app setup', 'Initialize Android project and setup development environment', 2, 4, 'todo', 'high', 16.0, '2024-03-15'),
('Email template design', 'Design responsive email templates for campaign', 3, 3, 'completed', 'medium', 24.0, '2024-02-28'),
('Campaign automation setup', 'Setup automated email sequences in marketing platform', 3, 3, 'in_progress', 'medium', 16.0, '2024-03-31');

-- Assign roles to users
INSERT OR IGNORE INTO user_roles (user_id, role_id, assigned_by) VALUES
(1, 1, 1), -- admin is admin
(2, 2, 1), -- jsmith is project_manager
(3, 3, 1), -- ajohnson is developer
(4, 3, 1), -- bwilson is developer
(5, 2, 1); -- cdavis is project_manager

-- Insert sample activity log entries
INSERT OR IGNORE INTO activity_log (user_id, action, entity_type, entity_id, details) VALUES
(1, 'USER_LOGIN', NULL, NULL, 'Admin user logged in'),
(2, 'PROJECT_CREATED', 'project', 1, 'Created Website Redesign project'),
(3, 'TASK_COMPLETED', 'task', 1, 'Completed wireframe design task'),
(2, 'TASK_UPDATED', 'task', 2, 'Updated frontend development task status to in_progress'),
(4, 'USER_LOGIN', NULL, NULL, 'User logged in from mobile device');

-- =====================================================
-- VIEWS
-- =====================================================

-- Project overview view
CREATE VIEW IF NOT EXISTS project_overview AS
SELECT 
    p.id,
    p.name as project_name,
    p.status,
    p.priority,
    d.name as department_name,
    u.first_name || ' ' || u.last_name as project_manager,
    COUNT(t.id) as total_tasks,
    SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) as completed_tasks,
    SUM(t.estimated_hours) as total_estimated_hours,
    SUM(t.actual_hours) as total_actual_hours,
    p.budget,
    p.start_date,
    p.end_date
FROM projects p
LEFT JOIN departments d ON p.department_id = d.id
LEFT JOIN users u ON p.project_manager_id = u.id
LEFT JOIN tasks t ON p.id = t.project_id
GROUP BY p.id, p.name, p.status, p.priority, d.name, u.first_name, u.last_name, p.budget, p.start_date, p.end_date;

-- User workload view
CREATE VIEW IF NOT EXISTS user_workload AS
SELECT 
    u.id,
    u.username,
    u.first_name || ' ' || u.last_name as full_name,
    COUNT(t.id) as total_tasks,
    SUM(CASE WHEN t.status = 'todo' THEN 1 ELSE 0 END) as todo_tasks,
    SUM(CASE WHEN t.status = 'in_progress' THEN 1 ELSE 0 END) as in_progress_tasks,
    SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) as completed_tasks,
    SUM(t.estimated_hours) as total_estimated_hours,
    SUM(t.actual_hours) as total_actual_hours
FROM users u
LEFT JOIN tasks t ON u.id = t.assigned_to
GROUP BY u.id, u.username, u.first_name, u.last_name;

-- =====================================================
-- STORED PROCEDURES / FUNCTIONS (SQLite doesn't support these, but here are equivalent queries)
-- =====================================================

-- Query to get project completion percentage
-- SELECT 
--     project_id,
--     ROUND((completed_tasks * 100.0 / total_tasks), 2) as completion_percentage
-- FROM project_overview
-- WHERE total_tasks > 0;

-- Query to get overdue tasks
-- SELECT 
--     t.id,
--     t.title,
--     t.due_date,
--     u.first_name || ' ' || u.last_name as assignee,
--     p.name as project_name
-- FROM tasks t
-- LEFT JOIN users u ON t.assigned_to = u.id
-- LEFT JOIN projects p ON t.project_id = p.id
-- WHERE t.due_date < CURRENT_TIMESTAMP 
--   AND t.status NOT IN ('completed', 'cancelled');

-- =====================================================
-- CLEANUP AND MAINTENANCE QUERIES
-- =====================================================

-- Delete old activity logs (older than 1 year)
-- DELETE FROM activity_log WHERE created_at < datetime('now', '-1 year');

-- Update project status based on task completion
-- UPDATE projects 
-- SET status = 'completed' 
-- WHERE id IN (
--     SELECT p.id 
--     FROM projects p
--     LEFT JOIN tasks t ON p.id = t.project_id
--     GROUP BY p.id
--     HAVING COUNT(t.id) > 0 
--       AND SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) = COUNT(t.id)
--       AND p.status != 'completed'
-- );

-- =====================================================
-- SAMPLE QUERIES FOR TESTING
-- =====================================================

-- Get all active projects with their tasks
-- SELECT 
--     p.name as project_name,
--     t.title as task_title,
--     t.status as task_status,
--     u.first_name || ' ' || u.last_name as assignee
-- FROM projects p
-- LEFT JOIN tasks t ON p.id = t.project_id
-- LEFT JOIN users u ON t.assigned_to = u.id
-- WHERE p.status = 'active'
-- ORDER BY p.name, t.title;

-- Get department workload summary
-- SELECT 
--     d.name as department,
--     COUNT(DISTINCT p.id) as total_projects,
--     COUNT(t.id) as total_tasks,
--     SUM(CASE WHEN t.status = 'completed' THEN 1 ELSE 0 END) as completed_tasks,
--     SUM(t.estimated_hours) as estimated_hours
-- FROM departments d
-- LEFT JOIN projects p ON d.id = p.department_id
-- LEFT JOIN tasks t ON p.id = t.project_id
-- GROUP BY d.id, d.name
-- ORDER BY total_projects DESC;
