package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"
	"time"

	"database/sql"
	_ "github.com/mattn/go-sqlite3"
)

// Configuration structure
type Config struct {
	Port         int    `json:"port"`
	DatabasePath string `json:"database_path"`
	Environment  string `json:"environment"`
	Debug        bool   `json:"debug"`
}

// Response structures
type APIResponse struct {
	Success bool        `json:"success"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
	Error   string      `json:"error,omitempty"`
}

type HealthStatus struct {
	Status    string    `json:"status"`
	Timestamp time.Time `json:"timestamp"`
	Version   string    `json:"version"`
	Uptime    string    `json:"uptime"`
}

type User struct {
	ID        int       `json:"id"`
	Username  string    `json:"username"`
	Email     string    `json:"email"`
	FirstName string    `json:"first_name"`
	LastName  string    `json:"last_name"`
	IsActive  bool      `json:"is_active"`
	CreatedAt time.Time `json:"created_at"`
}

type Project struct {
	ID          int     `json:"id"`
	Name        string  `json:"name"`
	Description string  `json:"description"`
	Status      string  `json:"status"`
	Priority    string  `json:"priority"`
	Budget      float64 `json:"budget"`
	StartDate   string  `json:"start_date"`
	EndDate     string  `json:"end_date"`
}

// Global variables
var (
	db        *sql.DB
	config    Config
	startTime time.Time
)

// Initialize database connection
func initDatabase() error {
	var err error
	db, err = sql.Open("sqlite3", config.DatabasePath)
	if err != nil {
		return fmt.Errorf("failed to open database: %v", err)
	}

	// Test connection
	if err = db.Ping(); err != nil {
		return fmt.Errorf("failed to ping database: %v", err)
	}

	log.Printf("Database connected successfully: %s", config.DatabasePath)
	return nil
}

// Load configuration
func loadConfig() {
	// Default configuration
	config = Config{
		Port:         8080,
		DatabasePath: "./data/sample.db",
		Environment:  "development",
		Debug:        true,
	}

	// Try to load from environment variables
	if port := os.Getenv("APP_PORT"); port != "" {
		if p, err := strconv.Atoi(port); err == nil {
			config.Port = p
		}
	}

	if dbPath := os.Getenv("DATABASE_PATH"); dbPath != "" {
		config.DatabasePath = dbPath
	}

	if env := os.Getenv("GO_ENV"); env != "" {
		config.Environment = env
		config.Debug = env != "production"
	}

	log.Printf("Configuration loaded: %+v", config)
}

// Middleware for logging requests
func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		
		// Call the next handler
		next.ServeHTTP(w, r)
		
		// Log the request
		duration := time.Since(start)
		log.Printf("%s %s %s %v", r.Method, r.RequestURI, r.RemoteAddr, duration)
	})
}

// Middleware for CORS
func corsMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Access-Control-Allow-Origin", "*")
		w.Header().Set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
		w.Header().Set("Access-Control-Allow-Headers", "Content-Type, Authorization")

		if r.Method == "OPTIONS" {
			w.WriteHeader(http.StatusOK)
			return
		}

		next.ServeHTTP(w, r)
	})
}

// JSON response helper
func jsonResponse(w http.ResponseWriter, status int, response APIResponse) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	json.NewEncoder(w).Encode(response)
}

// Health check handler
func healthHandler(w http.ResponseWriter, r *http.Request) {
	uptime := time.Since(startTime).String()
	
	status := HealthStatus{
		Status:    "healthy",
		Timestamp: time.Now(),
		Version:   "1.0.0",
		Uptime:    uptime,
	}

	// Check database connection
	if db != nil {
		if err := db.Ping(); err != nil {
			status.Status = "unhealthy"
		}
	}

	var statusCode int
	if status.Status == "healthy" {
		statusCode = http.StatusOK
	} else {
		statusCode = http.StatusServiceUnavailable
	}

	jsonResponse(w, statusCode, APIResponse{
		Success: status.Status == "healthy",
		Message: fmt.Sprintf("Service is %s", status.Status),
		Data:    status,
	})
}

// Users API handlers
func usersHandler(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		getUsersHandler(w, r)
	case http.MethodPost:
		createUserHandler(w, r)
	default:
		jsonResponse(w, http.StatusMethodNotAllowed, APIResponse{
			Success: false,
			Message: "Method not allowed",
			Error:   fmt.Sprintf("Method %s not allowed", r.Method),
		})
	}
}

// Get users handler
func getUsersHandler(w http.ResponseWriter, r *http.Request) {
	if db == nil {
		jsonResponse(w, http.StatusInternalServerError, APIResponse{
			Success: false,
			Message: "Database not available",
			Error:   "Database connection not initialized",
		})
		return
	}

	// Parse query parameters
	limit := 10
	offset := 0

	if l := r.URL.Query().Get("limit"); l != "" {
		if parsed, err := strconv.Atoi(l); err == nil && parsed > 0 {
			limit = parsed
		}
	}

	if o := r.URL.Query().Get("offset"); o != "" {
		if parsed, err := strconv.Atoi(o); err == nil && parsed >= 0 {
			offset = parsed
		}
	}

	// Query users
	query := `
		SELECT id, username, email, first_name, last_name, is_active, created_at 
		FROM users 
		WHERE is_active = 1 
		ORDER BY created_at DESC 
		LIMIT ? OFFSET ?
	`

	rows, err := db.Query(query, limit, offset)
	if err != nil {
		jsonResponse(w, http.StatusInternalServerError, APIResponse{
			Success: false,
			Message: "Failed to query users",
			Error:   err.Error(),
		})
		return
	}
	defer rows.Close()

	var users []User
	for rows.Next() {
		var user User
		err := rows.Scan(
			&user.ID, &user.Username, &user.Email,
			&user.FirstName, &user.LastName, &user.IsActive,
			&user.CreatedAt,
		)
		if err != nil {
			log.Printf("Error scanning user row: %v", err)
			continue
		}
		users = append(users, user)
	}

	jsonResponse(w, http.StatusOK, APIResponse{
		Success: true,
		Message: fmt.Sprintf("Retrieved %d users", len(users)),
		Data:    users,
	})
}

// Create user handler
func createUserHandler(w http.ResponseWriter, r *http.Request) {
	if r.Header.Get("Content-Type") != "application/json" {
		jsonResponse(w, http.StatusBadRequest, APIResponse{
			Success: false,
			Message: "Content-Type must be application/json",
		})
		return
	}

	body, err := io.ReadAll(r.Body)
	if err != nil {
		jsonResponse(w, http.StatusBadRequest, APIResponse{
			Success: false,
			Message: "Failed to read request body",
			Error:   err.Error(),
		})
		return
	}

	var user User
	if err := json.Unmarshal(body, &user); err != nil {
		jsonResponse(w, http.StatusBadRequest, APIResponse{
			Success: false,
			Message: "Invalid JSON format",
			Error:   err.Error(),
		})
		return
	}

	// Basic validation
	if user.Username == "" || user.Email == "" {
		jsonResponse(w, http.StatusBadRequest, APIResponse{
			Success: false,
			Message: "Username and email are required",
		})
		return
	}

	jsonResponse(w, http.StatusCreated, APIResponse{
		Success: true,
		Message: "User creation endpoint (demo)",
		Data:    user,
	})
}

// Projects API handler
func projectsHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		jsonResponse(w, http.StatusMethodNotAllowed, APIResponse{
			Success: false,
			Message: "Only GET method allowed",
		})
		return
	}

	if db == nil {
		jsonResponse(w, http.StatusInternalServerError, APIResponse{
			Success: false,
			Message: "Database not available",
		})
		return
	}

	// Query projects
	query := `
		SELECT id, name, description, status, priority, budget, start_date, end_date
		FROM projects 
		ORDER BY created_at DESC
	`

	rows, err := db.Query(query)
	if err != nil {
		jsonResponse(w, http.StatusInternalServerError, APIResponse{
			Success: false,
			Message: "Failed to query projects",
			Error:   err.Error(),
		})
		return
	}
	defer rows.Close()

	var projects []Project
	for rows.Next() {
		var project Project
		err := rows.Scan(
			&project.ID, &project.Name, &project.Description,
			&project.Status, &project.Priority, &project.Budget,
			&project.StartDate, &project.EndDate,
		)
		if err != nil {
			log.Printf("Error scanning project row: %v", err)
			continue
		}
		projects = append(projects, project)
	}

	jsonResponse(w, http.StatusOK, APIResponse{
		Success: true,
		Message: fmt.Sprintf("Retrieved %d projects", len(projects)),
		Data:    projects,
	})
}

// Statistics handler
func statsHandler(w http.ResponseWriter, r *http.Request) {
	if db == nil {
		jsonResponse(w, http.StatusServiceUnavailable, APIResponse{
			Success: false,
			Message: "Database not available",
		})
		return
	}

	stats := make(map[string]interface{})

	// Count users
	var userCount int
	err := db.QueryRow("SELECT COUNT(*) FROM users WHERE is_active = 1").Scan(&userCount)
	if err != nil {
		log.Printf("Error counting users: %v", err)
		userCount = 0
	}
	stats["active_users"] = userCount

	// Count projects by status
	projectStats := make(map[string]int)
	rows, err := db.Query("SELECT status, COUNT(*) FROM projects GROUP BY status")
	if err == nil {
		defer rows.Close()
		for rows.Next() {
			var status string
			var count int
			if err := rows.Scan(&status, &count); err == nil {
				projectStats[status] = count
			}
		}
	}
	stats["projects_by_status"] = projectStats

	// Count total tasks
	var taskCount int
	err = db.QueryRow("SELECT COUNT(*) FROM tasks").Scan(&taskCount)
	if err != nil {
		log.Printf("Error counting tasks: %v", err)
		taskCount = 0
	}
	stats["total_tasks"] = taskCount

	// Server stats
	stats["server_uptime"] = time.Since(startTime).String()
	stats["server_version"] = "1.0.0"
	stats["timestamp"] = time.Now()

	jsonResponse(w, http.StatusOK, APIResponse{
		Success: true,
		Message: "System statistics",
		Data:    stats,
	})
}

// Static file server for frontend assets
func staticHandler(w http.ResponseWriter, r *http.Request) {
	// Remove the /static/ prefix
	path := strings.TrimPrefix(r.URL.Path, "/static/")
	
	// Security check: prevent directory traversal
	if strings.Contains(path, "..") {
		http.Error(w, "Invalid path", http.StatusBadRequest)
		return
	}

	// Serve the file
	http.ServeFile(w, r, path)
}

// Root handler - serve index.html
func rootHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path == "/" {
		http.ServeFile(w, r, "index.html")
		return
	}
	
	// For any other path, return 404
	jsonResponse(w, http.StatusNotFound, APIResponse{
		Success: false,
		Message: "Endpoint not found",
		Error:   fmt.Sprintf("Path %s not found", r.URL.Path),
	})
}

// Setup routes
func setupRoutes() *http.ServeMux {
	mux := http.NewServeMux()

	// API routes
	mux.HandleFunc("/health", healthHandler)
	mux.HandleFunc("/api/users", usersHandler)
	mux.HandleFunc("/api/projects", projectsHandler)
	mux.HandleFunc("/api/stats", statsHandler)

	// Static files
	mux.HandleFunc("/static/", staticHandler)

	// Root handler
	mux.HandleFunc("/", rootHandler)

	return mux
}

func main() {
	startTime = time.Now()
	
	// Load configuration
	loadConfig()

	// Initialize database (optional, only if database file exists)
	if _, err := os.Stat(config.DatabasePath); err == nil {
		if err := initDatabase(); err != nil {
			log.Printf("Database initialization failed: %v", err)
			log.Println("Continuing without database...")
		} else {
			defer db.Close()
		}
	} else {
		log.Printf("Database file not found at %s, continuing without database", config.DatabasePath)
	}

	// Setup HTTP server
	mux := setupRoutes()
	
	// Apply middleware
	handler := corsMiddleware(loggingMiddleware(mux))

	// Configure server
	server := &http.Server{
		Addr:           fmt.Sprintf(":%d", config.Port),
		Handler:        handler,
		ReadTimeout:    15 * time.Second,
		WriteTimeout:   15 * time.Second,
		IdleTimeout:    60 * time.Second,
		MaxHeaderBytes: 1 << 20, // 1MB
	}

	// Start server
	log.Printf("🚀 Go server starting on port %d", config.Port)
	log.Printf("Environment: %s", config.Environment)
	log.Printf("Debug mode: %v", config.Debug)
	
	if config.Debug {
		log.Println("Available endpoints:")
		log.Println("  GET  /              - Main page")
		log.Println("  GET  /health        - Health check")
		log.Println("  GET  /api/users     - Get users")
		log.Println("  POST /api/users     - Create user (demo)")
		log.Println("  GET  /api/projects  - Get projects")
		log.Println("  GET  /api/stats     - Get statistics")
		log.Println("  GET  /static/*      - Static files")
	}

	if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		log.Fatalf("Server failed to start: %v", err)
	}
}
