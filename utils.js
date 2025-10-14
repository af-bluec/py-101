/**
 * Multi-Language Sample Project - JavaScript Utilities
 * 
 * This module provides various utility functions for common operations
 * including data manipulation, validation, and formatting.
 */

const fs = require('fs');
const path = require('path');

/**
 * Utility class for common operations
 */
class Utils {
    /**
     * Validate an email address
     * @param {string} email - Email address to validate
     * @returns {boolean} - True if valid, false otherwise
     */
    static validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    /**
     * Generate a random ID
     * @param {number} length - Length of the ID (default: 8)
     * @returns {string} - Random alphanumeric ID
     */
    static generateId(length = 8) {
        const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        let result = '';
        for (let i = 0; i < length; i++) {
            result += chars.charAt(Math.floor(Math.random() * chars.length));
        }
        return result;
    }

    /**
     * Format a date to a readable string
     * @param {Date} date - Date object to format
     * @param {string} format - Format type ('short', 'long', 'iso')
     * @returns {string} - Formatted date string
     */
    static formatDate(date, format = 'short') {
        if (!(date instanceof Date)) {
            throw new Error('Invalid date object');
        }

        switch (format) {
            case 'short':
                return date.toLocaleDateString();
            case 'long':
                return date.toLocaleDateString('en-US', { 
                    weekday: 'long', 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric' 
                });
            case 'iso':
                return date.toISOString();
            default:
                return date.toString();
        }
    }

    /**
     * Deep clone an object
     * @param {Object} obj - Object to clone
     * @returns {Object} - Cloned object
     */
    static deepClone(obj) {
        if (obj === null || typeof obj !== 'object') {
            return obj;
        }

        if (obj instanceof Date) {
            return new Date(obj.getTime());
        }

        if (obj instanceof Array) {
            return obj.map(item => Utils.deepClone(item));
        }

        const cloned = {};
        for (let key in obj) {
            if (obj.hasOwnProperty(key)) {
                cloned[key] = Utils.deepClone(obj[key]);
            }
        }
        return cloned;
    }

    /**
     * Debounce a function
     * @param {Function} func - Function to debounce
     * @param {number} delay - Delay in milliseconds
     * @returns {Function} - Debounced function
     */
    static debounce(func, delay) {
        let timeoutId;
        return function (...args) {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => func.apply(this, args), delay);
        };
    }

    /**
     * Throttle a function
     * @param {Function} func - Function to throttle
     * @param {number} limit - Time limit in milliseconds
     * @returns {Function} - Throttled function
     */
    static throttle(func, limit) {
        let inThrottle;
        return function (...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    }

    /**
     * Check if a string is empty or contains only whitespace
     * @param {string} str - String to check
     * @returns {boolean} - True if empty or whitespace only
     */
    static isEmpty(str) {
        return !str || str.trim().length === 0;
    }

    /**
     * Capitalize the first letter of a string
     * @param {string} str - String to capitalize
     * @returns {string} - Capitalized string
     */
    static capitalize(str) {
        if (!str) return str;
        return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
    }

    /**
     * Convert a string to camelCase
     * @param {string} str - String to convert
     * @returns {string} - camelCase string
     */
    static toCamelCase(str) {
        return str
            .replace(/(?:^\w|[A-Z]|\b\w)/g, (word, index) => 
                index === 0 ? word.toLowerCase() : word.toUpperCase()
            )
            .replace(/\s+/g, '');
    }

    /**
     * Retry a promise-returning function
     * @param {Function} fn - Function that returns a promise
     * @param {number} retries - Number of retry attempts
     * @param {number} delay - Delay between retries in milliseconds
     * @returns {Promise} - Promise that resolves when successful or rejects after all retries
     */
    static async retry(fn, retries = 3, delay = 1000) {
        try {
            return await fn();
        } catch (error) {
            if (retries > 0) {
                await new Promise(resolve => setTimeout(resolve, delay));
                return Utils.retry(fn, retries - 1, delay);
            }
            throw error;
        }
    }

    /**
     * Read a JSON file asynchronously
     * @param {string} filePath - Path to the JSON file
     * @returns {Promise<Object>} - Promise that resolves to the parsed JSON
     */
    static async readJsonFile(filePath) {
        try {
            const data = await fs.promises.readFile(filePath, 'utf8');
            return JSON.parse(data);
        } catch (error) {
            throw new Error(`Failed to read JSON file ${filePath}: ${error.message}`);
        }
    }

    /**
     * Write data to a JSON file asynchronously
     * @param {string} filePath - Path to write the file
     * @param {Object} data - Data to write
     * @returns {Promise<void>}
     */
    static async writeJsonFile(filePath, data) {
        try {
            const jsonString = JSON.stringify(data, null, 2);
            await fs.promises.writeFile(filePath, jsonString, 'utf8');
        } catch (error) {
            throw new Error(`Failed to write JSON file ${filePath}: ${error.message}`);
        }
    }
}

/**
 * Logger utility for consistent logging
 */
class Logger {
    constructor(name = 'App') {
        this.name = name;
    }

    log(level, message, ...args) {
        const timestamp = new Date().toISOString();
        console.log(`[${timestamp}] [${level.toUpperCase()}] [${this.name}] ${message}`, ...args);
    }

    info(message, ...args) {
        this.log('info', message, ...args);
    }

    warn(message, ...args) {
        this.log('warn', message, ...args);
    }

    error(message, ...args) {
        this.log('error', message, ...args);
    }

    debug(message, ...args) {
        this.log('debug', message, ...args);
    }
}

// Export for use in other modules
module.exports = {
    Utils,
    Logger
};

// Example usage if run directly
if (require.main === module) {
    const logger = new Logger('Utils');
    
    logger.info('Utils module loaded successfully');
    
    // Demonstrate some utility functions
    console.log('Email validation:', Utils.validateEmail('test@example.com'));
    console.log('Generated ID:', Utils.generateId(10));
    console.log('Formatted date:', Utils.formatDate(new Date(), 'long'));
    console.log('Capitalized string:', Utils.capitalize('hello world'));
    console.log('camelCase conversion:', Utils.toCamelCase('hello world example'));
    
    logger.info('Utils demonstration completed');
}
