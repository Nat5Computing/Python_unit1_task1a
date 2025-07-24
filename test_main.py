import unittest
import io
import sys
import runpy

class TestTask1A(unittest.TestCase):
    def test_print_output(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            runpy.run_path("main.py", run_name="__main__")
        except Exception as e:
            self.fail(f"main.py crashed with error: {e}")
        finally:
            sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip().lower()
        self.assertTrue("welcome" in output, "The output should include the word 'welcome'")

if __name__ == "__main__":
    unittest.main()