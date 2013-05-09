/*
 * xds_coordinate_system.cc
 *
 *  Copyright (C) 2013 Diamond Light Source
 *
 *  Author: James Parkhurst
 *
 *  This code is distributed under the BSD license, a copy of which is
 *  included in the root directory of this package.
 */
#include <boost/python.hpp>
#include <boost/python/def.hpp>
#include <dials/algorithms/integration/xds_coordinate_system.h>

using namespace boost::python;

namespace dials { namespace algorithms { namespace boost_python {

  void export_xds_coordinate_system()
  {
    def("zeta_factor", &zeta_factor, (arg("s0"), arg("s1"), arg("m2")));
  
    class_ <XdsCoordinateSystem> ("XdsCoordinateSystem", no_init)
      .def(init <vec3 <double>,
                 vec3 <double>,
                 vec3 <double>,
                 double > ((
          arg("s0"), 
          arg("s1"), 
          arg("m2"),
          arg("phi"))))
      .add_property("e1_axis", &XdsCoordinateSystem::get_e1_axis)
      .add_property("e2_axis", &XdsCoordinateSystem::get_e2_axis)
      .add_property("e3_axis", &XdsCoordinateSystem::get_e3_axis)
      .add_property("zeta",    &XdsCoordinateSystem::get_zeta);
  }

}}} // namespace = dials::algorithms::boost_python
