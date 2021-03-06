"""autogenerated by genpy from objdetect_msgs/DetectObjectGridServiceRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import objdetect_msgs.msg
import std_msgs.msg

class DetectObjectGridServiceRequest(genpy.Message):
  _md5sum = "355207a78269e9b7a5e2cc2db0546ba5"
  _type = "objdetect_msgs/DetectObjectGridServiceRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """DetectObjectGrid request_msg

================================================================================
MSG: objdetect_msgs/DetectObjectGrid
# To detect an object on a w,h,x,y grid. It is more compressed than listing all of the boxes we care about

Header header

# The image to find objects in
sensor_msgs/Image image

# The (w,h,x,y) grid to search on
Grid grid

# An optional binary mask that is 4 dimensional (w,h,x,y) and
# specifies which entries we actually want to search in
sensor_msgs/MatND mask




================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of cameara
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in src/image_encodings.cpp

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

================================================================================
MSG: objdetect_msgs/Grid
# Specifies a  w,h,x,y dense grid
# The starting points for the location search
uint32 minX
uint32 minY

# The strides in the location space
uint32 strideX
uint32 strideY

# The starting points for the scaling
uint32 minW
uint32 minH

# The strides in the w, h space. In this case, we step by growing by a
# fraction, so that width_i is round(minWidth*strideW^i)
float64 strideW
float64 strideH

# True if the width and height should be a consistent aspect ratio that are 
# defined by minW and minH. This reduces the grid to (s,x,y)
bool fixAspect
================================================================================
MSG: sensor_msgs/MatND
# A message that contains an uncompressed n dimensional
# matrix. Designed to be compatible with the opencv n-dimensional
# matrix.
Header header

int32[] sizes # The size of each dimension in the matrix

string encoding # The data type see src/image_encodings.cpp

bool is_bigendian # Is the data bigendian?

uint8[] data # The actual data

"""
  __slots__ = ['request_msg']
  _slot_types = ['objdetect_msgs/DetectObjectGrid']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       request_msg

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DetectObjectGridServiceRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.request_msg is None:
        self.request_msg = objdetect_msgs.msg.DetectObjectGrid()
    else:
      self.request_msg = objdetect_msgs.msg.DetectObjectGrid()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.request_msg.header.seq, _x.request_msg.header.stamp.secs, _x.request_msg.header.stamp.nsecs))
      _x = self.request_msg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.request_msg.image.header.seq, _x.request_msg.image.header.stamp.secs, _x.request_msg.image.header.stamp.nsecs))
      _x = self.request_msg.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.request_msg.image.height, _x.request_msg.image.width))
      _x = self.request_msg.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BI.pack(_x.request_msg.image.is_bigendian, _x.request_msg.image.step))
      _x = self.request_msg.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.request_msg.grid.minX, _x.request_msg.grid.minY, _x.request_msg.grid.strideX, _x.request_msg.grid.strideY, _x.request_msg.grid.minW, _x.request_msg.grid.minH, _x.request_msg.grid.strideW, _x.request_msg.grid.strideH, _x.request_msg.grid.fixAspect, _x.request_msg.mask.header.seq, _x.request_msg.mask.header.stamp.secs, _x.request_msg.mask.header.stamp.nsecs))
      _x = self.request_msg.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.request_msg.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.request_msg.mask.sizes))
      _x = self.request_msg.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.request_msg.mask.is_bigendian))
      _x = self.request_msg.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.request_msg is None:
        self.request_msg = objdetect_msgs.msg.DetectObjectGrid()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.request_msg.header.seq, _x.request_msg.header.stamp.secs, _x.request_msg.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.request_msg.image.header.seq, _x.request_msg.image.header.stamp.secs, _x.request_msg.image.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.request_msg.image.height, _x.request_msg.image.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.encoding = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.request_msg.image.is_bigendian, _x.request_msg.image.step,) = _struct_BI.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.data = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.data = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.request_msg.grid.minX, _x.request_msg.grid.minY, _x.request_msg.grid.strideX, _x.request_msg.grid.strideY, _x.request_msg.grid.minW, _x.request_msg.grid.minH, _x.request_msg.grid.strideW, _x.request_msg.grid.strideH, _x.request_msg.grid.fixAspect, _x.request_msg.mask.header.seq, _x.request_msg.mask.header.stamp.secs, _x.request_msg.mask.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.request_msg.grid.fixAspect = bool(self.request_msg.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.request_msg.mask.sizes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.request_msg.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.request_msg.mask.is_bigendian = bool(self.request_msg.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.data = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.request_msg.header.seq, _x.request_msg.header.stamp.secs, _x.request_msg.header.stamp.nsecs))
      _x = self.request_msg.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.request_msg.image.header.seq, _x.request_msg.image.header.stamp.secs, _x.request_msg.image.header.stamp.nsecs))
      _x = self.request_msg.image.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2I.pack(_x.request_msg.image.height, _x.request_msg.image.width))
      _x = self.request_msg.image.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_BI.pack(_x.request_msg.image.is_bigendian, _x.request_msg.image.step))
      _x = self.request_msg.image.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.request_msg.grid.minX, _x.request_msg.grid.minY, _x.request_msg.grid.strideX, _x.request_msg.grid.strideY, _x.request_msg.grid.minW, _x.request_msg.grid.minH, _x.request_msg.grid.strideW, _x.request_msg.grid.strideH, _x.request_msg.grid.fixAspect, _x.request_msg.mask.header.seq, _x.request_msg.mask.header.stamp.secs, _x.request_msg.mask.header.stamp.nsecs))
      _x = self.request_msg.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.request_msg.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.request_msg.mask.sizes.tostring())
      _x = self.request_msg.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.request_msg.mask.is_bigendian))
      _x = self.request_msg.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.request_msg is None:
        self.request_msg = objdetect_msgs.msg.DetectObjectGrid()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.request_msg.header.seq, _x.request_msg.header.stamp.secs, _x.request_msg.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.request_msg.image.header.seq, _x.request_msg.image.header.stamp.secs, _x.request_msg.image.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.request_msg.image.height, _x.request_msg.image.width,) = _struct_2I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.encoding = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.encoding = str[start:end]
      _x = self
      start = end
      end += 5
      (_x.request_msg.image.is_bigendian, _x.request_msg.image.step,) = _struct_BI.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.image.data = str[start:end].decode('utf-8')
      else:
        self.request_msg.image.data = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.request_msg.grid.minX, _x.request_msg.grid.minY, _x.request_msg.grid.strideX, _x.request_msg.grid.strideY, _x.request_msg.grid.minW, _x.request_msg.grid.minH, _x.request_msg.grid.strideW, _x.request_msg.grid.strideH, _x.request_msg.grid.fixAspect, _x.request_msg.mask.header.seq, _x.request_msg.mask.header.stamp.secs, _x.request_msg.mask.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.request_msg.grid.fixAspect = bool(self.request_msg.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.request_msg.mask.sizes = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.request_msg.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.request_msg.mask.is_bigendian = bool(self.request_msg.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.request_msg.mask.data = str[start:end].decode('utf-8')
      else:
        self.request_msg.mask.data = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_6I2dB3I = struct.Struct("<6I2dB3I")
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_2I = struct.Struct("<2I")
_struct_BI = struct.Struct("<BI")
"""autogenerated by genpy from objdetect_msgs/DetectObjectGridServiceResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import sensor_msgs.msg
import genpy
import objdetect_msgs.msg
import std_msgs.msg

