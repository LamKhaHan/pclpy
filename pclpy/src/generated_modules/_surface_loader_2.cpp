
#include <pybind11/pybind11.h>
#include <pybind11/eigen.h>
#include <pcl/point_types.h>

namespace py = pybind11;
using namespace pybind11::literals;

PYBIND11_DECLARE_HOLDER_TYPE(T, boost::shared_ptr<T>);
#include "../make_opaque_vectors.hpp"

#include "surface/poisson.hpp"
#include "surface/simplification_remove_unused_vertices.hpp"
#include "surface/surfel_smoothing.hpp"
#include "surface/texture_mapping.hpp"
#include "surface/vtk_mesh_quadric_decimation.hpp"
#include "surface/vtk_mesh_smoothing_laplacian.hpp"


void defineSurfaceClasses(py::module &m) {
    py::module m_surface = m.def_submodule("surface", "Submodule surface");
    defineSurfacePoissonClasses(m_surface);
    defineSurfaceSimplificationRemoveUnusedVerticesClasses(m_surface);
    defineSurfaceSurfelSmoothingClasses(m_surface);
    defineSurfaceTextureMappingClasses(m_surface);
    defineSurfaceVtkMeshQuadricDecimationClasses(m_surface);
    defineSurfaceVtkMeshSmoothingLaplacianClasses(m_surface);
}