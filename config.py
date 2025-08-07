"""Global configuration for simulation and inference parameters."""

# Measurement scatter for observed quantities (dex or mag)
OBS_SCATTER_STAR: float = 0.1
OBS_SCATTER_MAG: float = 0.1

# Fixed value of ``log10(alpha_sps)`` used throughout the simulation.
#
# Previously the mass-to-light ratio ``alpha_sps`` was drawn from a normal
# distribution for each mock lens.  For the simplified inference workflow we
# instead adopt a single deterministic value which can be adjusted here.
LOGALPHA_SPS: float = 0.1

