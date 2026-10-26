# Setup - do this before Class 1

You need Python installed, a folder, and three packages. Ten minutes.

## 1. Install Python 3.12

Not the newest version. 3.12. Newer versions break libraries we use later in the course.

- macOS: `brew install python@3.12`
- Windows: python.org downloads, tick "Add Python to PATH"
- Linux: `sudo apt install python3.12 python3.12-venv`

## 2. Create the environment, inside this folder

macOS / Linux:

    python3.12 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Windows PowerShell:

    py -3.12 -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

## 3. Your key

Create a file called `.env` in this folder, containing one line:

    GROQ_API_KEY=gsk_your_key_here

Get the key free at console.groq.com. No card required.

`Groq` with a q is the inference provider we use. `Grok` is a different thing
made by xAI. Groq keys start with `gsk_`. If yours starts with `xai-` you have
the wrong one.

`.env` is already in `.gitignore`. Never move it out.

## 4. Select the kernel in VS Code

Open `Class1.ipynb`, click the kernel name in the top right, and choose the one
whose path says `.venv`. If `.venv` is not listed, close and reopen VS Code.

If a cell says "Running cells requires the ipykernel package", you have selected
a system Python instead of `.venv`. Change it.

## 5. Check it works

Run the first two cells. You should see your key prefix and "Client ready."
If you do, you are ready for Class 1.
