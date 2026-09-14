"""
Alert System
============
Generates alerts when threats are detected and logs them.

YOUR TASKS:
1. Implement AlertManager.__init__() to set up state and log file
2. Implement AlertManager.create_alert() to build structured alert dicts
3. Implement AlertManager.log_alert() to write JSON Lines to disk
4. Implement AlertManager.print_alert() for color-coded console output
5. Implement AlertManager.get_summary() to return detection statistics
"""

import json
import os
from datetime import datetime
from pathlib import Path

DEFAULT_LOG_DIR = Path(__file__).resolve().parent.parent / 'logs'


class AlertManager:
    """
    Manages threat alerts — formats, logs, and tracks statistics.

    TODO: Implement all methods below.
    """

    def __init__(self, log_dir=None):
        """
        Initialize the alert manager.

        Steps:
        1. Set log_dir (use DEFAULT_LOG_DIR if not provided)
        2. Create the log directory if it doesn't exist
        3. Initialize:
           - self.alerts: empty list to store all alert dicts
           - self.stats: dict to count alerts by threat level
             {'LOW': 0, 'MEDIUM': 0, 'HIGH': 0, 'CRITICAL': 0}
           - self.log_file: path to 'alerts.log' inside log_dir
           - self.total_processed: 0  (tracks all connections, not just alerts)

        Args:
            log_dir (str or Path, optional): Directory for log files
        """
        # TODO: Implement this
        pass

    def create_alert(self, batch_num, connection_index, prediction, probability, threat_level):
        """
        Create a structured alert dictionary.

        The alert dict should include:
        - timestamp: current datetime as ISO-format string (datetime.now().isoformat())
        - alert_id: auto-incrementing integer (len(self.alerts) + 1)
        - batch_number: which batch this connection came from
        - connection_index: index within the batch
        - prediction: 0 or 1
        - probability: float between 0.0 and 1.0
        - threat_level: "LOW", "MEDIUM", "HIGH", or "CRITICAL"

        Steps:
        1. Build the alert dict with all fields above
        2. Append it to self.alerts
        3. Increment self.stats[threat_level]
        4. Return the alert dict

        Returns:
            dict: structured alert
        """
        # TODO: Implement this
        pass

    def log_alert(self, alert):
        """
        Write an alert to the log file as a JSON line.

        JSON Lines format = one JSON object per line. This is easy to parse
        programmatically and works well with streaming/append workflows.

        Steps:
        1. Open self.log_file in append mode ('a')
        2. Write json.dumps(alert) followed by a newline
        3. Close the file (or use a 'with' block)

        Args:
            alert (dict): The alert dict from create_alert()
        """
        # TODO: Implement this
        pass

    def print_alert(self, alert):
        """
        Print alert to console with color-coded threat level.

        ANSI color codes for terminal output:
        - LOW:      green    \\033[92m
        - MEDIUM:   yellow   \\033[93m
        - HIGH:     red      \\033[91m
        - CRITICAL: bold red \\033[1;91m
        - Reset:             \\033[0m

        Format:
        [2024-01-15T10:30:00] [CRITICAL] Alert #42 — Connection #7 flagged (probability: 95.3%)

        Args:
            alert (dict): The alert dict from create_alert()
        """
        # TODO: Implement this
        pass

    def get_summary(self):
        """
        Return a summary of all alerts generated during this session.

        Returns:
            dict: {
                'total_alerts': int,
                'total_processed': int,
                'alerts_by_level': dict of {level: count},
                'detection_rate': float (total_alerts / total_processed if > 0)
            }
        """
        # TODO: Implement this
        pass


if __name__ == '__main__':
    print("Testing AlertManager...")
    manager = AlertManager()
    print(f"Log file: {manager.log_file}")
    print("AlertManager initialized successfully.")
