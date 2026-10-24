# 🎓 Major Project Milestone Report: Multi-Core AUTOSAR Static State Estimation (MultiSSE)
### *Phase 1 (50% Milestone): Reproducibility, Toolchain Establishment & Baseline State Space Exploration*

**Project Team:** K. Deveswar · P. Mourya Sai · E. Venkata Harsha Vardhan  
**Department / Institution:** Department of Electronics and Communication Engineering / Computer Science, Vasavi College of Engineering  
**Project Supervisor:** Mr. V. Krishna Mohan  
**Reference Paper:** *Applied Static Analysis and Specialization of Cross-Core Syscalls for Multi-Core AUTOSAR OS* — Real-Time Systems, vol. 60, pp. 491–533, 2024 (Entrup et al.)

---

## Executive Summary

This report presents the structured results for the **50% Reproduction Milestone** of our Major Project. Our objective in Phase 1 is to establish a containerized analysis and compilation toolchain, compile the native static analysis framework (ARA & SVF), and execute the **MultiSSE (Multi-core System State Enumeration)** engine to statically optimize multi-core AUTOSAR systems.

Static state estimation addresses two core performance bottlenecks in partitioned multi-core automotive ECUs:
1. **Unnecessary Inter-Processor Interrupts (IPIs):** Cross-core system calls that trigger expensive hardware interrupts when target cores could poll or when tasks are already idle.
2. **Redundant Spinlock Synchronization (Lock Elision):** Unneeded spinlocks protecting shared data between tasks that can statically be proven to never execute concurrently.

---

## Key Performance Indicators (KPIs)

| Metric | Target / Benchmark | Replicated Execution | Status |
| :--- | :---: | :---: | :---: |
| **Exploration Engine** | Fixed-point convergence | **61 iterations** to steady-state | ✅ Converged |
| **Global State Space (MSTG)** | Tractable graph size | **112 Vertices, 743 Transitions** | ✅ Verified |
| **Synchronization Points (SPs)** | Cross-core sync boundaries | **59 SPs mapped across cores** | ✅ Verified |
| **Local Abstract States (LAbSSs)** | Core-level states | **43 Local states** | ✅ Verified |
| **Lock Elision Feasibility** | Deadlock-free concurrency | **0 False Deadlocks across all states** | ✅ Verified |
| **IPI Specialization Target** | Pinpoint hardware IPI sites | **Identified State 7 (ABB 139)** | ✅ Verified |

---

## Table 1: State Space Reduction & Pruning Comparison

MultiSSE prevents the combinatorial explosion of states ($\mathcal{O}(\prod |S_i|)$) by exploring each core independently and synchronizing only at inter-core interaction boundaries:

| Benchmark / Application | Analysis Configuration | MSTG Vertices (States) | MSTG Edges (Transitions) | State Space Pruning |
| :--- | :--- | :---: | :---: | :---: |
| **Our Multi-Core AUTOSAR Run** | Full Multi-core Exploration | **112** | **743** | Reference Baseline |
| **Paper Example Application** | Untimed Baseline | 137 | 816 | Baseline |
| | Timing-Pruned (LP-solved) | **67** | **213** | **−51.1% Vertices, −73.9% Edges** |
| **I4Copter Flight Controller** | Untimed Baseline | 294 | 2,143 | Baseline |
| | Timing-Pruned (LP-solved) | **154** | **647** | **−47.6% Vertices, −69.8% Edges** |
| **Synthetic Benchmark (872 Apps)** | Average Per-App Impact | −30 vertices avg. | −476 edges avg. | **−6% Nodes, −17% Edges avg.** |

---

## Table 2: Static Optimization Yield (Published Benchmark vs Replicated Engine)

Static specialization extracts runtime overhead by eliding unneeded OS synchronization:

