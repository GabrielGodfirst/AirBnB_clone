#!/usr/bin/python3
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand console."""

    def test_help_show(self):
        """Test the help output for the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
        self.assertIn(
            "Prints the instance the class name and id.",
            output
         )

    def test_create(self):
        """Test the 'create' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
        self.assertTrue(len(user_id) > 0)

    def test_show(self):
        """Test the 'show' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn(f"[User] ({user_id})", output)

    def test_all(self):
        """Test the 'all' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
        self.assertTrue(output.startswith("["))

    def test_destroy(self):
        """Test the 'destroy' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(f"destroy User {user_id}")
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn("** no instance found **", output)

    def test_update(self):
        """Test the 'update' command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(f'update User {user_id} first_name "John"')
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn('"first_name": "John"', output)

    def test_update_dict(self):
        """Test the 'update' command with a dictionary."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            user_id = f.getvalue().strip()
            HBNBCommand().onecmd(
                f'update User {user_id} '
                f'{{"first_name": "John", "age": 30}}'
            )
            HBNBCommand().onecmd(f"show User {user_id}")
            output = f.getvalue().strip()
        self.assertIn('"first_name": "John"', output)
        self.assertIn('"age": 30', output)
