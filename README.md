# qii-workshop
This repository contains the code for the QII Workshop on Characterization-based Error Mitigation for Quantum Computation.

Main Notebooks
  The repository includes two main notebooks: 
  -	`qesem_lab_qiskit_function.ipynb` – uses the [QESEM qiskit function](https://quantum.cloud.ibm.com/docs/en/guides/qedma-qesem).
  -	`qesem_lab_qedma_api.ipynb` - uses the [QEDMA SaaS API](https://docs.qedma.io).

How to Run the Notebooks
  -	Recommended (no local installations needed): 
    Run the notebook at Google Colab. 
    -	Qiskit function version: [click here](https://colab.research.google.com/github/Qedma/qii-workshop/blob/main/qesem_lab_qiskit_function.ipynb).
    -	QEDMA SaaS API version: [click here](https://colab.research.google.com/github/Qedma/qii-workshop/blob/main/qesem_lab_qedma_api.ipynb). 
  - Run locally:
    Clone the repository and run the main Python notebooks locally.
    
Package Requirements

All python package requirements appear at the top of each notebook, along with the pip command to install them: 
pip install "qiskit>=2.0.0" "qiskit-ibm-runtime>=0.40.0" "qiskit-aer>=0.17.1" "networkx>=3.5" "matplotlib==3.10.0" "tqdm>=4.67.1" "scipy" "numpy" "python-dotenv==1.2.1" "pylatexenc>=2.10"  "qiskit-ibm-catalog ==0.11.0" "qedma-api==0.18.3"
For your convenience, requirements can also be installed using poetry from the `poetry.lock` file.

Solution Notebooks

Solution versions of the notebooks are available here:
  - QEDMA SaaS API version:
    - Google Colab: [here](https://colab.research.google.com/github/Qedma/qii-workshop/blob/main/qesem_lab_solution_qedma_api.ipynb)
    - Github file: [here](https://github.com/Qedma/qii-workshop/blob/main/qesem_lab_solution_qedma_api.ipynb)
  - QESEM Qiskit function version:
    - Google Colab: [here](https://colab.research.google.com/github/Qedma/qii-workshop/blob/main/qesem_lab_solution_qiskit_function.ipynb)
    - Github file: [here](https://github.com/Qedma/qii-workshop/blob/main/qesem_lab_solution_qiskit_function.ipynb)
