"""
Phage-Virus-Defined-As-Phycnogonida: Section 12 - Biomass Solver Matrix
Module: src/biomass_solver.py
Author: Archival Software Component

This core tracks the differential biomass growth vector (dV/dt) under systemic 
protein depletion thresholds, identifies specific alkaline degradation bounds,
and computes total-body lymphatic sepsis clearance maps.
"""

import numpy as np
from scipy.ndimage import gaussian_filter

class NitrogenBiomassSolver:
    def __init__(self, volumetric_voxel_grid: np.ndarray, global_resolution_mm: tuple = (0.5, 0.5, 1.0)):
        """
        Initializes the Section 12 Advanced Macro-Somatic Fluid Engine.
        
        :param volumetric_voxel_grid: Co-registered 3D float matrix from scanner arrays.
        :param global_resolution_mm: Individual spatial voxel boundaries (dx, dy, dz).
        """
        self.grid = volumetric_voxel_grid.astype(np.float32)
        self.dx, self.dy, self.dz = global_resolution_mm
        self.depth, self.height, self.width = self.grid.shape
        
        # Internalized Pharmacokinetic Threshold Registers
        self.alkaline_degradation_bounds = {
            "Colossendeis": {"threshold_ph": 8.42, "target_hu": 690.0, "kappa": 0.85},
            "Achelia": {"threshold_ph": 8.15, "target_hu": 450.0, "kappa": 0.45},
            "Pycnogonum": {"threshold_ph": 8.55, "target_hu": 850.0, "kappa": 0.25},
            "Decolopoda": {"threshold_ph": 8.48, "target_hu": 720.0, "kappa": 0.90},
            "Dodecolopoda": {"threshold_ph": 8.55, "target_hu": 750.0, "kappa": 0.95}
        }

    def evaluate_nitrogen_limiting_growth(self, current_volume_v: float, available_nitrogen_pool: float, target_strain: str) -> dict:
        """
        Calculates the time-dependent biomass proliferation derivative (dV/dt).
        Formula: dV/dt = kappa * N_host * (1 - V/V_max) - delta * Phi_alkaline
        """
        profile = self.alkaline_degradation_bounds.get(target_strain, self.alkaline_degradation_bounds["Achelia"])
        v_max = 5000.0  # Critical volumetric pocket limit before capsule rupture threshold
        
        kappa = profile["kappa"]
        
        # Compute raw logistical growth vector
        growth_derivative = kappa * available_nitrogen_pool * (1.0 - (current_volume_v / v_max))
        
        # Flag structural containment metrics
        is_near_rupture = current_volume_v > (v_max * 0.85)
        
        return {
            "biomass_growth_derivative_dv_dt": float(growth_derivative),
            "current_saturation_ratio": float(current_volume_v / v_max),
            "containment_risk_status": "CRITICAL_THREAT_DETECTED" if is_near_rupture else "BOUNDED_STABLE",
            "required_degradation_ph": profile["threshold_ph"]
        }

    def compute_lymphatic_sepsis_clearance_map(self, low_ph_acid_matrix: np.ndarray, clearing_velocity_q: float) -> np.ndarray:
        """
        Solves the convective-diffusive transport of systemic cytolytic acidosis fronts 
        across global lymph basins undergoing active non-surgical flushing.
        """
        acid_field = low_ph_acid_matrix.astype(np.float32)
        
        # Calculate local spatial gradients to trace fluid leaching fronts
        grad_z, grad_y, grad_x = np.gradient(acid_field)
        magnitude = np.sqrt(grad_z**2 + grad_y**2 + grad_x**2)
        
        # Apply convective clearing displacement model
        cleared_field = acid_field - (clearing_velocity_q * magnitude * 0.037)
        
        # Suppress artifact noise while keeping clear structural boundaries intact
        return gaussian_filter(np.clip(cleared_field, 0.0, None), sigma=1.1)
