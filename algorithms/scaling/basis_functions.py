"""
Classes that take in a scaler and minimisation parameters and
return the scale factors and derivatives of the scale factors w.r.t.
the parameters
"""
from __future__ import print_function
from dials.array_family import flex
from dials_scaling_ext import row_multiply
from scitbx import sparse

class basis_function(object):
  """Class that takes in a scaling_apm and calcuates the scale factors,
  derivatives and optionally curvatures for minimisation."""
  def __init__(self, curvatures=False):
    self.curvatures = curvatures

  def update_scale_factors(self, apm):
    """Update the parameters in each SF object from the apm parameter list."""
    for component in apm.components.itervalues():
      component['object'].calculate_scales_and_derivatives(self.curvatures)

  @staticmethod
  def calculate_scale_factors(apm):
    """Calculate the overall scale factor for each reflection from individual
    components."""
    msf_list = []
    for block_id in range(len(apm.n_obs)):
      multiplied_scale_factors = flex.double(apm.n_obs[block_id], 1.0)
      for component in apm.components.itervalues():
        multiplied_scale_factors *= component['object'].inverse_scales[block_id]
      if apm.constant_g_values:
        multiplied_scale_factors *= apm.constant_g_values[block_id]
      msf_list.append(multiplied_scale_factors)
    return msf_list

  @staticmethod
  def calculate_derivatives(apm):
    """Calculate the derivatives matrix."""
    if not apm.components:
      return None
    deriv_list = []
    if len(apm.components) == 1:
      #only one active parameter, so don't need to chain rule any derivatives
      for block_id in range(len(apm.n_obs)):
        deriv_list.append(apm.components.values()[0]['object'].derivatives[block_id])
      return deriv_list
    for block_id in range(len(apm.n_obs)):
      derivatives = sparse.matrix(apm.n_obs[block_id], apm.n_active_params)
      for comp_name, component in apm.components.iteritems():
        derivs = component['object'].derivatives[block_id]
        scale_multipliers = flex.double(apm.n_obs[block_id], 1.0)
        for comp, obj in apm.components.iteritems():
          if comp != comp_name:
            scale_multipliers *= obj['object'].inverse_scales[block_id]
        if apm.constant_g_values:
          scale_multipliers *= apm.constant_g_values[block_id]
        next_deriv = row_multiply(derivs, scale_multipliers)
        derivatives.assign_block(next_deriv, 0, component['start_idx'])
      deriv_list.append(derivatives)
    return deriv_list

  @staticmethod
  def calculate_curvatures(apm):
    """Calculate the curvatures matrix."""
    if not apm.components:
      return None
    curv_list = []
    if len(apm.components) == 1:
      #only one active parameter, so don't need to chain rule any derivatives
      for block_id in range(len(apm.n_obs)):
        curv_list.append(apm.components.values()[0]['object'].curvatures[block_id])
      return curv_list
    for block_id in range(len(apm.n_obs)):
      curvatures = sparse.matrix(apm.n_obs[block_id], apm.n_active_params)
      for comp_name, component in apm.components.iteritems():
        curvs = component['object'].curvatures[block_id]
        if curvs != 0.0:
          scale_multipliers = flex.double(apm.n_obs[block_id], 1.0)
          for comp, obj in apm.components.iteritems():
            if comp != comp_name:
              scale_multipliers *= obj['object'].inverse_scales[block_id]
          if apm.constant_g_values:
            scale_multipliers *= apm.constant_g_values[block_id]
          next_curv = row_multiply(curvs, scale_multipliers)
          curvatures.assign_block(next_curv, 0, component['start_idx'])
      curv_list.append(curvatures)
    return curv_list

  def calculate_scales_and_derivatives(self, apm):
    """Calculate and return scale factors, derivatives and optionally
    curvatures to be used in minimisation."""
    self.update_scale_factors(apm)
    if self.curvatures:
      return (self.calculate_scale_factors(apm),
       self.calculate_derivatives(apm),
       self.calculate_curvatures(apm))
    return self.calculate_scale_factors(apm), self.calculate_derivatives(apm)
