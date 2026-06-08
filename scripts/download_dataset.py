import kagglehub

# Download latest version
path = kagglehub.dataset_download(
    "alistairking/nuclear-energy-datasets"
)

print("Path to dataset files:", path)