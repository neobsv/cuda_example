## Using Miniconda

```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
source ~/miniconda3/bin/activate
```

Close the terminal and reopen it

```
conda init --all
```

Install cudatoolkit:

```
conda install cudatoolkit
conda install numba
conda update numba
conda install -c conda-forge cuda-nvcc cuda-nvrtc "cuda-version>=12.0"
```



