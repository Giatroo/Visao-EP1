# Exercício-Projeto - Visão

To run the project, create a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

Then, run the `data_processing.ipynb` notebook to process the raw data in the
`original_files` folder and generate a new folder with the processed images.

Then, feel free to explore the repository.

## Notes for professor and TAs

In EP2, I'm saving all the images already converted to grayscale in a new
folder. On those images presaved, I'm going to apply the true data augmentation
techniques, as stated in the project description.
