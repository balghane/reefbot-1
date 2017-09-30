/* Auto-generated by genmsg_cpp for file /home/mdesnoyer/src/reefbot/ros/sensor_msgs/msg/PointField.msg */
#ifndef SENSOR_MSGS_MESSAGE_POINTFIELD_H
#define SENSOR_MSGS_MESSAGE_POINTFIELD_H
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


namespace sensor_msgs
{
template <class ContainerAllocator>
struct PointField_ {
  typedef PointField_<ContainerAllocator> Type;

  PointField_()
  : name()
  , offset(0)
  , datatype(0)
  , count(0)
  {
  }

  PointField_(const ContainerAllocator& _alloc)
  : name(_alloc)
  , offset(0)
  , datatype(0)
  , count(0)
  {
  }

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _name_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  name;

  typedef uint32_t _offset_type;
  uint32_t offset;

  typedef uint8_t _datatype_type;
  uint8_t datatype;

  typedef uint32_t _count_type;
  uint32_t count;

  enum { INT8 = 1 };
  enum { UINT8 = 2 };
  enum { INT16 = 3 };
  enum { UINT16 = 4 };
  enum { INT32 = 5 };
  enum { UINT32 = 6 };
  enum { FLOAT32 = 7 };
  enum { FLOAT64 = 8 };

  typedef boost::shared_ptr< ::sensor_msgs::PointField_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::sensor_msgs::PointField_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct PointField
typedef  ::sensor_msgs::PointField_<std::allocator<void> > PointField;

typedef boost::shared_ptr< ::sensor_msgs::PointField> PointFieldPtr;
typedef boost::shared_ptr< ::sensor_msgs::PointField const> PointFieldConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::sensor_msgs::PointField_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::sensor_msgs::PointField_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace sensor_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::sensor_msgs::PointField_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::sensor_msgs::PointField_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::sensor_msgs::PointField_<ContainerAllocator> > {
  static const char* value() 
  {
    return "268eacb2962780ceac86cbd17e328150";
  }

  static const char* value(const  ::sensor_msgs::PointField_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x268eacb2962780ceULL;
  static const uint64_t static_value2 = 0xac86cbd17e328150ULL;
};

template<class ContainerAllocator>
struct DataType< ::sensor_msgs::PointField_<ContainerAllocator> > {
  static const char* value() 
  {
    return "sensor_msgs/PointField";
  }

  static const char* value(const  ::sensor_msgs::PointField_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::sensor_msgs::PointField_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# This message holds the description of one point entry in the\n\
# PointCloud2 message format.\n\
uint8 INT8    = 1\n\
uint8 UINT8   = 2\n\
uint8 INT16   = 3\n\
uint8 UINT16  = 4\n\
uint8 INT32   = 5\n\
uint8 UINT32  = 6\n\
uint8 FLOAT32 = 7\n\
uint8 FLOAT64 = 8\n\
\n\
string name      # Name of field\n\
uint32 offset    # Offset from start of point struct\n\
uint8  datatype  # Datatype enumeration, see above\n\
uint32 count     # How many elements in the field\n\
\n\
";
  }

  static const char* value(const  ::sensor_msgs::PointField_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::sensor_msgs::PointField_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.name);
    stream.next(m.offset);
    stream.next(m.datatype);
    stream.next(m.count);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct PointField_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::sensor_msgs::PointField_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::sensor_msgs::PointField_<ContainerAllocator> & v) 
  {
    s << indent << "name: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.name);
    s << indent << "offset: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.offset);
    s << indent << "datatype: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.datatype);
    s << indent << "count: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.count);
  }
};


} // namespace message_operations
} // namespace ros

#endif // SENSOR_MSGS_MESSAGE_POINTFIELD_H
