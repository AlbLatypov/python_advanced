import subprocess
import sys

# Run ls -la and capture its output
output = subprocess.check_output(['ls', '-la'])

# Write the output to stdout
sys.stdout.write('     '+output.decode('utf-8'))

