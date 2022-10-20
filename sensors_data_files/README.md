# Format of Sensor Data Files

This directory contains timestamped sensor measurements (per smartphone of the acquisition system) at each sequence. The measurements can be associated with each image trough the sync_all.py script in Tools directory. The associated measurements text files are created at each downloaded sequence using download_mapillary_sequence.py script. 

## Files Per Sequence

- imu_X.txt
- gps_X.txt
- photo_meta_X.txt
- rgb_X.txt
- position_<id_sequence>.txt


Where X can be {B1, B2, B3, B4, T1, T2, T3, T4} for each sequence.

### Inertial Measurements Format

```
Timestamp[UNIX time] gx[rad/s]	gy[rad/s] gz[rad/s] ax[m/s^2] ay[m/s^2] az[m/s^2]	
```

### GPS Raw Measurements Format

```
Timestamp[UNIX time] latitude[deg] longitude[deg] altitude[deg]
```

### Photometric Information
```
Timestamp[UNIX time] Exposure_time[nanosec] ISO Lens_aperture Focal length Focus_distance
```

### Image Files
```
Timestamp[UNIX time] <PATH_TO_IMAGE>
```

### Corrected GPS Position (Mapillary)
```
Timestamp[UNIX time] latitude[deg] longitude[deg] altitude[deg]
```

