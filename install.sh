#!/usr/bin/env bash
# vim: set noexpandtab tabstop=2:

source trapdebug
set -euo pipefail

source "$MAMBA_ROOT_PREFIX/etc/profile.d/micromamba.sh"
pkg=(
poetry
wandb
python=3.10
pytorch
pytorch-cuda=12.1
scvi-tools
scanpy
pandas
numba
scikit-misc
umap-learn
leidenalg
matplotlib
packaging
ninja
numpy
h5py
rpy2
cxx-compiler
torchtext
transformers
jupyter
chex=0.1.7
)
mamba create -n u_scgpt -y -c pytorch-nightly -c nvidia "${pkg[@]}"
mamba activate u_scgpt
pip install flash-attn==1.0.9 --no-build-isolation
pip install scib
pip install git+https://github.com/lijinbio/scGPT
