# 🚗 AMSTE-MultiSSE: AUTOSAR Mixed-Signal Timing Extension & Multi-Core Static State Estimation

[![Milestone](https://img.shields.io/badge/Milestone-Phase%201%20(50%25)%20Complete-brightgreen)](#-replicated-milestone-results-phase-1)
[![Platform](https://img.shields.io/badge/Target-AUTOSAR%20Multi--Core-blue)](#-architecture--technologies)
[![Toolchain](https://img.shields.io/badge/LLVM-14.0.6-orange)](#-architecture--technologies)
[![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%204%20%2F%205-purple)](#-phase-2-roadmap-amste)

---

## 📌 Project Overview

This repository contains the reproduction and extension framework for **MultiSSE** (*Multi-Core System State Enumeration*), based on the research paper:
> **"Applied Static Analysis and Specialization of Cross-Core Syscalls for Multi-Core AUTOSAR OS"**  
> *Entrup et al., Real-Time Systems, vol. 60, pp. 491–533, 2024.*

### **Team Information**
* **Students:** K. Deveswar · P. Mourya Sai · E. Venkata Harsha Vardhan
* **Supervisor:** Mr. V. Krishna Mohan  
* **Institution:** Vasavi College of Engineering, Hyderabad  

---

## 🎯 Project Objectives & Roadmap

The project is structured into two main phases:

```
┌─────────────────────────────────────────────────────────┐
│              Phase 1: 50% Milestone (COMPLETED)          │
│   • Podman Container & LLVM 14 Toolchain Setup          │
│   • Native C++ & Cython ARA/SVF Engines Compiled        │
│   • MultiSSE State Exploration Pipeline Executed        │
│   • MSTG, SP Mapping, Lock Elision & IPI Analysis       │
└────────────────────────────┬────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────┐
│            Phase 2: 50% Extension (IN PROGRESS)         │
│   • AMSTE: AUTOSAR Mixed-Signal Timing Extension        │
│   • MATLAB / Simulink Analog Sensor Latency Model       │
│   • Timing-Aware State Pruning in LP Solver             │
│   • Bare-Metal Hardware Validation on Raspberry Pi 5    │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 Replicated Milestone Results (Phase 1)

Our replicated static state exploration engine analyzed a partitioned dual-core AUTOSAR OS application (`Core 0` & `Core 1`) across 61 fixed-point iterations:

| Metric | Measured Value | Description / Impact |
| :--- | :---: | :--- |
| **MSTG Global Vertices** | **112** | Total multi-core system states solved |
| **MSTG Transitions (Edges)** | **743** | Valid concurrent execution paths |
| **Synchronization Points (SPs)** | **59** | Inter-core interaction boundaries |
| **Local Abstract States (LAbSSs)** | **43** | Compressed single-core abstract states |
| **Deadlocks Verified** | **0** | Statically verified deadlock-free concurrency |
| **IPI Avoidance Target** | **State 7 (ABB 139)** | Identified mandatory cross-core interrupt |

### **Hardware Speedup Benchmarks (Paper Published & Reference Model)**

* **Lock Elision Rate:** **65.7%** of spinlocks in multi-core AUTOSAR systems can be statically deleted (saving **1,514 cycles** per lock pair).
* **IPI Avoidance Overhead Saved:** **1,140 cycles** saved per avoided Inter-Processor Interrupt (**61.9% speedup**).
* **State Space Pruning:** Timing-aware state bounds prune graph complexity by up to **−51.1% Vertices** and **−73.9% Edges**.

---

## 🖥️ Interactive Visualizers & Evaluation Dashboards

This repository includes standalone interactive HTML dashboards for project evaluations:

1. 📊 [**`Project_Evaluation_Dashboard.html`**](./dashboards/Project_Evaluation_Dashboard.html)  
   *Executive panel dashboard with KPI cards, state reduction charts, and hardware speedup comparisons. Printable to PDF.*

2. 🔀 [**`Structured_MSTG_Visualizer.html`**](./dashboards/Structured_MSTG_Visualizer.html)  
   *Multi-core Swimlane visualizer for the MSTG graph. Groups Core 0, Core 1, and Synchronization Points cleanly with dynamic path highlighting.*

3. 🖼️ [**`mstg_reduced_structured.svg`**](./parrot/dumps/mstg_reduced_structured.svg)  
   *Structured SVG vector graph of the reduced multi-core state transition graph.*

---

## 🛠️ Architecture & Technologies

* **Core Language & Runtime:** C++17, Python 3.11, Cython, LLVM 14.0.6 IR
* **OS Target:** Multi-Core AUTOSAR OS (dOSEK / Trampoline RTOS)
* **Static Analysis Engines:** ARA (*Automatic RTOS Analyzer*), SVF (*Static Value-Flow*)
* **Build System:** Meson 1.12, Ninja 1.11, Podman / Docker (WSL2 Rocky Linux 10)
* **Extension Phase:** MATLAB R2024b, Simulink AUTOSAR Blockset

---

## ⚡ Quickstart: Running the Analysis in WSL / Podman

### **Prerequisites**
* Windows 11 with WSL2 enabled.
* Container runtime (`podman` or `docker`).

### **Run the Analysis Pipeline (< 45 seconds)**

```bash
# Clone the repository
git clone https://github.com/your-username/AMSTE-MultiSSE.git
cd AMSTE-MultiSSE

# Execute MultiSSE analysis via Podman container
podman run --rm \
  -v $(pwd)/parrot:/mnt/d/Major_Project/parrot:rw \
  -w /mnt/d/Major_Project/parrot \
  -e LD_LIBRARY_PATH=/mnt/d/Major_Project/parrot/build/subprojects/svf:/mnt/d/Major_Project/parrot/build/subprojects/sparsedata \
  localhost/parrot-ara:latest \
  python3 run_ara.py \
    appl/AUTOSAR/autosar_multicore_minexample.pi4.ll \
    --os AUTOSAR \
    --oilfile build/appl/AUTOSAR/autosar_multicore_minexample.oil.json \
    --step-settings settings/autosar_generator_arm.json \
    --dump --log-level info
```

Outputs will be freshly dumped to `./parrot/dumps/`.

---

## 📄 License & Attribution

* Original MultiSSE paper & PARROT framework by **Entrup et al. (Leibniz Universität Hannover / SRA)**.
* Extended for AUTOSAR Mixed-Signal Timing (AMSTE) at **Vasavi College of Engineering**.
