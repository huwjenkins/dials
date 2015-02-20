#
#  Copyright (C) (2013) STFC Rutherford Appleton Laboratory, UK.
#
#  Author: David Waterman.
#
#  This code is distributed under the BSD license, a copy of which is
#  included in the root directory of this package.
#

"""Auxiliary functions for the refinement package"""

from __future__ import division
from math import sin, cos
from scitbx import matrix
import random

def dR_from_axis_and_angle(axis, angle, deg=False):
  """return the first derivative of a rotation matrix specified by its
  axis and angle"""

  # NB it is inefficient to do this separately from the calculation of
  # the rotation matrix itself, but it seems the Python interface to
  # scitbx does not have a suitable function. It might perhaps be
  # useful to write one, which could come straight from David Thomas'
  # RTMATS (present in Mosflm and MADNES).

  # NB RTMATS does calculation for a clockwise rotation of a vector
  # whereas axis_and_angle_as_r3_rotation_matrix does anticlockwise
  # rotation. Therefore flip the axis in here compared with
  # RTMATS in order to match the axis_and_angle_as_r3_rotation_matrix
  # convention

  assert axis.n in ((3,1), (1,3))
  if (deg): angle *= pi/180
  axis *= -1.
  ca, sa  = cos(angle), sin(angle)

  return(matrix.sqr((sa * axis[0] * axis[0] - sa ,
                  sa * axis[0] * axis[1] + ca * axis[2],
                  sa * axis[0] * axis[2] - ca * axis[1],
                  sa * axis[1] * axis[0] - ca * axis[2],
                  sa * axis[1] * axis[1] - sa,
                  sa * axis[1] * axis[2] + ca * axis[0],
                  sa * axis[2] * axis[0] + ca * axis[1],
                  sa * axis[2] * axis[1] - ca * axis[0],
                  sa * axis[2] * axis[2] - sa)))

def random_param_shift(vals, sigmas):
  """Add a random (normal) shift to a parameter set, for testing"""

  assert len(vals) == len(sigmas)
  shifts = [random.gauss(0, sd) for sd in sigmas]
  newvals = [(x + y) for x, y in zip(vals, shifts)]

  return newvals

def get_fd_gradients(mp, deltas, multi_state_elt=None):
  """Calculate centered finite difference gradients for each of the
  parameters of the model parameterisation mp.

  "deltas" must be a sequence of the same length as the parameter list, and
  contains the step size for the difference calculations for each parameter.

  "multi_state_elt" selects a particular state for use when mp is a multi-
  state parameterisation.
  """

  p_vals = mp.get_param_vals()
  assert len(deltas) == len(p_vals)
  fd_grad = []

  for i in range(len(deltas)):

    val = p_vals[i]

    p_vals[i] -= deltas[i] / 2.
    mp.set_param_vals(p_vals)
    if multi_state_elt is None:
      rev_state = mp.get_state()
    else:
      rev_state = mp.get_state(multi_state_elt=multi_state_elt)

    p_vals[i] += deltas[i]
    mp.set_param_vals(p_vals)
    if multi_state_elt is None:
      fwd_state = mp.get_state()
    else:
      fwd_state = mp.get_state(multi_state_elt=multi_state_elt)

    fd_grad.append((fwd_state - rev_state) / deltas[i])

    p_vals[i] = val

  # return to the initial state
  mp.set_param_vals(p_vals)

  return fd_grad

def print_model_geometry(beam = None, detector = None, crystal = None):

  # FIXME This function is essentially deprecated by the __str__ methods of
  # each of the experimental models.

  if beam:
    print "beam s0 = (%.4f, %.4f, %.4f)" % beam.get_s0()
  if detector:
    print "sensor origin = (%.4f, %.4f, %.4f)" % detector[0].get_origin()
    print "sensor dir1 = (%.4f, %.4f, %.4f)" % detector[0].get_fast_axis()
    print "sensor dir2 = (%.4f, %.4f, %.4f)" % detector[0].get_slow_axis()
  if crystal:
    uc = crystal.get_unit_cell()
    print "crystal unit cell = %.4f, %.4f, %.4f, %.4f, %.4f, %.4f" % uc.parameters()
    print "crystal orientation matrix U ="
    print crystal.get_U().round(4)

def print_grads(grad_list):
  for i, grad in enumerate(grad_list):
    print ("Param %02d. Gradients: "
           "%.5f, %.5f, %.5f" % ((i,) + tuple(grad)))

def get_panel_groups_at_depth(group, depth=0):
  """Return a list of the panel groups at a certain depth below the node group"""
  assert depth >= 0
  if depth == 0:
    return [group]
  else:
    return [p for gp in group.children() for p in get_panel_groups_at_depth(gp, depth-1)]

def get_panel_ids_at_root(panel_list, group):
  """Get the sequential panel IDs for a set of panels belonging to a group"""
  try:
    return [p for gp in group.children() for p in get_panel_ids_at_root(panel_list, gp)]
  except AttributeError: # we got down to Panels
    return [panel_list.index(group)]

def matrix_inverse_error_propagation(mat, cov_mat):
  """Implement analytical formula of Lefebvre et al. (1999)
  http://arxiv.org/abs/hep-ex/9909031 to calculate the covariances of elements
  of mat^-1, given the covariances of mat itself. This is not the most efficient
  way to approach the formula, but suitable for initial tests"""

  from scitbx.array_family import flex

  # initialise covariance matrix
  assert mat.is_square()
  assert cov_mat.is_square()
  n = mat.n_rows()
  assert cov_mat.n_rows() == n**2

  # use flex for nice 2D indexing
  inv_mat = flex.double(mat.inverse())
  inv_mat.reshape(flex.grid(n, n))
  cov_mat = cov_mat.as_flex_double_matrix()

  inv_cov_mat = flex.double(flex.grid(n**2,n**2), 0.0)
  for alpha in range(n):
    for beta in range(n):
      for a in range(n):
        for b in range(n):

          # index into inv_cov_mat after flattening inv_mat
          u = alpha * n + beta
          v = a * n + b
          # skip elements in the lower triangle
          if v < u: continue

          # The element u,v of the result is the calculation
          # cov(m^-1[alpha, beta], m^-1[a, b])
          elt = 0.0
          for i in range(n):
            for j in range(n):
              for k in range(n):
                for l in range(n):

                  # index into cov_mat after flattening mat
                  x = i * n + j
                  y = k * n + l
                  elt += inv_mat[alpha, i] * inv_mat[j, beta] * \
                       inv_mat[a, k] * inv_mat[l, b] * \
                       cov_mat[x, y]
          inv_cov_mat[u, v] = elt

  inv_cov_mat.matrix_copy_upper_to_lower_triangle_in_place()
  return inv_cov_mat.as_scitbx_matrix()
