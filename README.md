# NDP Framework
The goal of this project is to create a framework by which I can explore Near Data Processing (NDP) algorithms and, eventually, estimate the performance of an NDP-based appliance on relevant graph and AI benchmarks.

## Implementation Plan
The baseline is to have Python classes for the NDP storage nodes and different Python classes for moving data between the nodes. Then, I can ascribe performance numbers to each computation and move. 

While this may sound simple, even the computations can get complex, which is why the code has the beginnings of a TI DSP model in the Python code. They get even more complicated when factors, such as caching and cache misses, come into play for modern processors. I want to evaluate novel architectures, too, like Forth (https://www.forth.org and https://www.forth.org/cores.html) which focus on simplicity. I also wonder about unique architectures like **Mythic** or Micron's **Automata**.

The real challenges to modeling performance and power are in the movement, though, and that's where this structure should really shine. Whether DDR, NVMe, CXL, or NVLink, the traffic and routing (through CPU or node-to-node) will greatly impact the performance and power. I believe that I need all the resources that I can muster in a class.

I plan to build a, SQL ledger of each action when it happens in the simulation. Then, I can back-annotate with the performance implications to see where I am losing performance opportunity.

## Next steps
### Software infrastructure
I want to use NDP techniques to gain experience solving real-world problems. Examples include:
- Graph analytics game solvers (solitaire, poker, rubik's cube)
- GNNs for the stock market, taking into account fundmental, tachnical, seasonality, and cyclical events (dividends, earnings, major conferences).
- LLM inferencing
  
After gaining this experience, it should be more obvious what kind of software strategy to pursue. One thought is to use CUDA so that it can easily be substituted in for GPUs. I know Intel chose to develop their own OneAPI based on SyCL instead of using CUDA, though. I wonder if that was for legal reasons or NIH syndrome. Doing the very basic activities like those in the current code shows just how clunky both CUDA and SyCL are. After letting CoPilots develop this code in various Parallel processing models/languages, I am very interested in pursuing Julia. It was definitely the most intuitive CoPilot result.

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
