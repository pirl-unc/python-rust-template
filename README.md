# python-rust template
This repository is a template for integrating python and rust source codes into a package.
The template additionally includes a GitHub Actions workflow for unit testing.

[![build](https://github.com/pirl-unc/python-rust-template/actions/workflows/main.yml/badge.svg)](https://github.com/pirl-unc/python-rust-template/actions/workflows/main.yml)

## 01. Installation

```shell
pip install . --verbose
```

## 02. Usage

The `add` function uses a [rust function](https://github.com/pirl-unc/python-rust-template/blob/main/src/lib.rs).

```shell
testpkg add --value_1 5 --value_2 10
```

