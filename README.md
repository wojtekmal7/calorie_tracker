
# Radar Motion Trajectory Reconstruction

## Overview

This project performs 3D motion trajectory reconstruction of a person based on radar sensor data. The data used includes distances measured between the person and 4 radar sensors over time, stored in `.mat` and `.csv` files. The method applies a linearization of the multilateration problem and solves the system using LU decomposition.

## Structure

The project consists of four major tasks:

### Task 1: System Setup
- Loads the file `MNUB_24L_P1_dane17.mat`.
- Initializes matrices `A` and `b` based on radar positions `R` and measured distances `D`.

### Task 2: LU Decomposition
- Performs LU decomposition of matrix `A`.
- Solves for person’s position over time using forward and backward substitution.
- Reconstructs the 3D and 2D trajectories and visualizes them with `plot3()` and `plot()`.

### Task 3: Error Propagation due to Distance Noise
- Applies multiplicative Gaussian noise to distance measurements `D`.
- Calculates relative aggregated error for position estimation.
- Estimates theoretical error using the condition number of matrix `A`.

### Task 4: Sensitivity Analysis of Radar Sensor Placement
- Introduces variation in the z-coordinate of each radar individually.
- Computes impact on:
  - Aggregated position error
  - Determinant of `A`
  - Condition number of `A`
- Visualizes how sensitivity varies with respect to sensor perturbations.

## How to Run

Run the MATLAB script in any recent version of MATLAB:

```matlab
clear; close all; clc;
% paste the code into the MATLAB editor or run the file directly.
```

Ensure the data file `MNUB_24L_P1_dane17.mat` is in the current working directory.

## Dependencies

- MATLAB R2021a or newer (recommended)
- No external toolboxes required

## Data Files

- `MNUB_24L_P1_dane17.mat` – primary dataset containing matrices `R`, `D`, and `t`
- `MNUB_24L_P2_dane17.mat`, `MNUB_24L_P3_dane17.csv` – optional for comparative analysis

## Author

Wojciech Malesiński

## License

This project is for educational and demonstration purposes only.
