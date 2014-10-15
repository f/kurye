# Kurye: GitHub Project Cloner for Boilerplate Projects

Kurye clones boilerplate repositories and runs specified commands on the `.kurye` file.
By default it clones the repo as `upstream` origin.

## Install

```bash
pip install kurye
```
---

## Usage

```bash
kurye user/repo
```

### Change project name

```bash
kurye user/repo -n PROJECT_NAME
```

### Do not run `.kurye` file on the project.

```bash
kurye user/repo --noboot
```

### Remove `.git` repository

```bash
kurye user/repo --nogit
```

### Change origin name (`upstream` by default)

Using this with `--nogit` option won't make sense.

```bash
kurye user/repo -o ORIGIN_NAME
```

### Change base directory

```bash
kurye user/repo -b ~/MyProjects
```

## Name

Thanks [@emre](https://github.com/emre) for the cool name.