class DetectObjectGridServiceResponse(genpy.Message):
  _md5sum = "10d41d63f25679f70d16a37d38a4ce09"
  _type = "objdetect_msgs/DetectObjectGridServiceResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """DetectGridScores scores

================================================================================
MSG: objdetect_msgs/DetectGridScores
# Specifies socres on a detection grid that runs (x,y,w,h). If the aspect ratio is fixed, this will change to (x,y,s)

Header header

# The (w,h,x,y) grid that has a response
Grid grid

# A grid of scores across the space that are based on an evaluation
# for each box.
sensor_msgs/MatND scores

# An optional binary mask that is 4 dimensional (w,h,x,y) and
# specifies which entries have valid values
sensor_msgs/MatND mask

# The processing time to calculate the detection
std_msgs/Duration processing_time
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: objdetect_msgs/Grid
# Specifies a  w,h,x,y dense grid
# The starting points for the location search
uint32 minX
uint32 minY

# The strides in the location space
uint32 strideX
uint32 strideY

# The starting points for the scaling
uint32 minW
uint32 minH

# The strides in the w, h space. In this case, we step by growing by a
# fraction, so that width_i is round(minWidth*strideW^i)
float64 strideW
float64 strideH

# True if the width and height should be a consistent aspect ratio that are 
# defined by minW and minH. This reduces the grid to (s,x,y)
bool fixAspect
================================================================================
MSG: sensor_msgs/MatND
# A message that contains an uncompressed n dimensional
# matrix. Designed to be compatible with the opencv n-dimensional
# matrix.
Header header

int32[] sizes # The size of each dimension in the matrix

string encoding # The data type see src/image_encodings.cpp

bool is_bigendian # Is the data bigendian?

uint8[] data # The actual data

================================================================================
MSG: std_msgs/Duration
duration data

