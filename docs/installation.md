
Download and Installation
===========

### Download and Install GUI

To download the Desktop/GUI version of HyPhy, follow instructions on this [download page](http://hyphy.org/w/index.php/Download). Note that the GUI is no longer maintained, and at this time we recommend using HyPhy either via [Datamonkey](http://datamonkey.org) or from the command line on your local computer/server. 

Alternatively, you may download an installer for an older release of HyPhy (version 2.2.4) for your specific operating system using the appropriate link:

* [Mac OSX](https://github.com/veg/hyphy/releases/download/2.2.4/hyphy.dmg)
* [Windows XP or later](https://github.com/veg/hyphy/releases/download/2.2.4/HyPhy2.2.4.exe)


### Download and Install from source

> HyPhy depends on [CMake >3.0](https://cmake.org/) for its build system. Before installing HyPhy, please make sure that an appropriate version of CMake has been installed. HyPhy additionally depends on other development libraries like
libcurl and libpthread. Libcurl requires development libraries such as crypto++ and openssl (or gnutls depending on your configuration). On Ubuntu these are libcurl-dev, libcrypto++-dev and libssl-dev.


**You can download HyPhy source in two ways:**

* Download a specific HyPhy release (we recommend the latest release) from [this github repository](https://github.com/veg/hyphy/releases).
* Download the master branch of HyPhy by cloning the repository by entering this command into a terminal session:

        git clone git@github.com:veg/hyphy.git

**Once downloaded, install HyPhy as follows:**

1. Navigate to the newly downloaded/cloned HyPhy directory
        
        cd hyphy

2. Configure HyPhy using CMake

        cmake .
    
    * By default, HyPhy will install into `/usr/local/`, but it can be installed on any location of your system by providing an installation prefix:

            cmake -DINSTALL_PREFIX=/location/of/choice .
    
    * If you prefer to use other build systems, such as XCode, configure HyPhy using the -G switch:
    
            cmake -G Xcode .

    * If would like to specify a particular compiler for your HyPhy build, use this command:

            cmake . -DCMAKE_CXX_COMPILER=/path/to/C++-compiler -DCMAKE_C_COMPILER=/path/to/C-compiler
 
    * If you are on an OS X platform, you can specify which OS X SDK to use, for example:
    
            cmake -DCMAKE_OSX_SYSROOT=/Developer/SDKs/MacOSX10.9.sdk/ .

3. Build HyPhy by running `make` with one of the following build targets given below. For example, to install the executable `HYPHYMP`, you would enter the following command:

        make MP2

    *  `MP2` - build a HyPhy executable (`HYPHYMP`) using pthreads to do multiprocessing. For optimal performance, `openMP` should be installed and available in your path. You can check if this is the case by examining the output from running `cmake`. If `openMP` is installed, you should see something similar to the following in the output:

            -- Performing Test OpenMP_FLAG_DETECTED
            -- Performing Test OpenMP_FLAG_DETECTED - Success
            -- Try OpenMP CXX flag = [-fopenmp]
            -- Performing Test OpenMP_FLAG_DETECTED
            -- Performing Test OpenMP_FLAG_DETECTED - Success
            -- Found OpenMP: -fopenmp  

    *  `MPI` - build a HyPhy executable (`HYPHYMPI`) using MPI to do multiprocessing
    *  `HYPHYMPI` - build a HyPhy executable (`HYPHYMPI`) using `openMPI`, which must be installed and available in your path. You can check if this is the case by examining the output from running `cmake`. If `openMPI` is installed, you should see something similar to the following in the output:

                -- Found MPI_C: /opt/scyld/openmpi/1.6.3/gnu/lib/libmpi.so;/usr/lib64/libibverbs.so;/usr/lib64/libdat.so;/usr/lib64/librt.so;/usr/lib64/libnsl.so;/usr/lib64/libutil.so;/usr/lib64/libm.so;/usr/lib64/libtorque.so;/usr/lib64/libm.so;/usr/lib64/libnuma.so;/usr/lib64/librt.so;/usr/lib64/libnsl.so;/usr/lib64/libutil.so;/usr/lib64/libm.so

                -- Found MPI_CXX: /opt/scyld/openmpi/1.6.3/gnu/lib/libmpi_cxx.so;/opt/scyld/openmpi/1.6.3/gnu/lib/libmpi.so;/usr/lib64/libibverbs.so;/usr/lib64/libdat.so;/usr/lib64/librt.so;/usr/lib64/libnsl.so;/usr/lib64/libutil.so;/usr/lib64/libm.so;/usr/lib64/libtorque.so;/usr/lib64/libm.so;/usr/lib64/libnuma.so;/usr/lib64/librt.so;/usr/lib64/libnsl.so;/usr/lib64/libutil.so;/usr/lib64/libm.so
    
    <!-- I know that SP is now deprecated. Are these still available? -->
    
    *  `GTEST` - build HyPhy's gtest testing executable (`HYPHYGTEST`)
    *  `MAC` - build a Mac Carbon application
    *  `HYPHYGTK` - HYPHY with GTK
    *  `LIB` - build a HyPhy library (libhyphy_mp) using pthreads to do multiprocessing

4. Finally, install HyPhy on your system with the command

        make install

    HyPhy will install either in its default location `/usr/local/`, or in any custom  `/location/of/choice/` provided when calling cmake.
    
      * `HYPHYMP(I)` will be installed at  `/location/of/choice/bin`
      * `libhyphy_mp.(so/dylib/dll)` will be installed at `/location/of/choice/lib`
      * HyPhy's standard library of batchfiles will go into `/location/of/choice/lib/hyphy`



<!--
HYPHYGTEST isn't installed normally,
because it serves no utility outside of testing.

To test HyPhy, build with the  GTEST target and run ./HYPHYGTEST from the source directory.
`make GTEST`
`./HYPHYGTEST`
-->