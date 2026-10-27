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
2. On Ubuntu, install Python 3.13, pip, and virtual-environment support:

   ```bash
   sudo apt update
   sudo apt install python3.13 python3.13-venv python3-pip
   python -m pip install --upgrade pip setuptools wheel
   ```

   Python 3.13 is recommended because the pinned dependencies may not yet provide
   wheels for Python 3.14. If your Ubuntu release does not provide Python 3.13,
   install it with a Python version manager such as `uv`.
3. Create and activate a virtual environment, then install the project dependencies:

   ```bash
   python3.13 -m venv .venv313
   source .venv313/bin/activate
   python -m pip install -r requirements.txt
   ```

   On Windows, activate the environment with `.venv313\Scripts\activate` instead.
   The `pywinpty` requirement is restricted to Windows.

   Check for succesful dependency installment: 
   ```bash
   python -c "
   import streamlit
   import qiskit
   import qiskit_aer
   import sklearn
   import numpy
   import pandas
   import matplotlib
   import scipy

   print('All BB84 dependencies imported successfully!')
   "
   ```
   Expected: All BB84 dependencies imported successfully!

   Check for dependency conflicts: 
   ```bash
   python -m pip check
   ```
   Expected: No broken requirements found.
4. Start the Streamlit app:

   ```bash
   python -m streamlit run app_main.py
   ```


Presentation link: https://view.genially.com/6904d8d738afef9b6c88499e/guide-project
