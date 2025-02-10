# NDP Framework
The goal of this project is to create a framework by which I can explore Near Data Processing (NDP) algorithms and, eventually, estimate the performance of an NDP-based appliance on relevant graph and AI benchmarks.
The baseline is to have Python objects for the NDP storage nodes and different Python objects for the interconnect between the nodes. Then, I can ascribe performance numbers to each computation and move. I plan to build a ledger of each action when it happens in the simulation. Then, I can back-annotate with the performance implications.

## Next steps
### Software infrastructure
I want to use NDP techniques to gain experience solving real-world problems. Examples include:
- Graph analytics game solvers (solitaire, poker, rubik's cube)
- GNNs for the stock market, taking into account fundmental, tachnical, and cyclical events.
  
After gaining this experience, it should be more obvious what kind of software strategy to pursue. One thought is to use CUDA so that it can easily be substituted in for GPUs. I know Intel chose to develop their own OneAPI based on SyCL instead of using CUDA, though. I wonder if that was for legal reasons or NIH syndrome. Doing the very basic activities like those in the current code shows just how clunky both CUDA and SyCL are. After letting CoPilots develop this code in various Parallel processing models/languages, I am very interested in pursuing Julia. 

I asked Meta.AI about it:
> **SYCL Advantages**:
> - Open Standard: SYCL is an open standard, maintained by the Khronos Group, which ensures vendor neutrality and avoids lock-in to a specific proprietary technology.
> - Cross-Vendor Compatibility: SYCL allows for code portability across different vendors' hardware, including CPUs, GPUs, FPGAs, and other accelerators.
> - C++-Based: SYCL is built on top of C++ and provides a single-source, heterogeneous programming model, making it easier for developers to write code that can run on various devices.
> - Low Overhead: SYCL has a relatively low overhead compared to other programming models, which results in better performance and efficiency.
> 
> **Why Not CUDA?**
> - NVIDIA Proprietary: CUDA is a proprietary technology developed by NVIDIA, which would have limited Intel's ability to create a vendor-agnostic platform.
> - Limited Hardware Support: CUDA is primarily designed for NVIDIA GPUs, which would have restricted OneAPI's ability to support a broader range of hardware devices.
> 
> **Why Not Julia?**
> - Programming Language: Julia is a programming language, whereas SYCL is a programming model. Intel aimed to create a platform that could support multiple programming languages, not just one.
> - Maturity and Adoption: While Julia is a promising language, it is still evolving and has a smaller user base compared to C++ and other established languages.
> - Performance and Optimization: SYCL's focus on low-level, performance-oriented programming allows for finer-grained control over hardware resources, which is essential for achieving optimal performance in high-performance computing (HPC) and artificial intelligence (AI) workloads.
> By building OneAPI on SYCL, Intel aimed to create a flexible, vendor-agnostic platform that could support a wide range of hardware devices, programming languages, and use cases, while also providing low-level performance optimization capabilities.
