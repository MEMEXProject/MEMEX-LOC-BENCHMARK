# MEMEX-Benchmarks downloader

<br />
<p align="center">
  <p align="center">
    This tool allows to automatically download the sequence of images of a multi-camera system from the Mapillary server using a json file. 
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#installation">Installation and use</a>
    </li>
    <li>
      <a href="#directory-structure">Directory structure</a>
    </li>
    <li>
      <a href="#datasets-list">Datasets List</a>
    </li> 
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#about-the-project">About the Multicamera Acquisition System</a>
    </li> 
    <li>
      <a href="#acknowledgments">Acknowledgements</a>
    </li>   
  </ol>
</details>

## Installation And Use
To install the downloader script just clone this repository, create a new conda python3.8 environment and install the dependencies.  

```bash
conda create --name py38
conda activate py38
git clone git@gitlab.com:feriret/memex-benchmarking.git
cd memex-benchmarking
pip install --upgrade pip
pip install -r requirements.txt
```
### How to use:
Anonymized imagery can be downloaded from Mapillary server using the official Mapillary-SDK. This project is an extension for downloading original imagery (full resolution (4000x3000)). Images were syncronized and geotagged offline using a SLAM-GPS fusion approach.  
#### Download sequences from Json files
```bash
python download_mapillary_sequence.py -i <sequence_id> -r <resolution> -o <output_path>
```

#### Generate JSON files

## Directory Structure


## List of Sequences
### Lisbon
| Sequence ID | Sequence type | Number of images | GPS path | Mapillary Sample online image (Camera T1)
| --- | --- | --- | --- | --- |
| lis01 | outdoor | 40000 | | https://www.mapillary.com/app/?pKey=758173992140720

### Paris
| Sequence ID | Sequence type | Number of images | GPS path | Mapillary Sample online image (Camera T1)
| --- | --- | --- | --- | --- |
| par01 | outdoor | 40000 | |https://www.mapillary.com/app/?pKey=407583920850584

### Barcelona
| Sequence ID | Sequence type | Number of images | GPS path | Mapillary Sample online image (Camera T1)
| --- | --- | --- | --- | --- |
| bcn01 | outdoor | 40000 | |https://www.mapillary.com/app/?pKey=366250235589944

### CNRS-I3S (France)
| Sequence ID | Sequence type | Number of images | GPS path | Mapillary Sample online image (Camera T1)
| --- | --- | --- | --- | --- |
| i3s01 | outdoor/indoor | 40000 | |https://www.mapillary.com/app/?pKey=246105260801609

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a result of performing Visual-SLAM and GPS fusion for correct the GPS location of images in [Mapillary](https://www.mapillary.com) server. 



## Acknowledgements

