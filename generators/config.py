from os.path import join
import os

INDENT = " " * 4

PCL_BASE = join(os.environ["PCL_ROOT"], "include\pcl-1.8\pcl")
PATH_MAIN_CPP = join("..", "pclpy", "src", "pclpy.cpp")
PATH_MODULES = join("..", "pclpy", "src", "generated_modules")
PATH_LOADER = join(PATH_MODULES, "__main_loader.hpp")

common_includes = """
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/eigen.h>
#include <pybind11/stl.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>

namespace py = pybind11;
using namespace pybind11::literals;
"""

# ----------------------
# which modules to build
# ----------------------

MODULES_TO_BUILD = ['2d', 'common', 'geometry', 'features', 'filters', 'io', 'kdtree', 'keypoints', 'octree',
                    'recognition', 'sample_consensus', 'search', 'segmentation', 'stereo', 'surface',
                    'tracking', 'visualization']
# skipped for now:
# , 'ml', 'people', 'outofcore' 'registration']

# -----------------------------
# specific generator parameters
# -----------------------------

IGNORE_INHERITED_INSTANTIATIONS = [
    # "class"
    "OrganizedEdgeBase",
    "OrganizedEdgeFromRGB",
]

INHERITED_ENUMS = [
    # ("class", "type")
    ("ImageRGB24", "Timestamp"),
    ("ImageYUV422", "Timestamp"),
]

# ---
# When a base class contains only some types of the child class, and they are unordered.
# This happens but is sort of rare in PCL.

INHERITED_TEMPLATED_TYPES_FILTER = {
    # ("base_class", "child_class"): [0, 3, 5]

    "Feature": [0, 2],  # this is not a mistake, but it should be fixed. Feature is inherited from a lot.
    # I think narf or narf_descriptor could be an exception

    ("UniqueShapeContext", "FeatureWithLocalReferenceFrames"): [0, 2],
    ("SHOTEstimationBase", "FeatureWithLocalReferenceFrames"): [0, 3],
    ("SHOTEstimation", "FeatureWithLocalReferenceFrames"): [0, 3],
    ("SHOTEstimationOMP", "FeatureWithLocalReferenceFrames"): [0, 3],
    ("SHOTColorEstimation", "FeatureWithLocalReferenceFrames"): [0, 3],
    ("SHOTColorEstimationOMP", "FeatureWithLocalReferenceFrames"): [0, 3],
}

KEEP_ASIS_TYPES_STARTSWITH = [
    "Eigen::",
    "pcl::",
    "std::",
    "boost::shared_ptr",
    "boost::filesystem",
    "boost::uint64_t",
    "uint8_t",
    "unsigned",
    "uint16_t",
    "uint32_t",
    "uint64_t",
    "int",
    "int8_t",
    "int16_t",
    "int32_t",
    "int64_t",
    "bool",
    "char",
    "float",
    "double",
    "size_t",
]

# explicitely excluded classes
CLASSES_TO_IGNORE = [
    # ("module", "header", "class")

    # (not implemented in pcl source code)
    ("outofcore", "outofcore_iterator_base.h", "OutofcoreBreadthFirstIterator"),
    ("outofcore", "outofcore_iterator_base.h", "OutofcoreLeafIterator"),
    # constructor seems to access private member...
    ("io", "obj_io.h", "MTLReader"),
    ("io", "io_exception.h", "IOException"),  # linking error
]

