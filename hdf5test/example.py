import h5py
import numpy as np

def write_test_file(path="sample.h5"):
    with h5py.File(path, "w") as f:
        f.create_dataset("numbers", data=np.arange(10))
    print(f"Created HDF5 file at: {path}")


def read_test_file(path="sample.h5"):
    with h5py.File(path, "r") as f:
        print("Dataset contents:", f["numbers"][:])


if __name__ == "__main__":
    write_test_file()
    read_test_file()
