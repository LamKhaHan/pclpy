#include <pcl/geometry/polygon_mesh.h>
#include <pcl/geometry/triangle_mesh.h>
#include <pcl/geometry/mesh_io.h>

using namespace pcl::geometry;


template <class MeshT>
void defineGeometryMeshIO(py::module &m, std::string const & suffix) {
    using Class = pcl::geometry::MeshIO<MeshT>;
    using Mesh = Class::Mesh;
    using Vertex = Class::Vertex;
    using HalfEdge = Class::HalfEdge;
    using Face = Class::Face;
    using Vertices = Class::Vertices;
    using HalfEdges = Class::HalfEdges;
    using Faces = Class::Faces;
    using VertexIndex = Class::VertexIndex;
    using HalfEdgeIndex = Class::HalfEdgeIndex;
    using FaceIndex = Class::FaceIndex;
    py::class_<Class, boost::shared_ptr<Class>> cls(m, suffix.c_str());
    cls.def(py::init<>());
    cls.def("read", &Class::read, "filename"_a, "mesh"_a);
    cls.def("write", &Class::write, "filename"_a, "mesh"_a);
        
}

void defineGeometryMeshIoFunctions(py::module &m) {
}

void defineGeometryMeshIoClasses(py::module &sub_module) {
    py::module sub_module_MeshIO = sub_module.def_submodule("MeshIO", "Submodule MeshIO");
    defineGeometryMeshIO<pcl::geometry::PolygonMesh<DefaultMeshTraits<>>>(sub_module_MeshIO, "geometry::PolygonMesh<DefaultMeshTraits<>>");
    defineGeometryMeshIO<pcl::geometry::TriangleMesh<DefaultMeshTraits<>>>(sub_module_MeshIO, "geometry::TriangleMesh<DefaultMeshTraits<>>");
}