"""
  __slots__ = ['scores']
  _slot_types = ['objdetect_msgs/DetectGridScores']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       scores

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DetectObjectGridServiceResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.scores is None:
        self.scores = objdetect_msgs.msg.DetectGridScores()
    else:
      self.scores = objdetect_msgs.msg.DetectGridScores()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs))
      _x = self.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.scores.grid.minX, _x.scores.grid.minY, _x.scores.grid.strideX, _x.scores.grid.strideY, _x.scores.grid.minW, _x.scores.grid.minH, _x.scores.grid.strideW, _x.scores.grid.strideH, _x.scores.grid.fixAspect, _x.scores.scores.header.seq, _x.scores.scores.header.stamp.secs, _x.scores.scores.header.stamp.nsecs))
      _x = self.scores.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.scores.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.scores.scores.sizes))
      _x = self.scores.scores.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.scores.is_bigendian))
      _x = self.scores.scores.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.scores.mask.header.seq, _x.scores.mask.header.stamp.secs, _x.scores.mask.header.stamp.nsecs))
      _x = self.scores.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.scores.mask.sizes))
      _x = self.scores.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.mask.is_bigendian))
      _x = self.scores.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.scores.processing_time.data.secs, _x.scores.processing_time.data.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.scores is None:
        self.scores = objdetect_msgs.msg.DetectGridScores()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.scores.grid.minX, _x.scores.grid.minY, _x.scores.grid.strideX, _x.scores.grid.strideY, _x.scores.grid.minW, _x.scores.grid.minH, _x.scores.grid.strideW, _x.scores.grid.strideH, _x.scores.grid.fixAspect, _x.scores.scores.header.seq, _x.scores.scores.header.stamp.secs, _x.scores.scores.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.scores.grid.fixAspect = bool(self.scores.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.scores.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.scores.sizes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.scores.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.scores.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.scores.is_bigendian = bool(self.scores.scores.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.data = str[start:end].decode('utf-8')
      else:
        self.scores.scores.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.scores.mask.header.seq, _x.scores.mask.header.stamp.secs, _x.scores.mask.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.mask.sizes = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.mask.is_bigendian = bool(self.scores.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.data = str[start:end].decode('utf-8')
      else:
        self.scores.mask.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.scores.processing_time.data.secs, _x.scores.processing_time.data.nsecs,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_3I.pack(_x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs))
      _x = self.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_6I2dB3I.pack(_x.scores.grid.minX, _x.scores.grid.minY, _x.scores.grid.strideX, _x.scores.grid.strideY, _x.scores.grid.minW, _x.scores.grid.minH, _x.scores.grid.strideW, _x.scores.grid.strideH, _x.scores.grid.fixAspect, _x.scores.scores.header.seq, _x.scores.scores.header.stamp.secs, _x.scores.scores.header.stamp.nsecs))
      _x = self.scores.scores.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.scores.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.scores.scores.sizes.tostring())
      _x = self.scores.scores.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.scores.is_bigendian))
      _x = self.scores.scores.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_3I.pack(_x.scores.mask.header.seq, _x.scores.mask.header.stamp.secs, _x.scores.mask.header.stamp.nsecs))
      _x = self.scores.mask.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.scores.mask.sizes)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.scores.mask.sizes.tostring())
      _x = self.scores.mask.encoding
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_B.pack(self.scores.mask.is_bigendian))
      _x = self.scores.mask.data
      length = len(_x)
      # - if encoded as a list instead, serialize as bytes instead of string
      if type(_x) in [list, tuple]:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_struct_2i.pack(_x.scores.processing_time.data.secs, _x.scores.processing_time.data.nsecs))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.scores is None:
        self.scores = objdetect_msgs.msg.DetectGridScores()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.scores.header.seq, _x.scores.header.stamp.secs, _x.scores.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 53
      (_x.scores.grid.minX, _x.scores.grid.minY, _x.scores.grid.strideX, _x.scores.grid.strideY, _x.scores.grid.minW, _x.scores.grid.minH, _x.scores.grid.strideW, _x.scores.grid.strideH, _x.scores.grid.fixAspect, _x.scores.scores.header.seq, _x.scores.scores.header.stamp.secs, _x.scores.scores.header.stamp.nsecs,) = _struct_6I2dB3I.unpack(str[start:end])
      self.scores.grid.fixAspect = bool(self.scores.grid.fixAspect)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.scores.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.scores.sizes = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.scores.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.scores.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.scores.is_bigendian = bool(self.scores.scores.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.scores.data = str[start:end].decode('utf-8')
      else:
        self.scores.scores.data = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.scores.mask.header.seq, _x.scores.mask.header.stamp.secs, _x.scores.mask.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.scores.mask.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.scores.mask.sizes = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.encoding = str[start:end].decode('utf-8')
      else:
        self.scores.mask.encoding = str[start:end]
      start = end
      end += 1
      (self.scores.mask.is_bigendian,) = _struct_B.unpack(str[start:end])
      self.scores.mask.is_bigendian = bool(self.scores.mask.is_bigendian)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.scores.mask.data = str[start:end].decode('utf-8')
      else:
        self.scores.mask.data = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.scores.processing_time.data.secs, _x.scores.processing_time.data.nsecs,) = _struct_2i.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3I = struct.Struct("<3I")
_struct_B = struct.Struct("<B")
_struct_6I2dB3I = struct.Struct("<6I2dB3I")
_struct_2i = struct.Struct("<2i")
class DetectObjectGridService(object):
  _type          = 'objdetect_msgs/DetectObjectGridService'
  _md5sum = 'e387077e439fcb0349b2190bd0852bae'
  _request_class  = DetectObjectGridServiceRequest
  _response_class = DetectObjectGridServiceResponse
