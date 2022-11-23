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
conda create --name py38 python=3.8
conda activate py38
git clone git@gitlab.com:feriret/memex-benchmarking.git
cd memex-benchmarking
pip install --upgrade pip
pip install -r requirements.txt
```
### How to use:
Anonymized imagery can be downloaded from Mapillary server using the official [Mapillary-SDK](https://github.com/mapillary/mapillary-python-sdk). This project is an extension of the Mapillary scripts for downloading non-resized imagery (full resolution (4000x3000)). A Mapillary access token must be created for each user. Modify line 11 in the main script with you own Token. Instructions for generating an access token are found [here](https://help.mapillary.com/hc/en-us/articles/360010234680-Accessing-imagery-and-data-through-the-Mapillary-API#h_e18c3f92-8b3c-4d26-8a1b-a880bde3a645). Detailed information of functions used in the script are found [here](https://mapillary.github.io/mapillary-python-sdk/docs/mapillary/mapillary.interface/).

#### Download sequences from Json files
```bash
python download_mapillary_sequence.py -i <sequence_id> -r <resolution> -o <output_path>
```

#### Generate JSON files
JSON files provided in this project allows to download synchronized imagery+imu+gps generated with the acquisition system developed by CNRS. However, the script can also be used to download any sequence from Mapillary within an specific area. The script can also generate the JSON file with sorted images according to the creation data tag in the EXIF. The list of sequences ID's (From Mapillary) and the GPS coordinates (west,south,east,north), must be provided. 

## Directory Structure
### Barcelona: 8 smartphones OnePlus9 + GoProMax
```
Sequence_{bcn:1-12}/
|<BEGIN>
|
|---> position_gps.txt
|                                               | ...
|---> B1/				        |---> T1/
|     |						|     |
|     |---> rgb/				|     |---> rgb/
|     |     |---> {000001|XXXXXX}.jpg		|     |     |---> {000001|XXXXXX}.jpg
|     |---> gps.txt				|     |---> gps.txt
|     |---> imu.txt				|     |---> imu.txt
|     |---> rgb.txt				|     |---> rgb.txt
|						|
|---> B2/				        |---> T2/
|     |						|     |
|     |---> rgb/				|     |---> rgb/
|     |     |---> {000001|XXXXXX}.jpg		|     |     |---> {000001|XXXXXX}.jpg
|     |---> gps.txt				|     |---> gps.txt
|     |---> imu.txt				|     |---> imu.txt
|     |---> rgb.txt				|     |---> rgb.txt
|						|
|---> B3/				        |---> T3/
|     |						|     |
|     |---> rgb/				|     |---> rgb/
|     |     |---> {000001|XXXXXX}.jpg		|     |     |---> {000001|XXXXXX}.jpg
|     |---> gps.txt				|     |---> gps.txt
|     |---> imu.txt				|     |---> imu.txt
|     |---> rgb.txt				|     |---> rgb.txt
|						|
|---> B4/				        |---> T4/
|     |						|     |
|     |---> rgb/				|     |---> rgb/
|     |     |---> {000001|XXXXXX}.jpg		|     |     |---> {000001|XXXXXX}.jpg
|     |---> gps.txt				|     |---> gps.txt
|     |---> imu.txt				|     |---> imu.txt
|     |---> rgb.txt				|     |---> rgb.txt
|                                               |<END>
|---> GoProMax
|     |
|     |---> rgb/
|     |     |---> {000001|XXXXXX}.jpg
|     |---> gpx.gpx (GoPro Telemetry)
|     |---> imu.txt (GoPro Telemetry)
|     |---> rgb.txt 
| ...
```
### Lisbon 1: 2 GoProMAX 
Sequence_{lis:1-6}/
|<BEGIN>
|
|---> position_gps.txt
|                                               | ...
|---> GoProMax_B                                |---> GoProMax_T
|     |                                         |     |
|     |---> rgb/                                |     |---> rgb/                                
|     |     |---> {000001|XXXXXX}.jpg           |     |     |---> {000001|XXXXXX}.jpg
|     |---> gpx.gpx (GoPro Telemetry)           |     |---> gpx.gpx (GoPro Telemetry)
|     |---> imu.txt (GoPro Telemetry)           |     |---> imu.txt (GoPro Telemetry)        
|     |---> rgb.txt                             |     |---> rgb.txt 
| ...                                           |<END>
```


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
![360-Benchmark](/figures/Slam_framework_memex.png)

The framework for generating the multi-camera benchmarck is presented in the figure below. 

SLAM poses are fused with the GPS measurements in the UTM coordinate system for prediction and correction of the GPS when it is partially available or absent. 
![GPS-SLAM](/figures/gps_slam_filter.png)

### Multicamera Acquisition System

#### Devices
- 8 Smartphones OnePlus9 (4000x3000 30fps)
- 1 GoProMax (5.6K, 30fps)

#### Software
- Extended OpenCamera app for registering Inertial Sensors + GPS [source code](https://sourceforge.net/u/alnguyen/opencamera/ci/master/tree/)) (Configuration settings are found in Tools/MEMEX_conf.xml)


## Acknowledgements
This work is part of the ANR MEMEX project. [Website](https://memexproject.eu/en/)
