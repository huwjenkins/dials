
#ifndef DIALS_ALGORITHMS_SPOT_PREDICTION_SPOT_PREDICTOR_H
#define DIALS_ALGORITHMS_SPOT_PREDICTION_SPOT_PREDICTOR_H

#include <scitbx/constants.h>
#include <dials/model/experiment/beam.h>
#include <dials/model/experiment/detector.h>
#include <dials/model/experiment/goniometer.h>
#include "index_generator.h"
#include "rotation_angles.h"
//#include "../geometry/transform/from_beam_vector_to_detector.h"
#include <dials/model/data/reflection.h>

namespace dials { namespace algorithms {

  using scitbx::vec2;
  using scitbx::vec3;
  using scitbx::mat3;
  using model::Beam;
  using model::FlatPanelDetector;
  using model::Goniometer;
  using model::Reflection;
  using model::ReflectionList;

  typedef cctbx::miller::index <> miller_index;
  typedef scitbx::af::flex <miller_index> ::type flex_miller_index;

  class SpotPredictor {

  public:

    /**
     * Initialise the spot predictor.
     * @param beam The beam parameters
     * @param detector The detector parameters
     * @param gonio The goniometer parameters
     * @param unit_cell The unit cell parameters
     * @param space_group_type The space group struct
     * @param ub_matrix The ub matrix
     * @param d_min The resolution
     */
    SpotPredictor(const Beam &beam,
                  const FlatPanelDetector &detector,
                  const Goniometer &gonio,
                  const cctbx::uctbx::unit_cell &unit_cell,
                  const cctbx::sgtbx::space_group_type &space_group_type,
                  mat3 <double> ub_matrix,
                  double d_min)
      : index_generator_(unit_cell, space_group_type, false, d_min),
        rotation_angle_calculator_(
          beam.get_direction(),
          gonio.get_rotation_axis()),
//        from_beam_vector_to_detector_(detector),
        beam_(beam),
        detector_(detector),
        gonio_(gonio),
        ub_matrix_(gonio.get_fixed_rotation() * ub_matrix),
        s0_(beam.get_direction()),
        m2_(gonio.get_rotation_axis().normalize()) {}

    /**
     * Predict the spot locations on the image detector.
     *
     * The algorithm performs the following procedure:
     *
     *  - For the miller index, the rotation angle at which the diffraction
     *    conditions are met is calculated.
     *
     *  - The rotation angles are then checked to see if they are within the
     *    rotation range.
     *
     *  - The reciprocal lattice vectors are then calculated, followed by the
     *    diffracted beam vector for each reflection.
     *
     *  - The image volume coordinates are then calculated for each reflection.
     *
     *  - The image volume coordinates are then checked to see if they are
     *    within the image volume itself.
     *
     * @param h The miller index
     */
    vec2 <Reflection> predict(miller_index h) const {

      vec2 <Reflection> reflections;

      // Calculate the reciprocal space vector
      vec3 <double> pstar0 = ub_matrix_ * h;

      // Try to calculate the diffracting rotation angles
      vec2 <double> phi;
      try {
        phi = rotation_angle_calculator_.calculate(pstar0);
      } catch(error) {
        return reflections;
      }

      // Loop through the 2 rotation angles
      for (std::size_t i = 0; i < phi.size(); ++i) {

        // Check that the angles are within the rotation range
        //double phi_deg = mod_360(scitbx::rad_as_deg(phi[i]));
        //if (!gonio_.is_angle_valid(phi_deg, true)) {
        //  continue;
        //}

        // Calculate the reciprocal space vector
        //vec3 <double> pstar = pstar0.unit_rotate_around_origin(
        //  m2_, phi[i]);

        // Calculate the diffracted beam vector
        //vec3 <double> s1 = s0_ + pstar;

        // Try to calculate the detector coordinate
        //vec2 <double> xy;
        //try {
        //  xy = from_beam_vector_to_detector_.apply(s1);
        //} catch(error) {
        //  continue;
        //}

        // Calculate the frame number
        //double z = gonio_.get_zero_based_frame_from_angle(phi_deg, true);

        // Check the detector coordinate is valid and add the
        // elements to the arrays. NB. up to now, we have used
        // angles in radians, convert them to degrees before adding
        // them to the rotation angle array.
        //if (!detector_.is_coordinate_valid(xy)) {
        //  continue;
        //}

        // Add the reflection
        //reflections[i] = Reflection(
        //  h, phi_deg, s1, vec3 <double> (xy[0], xy[1], z));
      }
      return reflections;
    }

    /**
     * For a given set of miller indices, predict the detector coordinates.
     * @param miller_indices The array of miller indices.
     */
    scitbx::af::shared <Reflection>
    predict(const flex_miller_index &miller_indices) const {
      scitbx::af::shared <Reflection> reflections;
      for (std::size_t i = 0; i < miller_indices.size(); ++i) {
        vec2 <Reflection> r = predict(miller_indices[i]);
        for (std::size_t j = 0; j < r.size(); ++j) {
          if (!r[j].is_zero()) {
              reflections.push_back(r[j]);
          }
        }
      }
      return reflections;
    }

    /**
     * Generate a set of miller indices and predict the detector coordinates.
     */
    scitbx::af::shared <Reflection>
    predict() {
      scitbx::af::shared <Reflection> reflections;

      // Continue looping until we run out of miller indices
      for (;;) {

        // Get the next miller index
        miller_index h = index_generator_.next();
        if (h.is_zero()) {
          break;
        }

        // Predict the spot location for the miller index
        vec2 <Reflection> r = predict(h);
        for (std::size_t j = 0; j < r.size(); ++j) {
          if (!r[j].is_zero()) {
            reflections.push_back(r[j]);
          }
        }
      }
      return reflections;
    }

  private:

      /** Get the angle % 360 */
      double mod_360(double angle) const {
        return angle - 360.0 * std::floor(angle / 360.0);
      }

  private:

      IndexGenerator index_generator_;
      RotationAngles rotation_angle_calculator_;
      //geometry::transform::FromBeamVectorToDetector from_beam_vector_to_detector_;
      Beam beam_;
      FlatPanelDetector detector_;
      Goniometer gonio_;
      mat3 <double> ub_matrix_;
      vec3 <double> s0_;
      vec3 <double> m2_;
  };

}} // namespace dials::algorithms

#endif // DIALS_ALGORITHMS_SPOT_PREDICTION_SPOT_PREDICTOR_H
