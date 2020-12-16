from art.attacks.evasion import ProjectedGradientDescent
import numpy as np

import logging

logger = logging.getLogger(__name__)


class SNR_PGD(ProjectedGradientDescent):
    """
    Applies L2 PGD to signal based on an SNR bound defined by norm 'snr' or 'snr_db'.
        This is a *lower* bound on allowable SNR (as opposed to L2 upper bound)

    norm - snr or snr_db
    eps - the lower bound on allowable SNR and SNR_DB
    eps_step - float value in [0, 1] that is the ratio of max L2 distance per step
        NOTE: this is different from original PGD because SNR is not additive

    SNR measures the original signal power to adversarial perturbation power
        If there is no perturbation, SNR is np.inf; all other values are finite.
        If the perturbation is unbounded, SNR is 0
    SNR_DB = 10 * log10(SNR)

    If SNR is set to 0 or SNR_DB to -inf, no limit is provided to PGD
        If SNR or SNR_DB is set to Inf, this only returns the input
    """

    def __init__(self, estimator, norm="snr", eps=10, eps_step=0.5, **kwargs):
        super().__init__(estimator=estimator, norm=2, **kwargs)

        # Map to SNR domain
        eps = float(eps)
        if norm == "snr":
            snr = 10 ** (eps / 10)
        elif norm == "snr_db":
            snr = eps
        else:
            raise ValueError(f"norm must be 'snr' (default) or 'snr_db', not {norm}")

        if snr < 0:
            raise ValueError(f"snr must be nonnegative, not {snr}")
        elif snr == 0:
            self.snr_sqrt_reciprocal = np.inf
        else:
            self.snr_sqrt_reciprocal = 1 / np.sqrt(snr)

        eps_step = float(eps_step)
        if not (0 <= eps_step <= 1):
            raise ValueError(f"eps_step must be in [0, 1], not {eps_step}")
        self.step_fraction = eps_step

    def generate(self, x: np.ndarray, y=None, **kwargs) -> np.ndarray:
        x_l2 = np.linalg.norm(x, ord=2, axis=1)

        eps = x_l2 * self.snr_sqrt_reciprocal
        if self.snr_sqrt_reciprocal == np.inf and self.step_fraction == 0:
            eps_step = np.zeros(eps.shape)  # avoid nan if eps
        else:
            eps_step = eps * self.step_fraction

        self.set_params(eps=eps, eps_step=eps_step)
        return super().generate(x, y=y, **kwargs)
