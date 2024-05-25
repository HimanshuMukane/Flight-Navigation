package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func main() {
    // Initialize Gin
    r := gin.Default()

    // Enable CORS
    r.Use(corsMiddleware())

    // Serve static files from the "static" directory
    r.Static("/static", "./static")

    // Serve the HTML file
    r.StaticFile("/", "templates/index.html")

    // Run the server
    r.Run(":5500")
}

// Middleware function to enable CORS
func corsMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
        c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, GET, OPTIONS, PUT, DELETE")
        c.Writer.Header().Set("Access-Control-Allow-Headers", "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization")

        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(http.StatusOK)
            return
        }

        c.Next()
    }
}
