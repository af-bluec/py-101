#!/usr/bin/env python3
"""
Test Suite for Multi-Language Sample Project - Main Python Application

This module contains comprehensive unit tests for the main.py application,
demonstrating testing best practices including:
- Unit testing with pytest
- Test fixtures and mock data
- Exception handling tests
- Configuration testing
- Data validation tests
"""

import json
import os
import tempfile
import pytest
from unittest.mock import patch, mock_open, MagicMock
import yaml
from datetime import datetime

# Import the classes and functions we want to test
# In a real project, you would import from your main module
# For this example, we'll define simplified versions for testing

class DataProcessor:
    """Simplified DataProcessor class for testing."""
    
    def __init__(self, config_file="config.yaml"):
        self.config = self.load_config(config_file)
        self.data = []
    
    def load_config(self, config_file):
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r') as file:
                    return yaml.safe_load(file)
            else:
                return self.get_default_config()
        except Exception:
            return self.get_default_config()
    
    def get_default_config(self):
        return {
            'app_name': 'Sample Application',
            'version': '1.0.0',
            'debug': False,
            'data_source': 'sample_data.json'
        }
    
    def add_data(self, item):
        if isinstance(item, dict):
            item['timestamp'] = datetime.now().isoformat()
            self.data.append(item)
        else:
            raise ValueError("Item must be a dictionary")
    
    def process_data(self):
        if not self.data:
            return []
        
        processed_data = []
        for item in self.data:
            processed_item = item.copy()
            processed_item['id'] = len(processed_data) + 1
            processed_item['score'] = len(item.get('name', '')) * 10
            processed_data.append(processed_item)
        
        return processed_data
    
    def save_results(self, data, filename="results.json"):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2, default=str)
    
    def get_stats(self):
        return {
            'total_items': len(self.data),
            'config_loaded': bool(self.config),
            'app_name': self.config.get('app_name', 'Unknown'),
            'version': self.config.get('version', 'Unknown')
        }


