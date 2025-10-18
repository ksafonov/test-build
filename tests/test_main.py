"""Unit tests for main module."""
import pytest
from io import StringIO
from unittest.mock import patch

from test_build.main import main


class TestMain:
    """Test cases for the main function."""

    @pytest.mark.timeout(30)
    def test_main(self):
        """Test main function - unit_tests for main"""
        # Capture stdout to verify the output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()

        # Assert that "Hello" is printed followed by a newline
        assert output == "Hello\n"