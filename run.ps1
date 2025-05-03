# Create a virtual environment.
python -m venv venv

# Activate the virtual environment.
.\venv\Scripts\Activate.ps1

# Install dependencies.
pip install requests beautifulsoup4 schedule python-dotenv

# Run the `main` script.
python .\main.py