class TestDataProcessor:
    """Test class for DataProcessor functionality."""
    
    @pytest.fixture
    def processor(self):
        """Create a DataProcessor instance for testing."""
        with patch('os.path.exists', return_value=False):
            return DataProcessor()
    
    @pytest.fixture
    def sample_data(self):
        """Provide sample test data."""
        return [
            {'name': 'Alice Johnson', 'department': 'Engineering', 'role': 'Developer'},
            {'name': 'Bob Smith', 'department': 'Marketing', 'role': 'Manager'},
            {'name': 'Carol Davis', 'department': 'Engineering', 'role': 'Lead'}
        ]
    
    @pytest.fixture
    def config_data(self):
        """Provide sample configuration data."""
        return {
            'app_name': 'Test Application',
            'version': '2.0.0',
            'debug': True,
            'data_source': 'test_data.json'
        }
    
    def test_initialization_with_default_config(self, processor):
        """Test that DataProcessor initializes with default config."""
        assert processor.config['app_name'] == 'Sample Application'
        assert processor.config['version'] == '1.0.0'
        assert processor.config['debug'] is False
        assert processor.data == []
    
    def test_initialization_with_config_file(self, config_data):
        """Test initialization with existing config file."""
        mock_file_content = yaml.dump(config_data)
        
        with patch('os.path.exists', return_value=True), \
             patch('builtins.open', mock_open(read_data=mock_file_content)):
            processor = DataProcessor('test_config.yaml')
            
            assert processor.config['app_name'] == 'Test Application'
            assert processor.config['version'] == '2.0.0'
            assert processor.config['debug'] is True
    
    def test_add_valid_data(self, processor, sample_data):
        """Test adding valid data items."""
        for item in sample_data:
            processor.add_data(item)
        
        assert len(processor.data) == 3
        assert all('timestamp' in item for item in processor.data)
        assert processor.data[0]['name'] == 'Alice Johnson'
    
    def test_add_invalid_data_raises_exception(self, processor):
        """Test that adding invalid data raises ValueError."""
        with pytest.raises(ValueError, match="Item must be a dictionary"):
            processor.add_data("invalid_data")
        
        with pytest.raises(ValueError, match="Item must be a dictionary"):
            processor.add_data(123)
        
        with pytest.raises(ValueError, match="Item must be a dictionary"):
            processor.add_data(['list', 'data'])
    
    def test_process_empty_data(self, processor):
        """Test processing when no data is available."""
        result = processor.process_data()
        assert result == []
    
    def test_process_data_with_items(self, processor, sample_data):
        """Test data processing with sample items."""
        for item in sample_data:
            processor.add_data(item)
        
        processed = processor.process_data()
        
        assert len(processed) == 3
        assert processed[0]['id'] == 1
        assert processed[1]['id'] == 2
        assert processed[2]['id'] == 3
        
        # Test score calculation (name length * 10)
        assert processed[0]['score'] == len('Alice Johnson') * 10  # 120
        assert processed[1]['score'] == len('Bob Smith') * 10      # 90
        assert processed[2]['score'] == len('Carol Davis') * 10    # 110
    
    def test_process_data_with_missing_name(self, processor):
        """Test processing data items without name field."""
        processor.add_data({'department': 'Engineering'})
        
        processed = processor.process_data()
        
        assert len(processed) == 1
        assert processed[0]['score'] == 0  # No name, so 0 score
    
    def test_save_results(self, processor):
        """Test saving results to JSON file."""
        test_data = [{'id': 1, 'name': 'Test', 'score': 40}]
        
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
            temp_filename = temp_file.name
        
        try:
            processor.save_results(test_data, temp_filename)
            
            with open(temp_filename, 'r') as file:
                saved_data = json.load(file)
            
            assert saved_data == test_data
        finally:
            os.unlink(temp_filename)
    
    def test_save_results_handles_datetime(self, processor):
        """Test that save_results handles datetime objects."""
        test_data = [{'id': 1, 'timestamp': datetime.now()}]
        
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
            temp_filename = temp_file.name
        
        try:
            processor.save_results(test_data, temp_filename)
            
            with open(temp_filename, 'r') as file:
                saved_data = json.load(file)
            
            assert 'timestamp' in saved_data[0]
            assert isinstance(saved_data[0]['timestamp'], str)
        finally:
            os.unlink(temp_filename)
    
    def test_get_stats_empty_data(self, processor):
        """Test getting statistics with empty data."""
        stats = processor.get_stats()
        
        assert stats['total_items'] == 0
        assert stats['config_loaded'] is True
        assert stats['app_name'] == 'Sample Application'
        assert stats['version'] == '1.0.0'
    
    def test_get_stats_with_data(self, processor, sample_data):
        """Test getting statistics with data."""
        for item in sample_data:
            processor.add_data(item)
        
        stats = processor.get_stats()
        
        assert stats['total_items'] == 3
        assert stats['config_loaded'] is True
        assert stats['app_name'] == 'Sample Application'
        assert stats['version'] == '1.0.0'
    
    def test_config_loading_error_handling(self):
        """Test that config loading errors are handled gracefully."""
        with patch('os.path.exists', return_value=True), \
             patch('builtins.open', side_effect=IOError("File read error")):
            processor = DataProcessor('bad_config.yaml')
            
            # Should fall back to default config
            assert processor.config['app_name'] == 'Sample Application'
    
    def test_invalid_yaml_handling(self):
        """Test handling of invalid YAML content."""
        invalid_yaml = "invalid: yaml: content: ["
        
        with patch('os.path.exists', return_value=True), \
             patch('builtins.open', mock_open(read_data=invalid_yaml)):
            processor = DataProcessor('invalid.yaml')
            
            # Should fall back to default config
            assert processor.config['app_name'] == 'Sample Application'


class TestUtilityFunctions:
    """Test utility functions that might be used by the main application."""
    
    def test_validate_data_structure(self):
        """Test data structure validation."""
        valid_item = {'name': 'Test', 'department': 'IT', 'role': 'Developer'}
        invalid_item_1 = {'name': 'Test'}  # Missing required fields
        invalid_item_2 = {'department': 'IT', 'role': 'Developer'}  # Missing name
        
        def validate_item(item):
            required_fields = ['name', 'department', 'role']
            return all(field in item for field in required_fields)
        
        assert validate_item(valid_item) is True
        assert validate_item(invalid_item_1) is False
        assert validate_item(invalid_item_2) is False
    
    def test_data_sanitization(self):
        """Test data sanitization functions."""
        def sanitize_string(value):
            if not isinstance(value, str):
                return str(value)
            return value.strip().replace('\n', ' ').replace('\t', ' ')
        
        assert sanitize_string("  test  ") == "test"
        assert sanitize_string("test\nwith\nnewlines") == "test with newlines"
        assert sanitize_string("test\twith\ttabs") == "test with tabs"
        assert sanitize_string(123) == "123"
    
    def test_score_calculation_edge_cases(self):
        """Test score calculation with edge cases."""
        def calculate_score(name):
            return len(name.strip()) * 10 if name and isinstance(name, str) else 0
        
        assert calculate_score("Alice") == 50
        assert calculate_score("") == 0
        assert calculate_score("  ") == 0
        assert calculate_score(None) == 0
        assert calculate_score(123) == 0


