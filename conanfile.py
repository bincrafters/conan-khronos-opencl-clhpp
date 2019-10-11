from conans import ConanFile, CMake, tools
import os


class KhronosOpenCLCLHPPConan(ConanFile):
    name = "khronos-opencl-clhpp"
    version = "20190412"
    description = "OpenCL Host API C++ bindings"
    topics = ("conan", "opencl", "header-only", "opencl-headers", "clhpp", "khronos")
    url = "https://github.com/bincrafters/conan-khronos-opencl-clhpp"
    homepage = "https://github.com/KhronosGroup/OpenCL-CLHPP"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"
    no_copy_source = True
    _source_subfolder = "source_subfolder"
    requires = (
        "khronos-opencl-headers/20190412@bincrafters/stable",
        "khronos-opencl-icd-loader/20190412@bincrafters/stable"
    )

    def source(self):
        commit = "97a643f3bcb583fcbfb2a616d9b52790389514bc"
        sha256 = "46157b36bed68e661cc73d4794829b0a06005ca9dda512dc7e30a376bee33557"
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