CUSTOM_OVERLOAD_TYPES = {
    # ("class", "type"): "type_replacement"
    ("FastBilateralFilter", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("MedianFilter", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("FrustrumCulling", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("VoxelGridOcclusionEstimation", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("ConditionalRemoval", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("FastBilateralFilterOMP", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("CropBox", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("VoxelGridCovariance", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("ApproximateVoxelGrid", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("ProjectInliers", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("CropHull", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("BilateralFilter", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("UniformSampling", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("VoxelGrid", "PointCloud"): "pcl::Filter<PointT>::PointCloud",
    ("SamplingSurfaceNormal", "PointCloud"): "pcl::Filter<PointT>::PointCloud",

    ("DepthImage", "FrameWrapper::Ptr"): "FrameWrapper::Ptr",
    ("IRImage", "FrameWrapper::Ptr"): "FrameWrapper::Ptr",

    ("PointCloudColorHandlerCustom",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerGenericField",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerHSVField",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerLabelField",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerRGBAField",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerRGBField",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",
    ("PointCloudColorHandlerRandom",
     "PointCloudConstPtr"): "PointCloudColorHandler<PointT>::PointCloud::ConstPtr",

    ("LeastMedianSquares", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("MaximumLikelihoodSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("MEstimatorSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("ProgressiveSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("RandomSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("RandomizedMEstimatorSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",
    ("RandomizedRandomSampleConsensus", "SampleConsensusModelPtr"): "pcl::SampleConsensusModel<PointT>::Ptr",

    ("DisparityMapConverter", "PointCloud"): "pcl::PointCloud<PointT>",
}

# types that are explicitely considered as part of the "pcl" namespace
GLOBAL_PCL_IMPORTS = [
    "IndicesPtr",
    "IndicesConstPtr",
    "PointIndices",
    "ModelCoefficients",
    "PointWithRange",
    "PCLBase",
    "PlanarRegion",
    "PointXYZ",
    "SVMData",
]

EXPLICIT_IMPORTED_TYPES = [
    "Camera",
    "PointCloudGeometryHandler",
    "PointCloudColorHandler",
]

EXTERNAL_INHERITANCE = [
    "svm_parameter",
    "svm_model",
    "std",
    "boost",
    "vtk",
]

SKIPPED_INHERITANCE = [
    "boost::",
    "vtk",
]

TEMPLATED_METHOD_TYPES = {
    "PointT": "PCL_POINT_TYPES",
    "PointInT": "PCL_POINT_TYPES",
    "PointLT": ["pcl::Label"],
    "PointOutT": "PCL_POINT_TYPES",
    "PointTDiff": "PCL_XYZ_POINT_TYPES",
    "PointRFT": ["pcl::ReferenceFrame"],
    "StateT": "PCL_STATE_POINT_TYPES",
    "OutputType": "PCL_POINT_TYPES",
    "PointSource": "PCL_XYZ_POINT_TYPES",
    "PointFeature": "PCL_FEATURE_POINT_TYPES",
    "T": "PCL_POINT_TYPES",
    "PointNT": "PCL_NORMAL_POINT_TYPES",
    "NormalT": "PCL_NORMAL_POINT_TYPES",
    "GradientT": ["pcl::IntensityGradient"],
    "P1": "PCL_XYZ_POINT_TYPES",
    "P2": "PCL_XYZ_POINT_TYPES",
    "FeatureT": "PCL_FEATURE_POINT_TYPES",
}

pcl_visualizer_xyz = ["pcl::PointSurfel", "pcl::PointXYZ", "pcl::PointXYZL", "pcl::PointXYZI", "pcl::PointXYZRGB",
                      "pcl::PointXYZRGBA", "pcl::PointNormal", "pcl::PointXYZRGBNormal", "pcl::PointXYZRGBL",
                      "pcl::PointWithRange"]

SPECIFIC_TEMPLATED_METHOD_TYPES = {
    # ("class_name", "method_name", ("templated_parameter_names", ))
    # if method_name is empty, it's considered as the default template type for this class
    ("ImageViewer", "", ("T",)): ("PCL_RGB_POINT_TYPES",),
    ("ImageViewer", "", ("PointT",)): ("PCL_RGB_POINT_TYPES",),
    ("ImageViewer", "addRectangle", ("T",)): ("PCL_XYZ_POINT_TYPES",),

    ("LZFBayer8ImageReader", "", ("PointT",)): ("PCL_RGB_POINT_TYPES",),
    ("LZFDepth16ImageReader", "", ("PointT",)): ("PCL_XYZ_POINT_TYPES",),
    ("LZFRGB24ImageReader", "", ("PointT",)): ("PCL_RGB_POINT_TYPES",),
    ("LZFYUV422ImageReader", "", ("PointT",)): ("PCL_RGB_POINT_TYPES",),

    ("Camera", "", ("PointT",)): (pcl_visualizer_xyz,),
    ("PCLVisualizer", "", ("PointT",)): (pcl_visualizer_xyz,),
    ("PCLVisualizer", "", ("PointT", "GradientT")): (pcl_visualizer_xyz, ["pcl::IntensityGradient"]),
    ("PCLVisualizer", "", ("PointNT",)): (["pcl::PointNormal", "pcl::PointXYZRGBNormal", "pcl::PointXYZINormal",
                                           "pcl::PointXYZLNormal", "pcl::PointSurfel"],),
    ("PCLVisualizer", "", ("PointT", "PointNT")): (pcl_visualizer_xyz, "PCL_NORMAL_POINT_TYPES"),
}

EXPLICIT_INCLUDES = {
    # (module, header_name): "#include...",
    ("geometry", "mesh_io.h"): ("#include <pcl/geometry/polygon_mesh.h>\n"
                                "#include <pcl/geometry/triangle_mesh.h>"),
    ("segmentation", "plane_refinement_comparator.h"): "#include <pcl/ModelCoefficients.h>",
    ("features", "narf_descriptor.h"): "#include <pcl/range_image/range_image.h>",
    ("features", "from_meshes.h"): "#include <pcl/Vertices.h>",
    ("common", "synchronizer.h"): '#include <boost/thread/mutex.hpp>',
    ("visualization", "pcl_visualizer.h"): "#pragma warning(disable : 4996)",
    ("recognition", "orr_octree.h"): "#pragma warning(disable : 4800)",
    ("recognition", "obj_rec_ransac.h"): "#pragma warning(disable : 4267)",
    ("recognition", "model_library.h"): "#pragma warning(disable : 4267)",
    ("surface", "concave_hull.h"): "#pragma warning(disable : 4996)",
    ("features", "grsd.h"): "#pragma warning(disable : 4506)",
    ("outofcore", "axes.h"): "#include <vtkPointData.h>",
}

# ------------
# what to skip
# ------------

HEADERS_TO_SKIP = [
    # ("module", "header")
    ("io", "pxc_grabber.h"),  # deprecated
    ("ml", "multi_channel_2d_comparison_feature_handler.h"),  # can't find class FeatureHandlerCodeGenerator ??
    ("", "pcl_tests.h"),
    ("", "for_each_type.h"),

    # todo: everything in pcl/ml/dt/ is actually at pcl/ml/
    ("ml", "decision_tree_evaluator.h"),
    ("ml", "decision_forest.h"),
    ("ml", "decision_forest_evaluator.h"),
    ("ml", "decision_forest_trainer.h"),
    ("ml", "decision_tree.h"),
    ("ml", "decision_tree_data_provider.h"),
    ("ml", "decision_tree_evaluator.h"),
    ("ml", "decision_tree_trainer.h"),
    ("ml", "fern.h"),
    ("ml", "fern_evaluator.h"),
    ("ml", "fern_trainer.h"),

    ("io", "openni.h"),
    ("io", "openni2_grabber.h"),
    ("io", "openni2_convert.h"),
    ("io", "openni2_device.h"),
    ("io", "openni2_device_info.h"),
    ("io", "openni2_device_manager.h"),
    ("io", "openni2_frame_listener.h"),
    ("io", "openni2_metadata_wrapper.h"),
    ("io", "openni2_timer_filter.h"),
    ("io", "openni2_video_mode.h"),

    ("surface", "multi_grid_octree_data.h"),  # compile error in PCL "OctNode is not a member of pcl::poisson"

    ("recognition", "hv_go.h"),  # depends on metslib

    ("", "exceptions.h"),  # todo: implement exceptions
    ("registration", "exceptions.h"),  # todo: implement exceptions
    ("segmentation", "conditional_euclidean_clustering.h"),  # setConditionFunction hard to implement...
    ("segmentation", "seeded_hue_segmentation.h"),  # not exported in dll for some reason. Linking error.
    ("common", "time_trigger.h"),  # init containing boost::function
    ("common", "synchronizer.h"),

    ("visualization", "pcl_painter2D.h"),  # tricky protected vtkContextItem destructor
    ("visualization", "pcl_context_item.h"),  # tricky protected vtkContextItem destructor
    ("visualization", "interactor_style.h"),  # tricky protected vtkContextItem destructor
    ("visualization", "histogram_visualizer.h"),  # link error (visualization::RenWinInteract::RenWinInteract(void))
    ("visualization", "simple_buffer_visualizer.h"),  # link error (visualization::RenWinInteract::RenWinInteract(void))
    ("visualization", "ren_win_interact_map.h"),  # link error (visualization::RenWinInteract::RenWinInteract(void))

    ("common", "gaussian.h"),  # templated method?

    ("recognition", "trimmed_icp.h"),  # depends on registration
    ("recognition", "obj_rec_ransac.h"),  # depends on trimmed_icp, which depends on registration

    ("keypoints", "smoothed_surfaces_keypoint.h"),
    # Inherits from Keypoint <PointT, PointT> (which seems weird to me...)

    ("features", "range_image_border_extractor.h"),  # depends on range_image
    # ImportError: generic_type: type "NarfDescriptor" referenced unknown
    # base type "pcl::Feature<pcl::PointWithRange,pcl::Narf36>"
    ("features", "narf_descriptor.h"),  # depends on range_image
    ("features", "narf.h"),  # depends on range_image
    ("keypoints", "narf_keypoint.h"),  # depends on range_image and range_image_border_extractor

    ("filters", "conditional_removal.h"),
    # todo: parser error for ConditionalRemoval (int extract_removed_indices = false) :
    ("filters", "model_outlier_removal.h"),  # todo: boost::function as parameter
]

SUBMODULES_TO_SKIP = [
    "opennurbs",
    "face_detection",  # depends on ml/decision_tree_data_provider
    "metslib",  # lots of warnings, skip for now...
]

ATTRIBUTES_TO_SKIP = {
    # ("module", "header", "class"): ["attr1", "attr2"]
    ("features", "shot.h", "SHOTColorEstimation"): ["sRGB_LUT", "sXYZ_LUT"],  # todo: linking error
    ("features", "narf.h", "Narf"): ["max_no_of_threads"],  # todo: linking error
    ("recognition", "orr_octree.h", "ORROctree"): ["createLeaf"],  # todo: linking error
}

METHODS_TO_SKIP = [
    # ("class", "method")

    ("PointCloud", "insert"),  # templated InputIterator

    ("PCLVisualizer", "getCameraParameters"),  # fix char ** variable type

    ("ASCIIReader", "setInputFields"),
    ("PCLPlotter", "addPlotData"),
    ("PCLPlotter", "addFeatureHistogram"),
    ("PCLHistogramVisualizer", "spinOnce"),
    ("PCLHistogramVisualizer", "addFeatureHistogram"),
    ("PCLHistogramVisualizer", "updateFeatureHistogram"),
    ("ORROctree", "createLeaf"),  # linking error

    ("PCLVisualizer", "setupInteractor"),
    # an undefined class is not allowed as an argument to compiler intrinsic type trait '__is_base_of'
    ("PCLVisualizer", "addOrientationMarkerWidgetAxes"),
    # an undefined class is not allowed as an argument to compiler intrinsic type trait '__is_base_of'

    ("PCLHistogramVisualizer", "wasStopped"),  # only in vtk 5
    ("PCLHistogramVisualizer", "resetStoppedFlag"),  # only in vtk 5
]