class TestIntegration:
    """Integration tests for the complete workflow."""
    
    def test_complete_workflow(self):
        """Test the complete data processing workflow."""
        # Create processor with mocked config
        with patch('os.path.exists', return_value=False):
            processor = DataProcessor()
        
        # Add test data
        test_data = [
            {'name': 'John Doe', 'department': 'Engineering', 'role': 'Senior Developer'},
            {'name': 'Jane Smith', 'department': 'Marketing', 'role': 'Marketing Manager'},
            {'name': 'Bob Johnson', 'department': 'Sales', 'role': 'Sales Representative'}
        ]
        
        for item in test_data:
            processor.add_data(item)
        
        # Process data
        processed = processor.process_data()
        
        # Verify processed data
        assert len(processed) == 3
        assert all('id' in item for item in processed)
        assert all('score' in item for item in processed)
        assert all('timestamp' in item for item in processed)
        
        # Check that IDs are sequential
        ids = [item['id'] for item in processed]
        assert ids == [1, 2, 3]
        
        # Check scores are calculated correctly
        expected_scores = [
            len('John Doe') * 10,         # 80
            len('Jane Smith') * 10,       # 100
            len('Bob Johnson') * 10       # 110
        ]
        actual_scores = [item['score'] for item in processed]
        assert actual_scores == expected_scores
        
        # Test statistics
        stats = processor.get_stats()
        assert stats['total_items'] == 3
        assert stats['config_loaded'] is True
    
    def test_workflow_with_file_operations(self):
        """Test workflow including file save operations."""
        with patch('os.path.exists', return_value=False):
            processor = DataProcessor()
        
        # Add and process data
        processor.add_data({'name': 'Test User', 'department': 'IT', 'role': 'Tester'})
        processed = processor.process_data()
        
        # Test saving to temporary file
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json') as temp_file:
            temp_filename = temp_file.name
        
        try:
            processor.save_results(processed, temp_filename)
            
            # Verify file was created and contains correct data
            assert os.path.exists(temp_filename)
            
            with open(temp_filename, 'r') as file:
                saved_data = json.load(file)
            
            assert len(saved_data) == 1
            assert saved_data[0]['name'] == 'Test User'
            assert saved_data[0]['id'] == 1
            assert saved_data[0]['score'] == len('Test User') * 10
        finally:
            os.unlink(temp_filename)


# Test configuration and fixtures
@pytest.fixture(scope="session")
def test_config():
    """Session-wide test configuration."""
    return {
        'test_database_path': ':memory:',
        'test_data_size': 100,
        'performance_threshold': 1.0  # seconds
    }


# Performance tests
class TestPerformance:
    """Performance and load testing."""
    
    def test_large_dataset_processing(self, test_config):
        """Test processing large datasets within time constraints."""
        import time
        
        with patch('os.path.exists', return_value=False):
            processor = DataProcessor()
        
        # Generate large dataset
        large_dataset = [
            {'name': f'User {i}', 'department': f'Dept {i % 5}', 'role': f'Role {i % 3}'}
            for i in range(test_config['test_data_size'])
        ]
        
        # Measure processing time
        start_time = time.time()
        
        for item in large_dataset:
            processor.add_data(item)
        
        processed = processor.process_data()
        
        end_time = time.time()
        processing_time = end_time - start_time
        
        # Assert performance criteria
        assert processing_time < test_config['performance_threshold']
        assert len(processed) == test_config['test_data_size']
        
        # Verify data integrity
        assert all('id' in item for item in processed)
        assert all('score' in item for item in processed)


if __name__ == "__main__":
    # Run tests if this file is executed directly
    import sys
    
    # Add current directory to Python path
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    
    # Run pytest
    pytest.main([__file__, "-v", "--tb=short"])
