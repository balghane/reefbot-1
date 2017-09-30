/* Auto-generated by genmsg_cpp for file /home/mdesnoyer/src/reefbot/ros/reefbot_msgs/msg/CameraHealth.msg */
#ifndef REEFBOT_MSGS_MESSAGE_CAMERAHEALTH_H
#define REEFBOT_MSGS_MESSAGE_CAMERAHEALTH_H
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

namespace reefbot_msgs
{
template <class ContainerAllocator>
struct CameraHealth_ {
  typedef CameraHealth_<ContainerAllocator> Type;

  CameraHealth_()
  : header()
  , ping_ok(false)
  , http_ping_ok(false)
  , error_code(0)
  {
  }

  CameraHealth_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , ping_ok(false)
  , http_ping_ok(false)
  , error_code(0)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef uint8_t _ping_ok_type;
  uint8_t ping_ok;

  typedef uint8_t _http_ping_ok_type;
  uint8_t http_ping_ok;

  typedef int32_t _error_code_type;
  int32_t error_code;


  typedef boost::shared_ptr< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::reefbot_msgs::CameraHealth_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct CameraHealth
typedef  ::reefbot_msgs::CameraHealth_<std::allocator<void> > CameraHealth;

typedef boost::shared_ptr< ::reefbot_msgs::CameraHealth> CameraHealthPtr;
typedef boost::shared_ptr< ::reefbot_msgs::CameraHealth const> CameraHealthConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::reefbot_msgs::CameraHealth_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::reefbot_msgs::CameraHealth_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace reefbot_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::reefbot_msgs::CameraHealth_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > {
  static const char* value() 
  {
    return "45c3a1ccc9e7dc2f5a93095c761036c7";
  }

  static const char* value(const  ::reefbot_msgs::CameraHealth_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x45c3a1ccc9e7dc2fULL;
  static const uint64_t static_value2 = 0x5a93095c761036c7ULL;
};

template<class ContainerAllocator>
struct DataType< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > {
  static const char* value() 
  {
    return "reefbot_msgs/CameraHealth";
  }

  static const char* value(const  ::reefbot_msgs::CameraHealth_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > {
  static const char* value() 
  {
    return "# Message that specifies the camera's health\n\
#\n\
# Author: Mark Desnoyer\n\
# Date: July 2010\n\
\n\
Header header\n\
\n\
# Can we ping the camera?\n\
bool ping_ok\n\
\n\
# Can we connect to the http server on the camera\n\
bool http_ping_ok\n\
\n\
# Error code reported by the camera. 0 means that there is no\n\
# error. See CameraWatchdog.py for error codes.\n\
int32 error_code\n\
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
";
  }

  static const char* value(const  ::reefbot_msgs::CameraHealth_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::reefbot_msgs::CameraHealth_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::reefbot_msgs::CameraHealth_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::reefbot_msgs::CameraHealth_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.ping_ok);
    stream.next(m.http_ping_ok);
    stream.next(m.error_code);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct CameraHealth_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::reefbot_msgs::CameraHealth_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::reefbot_msgs::CameraHealth_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "ping_ok: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.ping_ok);
    s << indent << "http_ping_ok: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.http_ping_ok);
    s << indent << "error_code: ";
    Printer<int32_t>::stream(s, indent + "  ", v.error_code);
  }
};


} // namespace message_operations
} // namespace ros

#endif // REEFBOT_MSGS_MESSAGE_CAMERAHEALTH_H
