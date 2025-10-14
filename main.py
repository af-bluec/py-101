#!/usr/bin/env python3
"""
Multi-Language Sample Project - Main Python Application

This module demonstrates various Python programming concepts including:
- File operations
- Data structures
- Error handling
- Configuration management
- Logging
"""

import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class DataProcessor:
    """A sample data processing class."""
    
    def __init__(self, config_file="config.yaml"):
        """Initialize the data processor with configuration."""
        self.config = self.load_config(config_file)
        self.data = []
        logger.info("DataProcessor initialized")
    
    def load_config(self, config_file):
        """Load configuration from YAML file."""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as file:
                    config = yaml.safe_load(file)
                logger.info(f"Configuration loaded from {config_file}")
                return config
            else:
                logger.warning(f"Config file {config_file} not found, using defaults")
                return self.get_default_config()
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            return self.get_default_config()
    
    def get_default_config(self):
        """Return default configuration."""
        return {
            'app_name': 'Sample Application',
            'version': '1.0.0',
            'debug': False,
            'data_source': 'sample_data.json'
        }
    
    def add_data(self, item):
        """Add an item to the data collection."""
        if isinstance(item, dict):
            item['timestamp'] = datetime.now().isoformat()
            self.data.append(item)
            logger.info(f"Added item: {item}")
        else:
            logger.error(f"Invalid data type: {type(item)}")
            raise ValueError("Item must be a dictionary")
    
    def process_data(self):
        """Process the collected data."""
        logger.info("Starting data processing...")
        
        if not self.data:
            logger.warning("No data to process")
            return []
        
        processed_data = []
        for item in self.data:
            try:
                # Sample processing: add ID and calculate score
                processed_item = item.copy()
                processed_item['id'] = len(processed_data) + 1
                processed_item['score'] = len(item.get('name', '')) * 10
                processed_data.append(processed_item)
            except Exception as e:
                logger.error(f"Error processing item {item}: {e}")
        
        logger.info(f"Processed {len(processed_data)} items")
        return processed_data
    
    def save_results(self, data, filename="results.json"):
        """Save processed data to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, indent=2, default=str)
            logger.info(f"Results saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving results: {e}")
            raise
    
    def get_stats(self):
        """Get statistics about the processed data."""
        return {
            'total_items': len(self.data),
            'config_loaded': bool(self.config),
            'app_name': self.config.get('app_name', 'Unknown'),
            'version': self.config.get('version', 'Unknown')
        }


def main():
    """Main application entry point."""
    logger.info("Starting Multi-Language Sample Application")
    
    try:
        # Initialize the data processor
        processor = DataProcessor()
        
        # Add some sample data
        sample_data = [
            {'name': 'Alice Johnson', 'department': 'Engineering', 'role': 'Developer'},
            {'name': 'Bob Smith', 'department': 'Marketing', 'role': 'Manager'},
            {'name': 'Carol Davis', 'department': 'Engineering', 'role': 'Lead'},
            {'name': 'David Wilson', 'department': 'Sales', 'role': 'Representative'}
        ]
        
        for item in sample_data:
            processor.add_data(item)
        
        # Process the data
        results = processor.process_data()
        
        # Save results
        processor.save_results(results)
        
        # Display statistics
        stats = processor.get_stats()
        print("\n" + "="*50)
        print("APPLICATION STATISTICS")
        print("="*50)
        for key, value in stats.items():
            print(f"{key.upper()}: {value}")
        print("="*50)
        
        logger.info("Application completed successfully")
        
    except Exception as e:
        logger.error(f"Application failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
