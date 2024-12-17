### Hexlet tests and linter status, Code Climate Maintainability, Test Coverage
[![Actions Status](https://github.com/putilovms/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/putilovms/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/5303df8bc4f4d733c7a6/maintainability)](https://codeclimate.com/github/putilovms/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/5303df8bc4f4d733c7a6/test_coverage)](https://codeclimate.com/github/putilovms/python-project-50/test_coverage)
# Gendiff
*Educational project*

An application for finding the difference in 2 files of json, yaml, yaml formats and displaying the result in several variants

## Installation
1. Requires Python version 3.10 or higher and Poetry
2. Clone the project: `>> git clone https://github.com/putilovms/python-project-50.git`
3. Install the project: `>> make install`
4. Build the project: `>> make build`
5. Install the package: `>> make package-install`

### Usage and Options:
To use it just type `gendiff [-h] [-f FORMAT] <path_to_file_1> <path_to_file_2>`

* -h, --help - show help message.
* -f, --format - ability to specify format selection. Formats are available:
  * `stylish` - displaying differences in the form of a tree
  * `plain` - displaying differences line by line
  * `json` - output in json format

The command for the example: `gendiff example/file1.json example/file2.json`

## Docker
1. Create an image: `>> docker build . -t gendiff`
2. Run the container in the background: `>> docker run --name gendiff -itd --rm gendiff`
3. Connect to a container: `>> docker exec -it gendiff bash`

## Examples of uses
### Diff of flat files (JSON)
[![asciicast](https://asciinema.org/a/y883XzL7Hyb8cqRXrJXJ02CzI.svg)](https://asciinema.org/a/y883XzL7Hyb8cqRXrJXJ02CzI)
### Diff of flat files (YAML)
[![asciicast](https://asciinema.org/a/l7EZhGtKDNHAqiVdstUjr2J6e.svg)](https://asciinema.org/a/l7EZhGtKDNHAqiVdstUjr2J6e)
### Diff of deep files
[![asciicast](https://asciinema.org/a/rjQGoPbh9FlFMIS2p20Gjgqap.svg)](https://asciinema.org/a/rjQGoPbh9FlFMIS2p20Gjgqap)
### Diff of deep files with plain style
[![asciicast](https://asciinema.org/a/xHvBMNvqq0LXa5Lu1eIdzJiyw.svg)](https://asciinema.org/a/xHvBMNvqq0LXa5Lu1eIdzJiyw)
### Diff of deep files with json style
[![asciicast](https://asciinema.org/a/EgToweP5iXH1M11ZSdgqt5Riw.svg)](https://asciinema.org/a/EgToweP5iXH1M11ZSdgqt5Riw)
