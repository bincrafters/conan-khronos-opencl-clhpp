from conans import ConanFile, CMake, tools
import os


class KhronosOpenCLCLHPPConan(ConanFile):
    name = "khronos-opencl-clhpp"
    version = "20191105"
    description = "OpenCL Host API C++ bindings"
    topics = ("conan", "opencl", "header-only", "opencl-headers", "clhpp", "khronos")
    url = "https://github.com/bincrafters/conan-khronos-opencl-clhpp"
    homepage = "https://github.com/KhronosGroup/OpenCL-CLHPP"
    license = "MIT"
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    requires = (
        "opencl-headers/2020.03.13",
        "opencl-icd-loader/2020.06.16"
    )

    def source(self):
        commit = "cf9fc1035e8298c7ce65ee33066a660fd9892ebb"
        sha256 = "6b61e3958ed0b3b6bd4a8085946baf35987ced817f0d1b7b36b449cc57c0071e"
        tools.get("{0}/archive/{1}.tar.gz".format(self.homepage, commit), sha256=sha256)
        extracted_dir = "OpenCL-CLHPP-" + commit
        os.rename(extracted_dir, self._source_subfolder)

    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_DOCS"] = False
        cmake.definitions["BUILD_EXAMPLES"] = False
        cmake.definitions["BUILD_TESTS"] = False
        cmake.configure()
        return cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_id(self):
        self.info.header_only()