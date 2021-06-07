"""
Automatic speech recognition scenario
"""

import logging

import numpy as np
from art.preprocessing.audio import LFilter, LFilterPyTorch

from armory.scenarios.base import Scenario

logger = logging.getLogger(__name__)


def load_audio_channel(delay, attenuation, pytorch=True):
    """
    Return an art LFilter object for a simple delay (multipath) channel

    If attenuation == 0 or delay == 0, return an identity channel
        Otherwise, return a channel with length equal to delay + 1

    NOTE: lfilter truncates the end of the echo, so output length equals input length
    """
    delay = int(delay)
    attenuation = float(attenuation)
    if delay < 0:
        raise ValueError(f"delay {delay} must be a nonnegative number (of samples)")
    if delay == 0 or attenuation == 0:
        logger.warning("Using an identity channel")
        numerator_coef = np.array([1.0])
        denominator_coef = np.array([1.0])
    else:
        if not (-1 <= attenuation <= 1):
            logger.warning(f"filter attenuation {attenuation} not in [-1, 1]")

        # Simple FIR filter with a single multipath delay
        numerator_coef = np.zeros(delay + 1)
        numerator_coef[0] = 1.0
        numerator_coef[delay] = attenuation

        denominator_coef = np.zeros_like(numerator_coef)
        denominator_coef[0] = 1.0

    if pytorch:
        try:
            return LFilterPyTorch(
                numerator_coef=numerator_coef, denominator_coef=denominator_coef
            )
        except ImportError:
            logger.exception("PyTorch not available. Resorting to scipy filter")

    logger.warning("Scipy LFilter does not currently implement proper gradients")
    return LFilter(numerator_coef=numerator_coef, denominator_coef=denominator_coef)


class AutomaticSpeechRecognition(Scenario):
    def __init__(self, config, *args, skip_attack=None, **kwargs):
        # Imperceptible attack still WIP
        skip_adversarial = (config.get("adhoc") or {}).get("skip_adversarial")
        if skip_adversarial:
            if skip_attack is False:
                logger.warning(
                    "config['adhoc']['skip_adversarial']=True overridden by skip_attack=False"
                )
            elif skip_attack is None:
                logger.warning(
                    "skip_attack set by config['adhoc']['skip_adversarial']=True"
                )
                skip_attack = True
        elif skip_attack:
            logger.warning(
                "config['adhoc']['skip_adversarial']=False overridden by skip_attack=True"
            )

        super().__init__(config, *args, skip_attack=skip_attack, **kwargs)
        if self.skip_misclassified:
            raise ValueError("skip_misclassified shouldn't be set for ASR scenario")

    def get_audio_channel(self):
        audio_channel_config = self.config.get("adhoc", {}).get("audio_channel")
        if audio_channel_config is None:
            return None
        logger.info("loading audio channel")
        for k in "delay", "attenuation":
            if k not in audio_channel_config:
                raise ValueError(f"audio_channel must have key {k}")
        audio_channel = load_audio_channel(**audio_channel_config)
        return audio_channel

    def load_model(self, train_split_default="train_clean100"):
        estimator = self._load_estimator()
        audio_channel = self.get_audio_channel()
        if audio_channel:
            if estimator.preprocessing_defences:
                estimator.preprocessing_defences.insert(0, audio_channel)
            else:
                estimator.preprocessing_defences = [audio_channel]
            estimator._update_preprocessing_operations()  # TODO: FIX? ART Interface for 1.6.2?

        self.estimator = self._load_defense(
            estimator, train_split_default=train_split_default
        )

    def load_dataset(self, eval_split_default="test_clean"):
        if self.config["dataset"]["batch_size"] != 1:
            logger.warning("Evaluation batch_size != 1 may not be supported.")
        super().load_dataset(self, eval_split_default=eval_split_default)
