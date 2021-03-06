/* Auto-generated by genmsg_cpp for file /home/mdesnoyer/src/reefbot/ros/objdetect_msgs/msg/DetectObjectGrid.msg */
#ifndef OBJDETECT_MSGS_MESSAGE_DETECTOBJECTGRID_H
#define OBJDETECT_MSGS_MESSAGE_DETECTOBJECTGRID_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "sensor_msgs/Image.h"
#include "objdetect_msgs/Grid.h"
#include "sensor_msgs/MatND.h"

namespace objdetect_msgs
{
template <class ContainerAllocator>
struct DetectObjectGrid_ {
  typedef DetectObjectGrid_<ContainerAllocator> Type;

  DetectObjectGrid_()
  : header()
  , image()
  , grid()
  , mask()
  {
  }

  DetectObjectGrid_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , image(_alloc)
  , grid(_alloc)
  , mask(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef  ::sensor_msgs::Image_<ContainerAllocator>  _image_type;
   ::sensor_msgs::Image_<ContainerAllocator>  image;

  typedef  ::objdetect_msgs::Grid_<ContainerAllocator>  _grid_type;
   ::objdetect_msgs::Grid_<ContainerAllocator>  grid;

  typedef  ::sensor_msgs::MatND_<ContainerAllocator>  _mask_type;
   ::sensor_msgs::MatND_<ContainerAllocator>  mask;


  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct DetectObjectGrid
typedef  ::objdetect_msgs::DetectObjectGrid_<std::allocator<void> > DetectObjectGrid;

typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGrid> DetectObjectGridPtr;
typedef boost::shared_ptr< ::objdetect_msgs::DetectObjectGrid const> DetectObjectGridConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace objdetect_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > {
  static const char* value() 
  {
    return "b797b0432e7c2ecd0ace33d4c690869f";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xb797b0432e7c2ecdULL;
  static const uint64_t static_value2 = 0x0ace33d4c690869fULL;
};

template<class ContainerAllocator>
struct DataType< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > {
  static const char* value() 
  {
    return "objdetect_msgs/DetectObjectGrid";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# To detect an object on a w,h,x,y grid. It is more compressed than listing all of the boxes we care about\n\
\n\
Header header\n\
\n\
# The image to find objects in\n\
sensor_msgs/Image image\n\
\n\
# The (w,h,x,y) grid to search on\n\
Grid grid\n\
\n\
# An optional binary mask that is 4 dimensional (w,h,x,y) and\n\
# specifies which entries we actually want to search in\n\
sensor_msgs/MatND mask\n\
\n\
\n\
\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: sensor_msgs/Image\n\
# This message contains an uncompressed image\n\
# (0, 0) is at top-left corner of image\n\
#\n\
\n\
Header header        # Header timestamp should be acquisition time of image\n\
                     # Header frame_id should be optical frame of camera\n\
                     # origin of frame should be optical center of cameara\n\
                     # +x should point to the right in the image\n\
                     # +y should point down in the image\n\
                     # +z should point into to plane of the image\n\
                     # If the frame_id here and the frame_id of the CameraInfo\n\
                     # message associated with the image conflict\n\
                     # the behavior is undefined\n\
\n\
uint32 height         # image height, that is, number of rows\n\
uint32 width          # image width, that is, number of columns\n\
\n\
# The legal values for encoding are in file src/image_encodings.cpp\n\
# If you want to standardize a new string format, join\n\
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.\n\
\n\
string encoding       # Encoding of pixels -- channel meaning, ordering, size\n\
                      # taken from the list of strings in src/image_encodings.cpp\n\
\n\
uint8 is_bigendian    # is this data bigendian?\n\
uint32 step           # Full row length in bytes\n\
uint8[] data          # actual matrix data, size is (step * rows)\n\
\n\
================================================================================\n\
MSG: objdetect_msgs/Grid\n\
# Specifies a  w,h,x,y dense grid\n\
# The starting points for the location search\n\
uint32 minX\n\
uint32 minY\n\
\n\
# The strides in the location space\n\
uint32 strideX\n\
uint32 strideY\n\
\n\
# The starting points for the scaling\n\
uint32 minW\n\
uint32 minH\n\
\n\
# The strides in the w, h space. In this case, we step by growing by a\n\
# fraction, so that width_i is round(minWidth*strideW^i)\n\
float64 strideW\n\
float64 strideH\n\
\n\
# True if the width and height should be a consistent aspect ratio that are \n\
# defined by minW and minH. This reduces the grid to (s,x,y)\n\
bool fixAspect\n\
================================================================================\n\
MSG: sensor_msgs/MatND\n\
# A message that contains an uncompressed n dimensional\n\
# matrix. Designed to be compatible with the opencv n-dimensional\n\
# matrix.\n\
Header header\n\
\n\
int32[] sizes # The size of each dimension in the matrix\n\
\n\
string encoding # The data type see src/image_encodings.cpp\n\
\n\
bool is_bigendian # Is the data bigendian?\n\
\n\
uint8[] data # The actual data\n\
\n\
";
  }

  static const char* value(const  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.image);
    stream.next(m.grid);
    stream.next(m.mask);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct DetectObjectGrid_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::objdetect_msgs::DetectObjectGrid_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "image: ";
s << std::endl;
    Printer< ::sensor_msgs::Image_<ContainerAllocator> >::stream(s, indent + "  ", v.image);
    s << indent << "grid: ";
s << std::endl;
    Printer< ::objdetect_msgs::Grid_<ContainerAllocator> >::stream(s, indent + "  ", v.grid);
    s << indent << "mask: ";
s << std::endl;
    Printer< ::sensor_msgs::MatND_<ContainerAllocator> >::stream(s, indent + "  ", v.mask);
  }
};


} // namespace message_operations
} // namespace ros

#endif // OBJDETECT_MSGS_MESSAGE_DETECTOBJECTGRID_H

