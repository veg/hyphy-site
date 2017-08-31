### Download and Install GUI

To download the Desktop/GUI version of HyPhy, follow instructions on this [download page](http://hyphy.org/w/index.php/Download). 

> **NOTE**: The HyPhy GUI is no longer maintained and will be replaced in the near future with a JavaScript front-end. For those interested in a GUI experience, we recommend using HyPhy either via [Datamonkey](http://datamonkey.org) (for newer methods see [the development version of Datamonkey](http://test.datamonkey.org)) or from the command line on your local computer/server. 

Alternatively, you may download an installer for the final prebuilt release of HyPhy (version 2.2.4) for your specific operating system using the appropriate link:

* [Mac OSX](https://github.com/veg/hyphy/releases/download/2.2.4/hyphy.dmg)
* [Windows XP or later](https://github.com/veg/hyphy/releases/download/2.2.4/HyPhy2.2.4.exe)


### Download and Install from source

> HyPhy depends on [CMake version 3 or later](https://cmake.org/) for its build system. Before installing HyPhy, please make sure that an appropriate version of *CMake* has been installed. Some HyPhy configurations also depends on other development libraries like *libcurl* and  *libpthread*. *Libcurl* requires development libraries such as  *crypto++* and  *openssl* (or  *gnutls* depending on your configuration). On Ubuntu these are  *libcurl-dev*,  *libcrypto++-dev* and  *libssl-dev*.


**You can obtain HyPhy source in two ways:**

* Download a specific HyPhy release (we recommend the latest release) from [the HyPhy github repository](https://github.com/veg/hyphy/releases).
* Download the master branch of HyPhy by cloning the repository by entering this command into a terminal session:

```
git clone git@github.com:veg/hyphy.git
```

Once you have downloaded HyPhy, follow these [installation instructions](./installation.md).

### Developmental versions

> **Caution**: For advanced users only.

The most recent (not necessarily stable, but containing the latest features) versions of HyPhy can be obtained by checking out the current (working) development branch, by entering this command into a terminal session before proceeding with the install process

		git branch
		#select the branch that has the x.x.x-dev name 
		git checkout x.x.x-dev
        
    