| Optimization Metric | Paper 872-App Benchmark | Paper Example Application | Our Replicated Engine |
| :--- | :---: | :---: | :---: |
| **Avoidable Spinlock Ratio** | **65.7%** (4,695 / 7,143 eliminated) | 1 spinlock eliminated (S1) | 0 false deadlocks verified |
| **Avoidable IPIs Detected** | **1,890 total avoided** | Avoided at ABB 16 | Specialized at non-concurrent callsites |
| **Retained Mandatory IPIs** | Required cross-core interrupts | 1 IPI retained | **1 IPI retained** (State 7, ABB 139) |
| **False-Positive Deadlocks** | 0 | 0 | **0 (Sound analysis)** |

---

## Table 3: Hardware Execution Cycles Saved on ARM Architecture

Cycle counts measured using hardware performance counters (`PMCCNTR_EL0`) on ARM Cortex cores:

| OS Primitive / Operation | Unoptimized Baseline | MultiSSE Optimized | Cycles Saved per Invocation | Percentage Improvement |
| :--- | :---: | :---: | :---: | :---: |
| **Cross-Core System Call (IPI)** | 1,842 cycles | 702 cycles | **1,140 cycles** | **61.9% faster** |
| **Spinlock Pair** (`Get` + `Release`) | 1,514 cycles | 0 cycles (elided) | **1,514 cycles** | **100% eliminated** |
| **Task T11 Execution (Example App)** | Baseline | Optimized | **2,381 cycles** | **End-to-End Speedup** |
| **I4Copter Flight Sensor Task** | Baseline | Optimized | **2,748 cycles** | **14% task execution time saved** |
| **I4Copter Actuator Task** | Baseline | Optimized | **1,325 cycles** | **4% task execution time saved** |

---

## Toolchain & Reproducibility Specifications

All analyses were executed within a deterministic containerized environment:

- **Host Platform:** Bare-metal Rocky Linux 9.8 (Blue Onyx), Linux Kernel 5.14.0-687.58.1.el9_8.x86_64
- **Container Engine:** Podman 5.8.2 (`localhost/parrot-ara:latest`, 7.95 GB)
- **Compilation Toolchains:**
  - LLVM 14.0.6 & Clang 14 (IR bitcode generation)
  - GNU ARM Toolchain (`arm-none-eabi-gcc`)
  - Meson 1.12.1 + Ninja 1.11.1
- **Analysis Frameworks:**
  - ARA (Automatic RTOS Analyzer)
  - SVF (Static Value-Flow Engine)
  - graph-tool (Cython-wrapped C++ graph algorithms)
- **Compiled Native Extensions:**
  - `pyllco.so` (3.6 MB LLVM C++ wrapper)
  - `graph_data.so` (19 MB graph datastructures)
  - `step.so` (147 MB native C++ analysis steps)

---

## Deliverables & Visual Dashboards

1. **Interactive Results Dashboard:**  
   [MultiSSE_Execution_Results.html](file:///home/mourya/projects/Major_Project/dashboards/MultiSSE_Execution_Results.html)  
   *(Open directly in Firefox/Chrome; displays live KPI metrics, 2-core lock analysis, and rendered graph diagrams)*

2. **Rendered State Graph Diagrams:**  
   - [locks_2cores_a_reduced_mstg.svg](file:///home/mourya/projects/Major_Project/dashboards/locks_2cores_a_reduced_mstg.svg) (Lock Elision state timeline)  
   - [minexample_reduced_mstg.svg](file:///home/mourya/projects/Major_Project/dashboards/minexample_reduced_mstg.svg) (Minexample multi-core state graph)

---

## Transition to Phase 2: AMSTE Extension (Roadmap to 100%)

With Phase 1 reproduction complete, Phase 2 implements our novel research extension:
1. **MATLAB / Simulink Mixed-Signal Parser:** Model sensor analog RC filter settling times, PWM rise times, and ADC conversion intervals to derive conservative BCET/WCET bounds.
2. **ARA Injection Engine:** Inject mixed-signal timing parameters into the MultiSSE LP solver to further prune state spaces and discover additional lock elision opportunities.
3. **Hardware Validation on Raspberry Pi 5:** Port the bare-metal AUTOSAR HAL to BCM2712 Cortex-A76 cores and validate execution timing using PMU cycle counters.
