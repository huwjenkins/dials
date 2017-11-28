from __future__ import absolute_import, division, print_function
from libtbx.test_utils.pytest import discover

tst_list = [
    "$B/test/algorithms/spatial_indexing/tst_collision_detection",
    "$B/test/algorithms/spatial_indexing/tst_octree",
    "$B/test/algorithms/spatial_indexing/tst_quadtree",
    "$B/test/algorithms/spot_prediction/tst_reeke_model",
    "$D/test/algorithms/background/tst_creator.py",
    "$D/test/algorithms/background/tst_gmodel.py",
    "$D/test/algorithms/background/tst_modeller.py",
    "$D/test/algorithms/background/tst_mosflm_outlier_rejector.py",
    "$D/test/algorithms/background/tst_outlier_rejector.py",
    "$D/test/algorithms/generate_test_reflections/tst_generate_test_refl.py",
    "$D/test/algorithms/image/connected_components/tst_connected_components.py",
    "$D/test/algorithms/image/fill_holes/tst_simple_fill.py",
    "$D/test/algorithms/image/filter/tst_distance.py",
    "$D/test/algorithms/image/filter/tst_index_of_dispersion.py",
    "$D/test/algorithms/image/filter/tst_mean_and_variance.py",
    "$D/test/algorithms/image/filter/tst_median.py",
    "$D/test/algorithms/image/filter/tst_summed_area.py",
    "$D/test/algorithms/image/threshold/tst_local.py",
    "$D/test/algorithms/image/tst_centroid.py",
    "$D/test/algorithms/integration/profile/tst_circle_sampler.py",
    "$D/test/algorithms/integration/profile/tst_empirical_modeller.py",
    "$D/test/algorithms/integration/profile/tst_grid_sampler.py",
    "$D/test/algorithms/integration/profile/tst_multi_experiment_modeller.py",
    "$D/test/algorithms/integration/profile/tst_profile_fitting.py",
    "$D/test/algorithms/integration/profile/tst_single_sampler.py",
    "$D/test/algorithms/integration/tst_corrections.py",
    "$D/test/algorithms/integration/tst_interface.py",
    "$D/test/algorithms/integration/tst_profile_fitting_rs.py",
    "$D/test/algorithms/integration/tst_summation.py",
    "$D/test/algorithms/integration/tst_filter_overlaps.py",
    "$D/test/algorithms/polygon/clip/tst_clipping.py",
    "$D/test/algorithms/polygon/tst_spatial_interpolation.py",
    "$D/test/algorithms/profile_model/tst_profile_model.py",
    "$D/test/algorithms/profile_model/tst_ewald_sphere_sampler.py",
    "$D/test/algorithms/refinement/tst_beam_parameters.py",
    "$D/test/algorithms/refinement/tst_crystal_parameters.py",
    "$D/test/algorithms/refinement/tst_detector_parameters.py",
    "$D/test/algorithms/refinement/tst_finite_diffs.py",
    "$D/test/algorithms/refinement/tst_hierarchical_detector_refinement.py",
    "$D/test/algorithms/refinement/tst_multi_experiment_refinement.py",
    "$D/test/algorithms/refinement/tst_multi_panel_detector_parameterisation.py",
    "$D/test/algorithms/refinement/tst_prediction_parameters.py",
    "$D/test/algorithms/refinement/tst_ref_passage_categorisation.py",
    "$D/test/algorithms/refinement/tst_refine_multi_stills.py",
    "$D/test/algorithms/refinement/tst_refine_multi_wedges.py",
    "$D/test/algorithms/refinement/tst_refinement_regression.py",
    "$D/test/algorithms/refinement/tst_rotation_decomposition.py",
    "$D/test/algorithms/refinement/tst_scan_varying_model_parameters.py",
    "$D/test/algorithms/refinement/tst_scan_varying_prediction_parameters.py",
    "$D/test/algorithms/refinement/tst_stills_prediction_parameters.py",
    "$D/test/algorithms/refinement/tst_stills_refinement.py",
    "$D/test/algorithms/refinement/tst_stills_spherical_relp_derivatives.py",
    "$D/test/algorithms/refinement/tst_restraints_parameterisation.py",
    "$D/test/algorithms/refinement/tst_restraints_gradients.py",
    "$D/test/algorithms/refinement/tst_sv_multi_panel_refinement.py",
    "$D/test/algorithms/refinement/tst_xfel_metrology.py",
    "$D/test/algorithms/refinement/tst_two_theta_refinement.py",
    "$D/test/algorithms/refinement/tst_constraints.py",
    "$D/test/algorithms/refinement/tst_angle_derivatives_wrt_vector_elts.py",
    "$D/test/algorithms/refinement/tst_dials-423.py",
    "$D/test/algorithms/reflection_basis/tst_beam_vector_map.py",
    "$D/test/algorithms/reflection_basis/tst_coordinate_system.py",
    "$D/test/algorithms/reflection_basis/tst_grid_index_generator.py",
    "$D/test/algorithms/reflection_basis/tst_map_frames.py",
    "$D/test/algorithms/reflection_basis/tst_transform.py",
    "$D/test/algorithms/shoebox/tst_bbox_calculator.py",
    "$D/test/algorithms/shoebox/tst_find_overlapping.py",
    "$D/test/algorithms/shoebox/tst_mask_foreground.py",
    "$D/test/algorithms/shoebox/tst_mask_overlapping.py",
    "$D/test/algorithms/shoebox/tst_partiality_calculator.py",
    "$D/test/algorithms/spatial_indexing/tst_spatial_index.py",
    "$D/test/algorithms/spot_prediction/tst_index_generator.py",
    "$D/test/algorithms/spot_prediction/tst_pixel_to_miller_index.py",
    "$D/test/algorithms/spot_prediction/tst_ray_predictor.py",
    "$D/test/algorithms/spot_prediction/tst_reeke.py",
    "$D/test/algorithms/spot_prediction/tst_reeke_index_generator.py",
    "$D/test/algorithms/spot_prediction/tst_rotation_angles.py",
    "$D/test/algorithms/spot_prediction/tst_scan_static_reflection_predictor.py",
    "$D/test/algorithms/spot_prediction/tst_scan_varying_predictor.py",
    "$D/test/algorithms/spot_prediction/tst_scan_varying_reflection_predictor.py",
    "$D/test/algorithms/spot_prediction/tst_spot_prediction.py",
    "$D/test/algorithms/spot_prediction/tst_stills_reflection_predictor.py",
    "$D/test/algorithms/statistics/tst_fast_mcd.py",
    "$D/test/algorithms/scaling/tst_observation_manager.py",
    "$D/test/algorithms/scaling/tst_scale_parameterisation.py",
    "$D/test/algorithms/scaling/tst_HRS_derivatives.py",
    "$D/test/array_family/tst_flex_shoebox.py",
    "$D/test/array_family/tst_reflection_table.py",
    "$D/test/command_line/tst_modify_geometry.py",
    "$D/test/command_line/tst_export_bitmaps.py",
    "$D/test/command_line/tst_apply_mask.py",
    "$D/test/command_line/tst_check_indexing_symmetry.py",
    "$D/test/command_line/tst_combine_experiments.py",
    "$D/test/command_line/tst_combine_found_spots.py",
    "$D/test/command_line/tst_compare_orientation_matrices.py",
    "$D/test/command_line/tst_create_profile_model.py",
    "$D/test/command_line/tst_estimate_gain.py",
    "$D/test/command_line/tst_export.py",
    "$D/test/command_line/tst_export_mosflm.py",
    "$D/test/command_line/tst_export_xds.py",
    "$D/test/command_line/tst_export_best.py",
    "$D/test/command_line/tst_filter_reflections.py",
    "$D/test/command_line/tst_find_hot_pixels.py",
    "$D/test/command_line/tst_find_spots_server_client.py",
    "$D/test/command_line/tst_generate_mask.py",
    "$D/test/command_line/tst_idials.py",
    "$D/test/command_line/tst_import.py",
    "$D/test/command_line/tst_import_xds.py",
    "$D/test/command_line/tst_integrate.py",
    "$D/test/command_line/tst_kapton_correction.py",
    "$D/test/command_line/tst_merge_cbf.py",
    "$D/test/command_line/tst_merge_reflection_lists.py",
    "$D/test/command_line/tst_plot_scan_varying_crystal.py",
    "$D/test/command_line/tst_predict.py",
    "$D/test/command_line/tst_refine.py",
    "$D/test/command_line/tst_reindex.py",
    "$D/test/command_line/tst_rs_mapper.py",
    "$D/test/command_line/tst_rl_png.py",
    "$D/test/command_line/tst_show_extensions.py",
    "$D/test/command_line/tst_show.py",
    "$D/test/command_line/tst_slice_sweep.py",
    "$D/test/command_line/tst_sort_reflections.py",
    "$D/test/command_line/tst_spot_counts_per_image.py",
    "$D/test/command_line/tst_spotfinder.py",
    "$D/test/command_line/tst_stereographic_projections.py",
    "$D/test/command_line/tst_stills_detector_hybrid_refine.py",
    "$D/test/command_line/tst_stills_process.py",
    "$D/test/command_line/tst_two_theta_refine.py",
    "$D/test/command_line/tst_align_crystal.py",
    "$D/test/command_line/tst_goniometer_calibration.py",
    "$D/test/command_line/tst_combine_datablocks.py",
    "$D/test/framework/tst_interface.py",
    "$D/test/model/data/tst_observation.py",
    "$D/test/model/data/tst_pixel_list.py",
    "$D/test/model/data/tst_prediction.py",
    "$D/test/model/data/tst_shoebox.py",
    "$D/test/tst_phil.py",
    "$D/test/tst_plot_reflections.py",
    "$D/test/tst_scan_varying_integration_bug.py",
    "$D/test/util/tst_ascii_art.py",
    "$D/test/util/tst_nexus.py",
    "$D/test/util/tst_nexus_multi_experiment.py",
    "$D/test/util/tst_masking.py",
    "$D/test/algorithms/indexing/tst_phi_scan.py",
    ["$D/test/algorithms/indexing/tst_index.py", "1"],
    ["$D/test/algorithms/indexing/tst_index.py", "2"],
    ["$D/test/algorithms/indexing/tst_index.py", "3"],
    ["$D/test/algorithms/indexing/tst_index.py", "4"],
    ["$D/test/algorithms/indexing/tst_index.py", "7"],
    ["$D/test/algorithms/indexing/tst_index.py", "8"],
    ["$D/test/algorithms/indexing/tst_index.py", "9"],
    ["$D/test/algorithms/indexing/tst_index.py", "10"],
    ["$D/test/algorithms/indexing/tst_index.py", "11"],
    ["$D/test/algorithms/indexing/tst_index.py", "12"],
    ["$D/test/algorithms/indexing/tst_index.py", "13"],
    ["$D/test/algorithms/indexing/tst_index.py", "14"],
    ["$D/test/algorithms/indexing/tst_index.py", "15"],
    ["$D/test/algorithms/indexing/tst_index.py", "16"],
    ["$D/test/algorithms/indexing/tst_index.py", "17"],
    ["$D/test/algorithms/indexing/tst_index.py", "18"],
    "$D/test/algorithms/indexing/tst_assign_indices.py",
    "$D/test/command_line/tst_refine_bravais_settings.py",
    #["$D/test/command_line/tst_discover_better_experimental_model.py", "1"],
    ["$D/test/command_line/tst_discover_better_experimental_model.py", "2"],
    ["$D/test/command_line/tst_discover_better_experimental_model.py", "3"],
    "$D/test/algorithms/indexing/tst_compare_orientation_matrices.py",
    "$D/test/algorithms/indexing/tst_symmetry.py",
    #"$D/scratch/rjg/unit_cell_refinement.py",
    ] + discover()
