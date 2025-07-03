
import os
import sys
from subprocess import run, PIPE

def colab_fix():
    """
    Fixes and prepares the environment for running Ultroid on Google Colab.
    """
    try:
        import google.colab
        print("Running in Google Colab. Applying fixes...")
    except ImportError:
        # Not in colab
        return

    # 1. Install nest_asyncio
    print("Installing nest_asyncio...")
    run([sys.executable, "-m", "pip", "install", "-q", "nest_asyncio"], check=True)
    import nest_asyncio
    nest_asyncio.apply()
    print("nest_asyncio applied.")

    # 2. Install system dependencies
    print("Installing system dependencies (ffmpeg, mediainfo, neofetch)...")
    # Colab runs as root, so sudo is not needed.
    run(["apt-get", "update", "-y"], check=True, stdout=PIPE, stderr=PIPE)
    run(["apt-get", "install", "--yes", "ffmpeg", "mediainfo", "neofetch"], check=True, stdout=PIPE, stderr=PIPE)
    print("System dependencies installed.")

    # 3. Install Python requirements
    print("Installing Python requirements...")
    run([sys.executable, "-m", "pip", "install", "-q", "--upgrade", "pip"], check=True)
    run([sys.executable, "-m", "pip", "install", "-q", "https://github.com/New-dev0/Telethon-Patch/archive/main.zip"], check=True)
    run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"], check=True)
    if os.path.exists("resources/startup/optional-requirements.txt"):
        run([sys.executable, "-m", "pip", "install", "-q", "-r", "resources/startup/optional-requirements.txt"], check=True)
    print("Python requirements installed.")

    # 4. Install DB requirements based on .env file
    if os.path.exists(".env"):
        with open(".env", "r") as f:
            env_vars = f.read()
            if "MONGO_URI" in env_vars:
                print("Installing MongoDB requirements...")
                run([sys.executable, "-m", "pip", "install", "-q", "pymongo[srv]"], check=True)
            if "DATABASE_URL" in env_vars:
                print("Installing PostgreSQL requirements...")
                run([sys.executable, "-m", "pip", "install", "-q", "psycopg2-binary"], check=True)
            if "REDIS_URI" in env_vars:
                print("Installing Redis requirements...")
                run([sys.executable, "-m", "pip", "install", "-q", "redis", "hiredis"], check=True)
    
    print("Colab setup finished. You can now run the main Ultroid script.")
