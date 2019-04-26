#define CL_TARGET_OPENCL_VERSION 120
#define CL_HPP_MINIMUM_OPENCL_VERSION 120
#define CL_HPP_TARGET_OPENCL_VERSION 120
#include <CL/cl2.hpp>
#include <vector>

int main() {
    std::vector<cl::Platform> platforms;
	cl::Platform::get(&platforms);

	cl::Platform p;
	cl::Device d;
}
