# bb84 - task

## Implement

* end-to-end key generation
* measurement
* sifting procedures
* error-rate estimation to detect any eavesdropping

## What the project will do: 

* collect an plot key metrics
* illustrate how metrics shift when we introduce noise

## Visual output

* app using streamline
* visual run of bb84 protocol
* results for the n scenarios

## How to run:
1. Clone or fork the repository and navigate to the project directory.
2. On Ubuntu, install Python 3, pip, and virtual-environment support:

   ```bash
   sudo apt update
   sudo apt install python3 python3-venv python3-pip
   ```

   Ubuntu provides Python as `python3`; the package named `python` may not be available.
3. Create and activate a virtual environment, then install the project dependencies:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

   On Windows, activate the environment with `.venv\Scripts\activate` instead.
4. Start the Streamlit app:

   ```bash
   streamlit run app_main.py
   ```


Presentation link: https://view.genially.com/6904d8d738afef9b6c88499e/guide-project
